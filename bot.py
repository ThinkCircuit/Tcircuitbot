import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!!')

hogam = '0'
goback = '0'
kairoho = '0'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('일'))
    print('[알림][회로봇(일)이 성공적으로 구동되었습니다.]')


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return None
    await bot.process_commands(msg)

@bot.command()
async def 제작자(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 제작자: 생각회로')

@bot.command(aliases=["던등두", "등두", "승주", "ㅈㅅㅈ"])
async def 전승주(ctx):
    await ctx.channel.send('혹시 그 게이?')

@bot.command()
async def 게이(ctx):
    await ctx.channel.send('혹시 그 전승주?')

@bot.command()
async def 김성빈(ctx):
    await ctx.channel.send('혹시 그 햄버거?')

@bot.command()
async def 햄버거(ctx):
    await ctx.channel.send('혹시 그 김성빈?')

@bot.command(aliases=["사용법"])
async def 도움말(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}')
    embed = discord.Embed(title='회로봇 사용법',
                          description='뭐 하는 봇이고, 어떻게 쓰는 봇인가요?',
                          colour=0x7878FF)
    embed.add_field(name='> !!제작자', value='제작자 이름이 나옵니다.')
    embed.add_field(name='> !!도움말', value='명령어 목록을 볼 수 있습니다.')
    embed.add_field(name='> !!홀짝', value='간단한 홀짝 게임을 즐길 수 있습니다.')
    embed.add_field(name='> !!일정', value='2학년 2학기 일정을 볼 수 있습니다.')
    embed.add_field(name='> !!동아리', value='동아리 일정을 볼 수 있습니다.')
    embed.add_field(name='> !!시간표_(반)', value='시간표를 볼 수 있습니다.\r\n명령어 뒤에 반을 입력해주시면 됩니다.\r\n예: 2학년 5반 = 205')
    embed.set_footer(text='명령어가 생길 때마다 추가됩니다.\r\n!!사용법으로도 사용 가능합니다.')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 시간표_205(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}')
    embed = discord.Embed(title='2학년 5반 시간표',
                          colour=0x7878FF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/856170790201851964/866654989748928562/unknown.png")
    embed.set_footer(text='1학기 시간표입니다, 상황에 따라 변동 될 수 있습니다.')
    await ctx.channel.send(embed=embed)


@bot.command(aliases=["omori_omori"])
async def 오모리_오모리(ctx):
    embed = discord.Embed(title='오모리',
                          description='OMORI_omori',
                          colour=0x7878FF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/855722688428638218/855722838718808089/111118.png")
    await ctx.channel.send(embed=embed)

@bot.command(aliases=["hololive_amanekanata", "hololive_kanataamane"])
async def 홀로라이브_아마네카나타(ctx, https=None):
    await ctx.channel.send(f'{ctx.message.author.mention}')
    embed = discord.Embed(title='아마네 카나타',
                          description='Hololive_amane kanata',
                          colour=0x7878FF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/864341393291345970/864343029044740136/sample_71b7c319d41c09f2898d62f5257b003c233e6583.png")
    await ctx.channel.send(embed=embed)

@bot.command()
async def 아이작_아이작(ctx):
    embed = discord.Embed(title='아이작',
                          description='아이작의 번제_아이작',
                          colour=0x7878FF)
    embed.set_image(url="https://i.imgur.com/rYuVJf7.gif")
    await ctx.channel.send(embed=embed)

@bot.command()
async def 홀짝(ctx):
    import random
    dice = random.randint(1, 6)
    embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                          description='선택 한 뒤에 어떤 수가 나왔는지 알려드리겠습니다.')
    embed.add_field(name='> 주사위의 눈', value='???')
    embed.add_field(name='> 홀수', value='🔴')
    embed.add_field(name='> 짝수', value='🔵')
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('🔴')
    await msg.add_reaction('🔵')
    try:
        def check(reaction, user):
            return str(reaction) in ['🔴', '🔵'] and \
            user == ctx.author and reaction.message.id == msg.id
        reaction, user = await bot.wait_for('reaction_add', check=check)
        if (str(reaction) == '🔴' and dice % 2 == 1) or \
            (str(reaction) == '🔵' and dice % 2 == 0):
            embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                                  description='정답입니다! 계속해서 도전해보세요!')
        else:
            embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                                  description='틀렸습니다... 계속해서 도전해보세요!')
        embed.add_field(name='> 주사위의 눈', value=str(dice))
        embed.add_field(name='> 홀수', value='🔴')
        embed.add_field(name='> 짝수', value='🔵')
        await msg.clear_reactions()
        await msg.edit(embed=embed)
    except: pass

@bot.command()
async def 일정(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 2학년 2학기 일정입니다.')
    embed = discord.Embed(title='2학년 2학기 일정',
                          description='2021년 2학기 일정입니다.',
                          colour=0x7878FF)
    embed.add_field(name='> 8월 17일', value='개학식')
    embed.add_field(name='> 9월 16일', value='진로체험')
    embed.add_field(name='> 10월 5일', value='영어듣기평가')
    embed.add_field(name='> 11월 19일', value='재량휴업일')
    embed.add_field(name='> 12월 8일~12월 10일', value='기말고사')
    embed.add_field(name='> 12월 17일', value='동아리 작품전시회')
    embed.add_field(name='> 12월 30일', value='겨울방학식')
    embed.set_footer(text='학부모용 학교 생활 안내서 참고\r\n상황에 따라서 바뀔 수 있음')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 동아리(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 2학년 2학기 동아리 일정입니다.')
    embed = discord.Embed(title='2학년 2학기 동아리 일정',
                          description='2021년 2학기 동아리 일정입니다.',
                          colour=0x7878FF)
    embed.add_field(name='> 9월 3일', value='.')
    embed.add_field(name='> 9월 24일', value='.')
    embed.add_field(name='> 10월 15일', value='.')
    embed.add_field(name='> 11월 26일', value='.')
    embed.add_field(name='> 12월 17일', value='작품전시회')
    embed.set_footer(text='학부모용 학교 생활 안내서 참고\r\n상황에 따라서 바뀔 수 있음')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 미연시(ctx):
    embed = discord.Embed(title='간단한 미연시 게임입니다.',
                          description='미연시를 시작하시겠습니까?',
                          colour=0xFF8E99)
    embed.add_field(name='> 시작', value='❤')
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('❤')
    try:
        def check(reaction, user):
            return str(reaction) in ['❤'] and \
            user == ctx.author and reaction.message.id == msg.id
        reaction, user = await bot.wait_for('reaction_add', check=check)
        if (str(reaction) == '❤'):
            embed = discord.Embed(title='누구를 공략하시겠습니까?',
                                  description='캐릭터마다 성격이 다릅니다.',
                                  colour=0xFF8E99)
            embed.add_field(name='> 1️⃣명순', value='시험용')
            embed.set_footer(text='플레이하고 싶은 캐릭터의 번호의 이모지로 반응해주세요')
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('1️⃣')
            try:
                def check(reaction, user):
                    return str(reaction) in ['1️⃣'] and \
                    user == ctx.author and reaction.message.id == msg.id
                reaction, user = await bot.wait_for('reaction_add', check=check)
                if (str(reaction) == '1️⃣'):
                    embed = discord.Embed(title='대충 시험용 아무말',
                                          description='대충 시험용 아무말',
                                          colour=0xFF8E99)
                    embed.add_field(name='> 대충 시험용 아무말', value='대충 시험용 아무말')
                    embed.set_footer(text='이 버튼 🧡을 누르면 호감도 +70\r\n이 버튼 💛을 누르면 호감도 +30')
                    msg = await ctx.channel.send(embed=embed)
                    await msg.add_reaction('🧡')
                    await msg.add_reaction('💛')
                    try:
                        def check(reaction, user):
                            return str(reaction) in ['🧡','💛'] and \
                            user == ctx.author and reaction.message.id == msg.id
                        reaction, user = await bot.wait_for('reaction_add', check=check)
                        if (str(reaction) == '🧡'):
                            (hogam) = 70
                            embed = discord.Embed(title='대충 시험용 아무말',
                                                  description='대충 시험용 아무말',
                                                  colour=0xFF8E99)
                            embed.add_field(name='> 고백하기', value='고백하기')
                            embed.set_footer(text='이 버튼 ❤을 누르면 고백')
                            msg = await ctx.channel.send(embed=embed)
                            await msg.add_reaction('❤')
                        else:
                            if (str(reaction) == '💛'):
                             (hogam) = 30
                            embed = discord.Embed(title='대충 실험용 아무말',
                                                   description='대충 실험용 아무말',
                                                   colour=0xFF8E99)
                            embed.add_field(name='> 고백하기', value='고백하기')
                            embed.set_footer(text='이 버튼 ❤을 누르면 고백')
                            msg = await ctx.channel.send(embed=embed)
                            await msg.add_reaction('❤')
                        try:
                            def check(reaction, user):
                                return str(reaction) in ['❤'] and \
                                user == ctx.author and reaction.message.id == msg.id
                            reaction, user = await bot.wait_for('reaction_add', check=check)
                            if (str(reaction) == '❤' and (hogam) > 60):
                                embed = discord.Embed(title='고백 성공',
                                                      description='고백 성공',
                                                      colour=0xFF8E99)
                            else:
                                if (str(reaction) == '❤' and (hogam) < 60):
                                    embed = discord.Embed(title='고백 실패',
                                                          description = '고백 실패',
                                                          colour = 0xFF8E99)
                            msg = await ctx.channel.send(embed=embed)
                        except:pass
                    except:pass
            except:pass
    except:pass

@bot.command()
async def 오브리감정(ctx):
    embed = discord.Embed(title='시험용 오브리콘',
                          description='썸네일로 표정 바꾸기 가능?',
                          colour=0xFF8E99)
    embed.add_field(name='> 안녕', value='난 오브리야')
    embed.set_thumbnail(url='https://i.imgur.com/z9IPBGp.gif')
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('▶')
    try:
        def check(reaction, user):
            return str(reaction) in ['▶'] and \
            user == ctx.author and reaction.message.id == msg.id
        reaction, user = await bot.wait_for('reaction_add', check=check)
        if (str(reaction) == '▶'):
            embed = discord.Embed(title='시험용 오브리콘',
                                  description='썸네일로 표정 바꾸기 가능?',
                                  colour=0xFF8E99)
            embed.add_field(name='> 안 안녕', value='난 안 오브리야')
            embed.set_thumbnail(url='https://i.imgur.com/o3qSe2m.gif')
            await msg.edit(embed=embed)
    except:pass

@bot.command(aliases=["알러뷰","귀여워","고마워","수고했어","똑똑해"])
async def 사랑해(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 감사합니다!')

@bot.command(aliases=["시발","병신","ㅅㅂ","ㅄ","지랄","죽어","뒤져","니애미","ㅜ흐","ngm","느금","느금마","나가뒤져","자살해"])
async def 씨발(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 얼마나 할 게 없으면 봇한테 욕을..')

@bot.command()
async def 게이야(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 게이는 제가 아니라 전승주에요!')

access_token = os.environ["TOKEN"]
client.run(access_token)
