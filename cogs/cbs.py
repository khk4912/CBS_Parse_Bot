import discord
from discord.ext import commands
from logs import Logs
import aiohttp


""" CBS 관련 명령어들 """


class CBS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = Logs.create_logger(self)
        self.logger.info("{} Loaded.".format(self.__class__.__name__))
        self.CBSList = "http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json"

    @commands.command(name="재난문자", aliases=["안전안내문자", "긴급재난", "안전안내", "문자"])
    async def get_cbs(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.CBSList) as r:
                data = await r.json()
        embed = discord.Embed(
            title="📢 재난문자", description="최근 발송된 3개의 재난문자를 보여줘요.", color=0xE71212
        )
        for i in data[:3]:
            embed.add_field(name=i["SJ"], value=i["CONT"], inline=False)
        await ctx.send(embed=embed)


# 📢


def setup(bot):
    bot.add_cog(CBS(bot))
