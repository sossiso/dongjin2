import discord, datetime, asyncio

client = discord.Client()
token = "ODA5NzUxNDk4NjMyMDY5MTYw.YCZp2Q.7OR27XIwqJmmj8bVdLmYoZYm9iw"

@client.event
async def on_ready():
    print("로그인 완료")
    print(client.user)
    print("============================")
    import asyncio
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("ㄱㄷㄱㄷ 부팅 중")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("동진이 사용법이라고 쳐 봐!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(4)
        game = discord.Game("노래 기능 어떻게 하는 거지 ㅠ")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content.startswith("동진아"):
        await message.channel.send("왜불러")

    if message.content.startswith("앙"):
        await message.channel.send("기분좋아~~~!!")

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕은 하지 말지?")

    if message.content.startswith("ㅂㅅ"):
        await message.channel.send("욕은 하지 말지?")

    if message.content.startswith("서든"):
        await message.channel.send("ㄹㅇㅋㅋ")

    if message.content.startswith("ㅠ"):
        await message.channel.send("울지마!")

    if message.content.startswith("ㅋ"):
        await message.channel.send("뭘 웃어 ㅋㅋ")

    if message.content.startswith("음"):
        await message.channel.send("메~")

    if message.content.startswith("동진이 사용법"):
        embed = discord.Embed(title="**__동진이 2세 사용법__**", description="", color=0x62c1cc)
        embed.add_field(name="**가위바위보**", value="아무거나 하나 내 봐!", inline=False)
        embed.add_field(name="**명령어 사옹법**", value="명령어 앞에 ~를 붙이면 돼", inline=False)
        embed.add_field(name="**명령어 리스트**", value="내 정보, ||OO틀어줘||, 10초/15초/30초/1분 타이머, 청소, 찬반투표", inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/vf9XuJU.jpg")
        embed.set_footer(text="노래 아직 안 틀어짐 ㅠ")
        await message.channel.send(embed=embed)

    import random
    if message.content == "~가위" or message.content == "~바위" or message.content == "~보":
        random_ = random.randint(1, 3)

        if random_ == 1:
            if message.content == "~가위":
                await message.channel.send("가위!")
                await message.channel.send("ㅋㅋ")

            elif message.content == "~바위":
                await message.channel.send("가위!")
                await message.channel.send("아....")

            else:
                await message.channel.send("가위!")
                await message.channel.send("ㅉㅉ")

        if random_ == 2:
            if message.content == "~가위":
                await message.channel.send("바위!")
                await message.channel.send("ㅉㅉ")

            elif message.content == "~바위":
                await message.channel.send("바위!")
                await message.channel.send("ㅋㅋ")

            else:
                await message.channel.send("바위!")
                await message.channel.send("아.......")

        if random_ == 3:
            if message.content == "~가위":
                await message.channel.send("보!")
                await message.channel.send("아.....")

            elif message.content == "~바위":
                await message.channel.send("보!")
                await message.channel.send("ㅉㅉ")

            else:
                await message.channel.send("보!")
                await message.channel.send("ㅋㅋ")

    if message.content == '~내 정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 디스코드 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 별명 : {user.name} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content == "~10초 타이머":
        await message.channel.send("세는 중!")
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention} 10초 끝!")

    if message.content == "~15초 타이머":
        await message.channel.send("세는 중!")
        await asyncio.sleep(15)
        await message.channel.send(f"{message.author.mention} 15초 끝!")

    if message.content == "~30초 타이머":
        await message.channel.send("세는 중!")
        await asyncio.sleep(30)
        await message.channel.send(f"{message.author.mention} 30초 끝!")

    if message.content == "~1분 타이머":
        await message.channel.send("세는 중!")
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention} 1분 끝!")

    if message.content.startswith("~청소"):
        if message.content == '~청소':
            await message.channel.send(
                f"{message.author.mention}  얼마나 지워줄까?\n`₩청소 (숫자)`이렇게 써줘")
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(
                    f"{message.author.mention}  \n{number}개 지웠어!")
                await asyncio.sleep(2)
                await a.delete()
            else:
                await message.channel.send(
                    f"{message.author.mention}  미안.... 관리자가 아니라......")

    if message.content.startswith('~찬반투표'):
        await message.channel.send(f"{message.author.mention}")
        embed = discord.Embed(title="찬반투표!", description="찬성은 따봉을 반대는 봉따를!", color=0x0088ff)
        embed.add_field(name="찬성", value="↓", inline=True)
        embed.add_field(name="반대", value="↓", inline=True)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

client.run(token)