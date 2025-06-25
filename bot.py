import config
import nextcord
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
@bot.command("ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:nextcord.Member, * , reason = None):
    if ctx.author.top_role <= member.top_role:
        await ctx.send(str(member) + " could not be banned due to role rankings.")
    else:
        await member.ban(reason = reason)
        await ctx.send(str(member) + " was banned!")



bot.run(TOKEN)