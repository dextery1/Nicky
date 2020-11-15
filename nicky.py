import discord
from discord.ext import commands
from discord import Game
from pretty_help import PrettyHelp, Navigation

bot = commands.Bot(command_prefix="-")

nav = Navigation(":discord:743511195197374563", "👀", "\U0001F44D")
color = discord.Colour.blue()
bot.help_command = PrettyHelp(navigation=nav, color=color, active=5)


@bot.command(help="arg is the text", brief="Types the text after the command ")
async def say(ctx, *, arg):
	await ctx.channel.send(arg)


@bot.event
async def on_ready():
	await bot.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.listening, name="-HELP╏⚡"))


@bot.command(
    help="make sure to ping the user, even if its yourself",
    brief="Previews mentioned users avatar")
async def avatar(ctx, *, avamember: discord.Member = None):
	userAvatarUrl = avamember.avatar_url
	await ctx.send(userAvatarUrl)
	

@bot.command(
  
  help="-nick @user nickname",
  brief="Changes nickname"
   )
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f' ***Nickname Changed for {member.mention} to {nick}***')


@bot.command(
  help="-mute @user",
  brief="Mutes member")
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="GET MUTED NERD")
    await member.add_roles(role)
    await ctx.send(member.mention + " was muted :)")

@bot.command(
  help="-unmute @user",
  brief="Unmutes member"
  )
async def unmute(ctx, member: discord.Member):
 role = discord.utils.get(ctx.guild.roles,  name="GET MUTED NERD")
 await member.remove_roles(role)
 await ctx.send (member.mention  + " has been unmuted -_-")



    
 

     
    
bot.run('Mzk2Mjc3ODYyNDU5NzY4ODQz.WkY0hA.J4Yx_2skjE3ZMyrSfMWOKecOI2A')
