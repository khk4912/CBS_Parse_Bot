import discord
import aiohttp
import asyncio
import CONF

""" 새로 발생한 재난문자 알림 """
CBSList = "http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json"


async def warn_to_discord(bot):
    check = await get_new_message()
    while True:
        await asyncio.sleep(60)
        new = await get_new_message()
        if check != new:
            embed = discord.Embed(
                title="📢 {}".format(new["SJ"]), description=new["CONT"], color=0xE71212
            )
            target_channel = bot.get_channel(CONF.WARN_CHANNEL_ID)
            await target_channel.send(embed=embed)
        check = new


async def get_new_message():
    async with aiohttp.ClientSession() as session:
        async with session.get(CBSList) as r:
            data = await r.json()
    return data[0]
