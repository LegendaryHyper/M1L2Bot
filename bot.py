import config
import nextcord
import datetime
from nextcord.ext import commands

TOKEN = config.token


intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '$', intents=intents)

class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def openBook(self):
        print("Kitabın kapağı açıldı!")
    def info(self):
        return "Kitap ismi: " + self.name + "\n" + "Kitap yazarı: " + self.author


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.event
@bot.event
async def on_member_join(member:nextcord.Member):
    for channel in member.guild.text_channels:
        if channel.id == 1388173211728089208:
            await channel.send(f'Welcome, {member.mention}!')
#@bot.command()
#async def channels(ctx, member:nextcord.Member):
#    await ctx.send(member.guild.text_channels)
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
@bot.command()
async def classTest(ctx, nameInput, authorInput):
    book = Book(name = nameInput, author = authorInput)
    await ctx.send(book.info())
    
@bot.command("kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:nextcord.Member, * , reason = None):
    if ctx.author.top_role <= member.top_role:
        await ctx.send(str(member) + " could not be kicked due to role rankings.")
    else:
        await member.kick(reason = reason)
        await ctx.send(str(member) + " was kicked!")
@bot.command("timeout")
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member:nextcord.Member, days:int = 0, hours:int = 0, minutes:int = 0, seconds:int = 0, * , reason = None):
    if ctx.author.top_role <= member.top_role:
        await ctx.send(str(member) + " could not be timed out due to role rankings.")
    else:
        duration = datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
        await member.timeout(timeout=duration, reason = reason)
        await ctx.send(str(member) + f" has been timed out for {days}d {hours}h {minutes}m {seconds}s!")
@bot.command("revoke_timeout")
@commands.has_permissions(moderate_members=True)
async def revoke_timeout(ctx, member:nextcord.Member, * , reason = None):
    if ctx.author.top_role <= member.top_role:
        await ctx.send(str(member) + " could have their timeout revoked due to role rankings.")
    else:
        await member.timeout(timeout=None, reason = reason)
        await ctx.send(str(member) + "'s time out was revoked!")
@bot.command("ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:nextcord.Member, * , reason = None):
    if ctx.author.top_role <= member.top_role:
        await ctx.send(str(member) + " could not be banned due to role rankings.")
    else:
        await member.ban(reason = reason)
        await ctx.send(str(member) + " was banned!")



bot.run(TOKEN)