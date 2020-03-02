import discord
from discord.ext import commands
from logs import Logs
import CONF

""" 오너 전용 명령어 (오너 ID는 CONF.py 수정 요망) """


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = Logs.create_logger(self)
        self.logger.info("{} Loaded.".format(self.__class__.__name__))

    async def cog_check(self, ctx):
        if not ctx.author.id in CONF.OWNERS:
            embed = discord.Embed(
                title="⚠ 주의", description="관리자만 사용이 가능한 명령어에요!", color=0xD8EF56
            )
            await ctx.send(embed=embed)
            return False
        return True

    @commands.command(name="리로드", aliases=["reload"])
    async def reload(self, ctx, module):
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
            embed = discord.Embed(
                title="✅ 재로드 성공",
                description="**{}** 모듈 재로드 완료!".format(module),
                color=0x1DC73A,
            )
            await ctx.send(embed=embed)
        except Exception as error:
            await ctx.send("실패 {}".format(error))


def setup(bot):
    bot.add_cog(Owner(bot))
