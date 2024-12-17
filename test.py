import discord
from discord import app_commands
import logging
import typing
#from paginator import Paginator
#import expand
#from expand import message_expander
#import snek_paginator
#from dis_snek.client import Snake
#from dis_snek.models.application_commands import slash_command
#from dis_snek.models import Embed
#from snek_paginator import Paginator as pp
from discord import webhook
#import chatterbot
#from chatterbot import ChatBot
from discord.ext import commands, tasks
import asyncio
#import craiyon
import base64
#from craiyon import Craiyon
#import SafoneAPI
#from SafoneAPI import SafoneAPI
import aiohoripy
#import mediascraper
#from mediascraper import *
from aiohoripy import sfw, nsfw
#import keep_alive
#import googletrans
import datetime, time
from datetime import timedelta
#import paginator as lonice
#from lonice import Paginator as true
#from lonice import Page, NavigationType
import json
###import dinteractions_Paginator
###from dinteractions_Paginator import Paginator as yo
#import pilmoji
#from pilmoji import Pilmoji
#import discordbotdash.dash as dbd
#import openai
import aiohttp
import dispander
import opalart
import async_cse
import travitia_talk as tt
import cog_reloader
#import google_bing_trans
#import doc_search
#from doc_search import AsyncScraper
#from google_bing_trans import Google_translator
#import aiopentdb
#from aiohttp import request
#import google_images_download
from google_images_download import google_images_download
import badonker
import string
import re
#import difflibhelper
from difflib import get_close_matches
import jishaku
from gc import collect
#import genx
#from paginator import Paginator, Page, NavigationType
import logging
import discord_logging
from discord_logging import *
#from jikanpy import Jikan
#from jikanpy.exceptions import APIException
#jikan = Jikan() 
apI = 'https://trace.moe/api/search?url='
malu = 'https://myanimelist.net/anime/'
#log = logging.getLogger()

#WEBHOOK_URL = "https://discord.com/api/webhooks/872172597431906426/CVSSr_DMQO_BlICLr2YQXbGjSzk0ifFuZXC1xkMPHb7Q4PgcJbn0HHpOBdaNWjrqI6ce"
#handler = discord_logging.Discord_Handler(WEBHOOK_URL)

#log.addHandler(handler)

import discord_logger
from discord_logger import DiscordLogger
import loghooks
from loghooks import WebhookHandler
#import logging
#import dinteractions_Paginator
#from dinteractions_Paginator import Paginator
#from googlesearch.googlesearch import GoogleSearch
import randfacts
#from randfacts import *
#import dislash
#from dislash import SlashClient, SelectMenu, SelectOption
from string import ascii_letters
from asyncio import sleep
from itertools import cycle
from discord.ext.commands import MissingPermissions, cooldown, BucketType
import math
#import canvacord
#from canvacord import rankcard, trigger
#import disrank
#from disrank.generator import Generator
from discord.ext.commands.errors import BadArgument
import randomstuff
#import rsap
#from rsap import AsyncRSAP
import pysaucenao
from pysaucenao import DailyLimitReachedException, AnimeSource,UnknownStatusCodeException ,GenericSource, InvalidImageException, InvalidOrWrongApiKeyException, MangaSource, SauceNao, SauceNaoException, ShortLimitReachedException, VideoSource
from pysaucenao.containers import ACCOUNT_ENHANCED, AnimeSource, BooruSource
from covid import Covid 
import akinator as ak
import DiscordUtils
from DiscordUtils import *
import bs4
from bs4 import BeautifulSoup
import os
from os import path
import praw
#import hmtai
import utils
import urllib
from urllib import *
import urllib.parse as urllib
from urllib.parse import urlencode
from urllib.request import urlretrieve
from utils import *
from pyrandmeme import *
import requests
from youtube_dl import YoutubeDL
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from PIL import Image, ImageDraw, ImageFont
import aiofiles
import textwrap
from io import BytesIO
import urllib
from urllib import parse, request
import pyfiglet
from discord.utils import get
from discord.voice_client import VoiceClient
#import danksearch
import StringProgressBar
from StringProgressBar import *
import pokedex
#import openai
import animec
from animec import *
#from discord_slash import SlashCommand
#import words
#import prsaw
#from prsaw import RandomStuff
#from reactionmenu import ReactionMenu, Button, ButtonType
#from dpymenus import Page, PaginatedMenu
#import discord_components
#from discord_components import ComponentsBot, Button, Select, SelectOption, ButtonStyle
#from discord_components import *
#import ButtonPaginator
#from ButtonPaginator import Paginator as pgi
#import uuid
#from pygicord import Paginator
import google_trans_new
from google_trans_new import google_translator
import DiscordUtils
#import antispam
#from antispam import *
import giphy_client
import disputils
import hentai
from hentai import *
from disputils import BotEmbedPaginator
from giphy_client.rest import ApiException
#import tracemoepy
import pyjokes
#import search_engine_parser
#from search_engine_parser import GoogleSearch
import justgood
from justgood import imjustgood
from jishaku.features.baseclass import Feature
from jishaku.cog import STANDARD_FEATURES, OPTIONAL_FEATURES
from jishaku.paginators import PaginatorEmbedInterface, PaginatorInterface
from jishaku.functools import executor_function

class MinimalPaginatorHelp(commands.MinimalHelpCommand):
    """
    A subclass of :class:`commands.MinimalHelpCommand` that uses a PaginatorInterface for pages.
    """

    def __init__(self, **options):
        paginator = options.pop('paginator', commands.Paginator(prefix=None, suffix=None, max_size=1985))

        super().__init__(paginator=paginator, **options)

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)

api = imjustgood("imjustgood")
#s = Snake()
flush = opalart.yandere()
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.presences = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-", "nk "),intents=intents) #activity = discord.Activity(type=discord.ActivityType.competing, name="with other bots"), status="idle")
#handler = WebhookHandler(
    #webhook_url = "https://discord.com/api/webhooks/872172597431906426/CVSSr_DMQO_BlICLr2YQXbGjSzk0ifFuZXC1xkMPHb7Q4PgcJbn0HHpOBdaNWjrqI6ce",
    #session = aiohttp.ClientSession()

KEY="NrUv@n=,<-WJ4XsaQ3EA"
bot.sniped_messages = {}
bot.remove_command('help')
#ddd=DiscordComponents(bot)
#new = randomstuff.AsyncClient(api_key="wUxCLho95L4M")
#rs = RandomStuff(async_mode=True, api_key="wUxCLho95L4M")
#oh = AsyncRSAP("hmfk6KSIKb5o")
#slash = SlashCommand(bot, sync_commands=True)
guild_ids=[710528333632241676]
bot.poll_data={}
#ph = mediascraper.PornHub()
bot.warnings={}
#DiscordComponents(bot)
#lonice = true(bot)
music=DiscordUtils.Music()
time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
#slash2 = SlashClient(bot)
bot.reaction_roles = []
sus = async_cse.Search(["AIzaSyDo1o3Qb6fPQzXCt_2ufquoFk_7na-gi14", "AIzaSyBfPsM26F1nuXvp3vAESGnDI0tTiMv7H30", "AIzaSyB8hw9BrhLxcM9kCbTFh0W-MQxvopczywc", "AIzaSyAtPDfU-C_TG17nXXiq1DzCNVZ8wyt4RQA"])
#api_key = "hmfk6KSIKb5o"
#rs = RandomStuff(async_mode = True, api_key = api_key)

os.environ["JISHAKU_RETAIN"] = "True"
#os.environ["JISHAKU_SCOPE_PREFIX"] = ">"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
#os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
#tracker = DiscordUtils.InviteTracker(bot)

#bot.handler = AntiSpamHandler(bot)

#@bot.listen('on_message')
#async def ugh(message):
    #await bot.handler.propagate(message)

#@slash.slash(name="giphy", description="Get gifs", guild_ids=guild_ids)

bot.lavalink_nodes = [{"host": "lavalink.justapie.net", "port": 443, "password": "pieajust12@XyZ"}]

#@bot.listen('on_message')
#async def expand(message):
    #await message_expander(bot=bot, message=message)

@executor_function
def color_processing(color: discord.Color):
    with Image.new('RGB', (64, 64), color.to_rgb()) as im:
        buff = BytesIO()
        im.save(buff, 'png')

    buff.seek(0)
    return buff

#@slash_command('paginator')
@bot.command()
async def paginator(ctx):
    embed1 = discord.Embed(title="1", description="11222", color=ctx.guild.me.color)
    embed2 = discord.Embed(title="2", description="test", color= ctx.guild.me.color)
    embeds = [embed1, embed2]
    await pp(s, ctx, embeds).run()

#openai.api_key = "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"
    
#@bot.command()
#async def gpt(ctx, *,query):
  #await ctx.typing()
  #response = openai.Completion.create(
  		#model="text-davinci-003",
  		#prompt=query,
  		#temperature=0.3,
  		#max_tokens=4000,
  		#top_p=1,
  		#frequency_penalty=1,
  		#presence_penalty=1,
  		#stop=[" Human:", " AI:"]
  #texty = response['choices'][0]['text']
  #await ctx.reply(f"```{texty}```")    
    
    
#@bot.listen('on_message')
#async def chatbot(message):
    #if message.channel.id == 830643977022865458:
        #if message.author != bot.user:
            #async with aiohttp.ClientSession() as cs:
                #async with cs.get(f"http://api.brainshop.ai/get?bid=169559&key=EnMGqpkAW23Kz6KQ&uid=[uid]&msg=[{message}]") as r:
                    #res = await r.json()
                    #a = r["cnt"]
                #if message.author != bot.user:
                    #await message.reply(res['cnt'])

@bot.hybrid_command()
async def imagine(ctx, *,prompt):
    ETA = int(time.time() + 60)
    d = await ctx.reply(f"This may take some time, ETA: <t:{ETA}:R>")
    generator = Craiyon() # Instantiates the api wrapper
    result = await generator.async_generate(prompt)
    images = result.images[0]
    #for indx, i in images.items():
    byt = BytesIO()
    image = Image.open(BytesIO(base64.decodebytes(images.encode("utf-8"))))
    image.save(byt, 'PNG')
    byt.seek(0)
    await d.delete()
    await ctx.send(file=discord.File(fp=byt, filename=f"Image.png"))
    
@bot.command()
async def fm(ctx, num, name=None):
    r = requests.get(f"https://anime-api.hisoka17.repl.co/img/nsfw/boobs").json()
    ok = r["url"]
    p = requests.get(f"https://anime-api.hisoka17.repl.co/img/nsfw/hentai").json()
    no = p["url"]
    #q = requests.get(f"https://api.waifu.im/search/?included_tags={name}").json()
    #maybe= q["images"][0]["url"]
    if num=="1":
        await ctx.reply(ok)
    elif num=="2":
        await ctx.reply(no)
    #q = requests.get(f"https://api.waifu.im/search/?included_tags={name}").json()
    #maybe = q["images"][0]["url"]
    #elif num=="3":
        #await ctx.reply(maybe)
                    
@bot.command()
async def showcolor(ctx, *,color: discord.Color=None):
    color = color or ctx.author.color
    buff = await color_processing(color=color)

    await ctx.reply(file=discord.File(fp=buff, filename='color'))

@bot.command()
async def lookup(ctx, *,text):
    api = SafoneAPI()
    resp = await api.image(query=text, limit=1)
    await ctx.reply(resp["results"]["imageUrl"])

@bot.command()
async def lesgo(ctx, *,tags):












    r = requests.get(f"https://api.waifu.im/search?included_tags={tags}").json()
    req = r["images"][0]["url"]
    await ctx.reply(req)
    
@bot.event
async def on_reaction_add(reaction, user):
        # the user parameter is the person who adds the reaction
        if reaction.emoji == '⭐' and reaction.count == 1: # prevent the embed being added multiple times
            # check that the message is from Karuta
            message = reaction.message
            if message.author.id == 852585988936826910:
                content = message.content
                mentionList = message.mentions
                dropper = message.author # initially set to KarutaBot (assume server drop)
                # searches current guild (server) for first text-channel named 'pog-drops'
                channel = bot.get_channel(794075957463351296)
                if channel is None:
                    # did not find a text-channel named pog-drops in current guild
                    channel = message.channel
                    await channel.send(f'{user.mention}, please create a text-channel named **"pog-drops"** for me to record your pog drops!')
                    return
                # check for any mentions in this message. if there are none, it was a server drop.
                # otherwise this drop is from a user.
                if mentionList:
                    dropper = mentionList[0] # user who invoked the drop
                    # change content to remove the expiration, if any
                    # should be in the format {dropper} is dropping n cards!
                    content = content.split('!')[0] + '!'
                else:
                    # server drop
                    content = 'I\'m dropping 3 cards since this server is currently active!'
                try:
                    # create the embed
                    embed = discord.Embed(description=content, color=0xff0000)
                    embed.set_author(name=dropper.name, icon_url=dropper.avatar.url)
                    embed.set_image(url=message.attachments[0].url)
                    embed.add_field(name='\u2800', value=f'[**Jump to drop!**]({message.jump_url})', inline=False)
                    embed.set_footer(text = f' ⭐ {reaction.count} | # {message.channel.name}')
                    embed.timestamp = datetime.datetime.utcnow()
                    await channel.send(embed=embed)
                except:
                    pass


    
@bot.command()    
async def asauce(ctx, *,url):
        #url = "".join(args)
        res = requests.get(apI + url).json()
        entitle = res.get('docs')[0].get("title_english")
        nattitle = res.get('docs')[0].get("title_native")
        episodes = res.get('docs')[0].get("episode")
        season = res.get('docs')[0].get("season")
        malid = res.get('docs')[0].get("mal_id")
        perc = res.get('docs')[0].get("similarity")
        rperc = perc*100
        rperc = round(rperc,2)
        anime = jikan.anime(malid)
        imgurl = anime.get("image_url")
        embed = discord.Embed(
            title = 'getSauce',
            description = 'My top guess:',
            colour = ctx.guild.me.color
        )
        embed.add_field(name ='Similarity:', value = f'{rperc}',inline=False)
        embed.add_field(name = entitle + f' ({nattitle})', value = 'Episode: ' + str(episodes) + '\n Season: ' + str(season) + '\n MAL: ' + str(malu) + str(malid),inline= False)
        embed.set_footer(text='Sauce | Beta')
        embed.set_thumbnail(url = imgurl)
        await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def kiki(ctx):
    image = await nsfw("oppai")
    await ctx.reply(image)

@bot.command()
async def let(ctx):
    #image = await sfw(tag="waifu")
    image = await nsfw(tag="waifu")
    await ctx.send(image)  
    
@bot.hybrid_command()
async def onwhat(ctx, member:discord.Member=None):
    if member==None:
        member=ctx.author
    lo = member.is_on_mobile()
    if lo==False:
        lo="Theyre on PC/Laptop"
    else:
        lo="Theyre on Mobile"
        
    embed2=discord.Embed(title=member.name, url=member.avatar.url, color=ctx.guild.me.color, description=f">>> **Indicator: {member.raw_status}\n{lo}**")
    embed2.set_thumbnail(url=member.avatar.url)
    await ctx.send(embed=embed2)

@bot.command()
async def mycustomstatus(ctx):
    for s in ctx.author.activities:
        if isinstance(s, discord.CustomActivity):
            await ctx.sed(s)    

#@bot.command()
#async def tr(ctx, *,msg):
    #lang = "en"
    #if lang not in googletrans.LANGUAGES and lang not in googletrans.LANGCODES:
        #raise commands.BadArgument("Invalid language to translate text to")
    #text = ' '.join(msg)
    #translator = googletrans.Translator()
    #text_translated = translator.translate(text, dest=lang).text
    #await ctx.send(text_translated)
            
@bot.command()
async def sof(ctx, *,query:str):
    #import urllib.parse as urllib
    query = { 'q' : query}
    query = urllib.parse.urlencode(query)
    #import re
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"https://stackoverflow.com/search?{query}")
        mydata = await resp.text()
    links=re.findall(re.compile(r'<a href=(.*).* data-searchsession=.*>'),mydata)
    await ctx.reply(f"https://stackoverflow.com{links[0]}")

            
            
@bot.command()
async def gif(ctx,*,q="random"):

    api_key="PysQgdgNYJZ9ZNNUt9WkgyRCLWStWXWv"
    api_instance = giphy_client.DefaultApi()
    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random2.choice(lst)

        emb = discord.Embed(title=q, color=discord.Color.random())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

#logger = logging.getLogger("discord")
#logger.setLevel(logging.DEBUG)
#logger.addHandler(handler)
#handler.setLevel(logging.INFO)
@bot.command()
async def lego(ctx, *,args):
        await ctx.trigger_typing()
        
        image_url = await ctx.Parser.parse_image(ctx, args)
        lego_image = await ctx.lego(image_url, ctx.bot.http._HTTPClient__session)
        await ctx.send_image(lego_image)
        del image_url, lego_image
        collect()

@bot.command()
async def newtl(ctx, *,text):
    translator = google_translator()  
    translate_text = translator.translate(text, lang_src='auto', lang_tgt='en')  
    await ctx.reply(translate_text)

@bot.command()
async def jmsmskk(ctx):
    r="https://pic.re/image"
    embed=discord.Embed(title="Wallpaper", color=ctx.guild.me.color)
    embed.set_image(url=r)
    await ctx.send(embed=embed)
    
@bot.command()
async def goog(ctx, *, something):
    await ctx.message.add_reaction("🔍")
    #await ctx.trigger_typing()
    lo = await sus.search(something, safesearch=False)
    a = lo[:3]
    embed=discord.Embed(color=ctx.guild.me.color)
    await ctx.message.clear_reactions()
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
    #for i in a:
        #embed.add_field(name=i.title, value=f"{i.description}")
    #test = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.blue, label="Image"), Button(style=ButtonStyle.red, label="Show URL"),]],)
    #def check(res):
        #return res.user == ctx.author and res.message.id == test.id
    #while True:
        #ez = await bot.wait_for("button_click", check=check)
        #if ez.component.label=="Image":
            #hm = lo[0]
            #embed2=discord.Embed(color=ctx.guild.me.color)
            #embed2.set_image(url=hm.image_url)
            #await test.edit(embed=embed2, components=[Button(style=ButtonStyle.grey, label="Back"),],)
        #elif ez.component.label=="Back":
            #await test.edit(embed=embed, components=[[Button(style=ButtonStyle.blue, label="Image"), Button(style=ButtonStyle.red, label="Show URL"),]],)
        #elif ez.component.label=="Show URL":
           # for i in a:
            #embed3=discord.Embed(color=ctx.guild.me.color)
            #embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
            #for i in a:
                #embed3.add_field(name=i.title, value=f"{i.url}\n{i.description}")
            #await test.edit(embed=embed3, components=[])

@bot.command()
async def archive(ctx):
    lo = ctx.message.reference.resolved.content
    await ctx.author.send(lo)
    await ctx.message.delete()

#@bot.listen('on_message')
#async def lmaonew(message):
    #if message.content==("<@304911836460089345>"):
       # l = await message.reply("congratz you unlocked the rickroll")
       # await asyncio.sleep(0.7)
        #await l.edit("https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173", delete_after=0.5)
    
@bot.event
async def on_user_update(before, after):
    embed=discord.Embed(title=f"Old Avatar of {before.author.name} ---->", color=before.guild.me.color)
    embed.set_image(url=after.avatar.url)
    embed.set_thumbnail(url=before.avatar.url)
    channel = bot.get_channel(794080301604798515)
    await channel.send(embed=embed)
        

@bot.command()
async def activity(ctx, *,someone:discord.Member):
    #someone = ctx.author if not someone else someone
    await ctx.reply(someone.CustomActivity)
        
@bot.command()
async def newimg(ctx):
    my_string = "Hello, world! 👋 Here are some emojis: 🎨 🌊 😎I also support Discord emoji"

    with Image.new('RGB', (550, 80), (255, 255, 255)) as image:
        font = ImageFont.truetype('impact.ttf', 24)

        with Pilmoji(image) as pilmoji:
            pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)

        await ctx.reply(file=discord.File(image))
        
@bot.command()
@commands.is_owner()
async def ssweb(ctx, *,url):
    embed=discord.Embed(title="Screenshot", color=ctx.guild.me.color)
  #  params = urlencode(dict(access_key="9MAZWKE-ADAMKF9-GG7C1YV-XXKPN67",
                        #url=url))
    #lo = requests.get(f"https://shot.screenshotapi.net/screenshot?token=9MAZWKE-ADAMKF9-GG7C1YV-XXKPN67&url={url}").json()
   # lmao = lo["screenshot"]
    lmao = f"https://image.thum.io/get/{url}"
    urlretrieve(lmao, "screenshot.jpeg")
    #urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")
    #embed.set_image(url=f"https://api.apiflash.com/v1/urltoimage?access_key=dd7de7a83811421a9c18dd2a3b46979&url={url}")
    await ctx.reply(embed=embed, file=discord.File("screenshot.jpeg"))

@bot.hybrid_command()
async def shorten(ctx, *, url):
    r = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
    await ctx.reply(r.text)

@bot.command()
async def ech(ctx):
    r = requests.get(f"https://api.waifu.pics/nsfw/waifu)").json()
    lo = r["url"]
    await ctx.reply(lo)
    
@bot.command()
async def expand(ctx, *, url):
    r = requests.get(f"http://expandurl.com/api/v1/?url={url}")
    await ctx.reply(r.text)
    
@bot.command()
async def typerace(ctx):
    starttime = time.time()
    r = requests.get("http://api.quotable.io/random").json()
    lo = r["content"]
    answer = lo
    timer = 17.0
    await ctx.send(f"You have {timer} seconds to type: {answer}")

    def is_correct(msg):
        return msg.author==ctx.author

    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=timer)
    except asyncio.TimeoutError:
        return await ctx.send("You took too long :(")

    if guess.content == answer:
        await ctx.send("You got it!")
        fintime = time.time()
        total = fintime - starttime
        await ctx.send(f"{round(total)} seconds")

    else:
        await ctx.send("Nope, that wasn't really right")
        fintime = time.time()
        total = fintime - starttime
        await ctx.send(f"{round(total)} seconds")

bot.searches = {}
        
@bot.command()
@commands.is_owner()
async def lonew(ctx, *, search:str):

        response = google_images_download.googleimagesdownload()
        arguments = {"keywords":search, "no_download":True}
        print(arguments)
        image_urls = response.download(arguments)

        if ctx.guild.id in bot.searches:
            if bot.searches[ctx.guild.id] is not None:
                l = bot.searches[ctx.guild.id]
                l.update(image_urls[0])
                bot.searches[ctx.guild.id] = l
        else:
            bot.searches[ctx.guild.id] = []
            bot.searches[ctx.guild.id] = image_urls[0]

        maxPage = int(len(bot.searches[ctx.guild.id][search]))

        firstRun = True
        while True:
            if firstRun:
                firstRun = False
                num = 1

                url=bot.searches[ctx.guild.id][search][0]
                msg = await ctx.send(url)

            if maxPage == 1 and num == 1:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['✅']
            elif num == 1:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏩', '✅']
            elif num == maxPage:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏪', '✅']
            elif num > 1 and num < maxPage:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏪', '⏩', '✅']

            for reaction in toReact:
                await msg.add_reaction(reaction)
            
            def checkReaction(reaction, user):
                e = str(reaction.emoji)
                return e.startswith(('⏪', '⏩', '✅')) and reaction.message.id == msg.id and user.id != msg.author.id
            try:
                res = await bot.wait_for('reaction_add', timeout=60, check=checkReaction)
                if res is None:
                    await ctx.message.delete()
                    await msg.delete()
                    break
                elif res[0].emoji == '⏪':
                    num = num - 1

                    url=bot.searches[ctx.guild.id][search][num-1]
                    await msg.delete()
                    msg = await ctx.channel.send(url)
                elif res[0].emoji == '⏩':
                    num = num + 1
                    
                    url=bot.searches[ctx.guild.id][search][num-1]
                    await msg.delete()
                    msg = await ctx.channel.send(url)
                elif res[0].emoji == '✅':
                    await msg.clear_reactions()
                    break
            except:
                await msg.clear_reactions()
                break
        
@bot.command()
@commands.is_owner()
async def secret(ctx, *,ep):
    r = requests.get(f"https://nekos.life/api/v2/img/{ep}").json()
    lo = r["url"]
    await ctx.reply(lo)
        
@bot.command()
async def whoasked(ctx):
    await ctx.message.delete()
    await ctx.send("ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Who asked (Feat: No one)\n───────────:white_circle:────── ◄◄⠀▐▐ ⠀►► 5:12/ 7:𝟻𝟼 ───○ :loud_sound:⠀ ᴴᴰ :gear:", reference=ctx.message.reference)
        
@bot.command()
async def yeet(ctx):
    #async for message in channel.history(limit=num):
    await ctx.message.reference.resolved.delete()
   # await reference.delete()
    await ctx.message.delete()

@bot.command()
async def instagram(ctx, *,username):
    r = requests.get(f"https://api.popcat.xyz/instagram?user={username}").json()
    name = r["username"]
    full = r["full_name"]
    bio = r["biography"]
    post = r["posts"]
    reel = r["reels"]
    f1 = r["following"]
    f2 = r["followers"]
    priv = r["private"]
    ver = r["verified"]
    pfp = r["profile_pic"]
    embed = discord.Embed(title=name, description=full, color=ctx.guild.me.color)
    embed.add_field(name="Bio", value=bio)
    embed.add_field(name="Posts", value=post)
    embed.add_field(name="Reels", value=reel)
    embed.add_field(name="Verified?", value=ver)
    embed.set_thumbnail(url=pfp)
    embed2=discord.Embed(title=name, description=full, color=ctx.guild.me.color)
    embed2.add_field(name="Followers", value=f2)
    embed2.add_field(name="Following", value=f1)
    embed2.add_field(name="Private?", value=priv)
    embed3=discord.Embed(title=name, color=ctx.guild.me.color)
    embed3.set_image(url=pfp)
    embed2.set_thumbnail(url=pfp)
    #a = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="Next"), Button(style=ButtonStyle.blue, label="Show pic"),]],)
    #def check(res):
        #return res.user == ctx.author and res.message.id == a.id
    #while True:
        #lmao = await bot.wait_for("button_click", check=check, timeout=10)
        #try:
            #if lmao.component.label=="Next":
                #await a.edit(embed=embed2, components=[[Button(style=ButtonStyle.green, label="Back"), Button(style=ButtonStyle.red, label="Show pic"),]],)
            #elif lmao.component.label=="Back":
                #await a.edit(embed=embed, components=[[Button(style=ButtonStyle.green, label="Next"), Button(style=ButtonStyle.red, label="Show pic"),]],)
            #elif lmao.component.label=="Show pic":
                #await a.edit(embed=embed3, components=[Button(style=ButtonStyle.red, label="Go Back"),],)
            #elif lmao.component.label=="Go Back":
                #await a.edit(embed=embed, components=[[Button(style=ButtonStyle.green, label="Next"), Button(style=ButtonStyle.red, label="Show Pic"),]],)
        #except asyncio.TimeoutError:
            #await ctx.send("oops")
            #await a.delete()
            #await ctx.message.delete()
    
    
@bot.command()
async def pls(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/336642776609456130/881046859479650374/unknown.png", reference=ctx.message.reference)
    
@bot.command()
async def error(ctx):
    await ctx.message.delete()
    await ctx.send("**`error!!\njoke not processed, please try again later`**", reference=ctx.message.reference)
    
@bot.command()
@commands.is_owner()
async def uhm(ctx):
    image = await flush.randpost(['thighhighs'])
    await ctx.reply(image)
    
@bot.command()
@commands.is_owner()
async def one(ctx, *, query):
    data = api.image(query)
    image = data["result"]
    r = random2.choice(image)
    await ctx.reply(r)
    
@bot.command()
@commands.is_owner()
async def hh(ctx):
    data = api.hentai()
    result = random2.choice(data["result"])
    await ctx.reply(result)

@bot.command()
@commands.is_owner()
async def pornstar(ctx):
    data = api.pornstar()
    stars = random2.choice(data["result"])
    embed = discord.Embed(title=stars["pornstar"], color=ctx.guild.me.color)
    embed.add_field(name="Gender", value=stars["gender"])
    embed.add_field(name="Country", value=stars["country"])
    lo = stars["gender"]
    if stars["gender"]=="Female":
        embed.add_field(name="Breast", value=stars["breast"])
        embed.add_field(name="Tits", value=stars["tits"])
    elif stars["gender"]=="Male":
        embed.add_field(name="Dick", value=stars["dick"])
    embed.set_image(url=stars["image"])
    await ctx.reply(embed=embed)
    
    
@bot.command()
@commands.is_owner()
async def ss(ctx, *, something):
    data = api.screenshot(something)
    embed=discord.Embed(title="Result", color=discord.Color.random())
    embed.set_image(url=data["result"]["mobile"])
    await ctx.reply(embed=embed)
    
@bot.command()
@commands.is_owner()
async def findlyric(ctx, *,that):
    data = api.lyric(that)
    embed=discord.Embed(title="yeet", description=data["result"]["lyric"], color=discord.Color.random())
    await ctx.reply(embed=embed)
    
@bot.command()
@commands.is_owner()
async def nwall(ctx):
    data = api.wallpaper("nude")
    r = random2.choice(data["result"])
    await ctx.reply(r)

@bot.command()
@commands.is_owner()
async def na(ctx, *,ohyes):
    data = api.porn(ohyes)
    embed=discord.Embed(title=data["result"]["title"], color=discord.Color.random())
    embed.add_field(name="Duration", value=data["result"]["duration"])
    embed.add_field(name="Quality", value=data["result"]["quality"])
    embed.add_field(name="Watched", value=data["result"]["watched"])
    embed.add_field(name="Link", value=data["result"]["videoUrl"])
    embed.set_image(url=data["result"]["thumbnail"])
    await ctx.reply(embed=embed)

@bot.command()
async def hotmeme(ctx, *, text):
    o, t = text.split("|")
    text1 = o
    text2 = t
    lo = ctx.author.avatar.url
    imageUrl = lo #"http://www.gstatic.com/webp/gallery/1.png"
    data = api.meme(text1,text2,imageUrl)
    result = data["result"]
    await ctx.reply(result)

@bot.command()
@commands.is_owner()
async def thigh(ctx):
    await ctx.reply(badonker.random())

@bot.command()
async def closematch(ctx, *,m):
    member = discord.utils.get(ctx.guild.members, name=f"{m}")
    await ctx.reply(member.mention)

@bot.event
async def on_guild_role_create(role):
    channel = bot.get_channel(794080301604798515)
    embed=discord.Embed(title="New Role was created!", color=role.color)
    embed.add_field(name="Role", value=role.mention)
    await channel.send(embed=embed)
    
    
@bot.command()
async def rtfm(ctx, *,doc):

        embed = discord.Embed(title="a",description = f"__Results found for {doc}__:", color = 0x5865f2)
        embed.set_footer(text = ctx.author, icon_url= ctx.author.avatar.url)

        scraper = AsyncScraper()

        async def main(query):
            results = await scraper.search(query, page="https://discordpy.readthedocs.io/en/latest")
    
            if not results:
                await ctx.reply(embed = discord.Embed(title="ok", description = "No results found for this search.", color =0xFF0000),mention_author = False)
                return
            
            else:
                for item, url in results[:5]:    
                    embed.add_field(name = "\u200b", value = f"[{item}]({url})")

        await main(doc)
        await ctx.reply(embed = embed,mention_author = False)

    
    
#@bot.command()
#@commands.is_owner()
#async def eval(ctx, code: jishaku.codeblocks.CodeblockConverter):
   # await ctx.invoke(bot.get_command("jsk py", argument=code)
#api_key="AIzaSyBvgM2fduljYnlnyICjXRfuFvbu9-EaxRY"
#@bot.command()
#async def classic(ctx):
    #code = genx.nitro()
   # await ctx.reply(code)

#@bot.command()
#async def showpic(ctx, *, search):
    #ran = random2.randint(0, 9)
    #resource = build("customsearch", "v1", developerKey=api_key).cse()
   # result = resource.list(
     # q=f"{search}", cx="81f10f03a6f873ee2", searchType="image"
   #  ).execute()
  #  url = result["items"][ran]["link"]
   #embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
   # embed1.set_image(url=url)
  #  await ctx.reply(embed=embed1)
webhook_url = "https://discord.com/api/webhooks/872172597431906426/CVSSr_DMQO_BlICLr2YQXbGjSzk0ifFuZXC1xkMPHb7Q4PgcJbn0HHpOBdaNWjrqI6ce"
options = {
    "application_name": "Logger",
    "service_name": "Glitch",
    "service_icon.url": "https://images-ext-2.discordapp.net/external/JpzT57C1DbMXeAAcsYu19NoiDmqbcmLWLJm5LsjmHs8/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/396277862459768843/54b91bdd518744f196e51a658667545c.webp",
    "service_environment": "Production",
    "default_level": "info",
}

logger = DiscordLogger(webhook_url=webhook_url, **options)
logger.construct(
    title="Health Check",
    description="Issue in establishing DB connections!",
    error="Traceback (most recent call last):\n ValueError: Database connect accepts only string as a parameter!",
    metadata={"module": "DBConnector", "host": 123.332},
)

response = logger.send()

#@bot.command()
#async def rtfm(ctx, *,query):
    #embed = discord.Embed(title="Sucess", description = f"__Results found for {doc}__:", color = 0x5865f2)
    #embed.set_footer(text = ctx.author, icon = ctx.author.avatar.url)
    #scraper = AsyncScraper()
    #async def main(query):
        #results = await scraper.search(query, page="https://discordpy.readthedocs.io/en/latest")
        #if not results:
            #await ctx.reply(embed = discord.Embed(title="💀", description = "No results found for this search.", color =0xFF0000)
            #return
        #else:
            #for item, url in results[:5]:    
               # embed.add_field(name = "\u200b", value = f"[{item}]({url})")
    #await main(doc)
    #await ctx.reply(embed = embed,mention_author = False) 


@bot.listen('on_message')
async def deggs(message):
    lo = ["deggs", "deggstard", "dextoad"]
    ye = ["thats crazy", "that's crazy", "Thats crazy", "That's crazy"]
    hm = ["burgure", "el pepe"]
    if message.content in hm:
        await message.reply("that fucking loser still alive?")
    elif message.content in lo:
        await message.reply("shut up loser", delete_after=0.5)
    elif message.content in ye:
        await message.channel.send("https://tenor.com/view/yoo-that-crazy-did-iask-idont-remember-askng-dr-fate-injustice2-gif-16579106")

@bot.command()
@commands.is_owner()
async def serverlogs(ctx):
    guild = ctx.guild
    entries = guild.audit_logs(limit=10)
    for entry in entries:
        lo = "\n"
        await ctx.reply(", ".join(entry))


MAX_URLS_TO_SEARCH = 2000
URL = 'https://www.google.com/search?q=hot+anime+waifu+&tbm=isch&ved=2ahUKEwiytvHXv4DvAhXrK7cAHSZXBUoQ2-cCegQIABAA&oq=hot+anime+waifu+&gs_lcp=CgNpbWcQA1CZM1iZM2DWNGgAcAB4AIABVIgBVJIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=xTY1YPK_E-vX3LUPpq6V0AQ&bih=763&biw=1536'

@bot.command()
@commands.is_owner()
async def bar(ctx):
    with open("users.json", "r") as f:
        users = json.load(f)
    lvl = users[str(ctx.guild.id)][str(ctx.author.id)]['level']
    exp = users[str(ctx.guild.id)][str(ctx.author.id)]['experience']
    lo = int(lvl + 1)
    new = int(lo**4)
    try:
        await ctx.send(f"{progressBar.createBoxDiscord(exp, new, 20)}")
    except Exception as error:
        print(error)
        
bl = ["304911836460089345"]

#@bot.check
#async def blacklist(ctx):
    ##if str(ctx.author.id) in bl:
       # await ctx.reply("oops youre blacklisted")
async def save_audit_logs(guild):
    with open(f'audit_logs_{guild.name}', 'w+') as f:
        async for entry in guild.audit_logs(limit=100):
            f.write('\n{0.user} did {0.action} to {0.target}'.format(entry))

@bot.listen('on_message')
async def logs(message):
     if message.content.startswith('$AUDIT$'):
        await save_audit_logs(message.channel.guild)
        await message.reply("ight yo")

@bot.command()
async def ami(ctx):
     await ctx.reply("nah all good")

@bot.command()
async def stackoverflow(ctx, query:str):
    #import urllib.parse as urllib
    query = { 'q' : query}
    query = urllib.urlencode(query)
    import re
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"https://stackoverflow.com/search?{query}")
        mydata = await resp.text()
    links=re.findall(re.compile(r'<a href=(.*).* data-searchsession=.*>'),mydata)
    await ctx.reply(f"https://stackoverflow.com{links[0][1:-1]}")
        
        
        
@bot.command()
async def triggered(ctx, user:discord.Member=None):
    user = ctx.author if not user else user
    image = await trigger(user)
    file = discord.File(filename="triggered.gif", fp=image)
    await ctx.reply(file=file)        
        
@bot.command(aliases=["rank"])
async def level(ctx, *,member:discord.Member=None):
    bg = ["https://media.discordapp.net/attachments/794075957463351296/872300144345886781/0001-5323858189_20210804_073913_0000.png", "https://media.discordapp.net/attachments/794075957463351296/872372740852711434/pexels-johannes-plenio-1103970.jpg", "https://media.discordapp.net/attachments/794075957463351296/872372686867824650/polygonal19.jpg", "https://media.discordapp.net/attachments/794075957463351296/872372741171445770/pawel-czerwinski-6lQDFGOB1iw-unsplash.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374851548086312/8a0c8bf92fd1be7e90a007da1336b10c.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374851875246121/428471d4f6c147b88ee7c2cff3efc4cb.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374852122730516/b9ba446cca2bb06ff1a8d49fd46581ed.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374852294705152/d76aa42f9ea1749b709102be1c93f130.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374852495998997/7f3cb35ea078264bfdac8242939a919f.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374852663775232/6ed2075c4e7043e26694b2154e701449.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374852831567914/126417ad870c75dffeb80e6c6ae14969.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374853045485568/ce491e29535fce05266b83d04b3cc4e2.jpg", "https://media.discordapp.net/attachments/794075957463351296/872374853263573002/b006a825794ce16bd38211c883a090e8.jpg"]
    newbg = random2.choice(bg)
    await ctx.trigger_typing()
    with open("users.json", "r") as f:
        users = json.load(f)
    #with open("bg.json", "r") as f:
        #bgg = json.load(f)
    member = ctx.author if not member else member
    exp = users[str(ctx.guild.id)][str(member.id)]["experience"]
    lvl = users[str(ctx.guild.id)][str(member.id)]["level"]
    e = int(exp)
    a = int(lvl)
    newlo = int(a + 1)
    lo = int(newlo**4)
    okk = int(lo)
    user = member
    if len(member.name) > 10:
        lo = f"{member.name[:9]}.."
        username = lo
    else:
        lo = member.name
        username = lo + "#" + member.discriminator
    currentxp = e
    lastxp = 0
    nextxp = okk
    current_level = a
    current_rank = "-"
   # oh = bgg[str(member.id)]["bg"]
    #if str(member.id) in bgg:
        #background = oh
    #elif member.id not in bgg:
    background = newbg
    image = await rankcard(user=user, username=username, currentxp=currentxp, lastxp=lastxp, nextxp=nextxp, level=current_level, rank=current_rank, background=background)
    file = discord.File(filename="rankcard.png", fp=image)
    await ctx.reply(file=file)        

    
##logger = logging.getLogger()

##WEBHOOK_URL = "https://discord.com/api/webhooks/872172597431906426/CVSSr_DMQO_BlICLr2YQXbGjSzk0ifFuZXC1xkMPHb7Q4PgcJbn0HHpOBdaNWjrqI6ce"
#handler = discord_logging.Discord_Handler(WEBHOOK_URL)

#logger.addHandler(handler)     
@bot.command(aliases=["unrr"])
async def unrickroll(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/710528752911777934/874940657867825182/88e.jpg")

@bot.command()
@commands.is_owner()
async def blacklist(ctx, member:discord.Member):
    with open("blist.json", "r") as f:
        blacklist = json.load(f)
    if not member.id in blacklist.keys():
        blacklist["blacklist"] = {}
        blacklist["blacklist"] = member.id
    else:
        await ctx.reply("they are already blisted")
        return
    with open("blist.json", "w") as f:
        json.dump(blacklist, f, sort_keys=True)
    await ctx.reply("done")

@bot.command()
async def chat(ctx, *, message):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://dinosaur.ml/misc/chatbot/?msg={message}") as r:
            lo = await r.json()
            hm = lo["url"]
            await ctx.reply(hm)
    
@bot.command()
@commands.is_owner()
async def whitelist(ctx, member:discord.Member):
    with open("blist.json", "r") as f:
        blacklist = json.load(f)
    if member.id in blacklist.keys():
        del blacklist["blacklist"][member.id]
        await ctx.reply("ight")
        with open("blist.json", "w") as f:
            json.dump(blacklist, f, sort_keys=True)
    else:
        await ctx.reply("they were never blisted")

@bot.command()
#@commands.is_owner()
async def custombg(ctx, *, url):
    with open("bg.json", "r") as f:
        users = json.load(f)
    if not ctx.author in users:
        users[str(ctx.author.id)] = {}
        users[str(ctx.author.id)]["bg"] = url
    else:
        del users[str(ctx.author.id)]["bg"]
        await ctx.reply("deleted")
    #if ctx.author in users:
        #del users[str(ctx.guild.id)][(ctx.author.id)]["bg"]
    with open("bg.json", "w") as f:
        json.dump(users, f, sort_keys=True)
    await ctx.reply("ight")

@bot.command()
async def checkbg(ctx, member:discord.Member=None):
    if member==None:
        member=ctx.author
    with open("bg.json", "r") as f:
        users = json.load(f)
    bg = users[str(member.id)]["bg"]
    if str(member.id) in users:
        await ctx.reply(bg)
    elif member.id not in users:
        await ctx.reply("no")

@bot.command()
@commands.is_owner()
async def wow(ctx):
    args = {
	'bg_image' : 'https://media.discordapp.net/attachments/794075957463351296/872300144345886781/0001-5323858189_20210804_073913_0000.png', # Background image link 
	'profile_image' : lo, # User profile picture link
	'level' : 1, # User current level 
	'current_xp' : 0, # Current level minimum xp 
	'user_xp' : 10, # User current xp
	'next_xp' : 100, # xp required for next level
	'user_position' : 1, # User position in leaderboard
	'user_name' : 'lo#2929', # user name with descriminator 
	'user_status' : 'online', # User status eg. online, offline, idle, streaming, dnd
     }

    image = Generator().generate_profile(**args)
    file = discord.File(fp=image, filename='image.png')
    await ctx.send(file=file)
    
    
@bot.command()
async def recommend(ctx, *,anime):
    await ctx.message.add_reaction("<a:loading:852455265738817556>")
    try:
        result = Anime(anime)
    except:
        await ctx.reply("couldn't find the anime or any recommendations over it")
        await ctx.message.clear_reactions()
    lo='\n'
    embed=discord.Embed(title=result.title_english, url=result.url, color=discord.Color.random())
    try:
        embed.add_field(name="I'd Recommend:", value=f"{lo.join(result.recommend())}")
    except:
        embed.add_field(name="I'd Recommend:", value=f"{lo.join(result.recommend()[0])}")
    embed.set_thumbnail(url=result.poster)
    #pp=await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.blue, label="DM"),]],)
    #await ctx.message.clear_reactions()
    #def check(res):
        #return ctx.author==res.user and res.channel==ctx.channel and res.message.id==pp.id
    #butt=await bot.wait_for("button_click", check=check)
    #if butt.component.label=="DM":
        #await ctx.author.send(embed=embed, components=[])
        #await pp.edit(embed=embed, components=[Button(style=ButtonStyle.blue, label="DMED IT", disabled=True),],)
    
        
@bot.command()
async def lyrics(ctx, *, arg):
        await ctx.trigger_typing()
        data = requests.get(f"https://some-random-api.ml/lyrics?title={arg}").text
        try:
            jsontxt = json.loads(data)
            title = jsontxt["title"]
            author = jsontxt["author"]
            lyrics = jsontxt["lyrics"]
            #lo = jsontext["thumbnail"]["genius"]
        except:
            await ctx.reply("Sorry, I can't found the lyrics for the song you mentioned.")
            print("Error occured | "+str(e) + " | "+str(data))
        try:
            embed = discord.Embed(
                title = f":musical_note: Lyrics | {title} | {author}",
                description = lyrics if len(lyrics) <= 4096 else lyrics[:4096],
                timestamp=ctx.message.created_at,
                color = discord.Color.random()
            )
            #try:
                #embed.set_thumbnail(url=lo)
            #except:
                #pass
            await ctx.reply(embed = embed)
            if len(lyrics) > 4096:
                embed2=discord.Embed(title="Continuation", description=lyrics[4096:], color=discord.Color.random())
                await ctx.send(embed=embed2)
        except Exception as e:
            print("error")

@bot.command()
async def idk(ctx, *,name):
    image = await new.get_image(name)
    await ctx.reply(image.image)
    embed=discord.Embed(title="Random", color=discord.Color.random())
    embed.set_image(url=image.image)
    await ctx.reply(embed=embed)

@bot.command()
async def slash99(ctx):
    r = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    a = r['id']
    b = r['type']
    c = r['setup']
    d = r['punchline']
    embed = discord.Embed(title=f"{b} type!", description=f"**{c}\n\n||{d}||**", color=discord.Color.random())
    embed.set_footer(text=f"#{a}")
    await ctx.send(embed=embed)

#@bot.command()
#async def chat(ctx):
   # def check(m):
      #  return m.user==ctx.author and m.channel==ctx.channel
   # while True:
      #  lmao = await bot.wait_for('message', check=check)
      #  if lmao.content=="quit":
      #      return await ctx.reply("ok cya")
      #  lol = requests.get(f"https://dinosaur.ml/misc/chatbot/?msg={lmao.content}").json()
      #  auto = lol['msg']
      #  await lmao.reply(auto)#

@bot.command()
async def message(ctx, message: discord.Message):
        #lo = ["Here"]("https:discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}
        Embed=discord.Embed(title=f"In {message.channel.name} by {message.author.name}", description=f"**[Here]({message.jump_url})\n{message.content}**", color=0x5865f2)
        await ctx.reply(embed=Embed)
        
@bot.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.reply("Restarting bot...")
    os.system('clear')
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
@commands.is_owner()
async def imgsearch(ctx, *,name=None):
    query = "toulouse pink city"

    r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 50,
        'q': query,
        't': 'images',
        'safesearch': 1,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    print(random2.choice(urls))
    
@bot.command()
@commands.is_owner()
async def stfulevel(ctx, *,user:discord.Member=None):
    if user==None:
        user = ctx.author
        #await ctx.trigger_typing()
        with open('users.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']
        m = lvl+1
        lo = m**4
        embed=discord.Embed(description=f"> **Level: `{lvl}`**\n> **Exp: `{exp}/{lo}`**", color=discord.Color.random())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        #embed.set_thumbnail(url="https://media.discordapp.net/attachments/794075957463351296/870187980080447518/Screenshot_20210729-114544.jpg")
        embed.add_field(name="Progress", value=f"{progressBar.createBoxDiscord(exp, lo, 20)}")
        await ctx.reply(embed=embed)
        return
        #await ctx.reply(f"Level: {lvl}\nExp: {exp}")
    else:
        with open('users.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']
        a=lvl+1
        e=a**4
        embed=discord.Embed(description=f"> **Level: `{lvl}`**\n> **Exp: `{exp}/{e}`**", color=discord.Color.random())
        embed.set_author(name=user.name, icon_url=user.avatar.url)
        #embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(name="Progress", value=f"{progressBar.createBoxDiscord(exp, e, 20)}")
        await ctx.reply(embed=embed)
        return
        #await ctx.reply(f"Level: {lvl}\nExp: {exp}")
    yes =["1", "2"]
    e = random2.choice(yes)
    if e=="1":
        img = Image.open("rank.png")
    elif e=="2":
        img = Image.open("rank2.png")
    #elif e=="3":
        #mg = Image.open("rank4.png")
    #elif e=="4":
        #img = Image.open("rank5.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("LEMONMILK-Regular.otf", 215)
        #p=["1", "2"]
        #lo=random2.choice(p)
    lo = f"{lvl}"
    ep = f"{exp}"
    #if e=="3":
        #draw.text((885, 75), lo, (255, 0, 0), font=font)
        #draw.text((885, 325), ep, (255, 0, 0), font=font)
    #else:
    draw.text((885,75), lo, (255, 255, 255), font=font)
    draw.text((885,325), ep, (255, 255, 255), font=font)
    img.save("level.png")
    await ctx.reply(file=discord.File("level.png"))
    
@bot.hybrid_command()
async def define(ctx, *, search: commands.clean_content):
        """ Find the 'best' definition to your words """
        async with ctx.channel.typing():
            try:
                url = requests.get(f"https://api.urbandictionary.com/v0/define?term={search}").json()
            except Exception:
                return await ctx.send("Urban API returned invalid data... might be down atm.")

            if not url:
                return await ctx.send("I think the API broke...")

            if not len(url["list"]):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url["list"], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result["definition"]
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(" ", 1)[0]
                definition += "..."

            await ctx.reply(f"📚 Definitions for **{result['word']}**```fix\n{definition}```")

@bot.command()
async def homo(ctx):
    embed=discord.Embed(title="homo", color=ctx.author.color)
    await ctx.reply(embed=embed)
    embed.add_field(name="You?", value="yes")
    
@bot.command()
async def oldafping(ctx):
        """ Pong! """
        pings = []
        number = 0
        typings = time.monotonic()
        await ctx.trigger_typing()
        typinge = time.monotonic()
        typingms = round((typinge - typings) * 1000)
        pings.append(typingms)
        latencyms = round(bot.latency * 1000)
        pings.append(latencyms)
        discords = time.monotonic()
        url = "https://discord.com/"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as resp:
                if resp.status==200:
                    discorde = time.monotonic()
                    discordms = round((discorde-discords)*1000)
                    pings.append(discordms)
                    discordms = f"{discordms}ms"
                else:
                    discordms = "Failed"
            for ms in pings:
                number += ms
            average = round(number / len(pings))
            embed=discord.Embed(title="**__Ping__**", description=f"**<a:loading:852455265738817556> Calculated latencies:\n\n• Typing: `{typingms}ms` \n• Latency: `{latencyms}ms`\n• Discord: `{discordms}` \n• Average: `{average}ms`**", color=ctx.guild.me.color)
            this=await ctx.reply(embed=embed)
           # await asyncio.sleep(0.5)
            #embed2=discord.Embed(title="**__Ping__**", description=f"**Typing: `{typingms}ms` • Latency: `{latencyms}ms`\nDiscord: `{discordms}` • Average: `{average}ms`**", color=ctx.author.color)
           # await this.edit(embed=embed2)
    
    
    
@bot.command()
async def mods(ctx):
        """ Check which mods are online on current guild """
        message = ""
        all_status = {
            "online": {"users": [], "emoji": "🟢"},
            "idle": {"users": [], "emoji": "🟡"},
            "dnd": {"users": [], "emoji": "🔴"},
            "offline": {"users": [], "emoji": "⚫"}
        }

        for user in ctx.guild.members:
            user_perm = ctx.channel.permissions_for(user)
            if user_perm.kick_members or user_perm.ban_members:
                if not user.bot:
                    all_status[str(user.status)]["users"].append(f"**{user}**")

        for g in all_status:
            if all_status[g]["users"]:
                message += f"{all_status[g]['emoji']} {', '.join(all_status[g]['users'])}\n"

        await ctx.reply(f"Mods in **{ctx.guild.name}**\n{message}")
    
@bot.command()
async def mix(ctx):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(title="<:nhentai:865543197118824508>", color=discord.Color.random())
        embed.set_image(url=hmtai.useHM(version="custom", category="Vein05"))
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("nice nsfw channel 😈")
        
@bot.command()
@commands.is_owner()
async def wtf(ctx, *,ok):
    if ok in ["4k", "ass", "boobs", "bj", "cum", "feet", "hentai", "wallpapers", "spank", "gasm", "pussy", "bellevid"]:
        r = requests.get(f"http://api.nekos.fun:8080/api/{ok}").json()
        lo = r["image"]
        await ctx.reply(lo)
    else:
        await ctx.reply("4k ass boobs bj cum feet hentai wallpapers spank gasm pussy bellevid")
        
@bot.command()
async def newg(ctx, *,query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    e=gresults['links']
    await ctx.reply(e)

@bot.hybrid_command()
async def cemoji(ctx, link, *, name):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis:
        r = requests.get(link)
        img = Image.open(BytesIO(r.content), mode='r')
    try:
        img.seek(1)

    except EOFError:
        is_animated = False

    else:
        is_animated = True

    if is_animated == True:
        await ctx.send(":x: Animated emoji **not** supported")

    elif is_animated == False:
        b = BytesIO()
        img.save(b, format='PNG')
        b_value = b.getvalue()
        emoji = await guild.create_custom_emoji(image=b_value, name=name)
        em = discord.Embed(title=f":white_check_mark: New emoji created!", description=f"<:{name}:{emoji.id}>\n")
        em.set_footer(text=f"Emoji created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        await ctx.reply(embed=em)
    
    
@bot.command()
async def coder(ctx):
    e= pyjokes.get_joke()
    await ctx.reply(f"**{e}**")

#@bot.event
#async def on_member_join(member):
   # user = bot.get_user(304911836460089345)
   # inviter = await tracker.fetch_inviter(member)
  #  print(inviter)
  #  try:
   ##     await user.send(f"{inviter} invited {member}")
    #except:
      #  channel=bot.get_channel(800064480293027840)
       # await channel.send(f"{inviter} invited {member}")

#@slash.slash(name="topic", description="Gets a random topic", guild_ids=guild_ids)
@bot.hybrid_command()
async def newtopic(ctx):
    r=requests.get("https://dinosaur.ml/random/topic/").json()
    lolu = r['topic']
    embed=discord.Embed(title=lolu, color=discord.Color.random())
    await ctx.send(embed=embed)

@bot.command()
async def gimg(ctx, *, something):
    await ctx.trigger_typing()
    await ctx.message.add_reaction("🔍")
    some = something.replace(" ", "20%")
    try:
        r = requests.get(f"https://normal-api.ml/image-search?query={some}&redirect=false").json()
        lo = r["image"]
    except:
        lo = "https://tenor.com/view/error-glitch-gif-17863214"
    embed=discord.Embed(title=something, color=ctx.guild.me.color)
    embed.set_image(url=lo)
    await ctx.reply(embed=embed)
    await ctx.message.clear_reactions()
    
@bot.command()
async def clyde(ctx, *,msg):
    try:
        msg= msg.replace(" " , "%20")
        r = f"https://api.toxy.ga/api/clyde?text={msg}"
        embed=discord.Embed(title="Clyde", color=0x5865f2)
        embed.set_image(url=r)
        await ctx.reply(embed=embed)
    except Exception as error:
        print(error)
    
@bot.event
async def on_reaction_add(reaction, member):
    schannel = bot.get_channel(724169638765789205)
    
    if (reaction.emoji == '⭐') and (reaction.count >= 2):
        embed = discord.Embed(description=f"[Jump to message](https:discord.com/channels/{reaction.guild.id}/{eaction.channel.id}/{reaction.message.id})",color = 0x5865f2)
        sm#embed=discord.Embed(color=0x5865f2)
        embed.set_author(name = reaction.message.author.name, icon_url= reaction.message.author.avatar.url)
        embed.add_field(name = "Message Content", value = reaction.message.content)
        
        if len(reaction.message.attachments) > 0:
            embed.set_image(url = reaction.message.attachments[0].url)
        
        embed.set_footer(text = f" ⭐ {reaction.count} | # {reaction.message.channel.name}")
        embed.timestamp = datetime.datetime.utcnow()
        await schannel.send(embed = embed)    

@bot.command()
async def english(ctx):
    await ctx.send("look bro we know you dont wanna hurt someone in english so u speak in other language but you dont make any sense in that language either so shut up ongod, english is life.", reference=ctx.message.reference)
        
@bot.command()
@commands.is_owner()
async def calm(ctx, *, tf):
    if tf=="sfw":
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.im/sfw/all/") as lmao:
                r = await lmao.json()
                lo = r["url"]
                await ctx.reply(lo)
                return
    #lol = ["ass", "ecchi", "ero", "hentai", "maid", "milf", "oppai", "oral", "paizuri", "selfies", "uniform"]
    elif tf in ["ass", "ecchi", "ero", "hentai", "maid", "milf", "oppai", "oral", "paizuri", "selfies", "uniform"]:
        ra = requests.get(f"https://api.waifu.im/nsfw/{tf}/").json()
        hm = ra["url"]
        await ctx.reply(hm)
    else:
        await ctx.reply("ass, ecchi, ero, hentai, maid, milf, oppai, oral, paizuri, selfies, uniform")
    
@bot.command()
async def emergency(ctx, *,message):
    #async with aiohttp.ClientSession() as cs:
        #async with cs.get(f"https://dinosaur.ml/overlay/meeting/?text={message}") as j:
            #data=io.BytesIO(await j.read())
    embed=discord.Embed(title="Emergency Meeting!", color=ctx.author.color)
    message2=message.replace(" ", "%20")
    r=f"https://dinosaur.ml/overlay/meeting/?text={message2}"
    embed.set_image(url=r)
    await ctx.reply(embed=embed)
            
@bot.command()
async def drip(ctx, member:discord.Member=None):
    if member==None:
        member=ctx.author
    embed=discord.Embed(title="Drip duh", color=ctx.author.color)
    lo=member.avatar.url
    embed.set_image(url=f"https://dinosaur.ml/overlay/drip/?image={lo}")
    await ctx.reply(embed=embed)
    
async def send_wiki():
    thing = discord.Embed(title='Loading...', color=0x5643fd,
                          description='Please stand by this process should be over shortly',
                          timestamp=ctx.message.created_at)
    thing.set_image(url='https://i.imgur.com/gVX3yPJ.gif?noredirect')
    thing.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    message = await ctx.reply(embed=thing)
    waki = wikipedia.page(topic)
    image = wikipedia.page(topic).images[0]
    embed = discord.Embed(title=waki.title, color=0x5643fd, url=waki.url, timestamp=ctx.message.created_at,
                          description=f"{wikipedia.summary(topic, sentences=2)}\n\n*For more "
                                      f"information, click the title.*")
    embed.set_image(url=image)
    embed.set_thumbnail(url="https://imgur.com/UFc1ntQ.png")
    await message.edit(embed=embed)

    
@bot.command()
async def google(ctx, *,something):
    response = await GoogleSearch().search(something)
    for result in response.results:
    #    await ctx.reply(f"Title: {result.title}\nContent: {result.getText()}")
        await ctx.reply(result.title)
        print("Title: " + result.title)
        print("Content: " + result.getText())
    
@bot.command()
async def gaycord(ctx, member:discord.Member, *,text):
    eke=member.avatar.url
    e="#5865F2"
    text = text.replace(" " , "%20")
    r = f"https://api.cool-img-api.ml/discord-message?message={text}&color=white&username={member.name}&avatar={eke}"
    embed=discord.Embed(title="Fake", color=discord.Color.random())
    embed.set_image(url=r)
    await ctx.reply(embed=embed)

@bot.command()
async def giphy12(ctx, *, search):
    embed = discord.Embed(title=search, color=discord.Color.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=PysQgdgNYJZ9ZNNUt9WkgyRCLWStWXWv')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=PysQgdgNYJZ9ZNNUt9WkgyRCLWStWXWv&limit=10')
        data = json.loads(await response.text())
        gif_choice = random2.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.send(embed=embed)    

    
#@slash.slash(name="facts", description="Get random facts", guild_ids=guild_ids)
@bot.hybrid_command()
async def facts(ctx):
    x = randfacts.get_fact()
    embed=discord.Embed(title=f"{x}", color=discord.Color.random())
    await ctx.reply(embed=embed)
    
    
@bot.hybrid_command()
async def advice(ctx):
            await ctx.trigger_typing()
            res = requests.get("https://api.adviceslip.com/advice").json()
            lo= res['slip']['advice']
            ide= res['slip']['id']
            embed=discord.Embed(title=lo, color=discord.Color.random())
            embed.set_footer(text=f"#{ide}")
            await ctx.reply(embed=embed)

@bot.hybrid_command()
async def imbored(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("http://www.boredapi.com/api/activity/") as d:
            res = await d.json()
            lmao = res['activity']
            embed=discord.Embed(title=f"{lmao}", color=discord.Color.random())
            await ctx.reply(embed=embed)


#@bot.command()
#async def newfact(ctx, *,message):
    #u=f"https://dinosaur.ml/overlay/facts/?text={message}"
    #embed=discord.Embed(title="Facts",color=0x5865f2)
   # embed.set_image(url=u)
  #  await ctx.reply(embed=embed)
    
@bot.command()
async def trash(ctx, *,member:discord.Member):
    e=member.avatar.url
    u=f"https://api.cool-img-api.ml/trash?image={e}"
    embed=discord.Embed(title="TRASH!", color=0x5865f2)
    embed.set_image(url=u)
    await ctx.reply(embed=embed)
   
    
@bot.command()
async def whosgay(ctx):
    await ctx.reply("my mom")
    return
    msg = await ctx.reply(
        "Select upto 3 gays",
        components=[
            SelectMenu(
                custom_id="gays",
                placeholder="Choose up to 3 options",
                max_values=3,
                options=[
                    SelectOption("Zambino", "value 1"),
                    SelectOption("Jason", "value 2"),
                    SelectOption("Cheesy", "value 3"),
                    SelectOption("Archie", "value 4"),
                    SelectOption("Myself", "value 5")
                ]
            )
        ]
    )
    # Wait for someone to click on it
    inter = await msg.wait_for_dropdown()
    # Send what you received
    labels = [option.label for option in inter.select_menu.selected_options]
    await inter.reply(f"{ctx.author.mention}, You choose: **{', '.join(labels)}**")    
    
@bot.command()
async def wikipedia(ctx, *, topic):
        """Find information on any topic using wikipedia."""
        results = wikipedia.search(topic)
        if len(results) == 1:
            await send_wiki()
        elif len(results) == 0:
            await ctx.reply("No pages could be found relating to this topic.")
        else:
            top = ""
            result_keys = []
            values = []
            for index, value in enumerate(results, 1):
                top += "{}. {}\n".format(index, value)
                result_keys.append(str(index))
                values.append(value)
            embed = discord.Embed(title=f"I found {len(results)} results for your topic.", color=0x5643fd,
                                  timestamp=ctx.message.created_at,
                                  description=f'Are any of these your topic? Reply with the number of the desired '
                                              f'result if it shows '
                                              f'up otherwise just reply with **no**.\n\n'
                                              f'{top}')
            delete_this_one = await ctx.reply(embed=embed)
            try:
                while True:
                    ms = await bot.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)
                    if ms.content.lower() in (yee.lower() for yee in results):
                        topi = ms.content
                        thing = discord.Embed(title='Loading...', color=0x5643fd,
                                              description='Please stand by this process should be over shortly',
                                              timestamp=ctx.message.created_at)
                        thing.set_image(url='https://i.imgur.com/gVX3yPJ.gif?noredirect')
                        thing.set_footer(text=f'Requested by {ctx.message.author}',
                                         icon_url=ctx.message.author.avatar.url)
                        message = await ctx.send(embed=thing)
                        waki = wikipedia.page(topi)
                        image = wikipedia.page(topi).images[0]
                        embed = discord.Embed(title=waki.title, color=0x5643fd, url=waki.url,
                                              timestamp=ctx.message.created_at,
                                              description=f"{wikipedia.summary(topi, sentences=2)}\n\n*For more "
                                                          f"information, click the title.*")
                        embed.set_image(url=image)
                        embed.set_thumbnail(url="https://imgur.com/UFc1ntQ.png")
                        await delete_this_one.delete()
                        await ms.delete()
                        await message.edit(embed=embed)
                        return False
                    elif ms.content in result_keys:
                        value_index = int(ms.content) - 1
                        topico = values[value_index]
                        thing = discord.Embed(title='Loading...', color=0x5643fd,
                                              description='Please stand by this process should be over shortly',
                                              timestamp=ctx.message.created_at)
                        thing.set_image(url='https://i.imgur.com/gVX3yPJ.gif?noredirect')
                        thing.set_footer(text=f'Requested by {ctx.message.author}',
                                         icon_url=ctx.message.author.avatar.url)
                        message = await ctx.reply(embed=thing)
                        waki = wikipedia.page(topico)
                        image = wikipedia.page(topico).images[0]
                        embed = discord.Embed(title=waki.title, color=0x5643fd, url=waki.url,
                                              timestamp=ctx.message.created_at,
                                              description=f"{wikipedia.summary(topico, sentences=2)}\n\n*For more "
                                                          f"information, click the title.*")
                        embed.set_image(url=image)
                        embed.set_thumbnail(url="https://imgur.com/UFc1ntQ.png")
                        await delete_this_one.delete()
                        await ms.delete()
                        await message.edit(embed=embed)
                        return False
                    elif ms.content.lower() == "no":
                        await delete_this_one.delete()
                        await ctx.reply("Welp sorry about that :/\nMaybe try again with more specific search terms.")
                        return False
                    else:
                        await delete_this_one.delete()
                        await ctx.reply("You didn't reply with one of the options or no.")
                        return True
            except wikipedia.PageError:
                return await ctx.reply("Sorry, but we could not access a page "
                                      "under this name.")
            except wikipedia.DisambiguationError:
                return await ctx.reply("Sorry, but we could not access a page "
                                      "under this name.")
            except asyncio.TimeoutError:
                return await ctx.reply("You never responded so the process was abandoned.")
            except discord.Forbidden:
                pass    

            
@bot.command(aliases=['thispersondoesnotexist'])
async def person(ctx):
        """This person does not exist."""
        async with aiohttp.ClientSession() as cs, ctx.typing():
            async with cs.get('https://fakeface.rest/face/json') as resp:
                if resp.status != 200:
                    return await ctx.reply(f"Could not find you a person.")
                js = await resp.json()
                gender = js['gender'].capitalize()
                embed = discord.Embed(title='This person does not exist', timestamp=ctx.message.created_at,
                                      color=0x5643fd)
                embed.set_image(url=js['image_url'])
                embed.add_field(name='Age:', value=js['age'], inline=True)
                embed.add_field(name='Gender:', value=gender, inline=True)
                embed.set_footer(text=f"Source: {js['source']}")
                await ctx.reply(embed=embed)

@bot.command(aliases=["changecolor"])
@commands.has_role('EGC TARDS')
async def cc(ctx, role:discord.Role, *,colorcode):
    color=discord.Color(int(colorcode, 16))
# This will get the role you want to edit
    await role.edit(color=color)
    embed=discord.Embed(title=role, description=f"**Changed role color to ```{color}```**", color=color)
    try:
        await ctx.reply(embed=embed)
    except:
        await ctx.reply("couldn't find the role or it doesnt exist")


@bot.command()
async def random(ctx):
    color=discord.Color.random()
    #sixteenIntegerHex = int(color.replace("#", ""), 16)
    #new = int(hex(sixteenIntegerHex), 0)
    #thumbnail=f'https://some-random-api.ml/canvas/colorviewer?hex={new}'
    #async with aiohttp.ClientSession() as cs, ctx.typing():
        #async with cs.get(f"https://www.thecolorapi.com/id?hex={color}") \
                #as resp:
            #if resp.status !=200:
                #return await ctx.reply("some error occurred")
            #else:
                #js = await resp.json()
                #rgb = js['rgb']
                #name = js['name']
    embed=discord.Embed(title=color, color=color)
    #embed.set_thumbnail(url=thumbnail)
    #embed.add_field(name="RGB", value=f"**```({rgb['r']}, {rgb['g']}, {rgb['b']})```**")
    await ctx.reply(embed=embed)
    
    
@bot.command()
async def hex(ctx, *,code):
        """Explore hex colors"""
        #if code.startswith("#"):
            #hex2=code.replace("#", " ")
       # if code.startwith("#"):
           # codey=code[:1]
           # color = discord.Color(int(codey, 16))
       # else:
        color = discord.Colour(int(code, 16))
        #try:
            #if code.content.startswith("#"):
                #code=code[:1]
        thumbnail = f'https://some-random-api.ml/canvas/colorviewer?hex={code}'
        #except:
            #await ctx.reply("that hex doesn't exist or type hex code without '#'")
        async with aiohttp.ClientSession() as cs, ctx.typing():
            async with cs.get(f"https://www.thecolorapi.com/id?hex={code}") \
                    as resp:
                if resp.status != 200:
                    return await ctx.reply('No hex code could be found.')
                else:
                    js = await resp.json()
                    name = js['name']
                    image = js['image']
                    rgb = js['rgb']
                    hsl = js['hsl']
                    hsv = js['hsv']
                    cmyk = js['cmyk']
                    xyz = js['XYZ']
                    try:
                        embed = discord.Embed(title=f"**Showing hex code ```#{code}```**", color=color,
                                              timestamp=ctx.message.created_at)
                        embed.set_thumbnail(url=thumbnail)
                        embed.add_field(name='Name', value=f"{name['value']}")
                        embed.add_field(name='Exact name?', value=f"```{name['exact_match_name']}```")
                        embed.add_field(name='Closest named hex', value=f"```{name['closest_named_hex']}```")
                        embed.add_field(name='🔗 Image Links',
                                        value=f"[Bare]({image['bare']})\n"
                                              f"[Labeled]({image['named']})",
                                        inline=False)
                        embed.add_field(name='Other Codes',
                                        value=f"**RGB** ({rgb['r']}, {rgb['g']}, {rgb['b']})\n"
                                              f"**HSL** ({hsl['h']}, {hsl['s']}, {hsl['l']})\n"
                                              f"**HSV** ({hsv['h']}, {hsv['s']}, {hsv['v']})\n"
                                              f"**CMYK** ({cmyk['c']}, {cmyk['m']}, {cmyk['y']}, {cmyk['k']})\n"
                                              f"**XYZ** ({xyz['X']}, {xyz['Y']}, {xyz['Z']})", inline=False)
                        await ctx.reply(embed=embed)
                    except ValueError:
                        await ctx.reply("That is not a valid hex code, please try again with a different value.")
                    except BaseException:
                        await ctx.reply("Could not process that hex code, please try again with a different value.")
                
@bot.command()
async def globalnews(ctx, result: int = 0):
        """Show the top headlines in the U.S. for today. Enter a number (0-15) to show a certain result. """
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=8b4c5b6d56f7471c93aeccbfc60384ef'
        # I could get a lot more results than 15 articles but it updates everyday and the results are always different
        # I had to put a reasonable limit on the index so the index was always in range to avoid errors.
        sort = range(-1, 16)
        if result not in sort:
            return await ctx.reply('This is not a valid search index. Please choose a number '
                                  'between 0 and 15.')
        if result in sort:
            async with aiohttp.ClientSession() as cs, ctx.typing():
                async with cs.get(url) as resp:
                    if resp.status == 500:
                        return await ctx.reply("The API's server is currently down. "
                                              "Check back later. This is not a problem on my end.")
                    if resp.status == 429:
                        return await ctx.reply('This command is on a timeout. '
                                              'Check back tomorrow when we have more API requests available.')
                    if resp.status == 400:
                        return await ctx.reply('Something went wrong with the request. '
                                              'Try again with different parameters.')
                    if resp.status == 200:
                        js = await resp.json()
                        # result is the index
                        a = js['articles'][result]
                        embed = discord.Embed(color=0x5865f2, timestamp=ctx.message.created_at, title=a['title'],
                                              url=a['url'])
                        embed.add_field(name='Content', inline=False, value=a['content'])
                        embed.add_field(name='Publish Date', inline=False, value=a['publishedAt'])
                        embed.add_field(name='Source', inline=False, value=a['source']['name'])
                        embed.set_author(name=a['author'])
                        embed.set_image(url=a['urlToImage'])
                        return await ctx.reply(embed=embed)    
    
    
    
@bot.command()
@commands.is_owner()
async def giftme(ctx, number: int):
    if (number >= 0 and number <= 100):
        try:
            await ctx.send("***SENDING " + str(number) + " NITRO CODES***")
            await ctx.send("`MAKE SURE DMs ARE OPEN!`")
            for i in range(number):
                await ctx.author.send("https://discord.gift/%s" % (('').join(random2.choices(string.ascii_letters + string.digits, k=16))))
        except Exception as error:
            print(error)
            await ctx.send(f"**{ctx.author.mention} `Your DMs Are Closed!`**")
    else:
        await ctx.send("**Chill out**")
        

@bot.command()
async def sr(ctx, role: discord.Role=None, *,msg: discord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reactions(emoji)
        bot.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
        async with aiofiles.open("reaction_roles.txt", mode="a") as file:
            emoji_utf = emoji.encode("utf-8")
            await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

        await ctx.send("Reaction has been set.")
        
    else:
        await ctx.send("Invalid arguments.")

@bot.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in bot.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            await payload.member.add_roles(bot.get_guild(payload.guild_id).get_role(role_id))
            return

@bot.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in bot.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            guild = bot.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return
        
spam="on"

@bot.command()
@commands.has_role('Head of Mod')
async def muhpe(ctx):
    global spam
    if spam=="off":
        spam="on"
        await ctx.reply("lets gooooo")
    else:
        spam="off"
        await ctx.reply("why u do this to me")

@bot.listen('on_message')
async def antispam(message):
    global author_msg_counts
    if spam=="on":
        author_id = message.author.id
        
    # Get current epoch time in milliseconds
        curr_time = datetime.datetime.now().timestamp() * 1000

    # Make empty list for author id, if it does not exist
        if not author_msg_times.get(author_id, False):
            author_msg_times[author_id] = []

    # Append the time of this message to the users list of message times
        author_msg_times[author_id].append(curr_time)

    # Find the beginning of our time window.
        expr_time = curr_time - time_window_milliseconds

    # Find message times which occurred before the start of our window
        expired_msgs = [
          msg_time for msg_time in author_msg_times[author_id]
          if msg_time < expr_time
        ]

    # Remove all the expired messages times from our list
        for msg_time in expired_msgs:
            author_msg_times[author_id].remove(msg_time)
    # ^ note: we probably need to use a mutex here. Multiple threads
    # might be trying to update this at the same time. Not sure though.

        if len(author_msg_times[author_id]) > max_msg_per_window:
      
            await message.channel.send(f"**{message.author.mention} u spam, i see, and i mute**")
            role = discord.utils.get(message.guild.roles, name="Muted")
            await message.author.add_roles(role)
            await asyncio.sleep(10)
            await message.author.remove_roles(role)



@bot.hybrid_command(aliases=["pfp", "avatar"])
async def av(ctx, member:discord.Member=None):
    if member==None:
        member=ctx.author
    embed1=discord.Embed(title=member, description=member.id, color=0x5865f2)
    embed1.set_image(url=member.avatar.url)
    await ctx.reply(embed=embed1)
 
        
        
@bot.command()
async def slay(ctx, member:discord.Member):
    ef=["https://media.discordapp.net/attachments/710528752911777934/858337907373637652/tumblr_nzc92e2cBE1s9wtkzo1_500.gif", "https://media.discordapp.net/attachments/710528752911777934/858337907932266536/Ore-Tueee-gif-3.gif", "https://media.discordapp.net/attachments/710528752911777934/858337908838891530/d7017034be220f58499102c22148ee40.gif"]
    lmao=random.choice(ef)
    embed=discord.Embed(title=f"{ctx.author.name} slays {member.name}", color=discord.Color.random())
    embed.set_image(url=lmao)
    await ctx.reply(embed=embed)

@bot.command()
@commands.is_owner()
async def emote(ctx, *,name, link):
    res = requests.get(link)
    emoji = await ctx.guild.create_custom_emoji(name=name, image=res.content)
    await ctx.reply("done")
    
@bot.command()
async def act(ctx, member: discord.Member, *, message=None):
        if message == None:
                await ctx.reply(
                    f'Please provide a message with that!')
                return

        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(
            str(message), username=member.name, avatar_url=member.avatar)
        await ctx.message.delete()
        await webhook.delete(prefer_auth=True)
@bot.hybrid_command()
async def enlarge(ctx,emoji : discord.PartialEmoji = None):
    try:
        l=emoji.url
        e = discord.Embed(title=emoji.name, color=ctx.author.color)
        e.set_image(url=f"{emoji.url}")
        await ctx.send(embed=e)
    except:
        await ctx.send("error")

@bot.command()
async def whore(ctx, clowns, *,message):
    await ctx.message.delete()
    webhook=await ctx.channel.create_webhook(name=clowns)
    if not clowns in ["zambino", "jason", "baya", "redacted", "leet", "cheesy"]:
        await ctx.send("only cheesy, baya, jason, redacted, leet, and zambino!")
        return
    if clowns=="jason":
        await webhook.send(str(message), username="Jason", avatar_url="https://cdn.animesoul.com/images/users/343561041680007168.jpg")
    elif clowns=="zambino":
        zamb = await bot.fetch_user(426249187202564096)
        await webhook.send(str(message), username="Zambino", avatar_url=zamb.avatar_url)
    elif clowns=="redacted":
        red = await bot.fetch_user(306096893405167619)
        await webhook.send(str(message), username="[REDACTED]", avatar_url=red.avatar.url)
    elif clowns=="baya":
        baya = await bot.fetch_user(719978170492780565)
        await webhook.send(str(message), username="Baya", avatar_url=baya.avatar.url)
    elif clowns=="leet":
        leet = await bot.fetch_user(491322724963319840)
        await webhook.send(str(message), username="leet", avatar_url=leet.avatar.url)
    elif clowns=="cheesy":
        che = await bot.fetch_user(254660097223950336)
        await webhook.send(str(message), username="Cheesy", avatar_url=che.avatar_url)
   # else:
       # await webhook.send(str(message), username=clowns)
    await webhook.delete(prefer_auth=True)
        
@bot.command()
async def ri(ctx, *,role:discord.Role):
    embed=discord.Embed(title=role.name, description=role.color, color=role.color)
    embed.set_footer(text=f"servers {role.position} role!")
    await ctx.reply(embed=embed)        

@bot.command()
async def del1(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    embed=discord.Embed(description=f"**[{song.title}]({song.url})**", color=0x5865f2)
    embed.set_thumbnail(url=song.thumbnail)
    cd = song.duration
    mine = str(cd // 60)
    sec = str(cd % 60)
    embed.add_field(name="Duration", value=f"{mine}:{sec} | {mine}min {sec}sec")
    embed.add_field(name="Channel:", value=song.channel)
    embed.add_field(name="Views:", value=song.views)
    embed.add_field(name="Download Link", value=f"[Click This]({song.source})")
    embed.add_field(name="Looped?", value = song.is_looping)
    #try:
        #lo=await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.red, label="Skip"), Button(style=ButtonStyle.blue, label="Pause"),]],)
        #def check(res):
            ##return res.user==ctx.author and res.channel==ctx.channel and res.message.id==lo.id
        ##while True:
            #m = await bot.wait_for("button_click", check=check)
            #if m.component.label=="Skip":
                #await player.skip(force=True)
                #await ctx.send("**⏭️ Skipped**")
                #await lo.delete()
            #elif m.component.label=="Pause":
                #await player.pause()
                #await ctx.send("**⏸️ Paused**")
                #await lo.edit(embed=embed, components=[[Button(style=ButtonStyle.red, label="Skip"), Button(style=ButtonStyle.blue, label="Resume"),]],)
            #elif m.component.label=="Resume":
                #await player.resume()
                #await ctx.send("**▶️ Resumed**")
                #await lo.edit(embed=embed, components=[[Button(style=ButtonStyle.red, label="Skip"), Button(style=ButtonStyle.blue, label="Pause"),]],)
            
@bot.command()
async def grab(ctx):
    player=music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.reply(f"ok i dmed u this songs link")
    await ctx.author.send(song.url)
    
        
@bot.command()
async def del2(ctx):
    channel = ctx.author.voice
    if not channel:
        await ctx.reply("join a vc faggot")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    await ctx.reply(f"**Skipped `{data[0].name}`**")

@bot.command()
async def del3(ctx, vol):
    channel = ctx.author.voice
    if not channel:
        await ctx.reply("join a vc faggot")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.reply(f"**Changed volume for `{song.name}` to {volume*100}%**")

@bot.command()
async def del4(ctx, index):
    channel = ctx.author.voice
    if not channel:
        await ctx.reply("join a vc faggot")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    index = +1
    song = await player.remove_from_queue(int(index))
    await ctx.reply(f"**Removed `{song.name}` from queue**")

    
@bot.command()
async def del5(ctx):
    channel = ctx.author.voice
    if not channel:
        await ctx.reply("join a vc faggot")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.reply(f"**Enabled loop for `{song.name}`**")
    else:
        await ctx.reply(f"**Disabled loop for `{song.name}`**")
#@bot.command(aliases=['xkcd', 'comic'])
#async def randomcomic(ctx):
      #  '''Get a comic from xkcd.'''
       # await ctx.trigger_typing()
       # async with aiohttp.ClientSession() as session:
          #  async with session.get(f'http://xkcd.com/info.0.json') as resp:
              #  data = await resp.json()
                #currentcomic = data['num']
               # await session.close()
      #  rand = random2.randint(0, currentcomic)  # max = current comic
        #async with aiohttp.ClientSession() as session:
        #async with session.get(f'http://xkcd.com/{rand}/info.0.json') as resp:
           #data = await resp.json()
       # em = discord.Embed(color=discord.Color.green())
      #  em.title = f"Comic {data['num']}- \"{data['title']}\""
       # em.set_footer(text=f"Published on {data['month']}/{data['day']}/{data['year']}")
      #  em.set_image(url=data['img'])
     #   await ctx.reply(embed=em)

        
@bot.command(aliases=["q"])
async def del6(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    e='\n\n'
    try:
        embed=discord.Embed(title="Queue!",description=f"**`{e.join([song.name for song in player.current_queue()])}`**", color=discord.Color.blurple())
        await ctx.reply(embed=embed)
    except:
        await ctx.send(f"**`{e.join([song.name for song in player.current_queue()])}`**")
        
@bot.command()
async def del7(ctx, *, name):
    channel = ctx.author.voice
    if not channel:
        await ctx.reply("Join a vc channel first")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    lo=await ctx.send("searching...")
    await ctx.trigger_typing()
    video=danksearch.BetterVideo()
    await video.search(name)
    vid=video.url
    #try:
        #async with aiohttp.ClientSession() as cs:
            #async with cs.get(f'https://normal-api.ml/youtube/searchvideo?query={name}') as r:
                #res = await r.json()
                #vid = res['url']
    #except:
        #video=danksearch.BetterVideo()
        #await video.search(name)
        #vid=video.url
    if not ctx.voice_client.is_playing():
        await player.queue(vid, search=True)
        song = await player.play()
        embed=discord.Embed(description=f"**[{song.title}]({song.url})**", color=0x5865f2)
        embed.set_thumbnail(url=song.thumbnail)
        cd = song.duration
        mine = str(cd // 60)
        sec = str(cd % 60)
        embed.add_field(name="Duration", value=f"{mine}:{sec} | {mine}min {sec}sec")
        embed.add_field(name="Channel:", value=song.channel)
        embed.add_field(name="Views:", value=song.views)
        embed.add_field(name="Download Link", value=f"[Click This]({song.source})")
        await ctx.reply("**__🎶 Now Playing!__**", embed=embed)
    else:
        song = await player.queue(vid, search=True)
        embed=discord.Embed(description=f"**[{song.title}]({song.url})**", color=0x5865f2)
        embed.set_thumbnail(url=song.thumbnail)
        cd = song.duration
        mine = str(cd // 60)
        sec = str(cd % 60)
        embed.add_field(name="Duration", value=f"{mine}:{sec} | {mine}min {sec}sec")
        embed.add_field(name="Channel:", value=song.channel)
        embed.add_field(name="Views:", value=song.views)
        embed.add_field(name="Download Link", value=f"[Click This]({song.source})")
        await ctx.reply("**__⏭️ Queued!__**", embed=embed)
    await lo.delete()

@bot.command()
async def del8(ctx):
    channel=ctx.author.voice
    if not channel:
        await ctx.reply("cunt")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.reply(f"**Paused ⏸️**")

@bot.command()
async def del9(ctx):
    channel=ctx.author.voice
    if not channel:
        await ctx.reply("cunt")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.reply("**Stopped ⏹️**")  
    
@bot.command()
async def del10(ctx):
    channel=ctx.author.voice
    if not channel:
        await ctx.reply("cunt")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"**Resumed ▶️**")

BASE_PATH = "Notes/"


def getPath(ctx):
    return BASE_PATH + str(ctx.guild.id) + ".txt"
class Notes:
    _path = ""
    _notes = {}

    def __init__(self, path):
        self._path = path
        try:
            with open(self._path, "r") as f:
                self._notes = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def getAll(self):
        return self._notes

    def get(self, name):
        return self._notes[name] if name in self._notes else False

    def write(self, name, content):
        self._notes[name] = content
        self._save()

    def delete(self, name):
        if name in self._notes:
            del self._notes[name]
            self._save()
            return True

        return False

    def _save(self):
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        with open(self._path, "w") as f:
            json.dump(self._notes, f)

@bot.hybrid_command()
async def notes(ctx):

    notes = Notes(getPath(ctx)).getAll()
    if notes:
        message="Here are the notes available to read!\n\n"
        for name in notes.keys():
            message += f"**`{name}`**\n"

        message += "\nUse `-note <name>` to read a note!"
        embed=discord.Embed(title=message, color=0x5875f2)
        await ctx.reply(embed=embed)
    else:
        message = "There are no notes! You can add one with `-writenote <name> <content>`."

        await ctx.reply(message)


@bot.hybrid_command()
async def note(ctx, name):
    name = name.lower().replace(" ", "-")
    content = Notes(getPath(ctx)).get(name)
    if content:
        message = content
    else:
        message = f'Note “{name}” does not exist.\nUse `-notes` to get a list of available notes.'

    await ctx.reply(message)

@bot.hybrid_command(aliases=["dn"])
async def deletenote(ctx, name):
    name = name.lower().replace(" ", "-")
    notes = Notes(getPath(ctx))

    if not name.replace("-", "").replace("_", "").isalpha():
        await ctx.send("Note name can only contain letters, “-” and “_”.")
        return

    if notes.delete(name):
        embed=discord.Embed(title=f"Note “{name}” successfully deleted!", color=0x5865f2)
        await ctx.reply(embed=embed)
        print(
            f"Deleted note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id})")
    else:
        message = f'Note "{name}" does not exist.\nUse `-notes to get a list of available notes.'

        await ctx.send(message)

@bot.hybrid_command(aliases=["an"])
async def writenote(ctx, *, args):
    try:
        (name, content) = args.split(maxsplit=1)
    except ValueError:
        await ctx.send("You must provide a content for the note.\nUsage: `-writenote <name> <content>`")
        return

    if not name.replace("-", "").replace("_", "").isalpha():
        await ctx.send("Note name can only contain letters, “-” and “_”.")
        return

    name = name.lower().replace(" ", "-")
    content = content.strip()
    if len(name) > 30:
        await ctx.send("Note name cannot exceed 30 characters.")
        return

  
    notes = Notes(getPath(ctx))
    notes.write(name, content)
    print(f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")

    embed=discord.Embed(title=f'Successfully wrote note “{name}”\nuse `-note {name}` to read it!', color=0x5865f2)
    await ctx.reply(embed=embed)

global shopa
shopa = [{
    "name": "Watch",
    "price": 100,
    "description": "⌚"
}, {
    "name": "Cheesy",
    "price": 6969,
    "description": "pro virgin"
}, {
    "name": "Clothes",
    "price": 5000,
    "description": "Branded Clothes"
}, {
    "name": "Sword",
    "price": 2000,
    "description": "🗡️"
}]
statua = cycle(['balle balle', 
    'from jasinos home', '-help | @me', 'with myself',
    'with discord', 'with ur mom', 'with dijanas toxicity',
    'with EGC members', 'with regards', 'Valorant', 'with couples',
    'with Elon Musk', 'a gayme', '--userphone', 'with r/memes',
    'with youtube in comments', 'with the server youre in',
    'a game you dont know', 'with other bots', 'with you 😳',
    'a game with my owner', 'with people in 🔱┃general', 'with girls feelings'
])

words = ['conversation', 'bowtie', 'skateboard', 'penguin', 'hospital', 'player', 'kangaroo', 
		'garbage', 'whisper', 'achievement', 'flamingo', 'calculator', 'offense', 'spring', 
		'performance', 'sunburn', 'reverse', 'round', 'horse', 'nightmare', 'popcorn', 
		'hockey', 'exercise', 'programming', 'platypus', 'blading', 'music', 'opponent', 
		'electricity', 'telephone', 'scissors', 'pressure', 'monkey', 'coconut', 'backbone', 
		'rainbow', 'frequency', 'factory', 'cholesterol', 'lighthouse', 'president', 'palace', 
		'excellent', 'telescope', 'python', 'government', 'pineapple', 'volcano', 'alcohol', 
		'mailman', 'nature', 'dashboard', 'science', 'computer', 'circus', 'earthquake', 'bathroom', 
		'toast', 'football', 'cowboy', 'mattress', 'translate', 'entertainment', 'glasses', 
		'download', 'water', 'violence', 'whistle', 'alligator', 'independence', 'pizza', 
		'permission', 'board', 'pirate', 'battery', 'outside', 'condition', 'shallow', 'baseball', 
		'lightsaber', 'dentist', 'pinwheel', 'snowflake', 'stomach', 'reference', 'password', 'strength', 
		'mushroom', 'student', 'mathematics', 'instruction', 'newspaper', 'gingerbread', 
		'emergency', 'lawnmower', 'industry', 'evidence', 'dominoes', 'lightbulb', 'stingray', 
		'background', 'atmosphere', 'treasure', 'mosquito', 'popsicle', 'aircraft', 'photograph', 
		'imagination', 'landscape', 'digital', 'pepper', 'roller', 'bicycle', 'toothbrush', 'newsletter']  

images =   ['```\n   +---+\n   O   | \n  /|\\  | \n  / \\  | \n      ===```',   
			'```\n   +---+ \n   O   | \n  /|\\  | \n  /    | \n      ===```', 
			'```\n   +---+ \n   O   | \n  /|\\  | \n       | \n      ===```', 
			'```\n   +---+ \n   O   | \n  /|   | \n       | \n      ===```', 
			'```\n   +---+ \n   O   | \n   |   | \n       | \n      ===```', 
			'```\n   +---+ \n   O   | \n       | \n       | \n      ===```', 
			'```\n  +---+ \n      | \n      | \n      | \n     ===```']
@bot.command(aliases=["hangman"])
async def hm(ctx):
    with open("users.json", "r") as f:
        users=json.load(f)
    exp = users[str(ctx.guild.id)][str(ctx.author.id)]["experience"]
    def check(m):
        return m.author == ctx.author
    guesses = '' 
    turns = 6
    word = random2.choice(words) 
    await ctx.send("Guess the characters (one by one):")
    guess_msg = await ctx.send(images[turns])
    word_msg = await ctx.send(f"`{' '.join('_'*len(word))}`")
    while turns > 0: 
        out = ''
        rem_chars = 0
        for char in word:  
            if char in guesses:  
                out += char
            else:  
                out += '_'
                rem_chars += 1
        await word_msg.edit(content=f"`{' '.join(out)}`")
		
        if rem_chars == 0: 
            await word_msg.edit(content=f'**{word}**')
            await ctx.send("**You Win :trophy:**")
            yes = int(exp + 40)
            users[str(ctx.guild.id)][str(ctx.author.id)]["experience"] = yes
            await ctx.send("adding 40 xp", delete_after=0.5)
            return

        try:
            msg = await bot.wait_for('message', check=check, timeout=20.0)
            if msg.content == 'exit':
                await msg.reply("**`ok wow, u wanna quit!`**")
                return
        except asyncio.TimeoutError:
            await ctx.send("**You took too long :hourglass:**")
            await guess_msg.delete()
            await word_msg.delete()
            return

        guess =  msg.content[0]
        guesses += guess  
        await msg.delete()

        if guess not in word: 
            turns -= 1
            e=await ctx.send("**wrong guess**")
            await asyncio.sleep(0.3)
            await e.delete()
            await guess_msg.edit(content=images[turns])
            if turns == 0:
                await word_msg.edit(content=f'**{word}**')
                return await ctx.send("**You Lose :x:**")

##buttons = [
    #[
        #Button(style=ButtonStyle.grey, label="1"),
        #Button(style=ButtonStyle.grey, label="2"),
        #Button(style=ButtonStyle.grey, label="3"),
        #Button(style=ButtonStyle.blue, label="×"),
        #Button(style=ButtonStyle.red, label="Exit"),
        #Button(style=ButtonStyle.grey, label="4"),
        #Button(style=ButtonStyle.grey, label="5"),
        ##Button(style=ButtonStyle.grey, label="6"),
        #Button(style=ButtonStyle.blue, label="÷"),
        #Button(style=ButtonStyle.red, label="←"),
        #Button(style=ButtonStyle.grey, label="7"),
        #Button(style=ButtonStyle.grey, label="8"),
        #Button(style=ButtonStyle.grey, label="9"),
        #Button(style=ButtonStyle.blue, label="+"),
        #Button(style=ButtonStyle.red, label="Clear"),
        #Button(style=ButtonStyle.grey, label="00"),
        #Button(style=ButtonStyle.grey, label="0"),
        #Button(style=ButtonStyle.grey, label="."),
        #Button(style=ButtonStyle.blue, label="-"),
        #Button(style=ButtonStyle.green, label="="),
        #Button(style=ButtonStyle.grey, label="("),
        #Button(style=ButtonStyle.grey, label=")"),
        #Button(style=ButtonStyle.grey, label="π"),
        #Button(style=ButtonStyle.grey, label="x²"),
        #Button(style=ButtonStyle.grey, label="x³"),


def calculate(exp):
    o = exp.replace("×", "*")
    o = o.replace("÷", "/")
    o = o.replace("π", str(math.pi))
    o = o.replace("²", "**2")
    o = o.replace("³", "**3")
    result = ""
    try:
        result = str(eval(o))

    except BaseException:
        result = "An error occurred."

    return result


def get_pages():
    pages = []
    # Generate a list of 5 embeds
    for i in range(1, 6):
        embed = discord.Embed()
        embed.title = f"I'm the embed {i}!"
        pages.append(embed)
    return pages

@bot.command()
async def translate(ctx, *, text):
    translator = Google_translator()
    text = translator.translate(text, dest='en')
    await ctx.reply(text)

#@bot.command()
#async def translate(ctx, *, message):
    #translator = google_translator()
   # translate_text = translator.translate(message, lang_src="auto", lang_tgt='en')
   # await ctx.reply(translate_text)
   # embed=discord.Embed(title=f"{translate_text}", color=ctx.author.color)
   # await ctx.reply(embed=embed)
   

@bot.command()
async def eee(ctx):
  embed=discord.Embed(title="ok", color=0x7289da)
  e = await ctx.reply(embed=embed)
  await e.add_reaction("📜")
  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji)=="📜"
  await bot.wait_for('reaction_add', check=check)
  await e.edit(content="it workedddd", embed=None)

@bot.command()
async def test1(ctx):
    paginator = Paginator(pages=get_pages())
    await paginator.start(ctx)


@bot.command()
async def bans(ctx):
    bans = await ctx.guild.bans()
    pretty_list = ["{0.name}#{0.discriminator}".format(entry.user) for entry in bans]
    await ctx.send("**Ban list:** \n{}".format("\n".join(pretty_list)))

@bot.command()
@commands.is_owner()
async def newhelp(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `-help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.reply(embed=help_embed)
  


bot.launch_time = datetime.datetime.utcnow()


@bot.hybrid_command()
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    #embed=discord.Embed(title=f"ive been up for **`{days}d, {hours}h, {minutes}m, {seconds}s`**", color=discord.Color.blurple())
    #await ctx.reply(embed=embed)
    await ctx.reply(f"Uptime: **{days} days, {hours} hours, {minutes} minutes and {seconds} seconds**")

@bot.command()
async def give(ctx):
  await ctx.reply("**`-send`**")

bot.session_message={}




@bot.command()
async def dropk(ctx):
  gay=["https://cdn.discordapp.com/attachments/720550041185681440/852165342725537812/card-5.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/852165342516084786/card-4.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/852165342343331850/card-1.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/852165342171496448/card.jpg"]
  ga = random.choice(gay)
  channel = bot.get_channel(729627298634137600)
  ea=await channel.send(ga)
  await ea.add_reaction("1️⃣")
  await ea.add_reaction("2️⃣")
  await ea.add_reaction("3️⃣")
  if ga == gay[2]:
    await ea.add_reaction("4️⃣")
  return


@bot.command()
@commands.is_owner()
async def ehelp(ctx):
    embed1 = discord.Embed(title="1", color=ctx.author.color)
    embed2 = discord.Embed(title="2", color=ctx.author.color)
    embeds = [embed1, embed2]
    e = pgi(bot=bot,
                  ctx=ctx,
                  embeds=embeds,
                  only=ctx.author)
    await e.start()

@bot.event
async def on_member_join(member):
  embed=discord.Embed(title="Welcome!", description=f"Ayyy, you finally showed up\night so you can get your roles from <#710531658620731492>, Enjoy your stay here!", color=discord.Color.random())
  channel=bot.get_channel(800064480293027840)
  await channel.send(member.mention, embed=embed)

@bot.command()
@commands.is_owner()
async def update(ctx, *,text):
  img = Image.open("egc.png")
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Roboto-Bold.ttf", 31)
  
  draw.text((195,120), text, (255, 255, 255), font=font)
  
  img.save("newegc.png")
  await ctx.reply(file=discord.File("newegc.png"))


@bot.command()
async def news(ctx, *,amount=3):
   # await ctx.trigger_typing()
    news = Aninews(amount)
    embed=discord.Embed(title="Latest News", color=discord.Color.random())
    embed.set_thumbnail(url=news.images[0])
    for i in range(amount):
        embed.add_field(name=f"{i+1}) {news.titles[i]}", value=f"{news.description[i][:200]}...\n[Read More]({news.links[i]})")
    await ctx.reply(embed=embed)

    
@bot.command()
async def kaomoji(ctx):
    kaomojis = Kao(5)
    print(kaomojis)
    embed=discord.Embed(title="Kaomoji", description=kaomojis, color=discord.Color.random())
    await ctx.reply(embed=embed)

@bot.command()
async def anilyrics(ctx, *,name):
    try:
        lyrics = Anilyrics(name)
        embed=discord.Embed(title=name, description=lyrics.english, color=0x5865f2)
        await ctx.reply(embed=embed)
    except:
        await ctx.reply(f"couldn't find one for {name}")
    


wordlo=["mf", "Mf", "MF", "mF"]

global burgure
burgure="off"

@bot.listen('on_message')
async def mf_burgure(message):
  if burgure=="on":
	  if message.author.id==304911836460089345:
		  for word in wordlo:
			  if word in message.content:
				  await message.channel.send("i censored that, dont say it!", delete_after=1.5)
				  await message.delete()

@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def decipher(ctx, opt='Easy'):
        options = ['easy', 'medium', 'hard', 'impossible']
        if not opt.lower() in options:
            await ctx.send('Give a valid difficulty.\n**Current Difficulties:**\n> `Easy` `Medium` `Hard` `Impossible`')
            return
        choice = opt.lower()
        if choice == 'easy':
            choice = random2.choice(words.easy)
        elif choice == 'medium':
            choice = random2.choice(words.medium)
        elif choice == 'hard':
            choice = random2.choice(words.hard)
        elif choice == 'impossible':
            choice = random2.choice(words.impossible)
        x = list(choice)
        random2.shuffle(x)
        await ctx.send('**⬇ The word you must decipher is ⬇**')
        await ctx.send(' '.join(map(str, x)))

        def check(m):
            user = ctx.author
            if m.author.id == user.id and m.content.lower() == choice.lower():
                return True
            return False
        try:
            start = time.time()
            await bot.wait_for('message',timeout=30.0,check=check)
            end = time.time()
            await ctx.send(embed=discord.Embed(
                title='Congratulations!',
                colour=discord.Colour.green(),
                description='You were able to guess my word within **{:.2f}**s <a:tada:787761454564114444>'.format(end-start),
                timestamp=ctx.message.created_at
            ).set_footer(text='Well Done!', icon_url=bot.user.avatar.url))
        except asyncio.TimeoutError:
            await ctx.send(embed=discord.Embed(
                title='Failure...',
                colour=discord.Colour.red(),
                description='You weren\'t able to guess my word. Better luck next time, my word was **{}**'.format(choice),
                timestamp=ctx.message.created_at
            ).set_footer(text='You lost!', icon_url=bot.user.avatar.url))

@bot.command(aliases=["vc", "join"])
async def vcjoin(ctx):
    e=ctx.author.voice
    if not e:
        return await ctx.reply("join the vc first?")
    await ctx.reply("joined 🎶")
    await e.channel.connect()

@bot.command()
async def joinvca(ctx):

            destination = ctx.author.voice.channel
            if ctx.voice_state.voice:
                    await ctx.voice_state.voice.move_to(destination)
                    return

            ctx.voice_state.voice = await destination.connect()
            embed = discord.Embed(
                    title="Connected to Music :musical_note:",
                    color=0xFF0000,
            )
            await ctx.send(embed=embed)

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['warns'] = 0

async def add_warns(users, user, warns):
    users[f'{user.id}']['warns'] += warns

@bot.command()
@commands.is_owner()
async def ughwarn(ctx, user: discord.Member, *,reason):
    if user==ctx.author:
      await ctx.reply("no.")
      return
    with open('warn.json', 'r') as f:
        users = json.load(f)

    await update_data(users, user)
    await add_warns(users, user, 1)

    with open('warn.json', 'w') as f:
        json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)

    embed=discord.Embed(title=f'{user.name} was warned for __`{reason}`__', color=discord.Color.random(), timestamp=ctx.message.created_at)
    await ctx.reply(ctx.author.mention, embed=embed)

@bot.command(aliases=["rw"])
@commands.is_owner()
async def ughremovewarn(ctx, user: discord.Member, amount: int=None):
    user = user or ctx.author
    with open('warn.json', 'r') as f:
        users = json.load(f)

    amount = amount or 1

    await update_data(users, user)
    await add_warns(users, user, -amount)

    if users[f'{user.id}']['warns'] <= 0:
        with open('warn.json', 'w') as f:
            del users[f'{user.id}']['warns']
            del users[f'{user.id}']
            f.write(json.dumps(users, indent=4))
        await ctx.reply("**reset done!**")
        return

    else:

        with open('warn.json', 'w') as f:
            json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)

        embed=discord.Embed(title=f'Removed `{amount}` warns from {user.name}', color=discord.Color.random())
        await ctx.reply(ctx.author.mention, embed=embed)
        return



@bot.command()
@commands.is_owner()
async def ughwarns(ctx, user: discord.Member=None):
  user = user or ctx.author
  try:
    with open('warn.json', 'r') as f:
      users = json.load(f)

    warns = users[f'{user.id}']['warns']

    embed=discord.Embed(title=f'{user.name} has `{warns}` warnings', color=discord.Color.random())
    await ctx.reply(ctx.author.mention, embed=embed)
  except:
    await ctx.reply(f"**{user.name} doesn't have `any` warnings**")



@bot.command()
async def newaki(ctx):
      await ctx.message.delete()
      loading = await ctx.send("Loading... ")
      force_ended = False
      buttons = ['◀️', '✅', '❌', '🤷', '😕', '⁉️', '😔']
      aki = akinator.Akinator()
      q = aki.start_game()
      await loading.delete()
      target_progress = 80
      q_num = 1
      first_answer = True
      while True and not force_ended:
        while aki.progression <= target_progress:
          embed=discord.Embed(title=f"Q.{q_num} "+q + "\n\t", description="[ ◀️ (Back) / ✅ (Yes) / ❌ (No) / 🤷 (Probably) / 😕 (Probably Not) / ⁉️ (Idk) / 😔 (End)]", color=ctx.author.color)
          embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar.url)
          sent = await ctx.send(embed=embed)
          q_num += 1
          for num_of_answers in range(len(buttons)):
            await sent.add_reaction(buttons[num_of_answers])
          try: 
              reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)
          except asyncio.TimeoutError:
              embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red)
              await ctx.send(embed=embed)
              break
          else:
              if reaction.emoji == "◀️":
                try:
                    q = aki.back()
                    q_num -= 2
                except akinator.CantGoBackAnyFurther:
                    pass
              else:
                if reaction.emoji == "✅":
                  q = aki.answer("y")
                elif reaction.emoji == "❌":
                  q = aki.answer("n")
                elif reaction.emoji == "🤷":
                  q = aki.answer("p")
                elif reaction.emoji == "😕":
                  q = aki.answer("pn") 
                elif reaction.emoji == "⁉️":
                  q = aki.answer("idk")
                elif reaction.emoji == "😔":
                  embed=discord.Embed(title="Ended...", description="Akinator Has Force Ended!", color=ctx.author.color)
                  await ctx.send(embed=embed)
                  force_ended = True
                  break

        if not force_ended:      
          aki.win()
          embed1=discord.Embed(title=f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?", color=ctx.author.color)
          embed1.set_image(url=aki.first_guess['absolute_picture_path'])
          sent2 =await ctx.send(embed=embed1)
          buttons2 = ['✅', '❌']

          for emojis in range(len(buttons2)):
            await sent2.add_reaction(buttons2[emojis])

          while True:
            try: 
              reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)
            except:
              embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red)
              await ctx.send(embed=embed)
              break
          
            else:
              if reaction.emoji == '✅':
                if first_answer:
                  embed=discord.Embed(title="Yay, First Try!", color=discord.Colour.green())
                  await ctx.send(embed=embed)
                  force_ended = True
                  break
                else:
                  embed=discord.Embed(title="Yay", color=discord.Colour.green())
                  await ctx.send(embed=embed)
                  force_ended = True
                  break
                
              elif reaction.emoji == '❌':
                if aki.progression > 95:
                    force_eneded = True
                    embed=discord.Embed(title="You Have Defeated Me!", color=discord.Colour.red())
                    await ctx.send(embed=embed)
                    break
                target_progress = 95
                break

afkdict = {}

@bot.command()
async def newafk(ctx, message):
    global afkdict

    #remove member from afk dict if they are already in it
    if ctx.message.author in afkdict:
        afkdict.pop(ctx.message.author)
        await ctx.send('you are no longer afk')


    else:
        afkdict[ctx.message.author] = message
        await ctx.send(f"You are now afk with message - {message}")
    #check if mention is in afk dict
    for member in message.mentions: #loops through every mention in the message
        if member != message.author: #checks if mention isn't the person who sent the message
            if member in afkdict: #checks if person mentioned is afk
                afkmsg = afkdict[member] #gets the message the afk user set
                await message.channel.send(f" {member} is afk - {afkmsg}")

@bot.command()
async def newtrivia(ctx):
        await ctx.message.delete()
        wrong = False
        answers = []
        buttons = ["🔴","🟡","🟢", "🔵"]
        response = requests.get("https://opentdb.com/api.php?amount=1")
        trivia_json_data = json.loads(response.text)
        question = trivia_json_data['results'][0]["question"]
        correct_answers = trivia_json_data['results'][0]["correct_answer"]
        incorrect_answers = trivia_json_data['results'][0]["incorrect_answers"]

        embed=discord.Embed(title=f"{html.unescape(question)}", description="Show off your knowlege! Choose the correct answer! ", color=ctx.author.color)
        embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar.url)
        sent1=await ctx.send(embed=embed)

        answers.append(correct_answers)

        for i in range(len(incorrect_answers)):
          answers.append(incorrect_answers[i])
      
        if len(answers) > 2:
          random2.shuffle(answers)

        show_answers = answers.copy()

        for i in range(len(show_answers)):
          show_answers[i] = buttons[i] + " " + html.unescape(show_answers[i])

        embed=discord.Embed(title="\n".join(show_answers), color=ctx.author.color)
        sent2 = await ctx.send(embed=embed)

        for num_of_answers in range(len(show_answers)):
          await sent2.add_reaction(buttons[num_of_answers])

        while True:
          try:
              reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

          except asyncio.TimeoutError:
              if answers.index(correct_answers) == 0:
                embed=discord.Embed(title="Times up! The Answer Is 🔴", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 1:
                mbed=discord.Embed(title="Times up! The Answer Is 🟡", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 2:
                embed=discord.Embed(title="Times up! The Answer Is 🟢", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 3:
                embed=discord.Embed(title="Times up! The Answer Is 🔵", color=16711680)
                await ctx.send(embed=embed)
            
              await sent1.delete()
              await sent2.delete()
              break

          else:
              if reaction.emoji == "🔴":
                if answers.index(correct_answers) == 0:
                  embed=discord.Embed(title="Correct! The Answer Is 🔴", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🟡":
                if answers.index(correct_answers) == 1:
                  embed=discord.Embed(title="Correct! The Answer Is 🟡", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🟢":
                if answers.index(correct_answers) == 2:
                  embed=discord.Embed(title="Correct! The Answer Is 🟢", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🔵":
                if answers.index(correct_answers) == 3:
                  embed=discord.Embed(title="Correct! The Answer Is 🔵", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break

        if wrong:
          if answers.index(correct_answers) == 0:
            embed=discord.Embed(title="Incorrect! The Answer Is 🔴", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 1:
            embed=discord.Embed(title="Incorrect! The Answer Is 🟡", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 2:
            embed=discord.Embed(title="Incorrect! The Answer Is 🟢", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 3:
            embed=discord.Embed(title="Incorrect! The Answer Is 🔵", color=16711680)
            await ctx.send(embed=embed)

@bot.command()
async def giphy(ctx, *, search):
    embed = discord.Embed(title="GIF",colour=discord.Color.random())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=PysQgdgNYJZ9ZNNUt9WkgyRCLWStWXWv')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=PysQgdgNYJZ9ZNNUt9WkgyRCLWStWXWv&limit=10')
        data = json.loads(await response.text())
        gif_choice = random2.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.reply(embed=embed)

@bot.command()
async def tenor(ctx, *, name):
  async with aiohttp.ClientSession() as session:
    embed = discord.Embed(
        title = 'Tenor gif',
        colour = discord.Color.Random())
      
    response = await session.get(f'https://api.tenor.com/v1/search?q=' + name + '&key=BC7I2Y17MIIB&limit=30&media_filter=basic')
    data = json.loads(await response.text())
    gif_choice = random.randint(0,29)
    embed.set_image(url=data['data'][gif_choice]['gif']['url'])

    await session.close()
    await ctx.send(embed=embed)


@bot.hybrid_command(aliases=["vide", "yt", "youtube"])
async def search(ctx, *,name):
    await ctx.trigger_typing()
    video=danksearch.BetterVideo()
    await video.search(name)
    await ctx.reply(video.url)
 

 
@bot.command(aliases=["triv"])
async def trivia(ctx):
  URL = 'https://www.opinionstage.com/blog/trivia-questions/'
  page = requests.get(URL)
  questions = []
  soup = BeautifulSoup(page.content, 'html.parser')
  r = requests.get(URL, stream=True)
  w=await ctx.send("searching...")
  await asyncio.sleep(0.5)
  await w.delete()
  for line in r.iter_lines():
    if "<p><strong>" in str(line):
      line = line.decode("utf-8")
      linesplit = line.split(".")
      theq = linesplit[1]
      theq = theq.replace("</strong></p>", "")
      questions.append(theq)
  question = random2.choice(questions)
  ps = soup.find_all('p')
  for p in ps:
    if question in str(p):
      index = ps.index(p)
      answer = ps[index + 1]
      q=await ctx.reply(embed=discord.Embed(title=f"{question}\n`You get only 1 chance!`", description="20 secs time!", color=0x7289da))
      answer = str(answer)
      answer = answer.replace("<p>Answer: ", "")
      answer = answer.replace("</p>", "")
      answer = answer.lower()
      def check(m):
        if m.channel.id == ctx.channel.id:
          return ctx.author.id == m.author.id
        return False
      for i in range(1, 2):
        try:
       	  guess = await bot.wait_for("message", timeout=20, check=check)
        except asyncio.TimeoutError:
          await q.edit(content=f"**Time up! `{answer}`**", embed=None)
      if guess.content.lower() == answer.lower():
        await q.edit(embed=discord.Embed(title=f"{question}\n\nYou got it correct! `{answer}`", color=0x00FF66))
      else:
        await q.edit(embed=discord.Embed(title=f"{question}\n\nYou got it wrong! it was `{answer}`", color=0xFF0000))




@bot.command()
async def papi(ctx):
        page1 = Page(title='Papi', description='why', color=discord.Color.random())

        page2 = Page(title='Papi', description='why are you', color=discord.Color.random())

        page3 = Page(title='Papi', description='why are you so gay', color=discord.Color.random())

        menu = PaginatedMenu(ctx)
        menu.add_pages([page1, page2, page3])
        await menu.open()

@bot.command()
async def vote(ctx):
	embed=discord.Embed(description=f"**[Karuta](https://top.gg/bot/646937666251915264/vote)\n[AniGame](https://top.gg/bot/571027211407196161/vote)\n[OwO](https://discordbots.org/bot/408785106942164992/vote)\n[Tatsu](https://top.gg/bot/172002275412279296/vote)\n[Shoob](https://top.gg/bot/673362753489993749/vote)\n[Mudae](https://top.gg/bot/432610292342587392/vote)\n[Gachapon](https://top.gg/bot/815289915557675118/vote)**", color=0x7289da)
	embed.set_author(name=ctx.author,icon_url=ctx.author.avatar.url)
	embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/794075957463351296/846292388275421184/unknown.jpeg")
	await ctx.reply(embed=embed)
@bot.command()
@commands.has_role('EGC TARDS')
async def mf(ctx):
  if burgure=="off":
  	burgure="on"
  	await ctx.reply("aight imma fuck his ass now")
  else:
  	burgure="off"
  	await ctx.reply("oof ok")

@bot.hybrid_command(aliases=["whatis"])
async def ask(ctx, *, something):
        #await ctx.trigger_typing()
        something.replace(' ', '+')
        try:
            req = requests.get("http://api.wolframalpha.com/v1/result?appid=RPYQ54-Q3W9QJKWR9&i=" + something)
            if req.text=="Wolfram|Alpha did not understand your input":
                await ctx.reply("nothing found"),
                return
        except Exception as error:
            print(error)
        author = ctx.message.author
        em = discord.Embed(description=f"**{req.text}**", color=0x7289da)
        em.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
        await ctx.reply(embed=em)

api_key="4b6778943f78c6d3440db7be6bcf1d9c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@bot.command()
async def weather(ctx, *, City):
    complete_url = base_url + "appid=" + api_key + "&q=" + City
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = str(round(y["temp"]-273.15,2))
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"]
        min_temp = format(round(y["temp_min"]-273.15,2))
        max_temp = format(round(y["temp_max"]-273.15,2))
        feels_like = format(round(y["feels_like"]-273.15,2))
        z = x["weather"] 
        icon = z[0]["icon"]
        weather_description = z[0]["description"] 
        weather_main = z[0]["main"] 
        w = x["wind"]
        wind = w["speed"]
        wind_deg = w["deg"]

        def faren(tem):
          tem = float(tem)
          return str(round(tem*9/5+32,2))

        def degDir(d):
          dirs = ['N', 'N/NE', 'NE', 'E/NE', 'E', 'E/SE', 'SE', 'S/SE', 'S', 'S/SW', 'SW', 'W/SW', 'W', 'W/NW', 'NW', 'N/NW']
          ix = round(d / (360. / len(dirs)))
          return dirs[ix % len(dirs)]


        embed = discord.Embed(
            title= str(City),
            color= 0xADD8E6)
        embed.set_author(
            name="Weather Map", url="https://www.openweathermap.org")
        embed.set_thumbnail(url = str("http://openweathermap.org/img/w/" + icon + ".png"))

        embed.add_field(
            name="Temperature",
            value= current_temperature + "°C / " + str(faren(current_temperature)) + "°F",
            inline=True)
        
        embed.add_field(
            name="Feels Like",
            value=feels_like + "°C / " + str(faren(feels_like)) + "°F",
            inline=True)

        embed.add_field(
            name="Wind",
            value=str(wind) + " mph " + str(degDir(wind_deg)),inline=True)

        embed.add_field(
            name="Minimum Temperature",
            value=min_temp + "°C / " + str(faren(min_temp)) + "°F",
            inline=True)
        
        embed.add_field(
            name="Maximum Temperature",
            value=max_temp + "°C / " + str(faren(max_temp)) + "°F",
            inline=True)
            
        embed.add_field(
            name="Humidity", value= str(current_humidiy) + "%", inline=True)

        embed.add_field(
            name="Atmospheric Pressure",
            value= str(current_pressure) + " hPa",
            inline=True)
          
        embed.add_field(
            name="Description",
            value=weather_main + ": " + weather_description,inline=True)

        await ctx.reply(embed=embed)
    else: 
        await ctx.reply("City not found ") 

URL_API = 'https://pokeapi.co/api/v2/pokemon/'

def doALrequest(q: str, v: dict):
    r = requests.post('https://graphql.anilist.co',
                      json={'query': q, 'variables': v})
    return r.json()


@bot.command()
async def animegay(ctx, *, name: str):
        content = doALrequest(q="""query ($s: String, $page: Int) {
        Page(page: $page, perPage: 1) {
            pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
            }
            media(search: $s) {
            title {
                romaji
                english
                native
            }
            status
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            episodes
            duration
            source
            genres
            averageScore
            popularity
            coverImage {
                large
            }
            description
            }
        }
        }""", v={"s": name})
        if content['data']['Page']['media']:
            c = content['data']['Page']['media'][0]
            em = discord.Embed(
                title=f"{c['title']['english'] if c['title']['english'] else ''} |  {c['title']['romaji']} ({c['title']['native']})", color=discord.Color.random())
            em.add_field(name=c['status'], value='lol')
            em.add_field(name="Episodes", value=f"{c['episodes']}", inline=True)
            em.add_field(name="Duration", value=f"{c['duration']}min per ep", inline=True)
            em.add_field(name='Description', value=c['description'], inline=False)
            em.set_image(url=c['coverImage']['large'])
            await ctx.reply(embed=em)
        else:
            await ctx.reply("This anime doesn't exist or maybe try giving the full name")



@bot.command(aliases=["pkmn"])
async def dex2(ctx, pokemonname = None):
    if pokemonname == None:
      pokemonname = "pikachu"

    pokemon = pokemonname
    api = 'https://some-random-api.ml/pokedex?pokemon='+pokemon
    json_data = requests.get(api).json()
    name = json_data["name"]
    ids = json_data["id"]
    types = json_data["type"] 
    spe = json_data["species"]
    image = json_data["sprites"]
    desc = json_data["description"]
    evolu = json_data['family']
    abily = json_data['abilities']
    H = json_data['height']
    W = json_data['weight']
    G = json_data['generation']
    gender = json_data['gender']
    stat = json_data['stats']
    


    s = ", "
 
    com = s.join(types) 
    spes = s.join(spe)
    abi = s.join(abily)
    evo = s.join(evolu['evolutionLine'])
    gen = s.join(gender)
    name=name.upper()
    em = discord.Embed(title =f"{name} #{ids}",
      description=f"About: **{desc}**",
      color = 0x7289da)
    em.set_thumbnail(
      url=image["animated"])
    em.add_field(
      name="Types",
      value=f"{com}",
      inline=True
    )

    em.add_field(
      name="Species",
      value=f"{spes}",
      inline=True
    )

    em.add_field(
      name="Ability",
      value=f"{abi}",
      inline=True
    )

    em.add_field(
      name="Evolution Stage",
      value=f"The {evolu['evolutionStage']} Evolution",
      inline=True
    )

    em.add_field(
      name="Evolution Line",
      value=f"{evo}",
      inline=False
    )

    em.add_field(
      name="Height",
      value=f"{H}",
      inline=True
    )

    em.add_field(
      name="Weight",
      value=f"{W}",
      inline=True
    )

    em.add_field(
      name="Gender",
      value=f"{gen}",
      inline=True
    )

    em.add_field(
      name="Stats :",
      value=f":heart: : {stat['hp']}\n:crossed_swords: : {stat['attack']}\n:shield: : {stat['defense']}\n:dash: : {stat['speed']}",
      inline = True
    )

    em.add_field(
      name="Sp Stats :",
      value=f"Sp :crossed_swords: : {stat['sp_atk']}\nSp️ ️:shield: : {stat['sp_def']}",
      inline = True
    )

    em.set_footer(
      text=f"This Pokemon Is From The {G} Generation\nTotal Stats : {stat['total']}"
    )

    await ctx.send(embed=em)


@bot.command(aliases=["dex"])
async def pokedex(ctx, *, pokemon):

    pokeName = pokemon.lower()
    try:
        r = requests.get(f'{URL_API}{pokeName}')
        packages_json = r.json()
        packages_json.keys()

        embed = discord.Embed(title="Pokedex", color=0x7289da)
        embed.add_field(name="Name", value=packages_json['name'], inline=True)
        embed.add_field(name="Pokedex Order", value=packages_json['order'], inline=True)
        embed.set_image(url= f'https://play.pokemonshowdown.com/sprites/ani/{pokeName}.gif')
        embed.add_field(name="Weight", value=packages_json['weight'], inline=True)
        embed.add_field(name="Height", value=packages_json['height'], inline=True)
        embed.add_field(name="XP Base", value=packages_json['base_experience'], inline=True)
        for type in packages_json['types']: #FOR TO GET A TYPE OF A POKEMON
            embed.add_field(name="Types", value= type['type']['name'].upper(), inline=True)
        embed.set_footer(text=ctx.author)
        await ctx.reply(embed=embed)
    except:
        await ctx.reply("Pokemon not found!")


@bot.command()
async def world(ctx):
    embed = discord.Embed(
        title = "COVID-19 Global Satistics",
        colour = ctx.author.colour
    )
    api = requests.get("https://covid19.mathdro.id/api").json()
    confirmedCases = api["confirmed"]["value"]
    recoveredCases = api["recovered"]["value"]
    deaths = api["deaths"]["value"]
    embed.add_field(name = "Infected People", value = confirmedCases)
    embed.add_field(name = "People Recovered", value = recoveredCases)
    embed.add_field(name = "Deaths", value = deaths)
    embed.set_image(url = f"https://covid19.mathdro.id/api/og")
    await ctx.reply(embed = embed)

@bot.command(aliases=["cv", "covid"])
async def country(ctx, country):
    embed = discord.Embed(
        title = f"COVID-19 Satistics for {country}",
        colour = ctx.author.colour
    )
    api = requests.get(f"https://covid19.mathdro.id/api/countries/{country}").json()
    confirmedCases = api["confirmed"]["value"]
    recoveredCases = api["recovered"]["value"]
    deaths = api["deaths"]["value"]
    embed.add_field(name = "Infected People", value = confirmedCases)
    embed.add_field(name = "People Recovered", value = recoveredCases)
    embed.add_field(name = "Deaths", value = deaths)
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/794075957463351296/836259638319251466/unknown.jpeg")
    embed.set_image(url = f"https://covid19.mathdro.id/api/countries/{country}/og")
    await ctx.reply(embed = embed)

@bot.command()
async def helpnote(ctx, *, text):
    with open("news.json", "r") as f:
        news = json.load(f)
    news["news"] = {}
    news["news"] = text
    with open("news.json", "w") as f:
        json.dump(news, f, sort_keys=True)
    await ctx.message.add_reaction("✨")
    
@bot.hybrid_command()
async def help(ctx):
  #with open("news.json", "r") as f:
    #news = json.load(f)
  #lo = news["news"]
  embed1=discord.Embed(title=f"Prefix for the bot is `- or nk`!\n\nExample: `-help` or `nk help`", description=f">>> **Invite the bot from __[here](https://dis.gd/Threads)__**", color=discord.Color.blurple())
  #embed1.set_thumbnail(url=ctx.author.avatar.url)
  embed1.add_field(name="Features?", value=f">>> **• Moderation\n• Leveling\n• Music\n• Anime\n• Economy\n• Fun and alot more.**")
  embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
 # try:
  #  embed1.add_field(name="News", value=f"> **{lo}**")
 # except:
   # pass
  embed1.set_image(url="https://media.discordapp.net/attachments/794075957463351296/861938955158552576/standard_7.gif")
  embed2=discord.Embed(title="Start-ups", description=f"> **```embed, remindme, nitro, hack, color, fight, status, and say```**", color=ctx.guild.me.color)
  embed2.set_thumbnail(url=ctx.guild.icon)
  embed3=discord.Embed(title=f"Moderation", description=f"> **`mute, kick, ban, unban, arole, rrole, unmute, nick, color, whois, warn, warns, and serverinfo`**", color=discord.Color.blurple())
  #embed3.set_image(url="https://media.discordapp.net/attachments/794075957463351296/865466902407151626/standard_9.gif")
  embed3.set_thumbnail(url=ctx.guild.icon)
  embed4=discord.Embed(title="Economy", description="> **`work, bal, withdraw, deposit, rob, shop, buy, sell, bet, lb, available, and bag`**", color=ctx.guild.me.color)
  embed4.set_thumbnail(url=ctx.guild.icon)
  embed5=discord.Embed(title="Fun", description="> **`search (yt), akinator, hangman, tictactoe, snipe, coinflip, roll, meme, gaymeter, nitro, egayc, cheesylies, dm, egc, fact, inspire, and motivate`**", color=discord.Color.blurple())
  embed5.set_thumbnail(url=ctx.guild.icon)
  embed6=discord.Embed(title="Weeby", description=f"> **`pat, hug, kiss, slap, bonk, sex, cringe, cry, poke, highfive, and smug`**", color=ctx.guild.me.color)
  embed6.set_thumbnail(url=ctx.guild.icon)
  embed7=discord.Embed(title="Giveaway", description="> **`giveaway, and reroll`**", color=discord.Color.blurple())
  embed7.set_thumbnail(url=ctx.guild.icon)
  embed8=discord.Embed(title="Covid", description="> **`world, and country`**", color=ctx.guild.me.color)
  embed8.set_thumbnail(url=ctx.guild.icon)
  embed9=discord.Embed(title="Calculator", description="> **`math or calc`**", color=discord.Color.blurple())
  embed9.set_thumbnail(url=ctx.guild.icon)
  embed10=discord.Embed(title="Pokemon", description="> **```pokemon, dex, and dex2```**", color=ctx.guild.me.color)
  embed10.set_thumbnail(url=ctx.guild.icon)
  embed11=discord.Embed(title="Jokes and Motivation", description="> **`joke, yomomma, dadjoke, roast, inspire, motivate, and quote`**", color=discord.Color.blurple())
  embed11.set_thumbnail(url=ctx.guild.icon)
  embed12=discord.Embed(title="Anime/Hentai", description=f"> **`weeb/char, animeinfo, manga, w, animepfp, wallpapers, sfw, hentai, gen, and nsfw`**", color=ctx.guild.me.color)
  embed12.set_thumbnail(url=ctx.guild.icon)
  embed13=discord.Embed(title="Advanced Commands", description=f"> **`newcalc, newmute, newmeme, and newttt`**", color=discord.Color.blurple())
  embed13.set_thumbnail(url=ctx.guild.icon)
  embed14=discord.Embed(title="Notes", description=f"> **`notes, writenote/an, deletenote/dn, and note <name>`**",color=ctx.guild.me.color)
  embed14.set_thumbnail(url=ctx.guild.icon)
  embed15=discord.Embed(title="Music 🎶", description=f"> **`join, leave, play, queue, stop, skip, remove, np, grab and volume`**", color=discord.Color.blurple())
  embed15.set_thumbnail(url=ctx.guild.icon)
  embed16=discord.Embed(title="Channel Perms", description=f"> **`permn, permy, rolen, and roley`**", color=ctx.guild.me.color)
  embed17=discord.Embed(title="Colors", description=f"> **`hex, changecolor, and random`**", color=discord.Color.blurple())
  embed17.set_thumbnail(url=ctx.guild.icon)
  embed16.set_thumbnail(url=ctx.guild.icon)
  embed18=discord.Embed(title=f"Some API's", description=f"> **`globalnews, advice, facts, imbored, coder, and person`**", color=ctx.guild.me.color)
  embed18.set_thumbnail(url=ctx.guild.icon)
  embed19=discord.Embed(title=f"New Economy", description=f"> **`score, addabout, checkscore, and scorelb`**", color=discord.Color.blurple())
  embed19.set_thumbnail(url=ctx.guild.icon)
  embed20=discord.Embed(title="New Features", description=f"> **`button, and whosgay`**", color=ctx.guild.me.color)
  embed20.set_thumbnail(url=ctx.guild.icon)
  embed21=discord.Embed(title="Slash Commands", description=f"> **`meme, av, topic, joke and giphy`**", color=discord.Color.blurple())
  embed21.set_thumbnail(url=ctx.guild.icon)
  if ctx.channel.is_nsfw():
    embed22=discord.Embed(title="nhentai", description=f"> **`-nhentai <id>`**\n> **`-yknow <hentai/nhentai> -> gets random one`**\n> **`-mix -> gets a random image (hentai)`**", color=ctx.guild.me.color)
  else:
    embed22=discord.Embed(title="Can only be viewed in dungeon channel", color=0xFF0000)
  embed22.set_thumbnail(url=ctx.guild.icon)
  embed23=discord.Embed(title="Leveling", description=f"> **`-rank and ranklb`**", color=discord.Color.blurple())
  embed23.set_thumbnail(url=ctx.guild.icon)
  embed24=discord.Embed(title="Auto Responders", description=f"> **`didnt ask, burgure, and thats crazy`**", color=ctx.guild.me.color)
  embed24.set_thumbnail(url=ctx.guild.icon)
  embed25=discord.Embed(title="Reply to a message and use the command!", description=f"> **`whoasked, error and pls`**", color=discord.Color.blurple())
  embed25.set_thumbnail(url=ctx.guild.icon)
  embed26=discord.Embed(title="Custom Commands", description=f"> **||very soon||**", color=ctx.guild.me.color)
  embed26.set_thumbnail(url=ctx.guild.icon)
  embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24, embed25, embed26]
  paginator = BotEmbedPaginator(ctx, embeds)
  #try:
  #lo = pgi(bot=bot, ctx=ctx, embeds=embeds, only=ctx.author)
  #await lo.start()
 # except:
  #await yo(bot=bot, ctx=ctx, pages=embeds, content=["1", "2", "3", "4", "5"], timeout=60).run()
  #await yo(bot=bot, ctx=ctx, pages=embeds, content=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"], timeout=60).run()
  await paginator.run()

@bot.command()
async def hb(ctx, member:discord.Member):
  if member.id==432139817761898496:
    hb = await ctx.reply(f"his bday is already done")
    await hb.add_reaction("🎂")
    def check(reaction, user):
      return user== ctx.author and str(reaction.emoji)=="🎂"
    await bot.wait_for ('reaction_add', check=check)
    await hb.delete()
    await ctx.send(f"**`{ctx.author.name}`: Happy Birthday {member.mention} <a:tadafgw:800412709316722698>**")
    return
  if member==ctx.author:
  	await ctx.reply("wish yourself in the mirror?")
  	return
  else:
  	await ctx.reply("Couldn't track their birthday record")


@bot.command()
async def aadj(ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': bot.joke_api_key
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")

@bot.command()
async def thisorthat(ctx):
    lo = requests.get("http://itsthisforthat.com/api.php?json").json()
    a = lo["this"]
    e = lo["that"]
    embed=discord.Embed(title="That Instead!", description=f"> **This: {a}**\n> **That: {e}**", color=discord.Color.random())
    await ctx.reply(embed=embed)

@bot.command()
async def sex(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/handhold') as r:
        res = await r.json()
        if user == ctx.author:
        	#Checks if command user is themselves.
          embed = discord.Embed(
          title=f"{ctx.author.name} holds hands",
           color=discord.Colour.random()
          )
          embed.set_image(url=res['url'])
          await ctx.reply(embed=embed)
        else: 
          embed = discord.Embed(title=f"{ctx.author.name} holds hand with {user.name}",
           color=discord.Colour.random()
          )
          embed.set_image(url=res['url'])
          await ctx.reply(embed=embed)

@bot.command()
async def newyt(ctx, *,name):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://normal-api.ml/youtube/searchvideo?query={name}') as r:
            res = r.text()
            vid = res['url']
            await ctx.reply(vid)
        
        
@bot.command()
async def topic(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dinosaur.ml/random/topic/") as r:
            res = await r.text()
            el = res['topic']
            await ctx.reply(f"**{el}**")

@bot.command()
async def cry(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/cry') as r:
        res = await r.json()
        if user == ctx.author:
   # Checks if command user is themselves.
          embed = discord.Embed(
           title=f"{ctx.author.name} cries!",
           color=discord.Colour.random()
          )
          embed.set_image(url=res['url'])
          await ctx.reply(embed=embed)
        else: 
          embed = discord.Embed(
          title=f"{ctx.author.name} cries at {user.name}",
           color=discord.Colour.random()
         )
          embed.set_image(url=res['url'])
          await ctx.reply(embed=embed)

@bot.command()
async def bonk(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/bonk') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} bonks themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} bonks {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def highfive(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/highfive') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} hughfives themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} highfives {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def cringe(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/cringe') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"Look at cringeness of {ctx.author.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} cringes at {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def hug(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/hug') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} hugs themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} hugs {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
@bot.command()
async def kill(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/kill') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} kils themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} kills {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)


@bot.command()
async def bite(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.waifu.pics/sfw/bite') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} bites themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} bites {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def tickle(ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://nekos.life/api/v2/img/tickle') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} tickles themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} tickles {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def poke(ctx, *,user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://nekos.life/api/v2/img/poke') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           description=f"**{ctx.author.name}** pokes themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** pokes**{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def smug(ctx, *, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://nekos.life/api/v2/img/smug') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} smugs!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} smugs at {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def kiss(ctx, *, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/kiss') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} kisses themselves (i guess?)",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} kisses {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def slap(ctx, *, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/slap') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} slaps themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           title=f"{ctx.author.name} slaps {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def pat(ctx, *, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/pat') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           title=f"{ctx.author.name} gives themselves a pat on the back!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"{ctx.author.name} pats {user.name}",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

@bot.command()
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())

@bot.command()
async def wednesday(ctx):
  embed=discord.Embed(title="e",color=ctx.author.color)
  embed.set_image(url=f"https://cdn.discordapp.com/attachments/729627298634137600/839444102868762655/IMG_20210407_164815.jpg")
  await ctx.reply(embed=embed)

@bot.command()
async def adj(ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': bot.joke_api_key
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                await ctx.reply(f"{r['setup']}\n\n{r['punchline']}")

@bot.command(aliases=['affirmate', 'affirmation', 'motivate', 'motivation'])
async def quote(ctx):
        """Collect a truly motivational quote"""
        url = 'https://www.affirmations.dev'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                data = await r.json()
        embed = discord.Embed(
            color=ctx.author.color,
            title=data["affirmation"]
        )
        await ctx.reply(embed=embed)



@bot.command(aliases=['inspiro', 'inspirobot'])
async def inspire(ctx):
        """Collect a not so inspiring quote"""
        url = 'https://inspirobot.me/api?generate=true'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                data = await r.text()
        embed = discord.Embed(
            title="Some Motivation", color=ctx.author.color
        )
        embed.set_image(url=data)
        await ctx.reply(embed=embed)


@bot.command()
async def animepfp(ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/avatars') as r:
        res = await r.json()
        embed = discord.Embed(title="pfps",
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)

@bot.command()
async def yomomma(ctx):
	async with aiohttp.ClientSession() as cs:
		async with cs.get("https://api.yomomma.info/") as r:
			res = await r.json()
			yo=res['joke']
			embed=discord.Embed(title=yo,color=ctx.author.color)
			await ctx.reply(embed=embed)


@bot.command(aliases=["animequote","aq"])
async def animequotes(ctx):
	async with aiohttp.ClientSession() as cs:
		async with cs.get("https://animechan.vercel.app/api/random") as r:
			res = await r.json()
			title=res["anime"]
			des=res["character"]
			quo=res["quote"]
			em=discord.Embed(title=f"Anime: {title}\nCharacter: {des}\n\nQuote: ||{quo}||",color=ctx.author.color)
			await ctx.reply(embed=em)

@bot.listen('on_message')
async def da(message):
  if message.content == "didn't ask":
  	await message.channel.send(f"https://cdn.discordapp.com/attachments/729627298634137600/844240151864410122/image0.jpg")
  if message.content == "didnt ask":
  	await message.channel.send(f"https://cdn.discordapp.com/attachments/729627298634137600/844240151864410122/image0.jpg")
  if message.content == "Didnt ask":
  	await message.channel.send(f"https://cdn.discordapp.com/attachments/729627298634137600/844240151864410122/image0.jpg")
  if message.content == "Didn't ask":
  	await message.channel.send(f"https://cdn.discordapp.com/attachments/729627298634137600/844240151864410122/image0.jpg")



@bot.command(aliases=["wallpaper"])
async def wallpapers(ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/wallpapers') as r:
        res = await r.json()
        embed = discord.Embed(title="wallpapers",
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)

@bot.command()
async def fact(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://uselessfacts.jsph.pl/random.json?language=en") as r:
                data = await r.json()
        embed=discord.Embed(title=data["text"], color=ctx.author.color)
        await ctx.reply(embed=embed)
        
@bot.command()
async def white(ctx):
	await ctx.send(file=discord.File("white.jpg"))


@bot.command()
async def embed(ctx):
        await ctx.send("what do you want the title to be")

        def check(x):
            return x.author == ctx.author

        msg1 = await bot.wait_for('message', check=check, timeout=30)

        await ctx.send("what do you want the desc to be")

        def check(z):
            return z.author == ctx.author

        msg2 = await bot.wait_for('message', check=check, timeout=30)

        await ctx.send("what do you want the field title to be")

        def check(z):
            return z.author == ctx.author

        msg3 = await bot.wait_for('message', check=check, timeout=30)

        await ctx.send("what do you want the desc of the field to be")

        def check(z):
            return z.author == ctx.author

        msg4 = await bot.wait_for('message', check=check, timeout=30)

        await ctx.send("what do you want the footer to have?")

        def check(z):
            return z.author == ctx.author

        msg5 = await bot.wait_for('message', check=check, timeout=30)

        await ctx.send("what do you want the color to be? just make sure you replace the # of the hex code with a 0x like 0xff0000")
        
        def check(z):
            return z.author == ctx.author

        msg6 = await bot.wait_for('message', check=check, timeout=30)
        em = discord.Embed(
          title=msg1.content, 
          description=msg2.content,
          color=int(msg6.content,16)
          )
        em.add_field(name=msg3.content, value=msg4.content)
        em.set_footer(text=msg5.content)
        await ctx.send(embed=em)


repeat= {}

@bot.command()
@commands.is_owner()
async def repeat(ctx, *,member: discord.Member):
	global repeat
	repeat = member.id
	await ctx.send("k")
	


@bot.command()
async def roast(ctx, user: discord.Member = None):
		async with aiohttp.ClientSession().get('https://insult.mattbas.org/api/insult.json') as resp:
			data = await resp.json(content_type=None)
		await ctx.reply(data['insult'])

@bot.command(aliases=["pokemon"])
async def whosthatpokemon(ctx):
	    num = random2.randint(1, 926)
	    async with aiohttp.ClientSession().get(f'https://pokeapi.co/api/v2/pokemon-form/{num}/') as resp:
		    data = await resp.json()
	    embed = discord.Embed(title='Who\'s that pokemon?', color=discord.Color.blue())
	    embed.set_image(url=data['sprites']['front_default'])
	    await ctx.reply(embed=embed)
        #def check(m):
            #return m.author==ctx.author and m.channel==ctx.channel
	    guess = await bot.wait_for('message', check=check)
	    if guess.content == data['name']:
		    embed1=discord.Embed(title=f'Correct!\nThat pokemon is {data["name"]}', color=0x00FF5C)
		    await guess.reply(embed=embed1)
	    else:
		    embed2=discord.Embed(title=f'Incorrect!\nThat pokemon is {data["name"]}',color=0xFF0000)
		    await guess.reply(embed=embed2)



@bot.command()
async def onduty(ctx):
    online, idle, dnd, offline = [], [], [], []

    for user in ctx.guild.members:
        if ctx.channel.permissions_for(user).send_messages:
            if not user.bot and user.status is discord.Status.online:
                online.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.idle:
                idle.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.dnd:
                dnd.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.offline:
                offline.append(f"**{user}**")

    on = len(online)
    off = len(offline)
    dn = len(dnd)
    idlee = len(idle)
    await ctx.send(f"**Number of Mods In {str(ctx.guild.name)}**")
    await ctx.send(f"""**```🟢 - {str(on)} Members!
🟡 - {str(idlee)} Members!
🔴 - {str(dn)} Members!
⚫ - {str(off)} Members!
Total Members: {str(on + idlee + dn + off)}```**""")

@bot.command()
async def font(ctx, *, gene):
    gena = gene
    fontlist = ['random', 'rand' 'small', 'rnd-medium', 'cybermedum']
    fontrandom = random.choice(fontlist)
    arting = text2art(gena, font=f'{fontrandom}')
    await ctx.send(f"""```{arting}
```""")

@bot.command()
async def car(ctx):
        cars = ('Acura', 'Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti', 'Buick', 'Cadillac', 'Chevrolet', 'Chryler', 'Citroen', 'Dodge', 'Ferrari', 'Fiat', 'Ford', 'Geely', 'General Motors', 'GMC', 'Honda', 'Hyundai', 'Infinti', 'Jaguar', 'Jeep', 'Kia Motors', 'Koenigsegg', 'Lamborghini', 'Land Rover', 'Lexus', 'Maserati', 'Mazda', 'McLaren', 'Mercedez-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Pagani', 'Peugeot', 'Porsche', 'RAM', 'Renault', 'Rolls-Royce', 'SAAB', 'Subaru', 'Suzuki', 'Tata Motors', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo')
        message = await ctx.send("""```
    _______
    /|_||_\`.__
    (   _    _ _|
    =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
        _______
        /|_||_\`.__
        (   _    _ _|
        =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
            _______
            /|_||_\`.__
            (   _    _ _|
            =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
                _______
                /|_||_\`.__
                (   _    _ _|
                =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
                        _______
                        /|_||_\`.__
                        (   _    _ _|
                        =`-(_)--(_)-' 
        ```""")
        k = f'Car: {random2.choice(cars)}'
        await message.edit(content=f"""```
                                _______
                                /|_||_\`.__
     {k}                        (   _    _ |
                                =`-(_)--(_)-' 
        ```""")
       

  
@bot.command()
async def ascii(ctx, *, text=None):
    if text is None:
        await ctx.send("You must input some text to make into Ascii!")
        return
    result = pyfiglet.figlet_format(text)

    embed = discord.Embed(description=f"{result}")
    await ctx.send(embed=embed)



@bot.listen('on_message')
async def mod_mail(message):
  if message.author.id == bot.user.id:
    return
  if message.author != message.author.bot:
    if not message.guild:
      await bot.get_guild(710528333632241676).get_channel(798858682410598440).send(f"**`{message.author.name}`: {message.content}**")



@bot.listen('on_message')
async def on_message(msg):
  if msg.author.bot:
    return
  e=msg.author.nick
  file = open("afk.json", "r")
  afk = json.load(file)
  if not str(msg.guild.id) in afk:
    return
  if len(msg.mentions) > 0:
    user = msg.mentions[0]
    if user.id in afk[str(msg.guild.id)]["to-mention-ids"]:
      msgs = f"**{user.name}** is AFK with reason: **{afk[str(msg.guild.id)][str(user.id)]}**"
      await msg.channel.send(msgs)
  if msg.author.id in afk[str(msg.guild.id)]["to-mention-ids"]:
    index = afk[str(msg.guild.id)]["to-mention-ids"].index(msg.author.id)
    del afk[str(msg.guild.id)]["to-mention-ids"][index]
    afk[str(msg.guild.id)].pop(str(msg.author.id))
    dumps = open("afk.json", "w")
    json.dump(afk, dumps, indent = 4)
    await msg.channel.send("Welcome back {}, I removed your AFK.".format(msg.author.mention), delete_after = 10)
    await msg.author.edit(nick=f"{msg.author.name}")

@bot.command(aliases=["brb"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def afk(ctx, *, message = "AFK"):
    file = open("afk.json", "r")
    afk = json.load(file)
    if not str(ctx.guild.id) in afk:
      afk[str(ctx.guild.id)] = {}
    
    if not "to-mention-ids" in afk[str(ctx.guild.id)]:
      afk[str(ctx.guild.id)]["to-mention-ids"] = []
    if not ctx.author.id in afk[str(ctx.guild.id)]["to-mention-ids"]:
      afk[str(ctx.guild.id)][str(ctx.author.id)] = message
      afk[str(ctx.guild.id)]["to-mention-ids"].append(ctx.author.id)
      dumps = open("afk.json", "w")
      json.dump(afk, dumps, indent = 4)
      await ctx.reply("{}, I have set your AFK with reason: **{}**".format(ctx.author.mention, message))  
      await ctx.author.edit(nick = f"[AFK] {ctx.author.nick}")
    else:
      return

@bot.command()
async def wanted(ctx, member:discord.Member=None):
	if member==None:
		member=ctx.author
	wanted=Image.open("wanted.jpg")
	asset = member.avatar.url_as(size=128)
	data = BytesIO(await asset.read())
	pfp = Image.open(data)
	pfp = pfp.resize((177, 177))
	wanted.paste(pfp, ((120, 212)))
	wanted.save("profile.jpg")
	await ctx.reply(file=discord.File("profile.jpg"))

@bot.command()
@commands.is_owner()
async def img(ctx, *, text:str='none'):
  img = Image.open("bg.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Supercell-magic-webfont.ttf", 25)
  
  draw.text((10,200), text, (0,0,0), font=font)
  
  img.save("text.jpg")
  await ctx.send(file=discord.File("text.jpg"))
 
@bot.command()
async def image(ctx):
  await ctx.send(file=discord.File("white.jpg"))

  
@bot.command()
async def rm(ctx):
  embed=discord.Embed(title="Reminders", description="**🔔 Daily in `9 hours`\n🔔 Vote is ready\n🔔 Drop is ready\n🔔 Grab is ready\n🔔 Work in `4 hours`**", color=0x7289da)
  await ctx.reply(embed=embed)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bone(ctx):
  a=await ctx.reply("**__bone:__ i'd be a millionaire in india**")
  await asyncio.sleep(2)
  await a.edit(content="**__indians:__ nword first get a 6inch mobile and then talk about richness**")
  await asyncio.sleep(4)
  await a.edit(content="**__indians:__ now get ready to be killed, cuz u shit talk about india**")
  await asyncio.sleep(3)
  await a.edit(content="**__bone:__ wait wtf u mean**")
  await asyncio.sleep(3)
  await a.edit(content="<:bone1:842041273968099359> <a:die:842041319752728588>")
  await asyncio.sleep(2)
  await a.edit(content="<:bone2:842041221567479830>")
  await asyncio.sleep(2)
  await a.edit(content="👻")
  await asyncio.sleep(1.1)
  await a.edit(content="_ _")

@bone.error
async def bone_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'Hold up fag, try after {:.2f}s'.format(
		    error.retry_after)
		await ctx.reply(msg)
  
 
@bot.command()
async def pgy(ctx):
  embed1=discord.Embed(title="gay", description="ofc", color=0x7289da)
  embed1.set_thumbnail(url=ctx.guild.icon.url)
  embed2=discord.Embed(title="hm", description="alright • a • gay • homo • stfu • gay • brug • ge • ye • im • a • flood • this • sk hard •", color=0x7289da)
  embeds=[embed1, embed2]
  paginator = BotEmbedPaginator(ctx, embeds)
  await paginator.run()
  

    
@bot.command()
async def leave(ctx):
    channel=ctx.author.voice
    if not channel:
        return await ctx.reply("you aint in a vc")
    await ctx.voice_client.disconnect()
    await ctx.reply("i left the vc")
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed=discord.Embed(description=f"**[{rolls}d{limit}={result}]\n\nYou got a `{result}`**", color=ctx.author.color)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    await ctx.reply(content=f"{ctx.author.mention}",embed=embed)
@bot.command()
async def choice(ctx):
    multiple_choice = BotMultipleChoice(
        ctx, ["jason", "zambino", "cheesy", "redacted", "baya", "timmeh"], "Which one is most gay"
    )
    await multiple_choice.run()

    await multiple_choice.quit(multiple_choice.choice)

@bot.command()
@commands.is_owner()
async def admin(ctx, member:discord.Member):
  guild=ctx.guild
  q=await ctx.reply(f"**{member.mention}, `React below to get admin role!`**")
  await q.add_reaction("✅")
  def check(rctn, user):
    return user==member and str(rctn)=="✅"
  await bot.wait_for('reaction_add', check=check)
  for role in guild.roles:
    if role.id==710538260384055366:
      if role not in member.roles:
        await member.add_roles(role)
        await q.edit(content=f"**`you GOT the role!`**")



  
lol="off"
@bot.listen('on_message')
async def trap(message):
  global lol
  if lol=="on":
    if message.author.id==432139817761898496:
      await message.add_reaction("<:doge:803651195674820608>")
    if message.author.id==463984756586184715:
      await message.add_reaction("<:slut:770693048363384872>")
      await message.add_reaction("<:whore:770693334682304522>")
    if message.author.id==658685563263778837:
      await message.add_reaction("<:nibbapeepo:830440085811888157>")
      await message.add_reaction("<:smfd:793041486009860096>")
    if message.author.id==439468223038226434:
      await message.add_reaction("<:kekw:730690001599463457>")
    if message.author.id==520868186019856386:
      await message.add_reaction("<:hahalol:781744457170812928>")
@bot.command()
@commands.has_role('WE3')
async def rctn(ctx):
  global lol
  if lol=="off":
    lol="on"
    await ctx.reply("activated")
  else:
    lol="off"
    await ctx.reply("deactivated")
@bot.command(aliases=["dick", "penis"])
async def ds(ctx, member: discord.Member=None):
  member = member or ctx.message.author
  lol=random2.randint(0,20)
  if member.id==439468223038226434:
    lol=-1
  if member.id==658685563263778837:
    lol=0
  dick="="*lol
  if member.id==439468223038226434:
    embed=discord.Embed(title=f"👉👌 pussy", color=ctx.author.color)
  else:
    embed=discord.Embed(title=f"8{dick}D is your size", color=ctx.author.color)
  embed.set_author(name=f"{member}", icon_url=f"{member.avatar.url}")
  if lol==0:
    embed.set_footer(text=f"{lol} incher aka no dick") 
  elif lol==-1:
    embed.set_footer(text=f"gay af trap")
  else:
    embed.set_footer(text=f"{lol} inches!")
  await ctx.reply(embed=embed)

@bot.command()
async def troll(ctx):
  await ctx.reply(f"https://media.discordapp.net/attachments/805424624502308864/838800708638867476/image0-2-1.gif?width=361&height=500")

@bot.command()
async def oki(ctx):
  await ctx.send("sure?")
  def check(reaction, user):
    return user==ctx.author and str(reaction.emoji)=="✅"
  await bot.wait_for('reaction_add', check=check)
  await ctx.send("successful")
@bot.command()
async def hack(ctx, member:discord.Member=None):
  if member==None:
    await ctx.reply("mention a user along with the command")
    return
  if member==ctx.author:
    await ctx.reply("no")
    return
  b=await ctx.send("you serious? say `y` to confirm and `n` to end the hacking")
  def check(m):
    return m.channel==ctx.channel and m.author==ctx.author
  response=await bot.wait_for('message', check=check)
  if response.content=="y":
    a=await ctx.reply("`Starting..`")
    await asyncio.sleep(3)
    await b.delete()
    await response.delete()
    await a.edit(content=f"`Gathering {member}'s info..`")
    await asyncio.sleep(3)
    await a.edit(content="`Hack was successful, Here are the details`")
    await asyncio.sleep(4)
    await a.edit(content=f"`Name: {member.name}\nLocation: Your mom\nEmail: nevergonnagiveyouup@astley.com\nIP: 696.96.696.69`")
    await asyncio.sleep(6)
    await a.edit(content="https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825")
    await asyncio.sleep(3)
    await a.delete()
    await ctx.reply("nah why would i do that 😏")
  else:
    await ctx.send("hacking was cancelled")

@bot.command()
async def tias(ctx):
  await ctx.reply(f"https://i.imgur.com/jbz9ZBn.png")

@bot.command(aliases=["cl", "cheesylies"])
async def cheesy(ctx):
  lies=["dm me a number between 1 and 10 and i'll send the games when im free", "issue with verification bots been found and dealt with hopefully shouldn't happen again", "The guys been banned, I'll dm you some stuff to recover your account", "oh and ik its unhealthy but it aint jasons fault", "Do y'all ex staff just enjoy hating on everything the current staff do bruh, Get a life its a random valentines event and you man are out here sending essays of `criticism` dis shits so toxic", "id rather we just do like community game events and stuff ran by staff and whoever wants to chat and use the bots can use em yk dont really care bout the main activity and member counts anymore got way too much irl shit to focus on", "its kinda a long message, wanted to fit in as much as i could since we rarely do announcements\nFirst, I wanted to give you guys a little backstory on my journey here: my time in this server started in early 2018", "I took it from 2k to 7k and then the first raid happened and we went back to 3k.", "I then slowly took the server to 18.5k until the latest staff raid a few months ago taking us to 10k", "I've spent over £1k on the prizes, giveaways, contests etc and given out over 300 nitros and i don't regret any of it. Since the server first started","I've genuinely enjoyed giving out all these prizes to people who can't afford games and its all been really fun seeing peoples reactions in dms, hosting contests, forming a small community and meeting lots of different people. But in the past year i've experienced a lotta toxicity causing me to not enjoy being online more but hey thats just one of the things that comes from being an owner can't really complain much. Im sure a lot of you have noticed that the servers been slowly dying for the last month. To those of you asking me to `revive it` and do stuff, id already been losing motivation to run the server and then after the latest raids happened Ive fully lost motivation.", "Plus now that ive moved out and my unis started, Ive barely got any time to be on", "also had a lot of irl issues with multiple funerals recently Ill still be about but no longer directly involved in running events","promotions etc (its already been like this for a while, just haven't made it official here)", "However, just because Im no longer running the server doesn't mean the server will stop", "the staff will be fully running the server themselves and giveaways and contests will still run as usual (its been like this for a while already).", "Instead of focusing on general activity we'd like to try doing more Game Events, Anime/Movie nights and just more community events/tourneys (regardless of how many ppl join). Get roles from #🔰self-assignable-roles", "to get notified for these events. If you'd like to join staff and help run the server check #staff and if you'd like to help run any community events lie", "dm @Eckz (Not Gone)! And if you've got any suggestions on what you'd like us to do use #high_brightnesssuggestions. Also since #karuta-bot has been getting more inactive we've decided to make it public and see how it goes for now", "if too many issues arise it'll be changed back. Make sure you follow the no snipe rules in #🔰bot-rules or you will get banned from the channel", "I'm really thankful for this community and whoever is still using the server, running it has helped distract me from many dark times in my life and i'll always be thankful! Byeee"]
  lo=random2.choice(lies)
  embed=discord.Embed(title=lo, color=ctx.author.color)
  embed.set_author(name="Cheesy#5760", icon_url=f"https://cdn.discordapp.com/avatars/254660097223950336/aafa823c7b51062687a7db2e01fd2411.png?size=1024")
  await ctx.reply(embed=embed)
 

@bot.command()
async def confirme(ctx):
    confirmation = BotConfirmation(ctx, 0x012345)
    await confirmation.confirm("Are you sure?")

    if confirmation.confirmed:
        await confirmation.update("Confirmed", color=0x55FF55)
    else:
        await confirmation.update("Not confirmed", hide_author=True, color=0xFF5555)


  
@bot.command()
async def slot(ctx):
        """ Roll the slot machine """
        emojis = ["<:dijanafuckyou:772457404381790248>", "<:pepestop:730690438599540737>", "<:slut:770693048363384872>", "<:whore:770693334682304522>", "<:nibbakerm:770693023260475422>", "<:nibbapeepo:830440085811888157>"]
        a = random2.choice(emojis)
        b = random2.choice(emojis)
        c = random2.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**"

        if (a == b == c):
            await ctx.reply(f"{slotmachine}- All matching, you won")
        elif (a == b) or (a == c) or (b == c):
            await ctx.reply(f"{slotmachine}- 2 in a row, you won")
        else:
            await ctx.reply(f"{slotmachine}- No match, you lost")


@bot.command(aliases=["burgure"])
async def zucc(ctx):
  if ctx.author.id==658685563263778837:
    await ctx.reply("you're gay af")
  else:
    await ctx.reply("man hes totally a gay")


                

@bot.command()
async def treat(ctx, member:discord.Member):
    if member == ctx.author:
        await ctx.send("You can't treat youself!")
        return
    embed=discord.Embed(
        description=f'**You offered {member.name} a treat!\n{member.mention} react to the emoji below to accept!**',
        color=ctx.author.color
    )
    message = await ctx.reply(embed=embed)

    await message.add_reaction('🍫')
    
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍫'
        
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
        
    except asyncio.TimeoutError:
        msg=(f"**{member.mention} didn't accept the treat in time**")
        gay = await message.edit(content=msg, embed=None)

    else:
        await message.edit(content=f"**{member.mention}, You have accepted {ctx.author.name}'s treat aka `nothing`**", embed=None)



@bot.command(aliases=["aki"])
async def akinator(ctx):
        await ctx.send("Akinator is here to guess!")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b"]
        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while aki.progression < 80:
                embed=discord.Embed(title=q, description="**Your answer: `(y/n/p/b)`**", color=ctx.author.color)
                await ctx.send(f"{ctx.author.mention}",embed=embed)
                msg = await ctx.bot.wait_for("message", check=check)
                if msg.content.lower() == "b":
                    try:
                        q=aki.back()
                    except ak.CantGoBackAnyFurther as e:
                        await ctx.send(e)
                        continue
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except ak.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
            aki.win()
            embed2=discord.Embed(title=f"It's {aki.first_guess['name']} ({aki.first_guess['description']})", description="**Was I correct? `(y/n`**)\n", color=ctx.author.color)
            embed2.set_image(url=f"{aki.first_guess['absolute_picture_path']}\n\t")
            await ctx.reply(embed=embed2)
            correct = await ctx.bot.wait_for("message", check=check)
            if correct.content.lower() == "y":
                await correct.reply("yes im pro at guessing\n")
            else:
                await correct.reply("i tried my best\n")
        except Exception as e:
            print("hmmm")
            await ctx.send(e)
            


ajay='off'
@bot.listen('on_message')
async def ninja(message):
  global ajay
  member=message.author
  guild=message.guild
  if ajay=='on':
    for role in guild.roles:
      if role.id==720506367206621304:
        if role in member.roles:
          if message.content.startswith('<@304911836460089345>'):
            await message.channel.send(f"{member.mention} hes SLEEPING!")
@bot.command()
@commands.is_owner()
async def go(ctx):
  global ajay
  if ajay=='off':
    ajay='on'
    await ctx.reply("enabled")
  else:
    ajay='off'
    await ctx.reply("disabled")

@bot.command()
async def inrole(ctx, *,role:discord.Role):
  member=discord.Member
  for member in ctx.guild.members:
    if role in member.roles:
      people='\n'.join(map(str, role.members))
      embed=discord.Embed(title=f"Members in __{role.name}__", description=f"**`{people}`**", color=ctx.author.color, timestamp=ctx.message.created_at)
      embed.set_footer(text=f"{len(role.members)} in total!")
      await ctx.reply(embed=embed)
      return

@bot.command(aliases=["s"])
async def start(ctx):
  guild=ctx.guild
  member=ctx.author
  for role in guild.roles:
    if role.name== "chatbot: Auto":
      if role not in member.roles:
        await member.add_roles(role)
        await ctx.message.add_reaction("✅")
      else:
        await member.remove_roles(role)
        await ctx.message.add_reaction("❌")

auto_join='off'
@bot.event
async def on_member_join(member):
  global auto_join
  if auto_join=='on':
	  role1 = discord.utils.get(member.guild.roles, id=720506367206621304)
	  await member.add_roles(role1)
	  role2 = discord.utils.get(member.guild.roles, id=830844487349305355)
	  await member.remove_roles(role2)

@bot.command(aliases=["aj", "auto"])
@commands.is_owner()
async def autojoin(ctx):
  global auto_join
  if auto_join=='off':
    auto_join='on'
    await ctx.reply("**Password verification disabled**")
  else:
    auto_join='off'
    await ctx.reply("**Password verification enabled**")

@bot.listen('on_message')
async def chat(message):
    #hm = aiohttp.ClientSession()
    guild=message.guild
    member=message.author
    if message.content=="-start":
        return
    if message.content=="-s":
        return
    if bot.user == message.author:
        return
    for role in guild.roles:
        if role.name=="chatbot: Auto":
            if role in member.roles:
                lmao = [802502081528594472, 830643977022865458]
                if message.channel.id in lmao:
                    api = SafoneAPI()
                    resp = await api.chatbot(query=message, user_id=852585988936826910)
                    await message.reply(resp["answer"].lower())

                    
@bot.command(aliases=["app"])
@commands.has_role('WE3')
async def approve(ctx, member:discord.Member):
  guild=ctx.guild
  for role in guild.roles:
    if role.id==830844487349305355:
      if role in member.roles:
        await member.remove_roles(role)
  for role in guild.roles:
    if role.id==720506367206621304:
      if role not in member.roles:
        await member.add_roles(role)
        await ctx.message.add_reaction("✅")
        return
      if role in member.roles:
        await ctx.reply(f"**{ctx.author.mention}, theyre already approved!**")
        return


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      #await ctx.trigger_typing()
      embed=discord.Embed(color=discord.Color.blurple())
      embed.add_field(name="Usage:", value=f"**```{ctx.prefix}{ctx.command.name} {ctx.command.signature}```**")
      embed.set_author(name=f"{ctx.command.name} info!", icon_url=ctx.author.avatar.url)
      alias = ctx.command.aliases
      if alias:
          embed.add_field(name="Aliases", value=", ".join(alias))
      embed.set_footer(text="thats how to use it")
      e=await ctx.reply(embed=embed)
      await e.add_reaction("⏹️")
      def check(reaction, user):
            return user==ctx.author and str(reaction.emoji)=="⏹️"
      await bot.wait_for("reaction_add", check=check)
      await e.delete()
    elif isinstance(error, commands.CommandNotFound):
        command_names = [str(x) for x in ctx.bot.commands]
        matches = get_close_matches(ctx.invoked_with, command_names)
        if matches:
            embed=discord.Embed(color=ctx.guild.me.color)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            a = "\n"
            embed.add_field(name=f"Did you mean >.<", value=f"** • `{matches[0]}`**")
            return await ctx.reply(embed=embed)
        else:
            pass
    #if isinstance(error, commands.MissingRequiredArgument):
      #await ctx.reply("**`if you dont know how to use a command, just dont?`**")
    elif isinstance(error, commands.DisabledCommand):
      await ctx.reply("**`The command is disabled like your life is`**")
    elif isinstance(error, commands.CheckFailure):
      await ctx.message.add_reaction("<a:noperms:874542960832819232>")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.reply(f"The mentioned member was not found")
      #await ctx.reply("**`You do not have the permissions to do this`**")
    elif isinstance(error, commands.MissingRole):
      await ctx.reply("**`You lack the required role to use this command`**")
    else:
        print(error)

@bot.command()
async def et(ctx):
  embed=discord.Embed(title="a", color=ctx.author.color)
  await ctx.reply("a", embed=embed)


@bot.hybrid_command(aliases=["egayc"])
async def egc(ctx):
  new=["https://media.discordapp.net/attachments/710528752911777934/887328638138212352/unknown.png","https://media.discordapp.net/attachments/710528752911777934/887017732766310410/unknown.png","https://cdn.discordapp.com/attachments/710528752911777934/837218848972341258/20210429_084839.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/837217646130757672/Screenshot_20201230-082834.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/837217646336016384/Screenshot_20210102-175146.jpg", "https://cdn.discordapp.com/attachments/752000823944282112/772021290965401640/Screenshot_20201029-224453.jpg", "https://cdn.discordapp.com/attachments/752000823944282112/760387197366304828/Screenshot_20200928-215933__01.jpg", "https://cdn.discordapp.com/attachments/729627298634137600/834458506672472124/unknown.png", "https://cdn.discordapp.com/attachments/828227950633025536/832647105000505372/Screenshot_20210416-213129.jpg", "https://cdn.discordapp.com/attachments/729627298634137600/832280150137241660/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/832237509417238558/20210415_145426.jpg", "https://cdn.discordapp.com/attachments/729627298634137600/832138962041700383/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/831882045386129418/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/831882140164947978/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/831881477582356510/20210414_151906.jpg","https://cdn.discordapp.com/attachments/710528752911777934/831881341733568552/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/831880975386017812/Screenshot_20210414-184747.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/831880136504377354/20210414_151423.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/831877583733522512/20200923_115743.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/831834770328518666/20200129_142119.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829317960811675718/Screenshot_20210404-181206.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/829302352585949214/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/825720742204932146/Screenshot_20210328-184056.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/812617237310865449/20210220_103033.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/802873736600092672/Screenshot_20210124_121244.jpg", "https://cdn.discordapp.com/attachments/769776058362101780/783350586548027413/unknown.png", "https://cdn.discordapp.com/attachments/492560966383304726/772391627066441728/Screenshot_20200906-134117__01.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/771359531816189962/20200926_214119.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/771362155651137536/Screenshot_20201004-014354.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/771362949515313192/Screenshot_20201016-154038.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/771771437224558682/Screenshot_20201030-212346.jpg", "https://cdn.discordapp.com/attachments/492560966383304726/772391626844405800/Screenshot_20200906-154006__01.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/783350820249927681/unknown.png", "https://cdn.discordapp.com/attachments/689818906956922959/829331103729844244/Screenshot_20201009_213148.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331103927894066/unknown.png", "https://cdn.discordapp.com/attachments/689818906956922959/829331104191610920/Screenshot_20200815_182743_com.discord.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331104719831120/Screenshot_20201005_182343.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331104870694932/Screenshot_20200814_164945.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331105102299196/Screenshot_20201009-205408.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331105709948968/Screenshot_20200703_185600_com.discord.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331106020589588/Screenshot_257.png", "https://cdn.discordapp.com/attachments/689818906956922959/829331106352201768/Screenshot_20200708_034020_com.discord.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331339211046932/20201017_103347.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331339378556978/Screenshot_20201028-150546.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331339639521320/Screenshot_20201030_140157.jpg","https://cdn.discordapp.com/attachments/689818906956922959/829331339827478599/20201018_122022.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331340016615454/IMG_20201013_025133.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331340373655572/20201017_221807.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331340637503508/20201018_112013.jpg","https://cdn.discordapp.com/attachments/689818906956922959/829331340850888774/unknown-2.png", "https://cdn.discordapp.com/attachments/689818906956922959/829331341001621560/Screenshot_20201029_131638.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331341173981204/20201012_112734.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331428046274570/Screenshot_20201220_155611.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331428419436574/Screenshot_20210203_144234.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331428608442378/Screenshot_20210122_102314.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331428881858560/Screenshot_2020-10-31_at_2.10.53_AM.png", "https://cdn.discordapp.com/attachments/689818906956922959/829331429099569212/Screenshot_20210203_143649.jpg", "https://cdn.discordapp.com/attachments/689818906956922959/829331429241651240/Screenshot_20201214_133413.jpg", "https://cdn.discordapp.com/attachments/667355956014743572/829370874476888084/unknown.png", "https://cdn.discordapp.com/attachments/710545224350302319/829394258657935420/20201213_122854.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394258850611250/20201212_192545.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394259073040444/20201125_101111.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394259320111205/20201123_103120.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394665714876426/20201030_102451.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394665908338718/20201026_104947.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394666109272124/20201017_104249.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829394666310729768/20201016_165933.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395019018403900/20201016_162331.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395019227856957/20201016_150450.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395019415945276/20201012_173409.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395019676516382/20201010_165950.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395019969724477/20201003_093143.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395020150865990/20200919_101817.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395137938325534/20200911_194258.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395138132312084/20200907_215231.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395138349760512/20200907_160100.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395138550956032/20200902_190710.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395311323512852/20200820_180036.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395311691825152/20200820_100652.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395312229089344/20200808_223604.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395514315112498/20200802_130534.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395514574372864/20200726_092130.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395514855784508/20200722_120031.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395515238121482/20200721_000000.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395515460157460/20200720_230542.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395895958896640/20200720_225805.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395896637980792/20200717_185812.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395897229115433/20200701_174954.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395897695338556/20200627_184734.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395898110050334/20200619_080603.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395898626605056/20200516_102328.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395898994786314/20200604_140239.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395899452620800/20200513_101612.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829395985822253117/Screenshot_20200509-100705_Discord.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398528668205146/Screenshot_20201206-130222.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398528929431593/Screenshot_20201219-195304.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398529289355294/Screenshot_20201231-190940.jpg","https://cdn.discordapp.com/attachments/786864805554290709/829398529633812480/Screenshot_20210103-133022__01.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398529867907082/Screenshot_20210107-120726.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398530481324042/Screenshot_20210111-142818__01.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398530782789652/Screenshot_20210124-185759.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398531139567696/Screenshot_20210224-194126.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398531365273600/Screenshot_20210228-124746.jpg", "https://cdn.discordapp.com/attachments/786864805554290709/829398531625713732/Screenshot_20210215-155309.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399389961191424/20201017_235057.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399390178771004/20201014_094614.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399390446944336/20201003_095920.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399390833213490/20201015_210032.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399391008718878/Screenshot_20200831-093613_Discord.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399391253037077/20200816_115810.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399391474810890/20200818_191313.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829399836746711050/image.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400068649123840/unknown-149.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400121938018354/1599640969706-1.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829400278796730388/Screenshot_246.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400412792029205/Screenshot_2020-10-08_at_8.11.08_PM-1.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400513300004864/Screenshot_2020-08-27-12-39-24-1.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400671538249829/unknown-11.png", "https://cdn.discordapp.com/attachments/710545224350302319/829400792670797935/IMG_20200719_010443.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829400875175903242/894653258.png", "https://cdn.discordapp.com/attachments/710545224350302319/829401613927448626/IMG_20190423_014735.png", "https://cdn.discordapp.com/attachments/720550041185681440/754319915837685780/Screenshot_20200911-191913__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754319916047400970/Screenshot_20200907-193019__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754319916835799040/Screenshot_20200905-202820__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754319917016285284/Screenshot_20200904-220935__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320132674814082/Screenshot_20200828-135129__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320132842717304/Screenshot_20200828-084313__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320133022941244/Screenshot_20200824-105229__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320133236981770/Screenshot_20200824-105401__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320133387714651/Screenshot_20200823-204918__01.jpg", "https://cdn.discordapp.com/attachments/720550041185681440/754320133698355280/Screenshot_20200822-201216__01.jpg", "https://cdn.discordapp.com/attachments/710545224350302319/829400068649123840/unknown-149.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013320367046697/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013361466638426/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013465548161064/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013625728106506/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013726399791104/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013792414335036/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830013977677135922/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830014025264791562/unknown.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097378496610394/unknown-37.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097378882748466/unknown-114.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097379133751306/unknown-140.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097379352117268/Screenshot_2020-10-30_at_4.15.16_PM.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097379537322024/unknown-35-1.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097379696967730/unknown-154.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097379864346654/Screenshot_20201030-212346.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/830097380266344459/Screenshot_20200926-101801_Discord.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/830097794618228746/unknown-61.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097795154837564/unknown-53.png", "https://cdn.discordapp.com/attachments/710528752911777934/830097795598909450/20201025_112407.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/830098573710458913/unknown-164.png", "https://cdn.discordapp.com/attachments/710528752911777934/830098573957660672/unknown-56.png", "https://cdn.discordapp.com/attachments/710528752911777934/830098574293336164/Screenshot_20200719-212432_Discord.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/830098574523629589/IMG_20200814_160546.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/830098574708703252/unknown-41.png", "https://cdn.discordapp.com/attachments/710528752911777934/830098988304433152/unknown-78.png", "https://cdn.discordapp.com/attachments/710528752911777934/830098988756631562/unknown-60.png", "https://cdn.discordapp.com/attachments/710528752911777934/830099330957967390/unknown-31.png", "https://cdn.discordapp.com/attachments/710528752911777934/830099331154575451/dsmsdds.png", "https://cdn.discordapp.com/attachments/769776058362101780/800806589022863360/20210112_152335.png", "https://cdn.discordapp.com/attachments/769776058362101780/796325247195807794/20210106_113157.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/831562326292561930/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/789215836518613022/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/789104627723141120/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/788416214887694356/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/788844501963767858/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/787728107909152808/20201130_102510.jpg", "https://cdn.discordapp.com/attachments/769776058362101780/780814729169862706/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/780815901338501130/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/778295981154238564/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/777650082342240276/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/777121077658648627/20200725_102007.jpg", "https://cdn.discordapp.com/attachments/769776058362101780/776389533465575464/20201010_165652.jpg", "https://cdn.discordapp.com/attachments/769734245299781662/774635883344691200/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/774617261105086464/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/773614290061099068/unknown.png", "https://cdn.discordapp.com/attachments/769776058362101780/772771530270441472/Screenshot_20201102-113800_Discord.jpg", "https://cdn.discordapp.com/attachments/711664374997319741/737999034907623544/unknown.png", "https://cdn.discordapp.com/attachments/711664374997319741/728711316788871198/20200703_223831.jpg", "https://cdn.discordapp.com/attachments/711664374997319741/727473590143942757/unknown.png", "https://cdn.discordapp.com/attachments/711664374997319741/726879358483955762/unknown.png", "https://cdn.discordapp.com/attachments/711664374997319741/721776764505817088/Pokemon_-_Silver_Version_UE_C.png", "https://cdn.discordapp.com/attachments/794075957463351296/850677235395723294/Screenshot_20210603-192004.jpg", "https://cdn.discordapp.com/attachments/794075957463351296/850677235194920970/Screenshot_20210603-205020.jpg", "https://cdn.discordapp.com/attachments/794075957463351296/850677234972753930/Screenshot_20210603-195831.jpg", "https://cdn.discordapp.com/attachments/710528752911777934/850720749227474944/Screenshot_20210515-221125__01.jpg"]

  gay = random2.choice(new)
  await ctx.reply(gay)



@bot.command()
async def reply(ctx, *,gay=None):
  if gay==None:
    await ctx.reply("tf do u want me to reply with? type it out.")
  else:
    await ctx.reply(f"{gay}")

@bot.command()
async def pp(ctx):
  embed=discord.Embed(title="Yes, wanna suck?", color=ctx.author.color)
  await ctx.send(embed=embed)

@bot.hybrid_command(aliases=["v"])
async def view(ctx):
  if ctx.author.id==852585988936826910:
    embed=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n **`hpzccx · ★★★★ · #1 · ◈2`**    Jujutsu Kaisen · **Gojo Satoru**",color=0xEBD47F)
    embed.set_image(url="https://cdn.discordapp.com/attachments/729627298634137600/843471218158075914/gojo-satoru-2-1.png")
    await ctx.reply(embed=embed)
  elif ctx.author.id==574185390001487883:
    embed2=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n**`qdk32h · ★★★★ · #2 · ◈2 ·`** Horimiya · **Kyouko Hori**", color=0xFDFDFF)
    embed2.set_image(url="https://media.discordapp.net/attachments/729627298634137600/849146982626230292/kyouko-hori-2-2.png")
    await ctx.reply(embed=embed2)
  elif ctx.author.id==423851999038144514:
    embed7=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n**`nhg24kz · ★★★★ · #8 · ◈2 ·`** Kanojo Okarishimasu · **Chizuru Mizuhara**", color=0xff0000)
    embed7.set_image(url="https://media.discordapp.net/attachments/676183322090799104/850263975006699550/chizuru-mizuhara-2-8.png")
    await ctx.reply(embed=embed7)
  elif ctx.author.id==377360707944972290:
    embed3=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n**`dfx · ★★★★ · #1 · ◈1 ·`** The Asterisk War · **Julis Alexia Van Riessfeld**", color=0xECB0FB)
    embed3.set_image(url="https://cdn.discordapp.com/attachments/729627298634137600/828242978899623956/julis-alexia-van-riessfeld-1-1.png")
    await ctx.reply(embed=embed3)
  elif ctx.author.id==685634495839469628:
    embed4=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n **`qfzv5r · ★★★★ · #1 · ◈2 ·`** Tokyo Ghoul · **Ayato Kirishima**", color=0x7BA3F9)
    embed4.set_image(url="https://cdn.discordapp.com/attachments/729627298634137600/828294538514530304/ayato-kirishima-2-1.png")
    await ctx.reply(embed=embed4)
  elif ctx.author.id==520868186019856386:
    embed5=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n   **`h4sgsm · ★★★★ · #1 · ◈2 · `**Genshin Impact · **Keqing**", color=0xD1ADE3)
    embed5.set_image(url=f"https://cdn.discordapp.com/attachments/729627298634137600/829294653223600178/keqing-2-1.png")
    await ctx.reply(embed=embed5)
  elif ctx.author.id==658685563263778837:
    embed6=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n **`hft5d6 · ★★★★ · #592 · ◈2 · `**Attack on Titan: The Final Season · **War Hammer Titan**", color=0x7FAAFF)
    embed6.set_image(url=f"https://cdn.discordapp.com/attachments/729627298634137600/836294716660252754/war-hammer-titan-2-592.png")
    await ctx.reply(embed=embed6)
  elif ctx.author.id==463984756586184715:
    embed7=discord.Embed(title="Card Details", description=f"Owned by {ctx.author.mention}\n\n **`hjqzc7 · ★★★★ · #1 · ◈2 · `**Yu-Gi-Oh! Duel Monsters · **Yami Yugi**", color=0xFFDC00)
    embed7.set_image(url="https://media.discordapp.net/attachments/729627298634137600/885868342907404308/yami-yugi-2-1.png")
    await ctx.reply(embed=embed7)
 
@bot.command(aliases=["dj"])
async def dadjoke(ctx):
	api = 'https://icanhazdadjoke.com/'
	async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
		result = await r.text()
		embed=discord.Embed(title='' +result+ '',color=random.randrange(0x1000000))
		await ctx.reply(embed=embed)

@bot.command()
async def kar(ctx, *, message):
  channel = bot.get_channel(729627298634137600)
  await channel.send(message)
  
@bot.command()
async def info(ctx, member: discord.Member, *,gay=None):
	date_format = "%a, %d %b %Y - %I:%M %p"
	if gay == None:
	  embed = discord.Embed(title=member.created_at.strftime(date_format),
	                      color=ctx.author.color)
	  await ctx.send(embed=embed)
	else:
	  embed1 = discord.Embed(title=member.created_at.strftime(date_format), description=member.joined_at.strftime(date_format), color=ctx.author.color)
	  await ctx.send(embed=embed1)
	  


@bot.command()
@commands.is_owner()
async def choose(ctx, *, choices):
    e = choices.split(',')
    await ctx.send(random2.choice(e))



@bot.command()
@commands.has_role('• Server Managers')
async def sm(ctx, seconds: int):

    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.message.add_reaction("⌛")
    role = get(ctx.guild.roles, name="EGC TARDS")
    perms = ctx.channel.overwrites_for(role)
    if seconds==0:
        await ctx.channel.set_permissions(role, manage_messages=True)
        return
    else:
	    await ctx.channel.set_permissions(role, manage_messages=False)
    await ctx.reply(f"**Slowmode of `{seconds}`secs has been initiated**")


@bot.hybrid_command()
@commands.has_role("Head of Mod")
async def ban(ctx, member: discord.Member, *,reason='no reason'):
	if member.id == 304911836460089345:
		await ctx.send("sorry i can't")
		return
	if reason == None:
		await ctx.send(
		    f"Woah {ctx.author.mention}, Make sure you provide a reason!")
	for role in ctx.guild.roles:
	  if role.name=="EGC TARDS":
	    if role in member.roles:
	      await ctx.reply("**i can't ban them cuz of the `EGC TARDS` role**")
	      return
	else:
		messageok = discord.Embed(
		    title=f"You Successfully banned {member} from __{ctx.guild.name}__ \n**Reason: {reason}**", color=0xFCCAA1)
		await ctx.reply(embed=messageok)
		await member.ban(reason=reason)


@bot.hybrid_command()
@commands.has_role("Head of Mod")
async def kick(ctx, *,member: discord.Member):
  if member == ctx.author:
    await ctx.reply("no")
    return
  for role in ctx.guild.roles:
	    if role.name=="EGC TARDS":
	      if role in member.roles:
	        await ctx.reply("**i can't kick them cuz of the `EGC TARDS` role**")
	        return
  else:
    await member.kick()
    await ctx.reply("done")

@bot.hybrid_command()
@commands.has_role("Head of Mod")
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split("#")
	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			embed1=discord.Embed(title=f"Unbanned {member}!", color=0x00FFD2)
			await ctx.reply(embed=embed1)


@bot.command()
async def typerk(ctx, *, msg):

	channel = bot.get_channel(729627298634137600)
	async with channel.typing():

		await asyncio.sleep(10000)
		await channel.send(msg)

@bot.command()
async def typer(ctx, *, msg):

	channel = bot.get_channel(710528752911777934)
	async with channel.typing():

		await asyncio.sleep(10000)
		await channel.send(msg) 


@bot.command()
async def mycommand(ctx):
	async with ctx.typing():
		# do expensive stuff here
		await asyncio.sleep(5)
	await ctx.send('done!')


@bot.command()
async def wiki(ctx, *, word):
	await ctx.reply(f"https://www.urbandictionary.com/{word}")

@bot.command()
async def rev(ctx):
  embed=discord.Embed(color=ctx.author.color)
  embed.set_image(url="https://cdn.discordapp.com/attachments/710528752911777934/835553443388981258/Youre_Hired_24042021183041.jpg")
  cg=await ctx.reply("**rev who? oh wait that fag**")
  await asyncio.sleep(1.5)
  await cg.edit(content=None,embed=embed)

@bot.command(aliases=["sucy"])
async def katie(ctx):
  embed=discord.Embed(title="katie lol", color=ctx.author.color)
  embed.set_image(url="https://cdn.discordapp.com/attachments/710528752911777934/835554980445552690/unknown-39.png")
  await ctx.reply(embed=embed)
  
@bot.command(aliases=["howtosex"])
async def howtohavesex(ctx):
  embed=discord.Embed(title="explanation",color=ctx.author.color)
  embed.set_image(url="https://cdn.discordapp.com/attachments/710528752911777934/835554331528134716/unknown-7.png")
  await ctx.reply(embed=embed)
  
@bot.command()
async def yare(ctx):
  embed=discord.Embed(title="played himself",color=ctx.author.color)
  embed.set_image(url="https://cdn.discordapp.com/attachments/710528752911777934/835556213525577788/unknown-139.png")
  await ctx.reply(embed=embed)
  
  
@bot.command()
async def style(ctx):
	embed = discord.Embed(
	    title=f"WHAT ARE YOU DOING?",
	    description=f"why do you wanna know my style? are u 12 or somethin?",
	    color=0xe74c3c)
	await ctx.reply(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def ughcolor(ctx, color: discord.Color):
	if color == None:
		color_error_embed = discord.Embed(title="Invalid Arguments!",
		                                  description="usage: `-color <role name or id>`.")
		await ctx.reply(embed=color_error_embed)
		sixteenIntegerHex = int(color.content.replace("#", ""), 16)
		readableHex = int(hex(sixteenIntegerHex), 0)
		color = readableHex
	else:
		color_set_embed = discord.Embed(title="Hex color",
		                                description=f"{color}",
		                                color=color)
		await ctx.reply(embed=color_set_embed)
	
	
	
@bot.command()
@commands.is_owner()
async def deleted(ctx):
	embed = discord.Embed(description=f"> **Prefix for the bot is `-`**\n**Invite the bot from [here](http://dis.gd/Threads)**",
	    color=0x7289da,
	    timestamp=ctx.message.created_at)
	embed.add_field(name="Start-ups",
	                value="> **`ping • reminder • nitro • fbi • embed • test`**", inline=True)
	embed.add_field(
	    name="Moderation",
	    value=
	    "> **`mute • unmute • ban • kick • unban • arole • rrole • nick • whois • color • serverinfo`**", inline=False)
	embed.add_field(
	    name="Economy",
	    value="> **`balance • work • withdraw • deposit • rob • shop • bag`**", inline=True)
	embed.add_field(
	    name="Fun",
	    value=
	    "> **`akinator • snipe • tictactoe/ttt • coinflip • pfp • guildicon • question • reddit • meme • joke • nitro • spam •  facts • report • gaymeter • dm • rgb • slap`**", inline=False)
	embed.add_field(name="Weeby", value="> **`pat • hug • kiss • slap • tickle • poke • smug • cringe • highfive • bonk • cry • sex`**", inline=True)
	embed.add_field(name="Giveaway", value="> **`giveaway • reroll`**", inline=False)
	embed.add_field(name="Math", value="> **`calc`**", inline=True)
	embed.set_author(name="Help Command", icon_url=ctx.guild.icon.url)
	embed.set_thumbnail(url=ctx.author.avatar.url)
	embed.set_footer(icon_url=f"{ctx.guild.icon.url}",
	                 text=f"Requested by {ctx.author}")
	await ctx.reply(embed=embed)


@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def list(ctx, *, lmao):

	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.listening, name=f"{lmao}"))


@bot.command()
async def reddit(ctx):
	await ctx.send("https://i.redd.it/2felmvkpxlc61.gif")


@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def watch(ctx, *, lmao):

	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.watching, name=f"{lmao}"))


@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def playe(ctx, *, lmao):
	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.playing, name=f"{lmao}"))


@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def stream(ctx, *, lmao):
	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.streaming, name=f"{lmao}"))


@bot.command()
async def status(ctx, *, lmao):
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{lmao}"))
  
@bot.command()
async def jd(ctx):
	"gets an invite link of this server"
	await ctx.reply("https://discord.gg/RWEqRy9Qpc")


@bot.command()
async def game(ctx):
	if ctx.author.id == 304911836460089345:
		pp = ["winner", "loser"]
		hmm = random2.choice(pp)
		cock = await ctx.reply("try to be a **WINNER**")
		await asyncio.sleep(1)
		await cock.edit(content=f"{ctx.author.mention} you were a **{hmm}**")
	else:
		lmao = [
		    "loser", "loser", "loser", "loser", "loser", "loser", "loser",
		    "loser", "loser", "loser", "loser", "loser", "loser", "winner",
		    "loser"
		]
		rand = random2.choice(lmao)
		msg = await ctx.send("try to be a **WINNER**")
		await asyncio.sleep(1)
		await msg.edit(content=f"{ctx.author.mention} you were a **{rand}**")


@bot.hybrid_command(help="arg is the text",
             brief="Types the text after the command ",
             aliases=["type"])
async def say(ctx, *, msg):
	if msg == "@everyone":
		await ctx.send("cant say that")
		return
	else:
		await ctx.channel.send(msg)
		await ctx.message.delete()


@bot.command()
async def ughavatar(ctx, *, mem:discord.Member=None):
    mem=ctx.author or mem
    gay=await bot.fetch_user(int(mem))
    embed1 = discord.Embed(color=ctx.author.color, title=f"{gay}", description=gay.id)
    embed1.set_image(url=f"{gay.avatar.url}")
    await ctx.reply(embed=embed1)


@bot.hybrid_command(help="-nick @user nickname", brief="changes nickname")
async def nick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.message.add_reaction("✅")
    embed = discord.Embed(
        title="Nickname Changed!",
        description=f"Nickname has been changed to **__{nick}__**",
        color=ctx.author.color)
    await ctx.reply(embed=embed)

#@nick.error
#async def nick_error(ctx, error):
    #await ctx.reply("nickname too long")
    
@bot.hybrid_command()
async def ping(ctx):
	await ctx.message.add_reaction("🏓")
	"""check the latency of the bot"""
	embed1 = discord.Embed(title=f"yes, {ctx.author}?", color=0xe74c3c)
	msg = await ctx.reply(embed=embed1)
	embed2 = discord.Embed(
	    title=f'Pong! {round(bot.latency * 1000)}ms :ping_pong:',
	    color=ctx.author.color)
	await asyncio.sleep(0.3)
	await msg.edit(embed=embed2)


@bot.hybrid_command(aliases=["c"])
async def clear(ctx, number):
	number = int(number)
	await ctx.channel.purge(limit=(number + 1))
	await ctx.message.delete()


@bot.command()
async def actualfact(ctx):
	msg = await ctx.reply(
	    "you really wanna know what an actual fact is?:flushed:")
	await asyncio.sleep(1)
	await msg.edit(
	    content=
	    "https://media.discordapp.net/attachments/710528752911777934/794824138614374430/unknown.png"
	)


@bot.command(aliases=["yo"])
async def test(ctx):
	"""yeah a test command"""
	message = await ctx.reply("hello")

	await asyncio.sleep(0.5)
	await message.edit(content="goodbye")
	await message.delete()


@bot.command()
async def fbi(ctx):
	msg = await ctx.reply("dialling fbi....")
	await asyncio.sleep(0.7)
	await msg.edit(content="dialling..")
	await asyncio.sleep(1)
	await msg.edit(content="stfu and hang up bitch")


@bot.command(pass_context=True, no_pm=True)
async def guildicon(ctx):
	"""Guild Icon"""
	await ctx.reply("{}".format(ctx.guild.icon.url))


@bot.command()
async def joke(ctx):
	"""listen to the joke"""
	await ctx.message.add_reaction('👀')
	choices = [
	    "leave the server fucking bitch", "aint your life already a joke",
	    "idk im already seeing a joke", "look at r/stfu", "suck my dick",
	    "your birth aint any better stfu",
	    "have u seen a flea? that your penis size"
	]
	randomjoke = random2.choice(choices)
	message = await ctx.reply(f"{randomjoke}")

	await asyncio.sleep(0.7)
	await message.edit(content="jk")


@bot.hybrid_command()
async def dm(ctx, member: discord.Member, *, msg):
	"""dms the mentioned user!"""
	embed = discord.Embed(title=msg)
	await member.send(embed=embed)
	await ctx.message.delete()


@bot.check
async def globally_block_dms(ctx):
	return ctx.guild is not None


@bot.command()
async def rgb(self):
	"""Embed color changing"""
	em1 = discord.Embed(title="Red", colour=0xFF0000)
	await self.message.add_reaction('👀')
	msg = await self.message.channel.send(embed=em1)
	em2 = discord.Embed(title="Green", colour=0x00FF00)
	await asyncio.sleep(0.5)
	await msg.edit(embed=em2)
	em3 = discord.Embed(title="Blue", colour=0x206694)
	await asyncio.sleep(0.5)
	await msg.edit(embed=em3)


@bot.command()
async def jason(ctx):
	"lmao look what bot responds"
	embed=discord.Embed(title="Joker Lookup", description=f"**Character: Jason Vorhees\nSeries: Raiders\n Wishlisted • 6969\n\nEdition • 69\n\nTotal Generated • 6969\nTotal Grabbed • 6969\nTotal Burned • 6969\nBurn Rate = 100%**", color=ctx.author.color)
	embed.set_footer(text="Showing a clown 69 of 69")
	embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/710528752911777934/835877302171992084/rainbowfilter.png")
	await ctx.reply(embed=embed)

@bot.command()
async def henkie(ctx):
	"oh shit henkie is dumb"
	await ctx.reply("henkie is sex")


@bot.command()
async def henry(ctx):
	await ctx.reply(
	    "https://cdn.discordapp.com/attachments/794075957463351296/798114131378438164/Screenshot_20210111-142818__01.jpg"
	)


@bot.command()
async def honoka(ctx):
	await ctx.reply("The only boy with 11bfs")

@bot.command()
async def zambino(ctx):
	"fucking cock sucker"
	embed=discord.Embed(title="Brother of `-jason`",color=ctx.author.color)
	embed.set_image(url=f"https://cdn.discordapp.com/attachments/710528752911777934/835879689184346112/20210425_160711.png")
	await ctx.reply(embed=embed)


@bot.command()
async def dijana(ctx):
	"dijana the lord"
	noob = [463984756586184715]
	if ctx.author.id in noob:
		await ctx.reply(f"{ctx.author.mention} youre so gay")
	else:
		msg = await ctx.reply("stop talking about someone whos gay")
		await asyncio.sleep(0.7)
		await msg.delete()


@bot.command(hidden=True)
async def x(ctx):

	blacklist = [321562647084662794]
	if ctx.author.id in blacklist:
		await ctx.reply(
		    f"{ctx.author.mention} tell me some hacks to be a pro like you")
	else:
		await ctx.reply("man hes pro af")


@bot.command()
async def fizer(ctx):
	await ctx.reply(f"{ctx.author.mention} you son of a.... go study")


@bot.hybrid_command(aliases=["addrole"])
@commands.has_role('Head of Mod')
async def arole(ctx, user: discord.Member, *, role: discord.Role):
	if role in user.roles:
		await ctx.reply(f"{user.mention} already has the **__{role}__** role")
	else:
		await user.add_roles(role)
		embed = discord.Embed(
		    title="Added Role",
		    description=f"**{user.mention} was given a role called: {role.mention}**",
		    color=ctx.author.color)
		await ctx.reply(embed=embed)


@bot.hybrid_command(aliases=["removerole"])
@commands.has_role('Head of Mod')
async def rrole(ctx, user: discord.Member, *, role: discord.Role):
	"""removes a mentioned user role"""
	if role not in user.roles:
		await ctx.reply(f"{user.mention} doesnt have the **__{role}__** role")
	else:
		await user.remove_roles(role)
		embed = discord.Embed(
		    title="Removed Role",
		    description=f"**{user.mention} was removed from the role: {role.mention}**",
		    color=ctx.author.color)
		await ctx.reply(embed=embed)


@bot.command()
async def coinflip(ctx):
	"""as the name says flips the coin"""
	choices = ["🙆 - Heads", "🐒 - Tails"]
	randomcoin = random2.choice(choices)

	embed = discord.Embed(title=f"Flipping coin!",
	                      description="........",
	                      color=ctx.author.color)
	message = await ctx.reply(embed=embed)
	await asyncio.sleep(0.5)

	embed2 = discord.Embed(title=f"Flipped!",
	                       description=f"{randomcoin}",
	                       color=ctx.author.color)
	await message.edit(embed=embed2)


@bot.hybrid_command()
async def serverinfo(ctx):
	"""Gives some info about the server"""
	date_format = "%a, %d %b %Y - %I:%M %p"
	embed = discord.Embed(color=ctx.author.color,
	                      title=f"{ctx.guild.name}",
	                      timestamp=ctx.message.created_at)
	embed.set_thumbnail(url=f"{ctx.guild.icon.url}")
	embed.add_field(name="Owner", value="Cheesy#5760")
	embed.add_field(name="Region", value=f"{ctx.guild.region}")
	embed.add_field(name="Created", value=f"{ctx.guild.created_at.strftime(date_format)}")
	embed.add_field(name="Member Count", value=f"{ctx.guild.member_count}")
	embed.add_field(name="Channels", value=len(ctx.guild.channels))
	embed.add_field(name="Roles", value=len(ctx.guild.roles))

	embed.set_footer(icon_url=f"{ctx.guild.icon.url}",
	                 text=f"Guild ID: {ctx.guild.id}")
	await ctx.reply(embed=embed)


@bot.hybrid_command(aliases=["userinfo", "ui"])
async def whois(ctx, user: discord.Member = None):
	"""an userinfo command"""
	if user == None:
		user = ctx.author
	roles = [role for role in user.roles[1:]]

	embed = discord.Embed(color=user.color,
	                      title=f"{user}",
	                      timestamp=ctx.message.created_at)
	embed.set_thumbnail(url=f"{user.avatar.url}")
	embed.add_field(name="User ID", value=user.id)
	embed.add_field(name="Guild Name", value=user.display_name)
	embed.add_field(
	    name="Joined",
	    value=user.joined_at.strftime("%a, %#d, %B %Y, %I:%M %p"))
	embed.add_field(
	    name="Created",
	    value=user.created_at.strftime("%a, %#d, %B %Y, %I:%M %p"))
	embed.add_field(name="Roles",
	                value=" ".join([role.mention for role in roles]))
	embed.add_field(name="Top Role", value=user.top_role.mention)
	await ctx.reply(embed=embed)


@bot.command(aliases=["stfu"])
async def mute(ctx, member: discord.Member = None, *, reason=None):
    guild = ctx.guild
    user = member
    if member == None:
        await ctx.reply(f'**{ctx.author.mention},** please mention somebody to mute.')
        return
    if member == ctx.message.author:
        await ctx.reply(f"{ctx.author.mention} you can't mute yourself")
        return
    if member.id == 304911836460089345:
        await ctx.reply(f"{ctx.author.mention} you really think you can mute him? LOL")
        return

    for role in guild.roles:
        if role.name == "Muted":
            if role in user.roles:
                await ctx.reply("**{}** is already muted.".format(user))
                return

    embedcheck = discord.Embed(title="Mute",colour=0xFFD166,description=f'Are you sure you want to mute **{user}**\n```Timeout = 5 seconds```')

    embeddone = discord.Embed(title="Muted",colour=0x06D6A0,description=f'The mute has been done. **{user}** cannot talk in any channels anymore\nReason: {reason}')
    embeddone.set_footer(icon_url=ctx.guild.icon.url, text=ctx.guild.name)

    embedfail = discord.Embed(title="Not Muted",colour=0xEF476F,description=f'The mute did not carry out as I did not receive a reaction in time.')

				


@bot.command()
async def fight(ctx, member:discord.Member):
  user1=0
  user2=0
  if member==ctx.author:
    await ctx.reply("**can't fight for your own ass**")
    return
  else:
    embed=discord.Embed(title=f"**{member.name} you down for a fight with {ctx.author.name}**?", color=ctx.author.color)
    az = await ctx.send(f"{member.mention}",embed=embed)
    await az.add_reaction("✅")
    await az.add_reaction("❌")
  
    try:
    
      def check(rctn, user):
        return user.id==member.id and str(rctn) == "✅"
      reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
    except asyncio.TimeoutError:
      await az.edit(content="**Time out!**")
    else:
      await az.edit(content=f"**{ctx.author.name} faces off {member.name}**", embed=None)
      await asyncio.sleep(3)
      await az.delete()
      embed3=discord.Embed(title=f"**Your turn, wanna `attack, defend, kick or slap?`**", color=ctx.author.color)
      await ctx.send(content=f"{member.mention}",embed=embed3)
      def check(m):
        return m.channel == ctx.channel and m.author == member
      response = await bot.wait_for('message', check=check)
      if response.content=="defend":
        user1=random2.randint(50, 100)
      if response.content=="attack":
        user1=random2.randint(70, 100)
      if response.content=="kick":
        user1=random2.randint(150, 200)
      if response.content=="slap":
        user1=random2.randint(40, 60)
      embed4=discord.Embed(title=f"**Your turn, wanna `attack, defend, kick or slap?`**", color=ctx.author.color)
      await ctx.send(content=f"{ctx.author.mention}", embed=embed4)
      def check(m):
        return m.channel == ctx.channel and m.author == ctx.author
      response = await bot.wait_for('message', check=check)
      if response.content=="defend":
        user2=random2.randint(50, 100)
      if response.content=="attack":
        user2=random2.randint(70, 100)
      if response.content=="kick":
        user2=random2.randint(150, 200)
      if response.content=="slap":
        user2=random2.randint(40, 60)
      if (user1) > (user2):
        io=discord.Embed(title=f"{member} dealth `{user1}` damage\n\n{ctx.author} dealth `{user2}` damage", color=ctx.author.color)
        await ctx.send(content=f"{member.mention} WON!", embed=io)
      if (user2) > (user1):
        oi=discord.Embed(title=f"{ctx.author} dealth `{user2}` damage\n\n{member} dealth `{user1}` damage", color=ctx.author.color)
        await ctx.send(content=f"{ctx.author.mention} WON!",embed=oi)
        
@bot.command(aliases=["unstfu"])
async def unmute(ctx, member: discord.Member, *, reason=None):

	muterole = discord.utils.get(member.guild.roles, name='Muted')
	if member == ctx.message.author:
		await ctx.reply(f"{ctx.author.mention} you can't unmute yourself")
		return
	if muterole in member.roles:
		infoembed = discord.Embed(
		    title=f'User has been unmuted',
		    description=
		    f'{member.mention} has been unmuted by ||{ctx.author.mention}||\nReason: {reason}',
		    color=ctx.author.color)
		infoembed.set_thumbnail(url=ctx.guild.icon.url)
		infoembed.set_footer(icon_url=ctx.guild.icon.url, text=ctx.guild.name)
		await member.remove_roles(muterole, reason=reason)
		await ctx.reply(embed=infoembed)
	else:
		await ctx.reply(f'{member.mention} is not muted')
		return


@bot.command()
async def question(ctx, *, question):
	"ask the question"
	embed = discord.Embed(title=question,
	                      description="\n✅ = Yes**\n**❎ = No",
	                      color=ctx.author.color)
	msg = await ctx.send(embed=embed)
	await msg.add_reaction('✅')
	await msg.add_reaction('❎')
	await ctx.message.delete()


@bot.command()
@commands.is_owner()
async def moverole(ctx, pos: int, *, role: discord.Role):

	try:
		await role.edit(position=pos)
		await ctx.send("Role moved.")
	except discord.Forbidden:
		await ctx.send("You do not have permission to do that")
	except discord.HTTPException:
		await ctx.send("Failed to move role")
	except discord.InvalidArgument:
		await ctx.send("Invalid argument")


@bot.hybrid_command(aliases=['ball'])
async def eball(ctx, *, question):

	responses = [
	    "It is certain.", "It is decidedly so.", "Without a doubt.",
	    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
	    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
	    "Reply hazy, try again.", "Ask again later.",
	    "Better not tell you now.", "Cannot predict now.",
	    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	    "My sources say no.", "Outlook not so good.", "Very doubtful.,"
	    "ask your mom :)"
	]

	embed = discord.Embed(
	    title="8ball",
	    description=f'Question: {question}\nAnswer: {random2.choice(responses)}',
	    color=ctx.author.color)
	await ctx.reply(embed=embed)


@bot.command()
async def shutdown(ctx):

	await ctx.reply(f"{ctx.author.mention} ill shut your ass down")


@bot.command()
async def lmao(ctx, *, msg):
  channel = bot.get_channel(710528752911777934)
  await channel.send(msg)
	  

@bot.command()
async def msg(ctx, chanl:int, *,gay):
  channel=bot.get_channel(chanl)
  await channel.send(gay)
  
 
@bot.hybrid_command()
async def invite(ctx, a=None):
  if a==None:
    link = await ctx.channel.create_invite(max_age = 300)
    await ctx.reply(f"Here is an instant invite to your server \n{link}")
  else:
    channel=bot.get_channel(830844488645738501)
    link = await channel.create_invite(max_age=300)
    await ctx.reply(f"Here\n {link}")
    
    
@bot.command()
async def nitro(ctx):
	"GET FREE NITRO"
	await ctx.reply(
	    "https://cdn.discordapp.com/attachments/763631707341455370/763631736222908446/image0.png")

@bot.event
async def on_member_update(before, after):
    guild = before.guild
    for role in guild.roles:
        if role.id == 720506367206621304:
            if role in before.roles:
                channel = bot.get_channel(794080301604798515)
                if before.display_name != after.display_name:
                    embed = discord.Embed(#title="Member update",
                              title="Nickname change",
                              color=0x00ff93)
                              #timestamp=datetime.utcnow())
                    embed.set_thumbnail(url=before.avatar.url)
                    #fields = [("Before", before.display_name, False), ("After", after.display_name, False)]
                        
                    #for name, value, inline in fields:
                    embed.add_field(name="Before", value=before.display_name, inline=False)
                    embed.add_field(name="After", value=after.display_name, inline=False)
    
                    await channel.send(embed=embed)


@bot.event
async def on_message_delete(message):
  member=message.author
  guild=message.guild
  for role in guild.roles:
    if role.id==720506367206621304:
      if role in member.roles:
        try:
            if message.content.startswith("https://"):
                return
            deleted = discord.Embed(description=f"Message deleted in {message.channel.mention}", color=0x4040EC).set_author(name=message.author, icon_url=message.author.avatar.url)
            deleted.add_field(name="Message", value=message.content)
            deleted.timestamp = message.created_at
            channel=bot.get_channel(794080301604798515)
            await channel.send(embed=deleted)
        except:
            embed=discord.Embed(description=f"Image/link deleted in {message.channel.mention}",color=discord.Color.blurple())
            embed.set_author(name=message.author, icon_url=message.author.avatar.url)
            embed.set_image(url=message.attachments[0].proxy_url)
            chan=bot.get_channel(794080301604798515)
            await chan.send(embed=embed)
            
            
@bot.event
async def on_message_edit(before, after):
  member=before.author
  guild=before.author.guild
  for role in guild.roles:
    if role.id==720506367206621304:
      if role in member.roles:
        embed = discord.Embed(
        timestamp=after.created_at,
        description = f"<@{member.id}>**'s message was edited in** <#{before.channel.id}>.",
        colour = (0xFF0000))
        embed.set_author(name=f'{member.name}#{member.discriminator}', icon_url=before.author.avatar.url)
        embed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
        embed.add_field(name="After:", value=after.content + "\u200b", inline=False)
        channel = bot.get_channel(794080301604798515)
        await channel.send(embed=embed)
  await bot.process_commands(after)
    
    
@bot.command()
@commands.is_owner()
async def logs(ctx, *, aa):
	channel = bot.get_channel(794080301604798515)
	await channel.send(aa)


@bot.hybrid_command(pass_context=True)
async def gaymeter(ctx):
	dexter = [304911836460089345]
	responses = [
	    "jason af",
	    "extremely gay",
	    "so gay like literally",
	    "gay af",
	    "bi bruh",
	    "straight af",
	    "very straight",
	    "30% gay",
	    "20% gay",
	    "10% gay",
	]
	randomlmao = random2.choice(responses)
	if ctx.author.id in dexter:
		await ctx.reply(f"{ctx.author.mention} you aint gay cuz youre so pro")

	else:
		await ctx.reply(f"{ctx.author.mention} youre {randomlmao}")


@bot.listen('on_message')
async def nibba_ping(msg):
	if msg.content=="<@396277862459768843>":
		embed = discord.Embed(title="The prefix is **`-`**",
		                      description="To view my commands, type `-help`",
		                      color=0xFF0000)
		gay= await msg.reply(embed=embed)
		await asyncio.sleep(2.5)
		await gay.delete()


@bot.command()
async def yesorno(ctx):
	global times_used
	await ctx.send(f"y or n")

	# This will make sure that the response will only be registered if the following
	# conditions are met:
	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["y", "n"]

	msg = await bot.wait_for("message", check=check)
	if msg.content.lower() == "y":
		await ctx.send("You said yes!")
	else:
		await ctx.send("You said no!")

	times_used = times_used + 1


@bot.command(hidden=True)
@commands.has_role('Head of Mod')
async def permn(ctx, member: discord.Member):

	perms = ctx.channel.overwrites_for(member)
	await ctx.channel.set_permissions(member, read_messages=False)
	embed = discord.Embed(
	    title=f"{member}'s perms",
	    description=f"{member.mention} cant read this channel now rip",
	    color=ctx.author.color)
	await ctx.reply(embed=embed)


@bot.command(hidden=True)
@commands.has_role('Head of Mod')
async def permy(ctx, member: discord.Member):

	perms = ctx.channel.overwrites_for(member)
	await ctx.channel.set_permissions(member, read_messages=True)
	embed = discord.Embed(
	    title=f"{member}'s Perms",
	    description=f"lmao {member.mention} can read this channel now!",
	    color=ctx.author.color)
	await ctx.reply(embed=embed)


@bot.command()
async def number(ctx):
	stfu = [1, 2, 3]
	lmao = random2.choice(stfu)
	await ctx.send(f"{lmao}")


@bot.command()
async def report(ctx, member: discord.Member, *, text):
	embed = discord.Embed(
	    title="Listen up you little shit",
	    description=
	    f"Youve been reported by **{ctx.author}** for ||**`{text}`**||",
	    color=0xf1c40f,
	    timestamp=ctx.message.created_at)
	await member.send(embed=embed)
	await ctx.message.delete()


@bot.command()
async def cock(ctx):
	await ctx.send(f"{ctx.author.mention} stfu cock sucker")


@bot.command(hidden=True)
async def rules(ctx, member: discord.Member):

	embed = discord.Embed(
	    title=f"{member} broke a rule",
	    description=
	    f"{member.mention} you just broke a rule, resulting will lead to mute ||ofc im jk||",
	    color=ctx.author.color,
	    timestamp=ctx.message.created_at)
	await ctx.reply(embed=embed)


@bot.command(hidden=True, aliases=["bye"])
async def logout(ctx):
	if ctx.author.id == 304911836460089345:
		await ctx.reply("logging out")
		await ctx.bot.close()
	else:
		await ctx.reply("youve no permission to log me out")


@bot.command(hidden=True)
@commands.is_owner()
async def check(ctx):
	await ctx.reply("im hosted")
	await bot.start(
	    "Mzk2Mjc3ODYyNDU5NzY4ODQz.WkY0hA._ciCProJHnul_CTceHrwPrN_3t4")


@bot.command(hidden=True)
async def xmf(ctx):
	await ctx.reply(
	    "https://cdn.discordapp.com/attachments/769776058362101780/798106173240246322/PicsArt_01-11-01.53.05.jpg"
	)


@bot.command()
@commands.is_owner()
async def rekt(ctx, user: discord.User):

	if user.id == 304911836460089345:
		await ctx.send("you cant spam my master, sorry")

	else:

		await ctx.send("Wait for it....")
		await asyncio.sleep(0.7)
		for _ in range(6):
			await ctx.send(user.mention)
			await asyncio.sleep(0.1)
		else:
			await ctx.send("<:shutup:801471938362212373>")


@bot.command(hidden=True)
async def spam(ctx, member: discord.Member):
	msg = await ctx.send("Wait for it")
	await asyncio.sleep(1)
	await msg.edit(content="<:shutup:801471938362212373>")



@bot.command(hidden=True)
async def short(ctx):
	await ctx.send("http://checkshorturl.com/expand.php")


@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def roley(ctx, role: discord.Role):

	perms = ctx.channel.overwrites_for(role)
	await ctx.channel.set_permissions(role,
	                                  read_messages=True,
	  )
	embed = discord.Embed(
	    title="Perms",
	    description=
	    f"{role.mention} can now read messages but can't send messages",
	    color=ctx.author.color)
	await ctx.reply(embed=embed)

    
@bot.command(hidden=True)
@commands.has_role('• Server Managers')
async def rolen(ctx, role: discord.Role):
	perms = ctx.channel.overwrites_for(role)
	await ctx.channel.set_permissions(role, read_messages=False)
	embed = discord.Embed(
	    title="Perms",
	    description=f"{role.mention} cant read the channel anymore",
	    color=ctx.author.color)
	await ctx.reply(embed=embed)


@bot.command(hidden=True)
async def members(ctx):

	await ctx.send("||ye stfu||")


@bot.command(case_insensitive=True, aliases=["r"])
async def remindme(ctx, time, *, reminder):

    print(time)
    print(reminder)
    await ctx.message.add_reaction("🔔")
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())

    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning',value='Please specify what do you want me to remind you about')  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',value='Please specify a proper duration')
    elif seconds < 1:
        embed.add_field(name='Warning',value='You have specified a too short duration!\nMinimum duration is 1 second')
    elif seconds > 7776000:
        embed.add_field(name='Warning',value='You have specified a too long duration!\nMaximum duration is 90 days')
    else:
        await ctx.reply(f"Alright, I will remind you about **__{reminder}__** in {counter}")
        await asyncio.sleep(seconds)
        embed2=discord.Embed(title=f"Reminder", description=f"**```{reminder}```**", color=0x5865f2)
        await user.send(embed=embed2)
		#await user.send(f"Reminder!{lo}**{reminder}**")


@bot.command()
async def password(ctx):
	await ctx.send("Enter Password")
	lmao = await ctx.send("guess the password and you get admin :) no scam")
	msg = await bot.wait_for(
	    'message', check=lambda message: message.author == ctx.author)
	if msg.content == "jasoncansmd":
		await lmao.delete()
		await ctx.send("correct lmfaoo")
	else:
		await ctx.send("wrong smh")


def convert(time):
	pos = ["s", "m", "h", "d"]

	time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

	unit = time[-1]

	if unit not in pos:
		return -1
	try:
		val = int(time[:-1])
	except:
		return -2

	return val * time_dict[unit]


@bot.command()
async def ughgiveaway(ctx):
	await ctx.send(
	    "Let's start with this giveaway! Answer these questions within 15 seconds!"
	)

	questions = [
	    "Which channel should it be hosted in?",
	    "What should be the duration of the giveaway? (s|m|h|d)",
	    "What is the prize of the giveaway?"
	]

	answers = []

	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel

	for i in questions:
		await ctx.send(i)

		try:
			msg = await bot.wait_for('message', timeout=15.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send(
			    'You didn\'t answer in time, please be quicker next time!')
			return
		else:
			answers.append(msg.content)

	try:
		c_id = int(answers[0][2:-1])
	except:
		await ctx.send(
		    f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time."
		)
		return

	channel = bot.get_channel(c_id)

	time = convert(answers[1])
	if time == -1:
		await ctx.send(
		    f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
		return
	elif time == -2:
		await ctx.send(
		    f"The time just be an integer. Please enter an integer next time.")
		return

	prize = answers[2]

	await ctx.send(
	    f"The giveaway will be in {channel.mention} and will last {answers[1]} seconds!"
	)

	embed = discord.Embed(title="Giveaway!",
	                      description=f"🎁 **__{prize}__**",
	                      color=random.randrange(0x1000000))

	embed.add_field(name="Hosted by:", value=ctx.author.mention)

	embed.set_footer(text=f"Ends {answers[1]} from now!")

	my_msg = await channel.send(embed=embed)

	await my_msg.add_reaction("<a:tadafgw:800412709316722698>")

	await asyncio.sleep(time)

	new_msg = await channel.fetch_message(my_msg.id)

	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(bot.user))

	winner = random.choice(users)

	await channel.send(
	    f"Congratulations!\n __{winner.mention}__ won the prize: **`{prize}`**!")
	await my_msg.edit(content="Giveaway ended!")

@bot.command()
async def ughreroll(ctx, channel : discord.TextChannel, id : int):
    try:
        new_msg = await channel.fetch_message(id)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")    

@bot.command(aliases=["wifa", "w"])
async def wai(ctx):
  r = requests.get("https://memes.blademaker.tv/api/awwnime")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)

@bot.command()
async def sfw(ctx):
    await ctx.trigger_typing()
    async with aiohttp.ClientSession() as cs:
	    async with cs.get("https://api.waifu.pics/sfw/waifu") as r:
		    res = await r.json()
		    wai=res["url"]
		    em = discord.Embed(title="SFW waifu",color=discord.Color.random())
		    em.set_image(url=res["url"])
		    await ctx.reply(embed=em)

@bot.command()
async def nsfw(ctx):
	async with aiohttp.ClientSession() as cs:
		async with cs.get("https://api.waifu.pics/nsfw/waifu") as r:
			res = await r.json()
			wai=res["url"]
			em = discord.Embed(title="NSFW waifu",color=discord.Color.random())
			em.set_image(url=res["url"])
			if ctx.channel.is_nsfw():
			  await ctx.reply(embed=em)

@bot.command(aliases=["ll"])
@commands.is_owner()
async def lexiluna(ctx):
  r = requests.get("https://memes.blademaker.tv/api/lexiluna")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)


@bot.command()
async def newmeme(ctx):
  r = requests.get("https://memes.blademaker.tv/api?lang=en")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)


@bot.command(aliases=["bz"])
@commands.is_owner()
async def brazz(ctx):
  r = requests.get("https://memes.blademaker.tv/api/BrazzersTube")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)

@bot.command(aliases=["cg"])
@commands.is_owner()
async def cowgirl(ctx):
  r = requests.get("https://memes.blademaker.tv/api/Cowgirl_Riding_Babes")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)

@bot.command()
@commands.is_owner()
async def ns(ctx):
  r = requests.get("https://memes.blademaker.tv/api/NicoletteShea")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  await ctx.reply(embed=embed)


@bot.command()
async def hentai(ctx):
  r = requests.get("https://memes.blademaker.tv/api/waifusgonewild")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  if ctx.channel.is_nsfw():
    await ctx.reply(embed=embed)
  else:
  	await ctx.reply("this channel aint a nsfw one faggot")
	

@bot.command(aliases=["genshin"])
async def gen(ctx):
  r = requests.get("https://memes.blademaker.tv/api/GenshinImpactNSFW")
  res = r.json()
  title = res["title"]
  ups = res["ups"]
  downs = res["downs"]
  embed = discord.Embed(title=f"{title}", color=ctx.author.color)
  embed.set_image(url=res["image"])
  embed.set_footer(text=f"👍: {ups} 👎: {downs}")
  if ctx.channel.is_nsfw():
    await ctx.reply(embed=embed)
  else:
  	await ctx.reply("this channel aint a nsfw one faggot")



@bot.command()
async def sta(ctx, member: discord.Member):
	await ctx.send(str(member.status))


@bot.command(aliases=["bal", "g"])
async def balance(ctx, *, member: discord.Member = None):

	if member == None:
		await open_account(ctx.author)
		user = ctx.author
		users = await get_bank_data()

		wallet_amt = users[str(user.id)]["wallet"]
		bank_amt = users[str(user.id)]["bank"]

		embed = discord.Embed(title=f"{ctx.author}'s balance:",
		                      color=ctx.author.color)
		embed.add_field(name="__Wallet:__", value=f"> **`{wallet_amt}`** 💰")
		embed.add_field(name="__Bank:__",
		                value=f"> **`{bank_amt}`** 💸",
		                inline=True)
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(icon_url=f"{ctx.guild.icon.url}",
		                 text=f"{ctx.author.id}")
		await ctx.reply(embed=embed)
	else:
		await open_account(member)
		user = member
		users = await get_bank_data()

		wallet_mon = users[str(user.id)]["wallet"]
		bank_mon = users[str(user.id)]["bank"]

		emb0 = discord.Embed(title=f"{member}'s balance:",
		                     color=ctx.author.color)
		emb0.add_field(name="__Wallet:__", value=f"> **`{wallet_mon}`** 💰")
		emb0.add_field(name="__Bank:__",
		               value=f"> **`{bank_mon}`** 💸",
		               inline=True)
		emb0.set_thumbnail(url=member.avatar.url)
		emb0.set_footer(icon_url=f"{ctx.guild.icon.url}", text=f"{member.id}")
		await ctx.reply(embed=emb0)


async def open_account(user):
	users = await get_bank_data()

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0

	with open("bank2.json", "w") as f:
		json.dump(users, f)
	return True


async def get_bank_data():
	with open("bank2.json", "r") as f:
		users = json.load(f)
	return users


@bot.command()
async def beg(ctx):
	await ctx.reply(f"{ctx.author.mention} its called `-work` now")


@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(ctx):
	await open_account(ctx.author)

	users = await get_bank_data()
	user = ctx.author
	earnings = random2.randrange(500, 2000)

	embed = discord.Embed(
	    description=
	    f"**{user.mention}, You worked and got `{earnings}` coins 💰**",
	    color=0xF9FF00)

	await ctx.reply(embed=embed)

	users[str(user.id)]["wallet"] += earnings

	with open("bank2.json", "w") as f:
		json.dump(users, f)


@work.error
async def beg_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'This command is on cooldown, please try again in {:.2f}s'.format(
		    error.retry_after)
		await ctx.reply(msg)


@bot.command(aliases=["with"])
async def withdraw(ctx, amount=None):
	await open_account(ctx.author)

	if amount == None:
		await ctx.reply("**Please enter the amount**")
		return

	bal = await update_bank(ctx.author)
	if amount == "all":
		amount = bal[1]

	amount = int(amount)
	if amount > bal[1]:
		await ctx.reply("**You dont have that much coins in your bank**")
		return

	if amount < 0:
		await ctx.reply("**Amount must be positive**")
		return

	await update_bank(ctx.author, amount)
	await update_bank(ctx.author, -1 * amount, "bank")

	embed = discord.Embed(
	    description=
	    f"**{ctx.author.mention}, You withdrew `{amount}` coins 💰**",
	    color=0xc1f6bd,
	    timestamp=ctx.message.created_at)
	await ctx.reply(embed=embed)


@bot.command(aliases=["dep"])
async def deposit(ctx, amount=None):
	await open_account(ctx.author)

	if amount == None:
		await ctx.reply("**Please enter the amount**")
		return

	bal = await update_bank(ctx.author)
	if amount == "all":
		amount = bal[0]

	amount = int(amount)
	if amount > bal[0]:
		await ctx.reply("**You dont have that much coins**")
		return

	if amount < 0:
		await ctx.reply("**Amount must be positive**")
		return
	await update_bank(ctx.author, -1 * amount)
	await update_bank(ctx.author, amount, "bank")

	embed = discord.Embed(
	    description=
	    f"**{ctx.author.mention}, You deposited `{amount}` coins 💸**",
	    color=0x00ffdb,
	    timestamp=ctx.message.created_at)
	await ctx.reply(embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bet(ctx, amount, *, ht: str):
	await open_account(ctx.author)
	amount = int(amount)
	if amount == None:
		await ctx.reply("**Please enter the amount**")
		return
	if amount > 100000:
		await ctx.reply("You can't bet that much stfu")
		return

	bets = ['h', 't']
	if ht not in bets:
		await ctx.reply("only say 'h' or 't")
		return

	bal = await update_bank(ctx.author)

	amount = int(amount)
	if amount > bal[1]:
		await ctx.reply("**You dont have that much coins**")
		return

	if amount < 0:
		await ctx.reply("**Amount must be positive**")
		return
	cool = [
	    "h",
	    "t",
	]
	okok = random2.choice(cool)

	if ht == okok:
		ok = int(2 * amount)
		await update_bank(ctx.author, -1 * amount, "bank")
		embed = discord.Embed(
		    title="You won!",
		    description=f"**{ctx.author.mention}, You've got `{ok}` coins 💸**",
		    color=0x04f751)
		await ctx.reply(embed=embed)
		await update_bank(ctx.author, 2 * amount, "bank")
	else:

		emo = discord.Embed(
		    title="You lost",
		    description=
		    f"**{ctx.author.mention}, You lost `{amount}` coins :/**",
		    color=0xf2120c)
		await ctx.reply(embed=emo)
		await update_bank(ctx.author, -1 * amount, "bank")


@bet.error
async def bet_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'This command is on cooldown, please try again in {:.2f}s'.format(
		    error.retry_after)
		await ctx.reply(msg)


@bot.command()
async def send(ctx, member: discord.Member, amount=None):
	await open_account(ctx.author)
	await open_account(member)
	if member == ctx.author:
		await ctx.reply("why would i do that?")
		return
	if amount == None:
		await ctx.reply("**Please enter the amount**")
		return

	bal = await update_bank(ctx.author)

	amount = int(amount)
	if amount > bal[1]:
		await ctx.reply("**You dont have that much coins in your bank**")
		return

	if amount < 0:
		await ctx.reply("**Amount must be positive**")
		return

	await update_bank(ctx.author, -1 * amount, "bank")
	await update_bank(member, amount, "bank")

	embed = discord.Embed(
	    title="Money transfer",
	    description=
	    f"**{ctx.author.mention}, You gave {member} - `{amount}` coins 💰**",
	    color=0x00ffd2,
	    timestamp=ctx.message.created_at)
	await ctx.reply(embed=embed)


@bot.command(aliases=["steal"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def rob(ctx, member: discord.Member):
	await open_account(ctx.author)
	await open_account(member)
	if member.id == 423851999038144514:
	  await ctx.reply("cunt")
	  return
	if member == ctx.author:
		await ctx.reply(f"{ctx.author.mention} imagine robbing your own ass")
		return
 
	bal = await update_bank(member)

	if bal[0] < 1:
		await ctx.reply("It's not worth it!")
		return

	earnings = random.randrange(0, bal[0])

	await update_bank(ctx.author, earnings)
	await update_bank(member, -1 * earnings)

	embed = discord.Embed(
	    description=
	    f"{ctx.author.mention}, **You robbed and got `{earnings}` coins!** 💰",
	    color=0xffffff)
	await ctx.reply(embed=embed)


@rob.error
async def rob_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    
    cd = round(error.retry_after)
    #minutes = str(cd // 60)
    seconds = str(cd % 60)

    embed = discord.Embed(title="You're on a cooldown!", description=f"**Slow down will ya?\nWait for `{(seconds)}` secs more**", color=ctx.author.color)
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 65, commands.BucketType.user)
async def yourass(ctx):
  await ctx.send("no urs")
  
@yourass.error
async def yourass_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="You're on a cooldown!", color=ctx.author.color)

    cd = round(error.retry_after)
    minutes = str(cd // 60)
    seconds = str(cd % 60)

    embed.add_field(name="\u200b", value=f"**Slow down will ya?\nWait for `{(minutes)}:{(seconds)} min`**")
    await ctx.send(embed=embed)
  

@bot.command(aliases=["market"])
async def shop(ctx):
	await open_account(ctx.author)
	em = discord.Embed(title="💵 Shop 💴", color=ctx.author.color)

	for item in shopa:
		name = item["name"]
		price = item["price"]
		desc = item["description"]
		em.add_field(name=name, value=f"> **`{price}` coins | {desc}**")

	await ctx.reply(embed=em)


@bot.command()
async def buy(ctx, item, amount=1):
	await open_account(ctx.author)
	res = await buy_this(ctx.author, item, amount)
  
	if not res[0]:
		if res[1] == 1:
			await ctx.reply(
			    "That item isn't there! (remember its case sensitive name)")
			return
		if res[1] == 2:
			await ctx.reply(
			    f"You don't have enough money in your wallet to buy {amount} - {item}"
			)
			return

		with open('bank2.json', 'w') as f:
			json.dump(users, f)

	embed = discord.Embed(
	    description=
	    f"{ctx.author.mention}, **You just bought {amount} - {item}**",
	    color=0xECB0FB)
	await ctx.reply(embed=embed)


async def buy_this(user, item_name, amount):

	item_name = item_name
	name_ = None

	for item in shopa:
		name = item["name"]
		if name == item_name:
			name_ = name
			price = item["price"]
			break

	if name_ == None:
		return [False, 1]

	cost = price * amount

	users = await get_bank_data()

	bal = await update_bank(user)

	if int(bal[0]) < (cost):
		return [False, 2]

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]["bag"]:
			n = thing["item"]
			if n == item_name:
				old_amt = thing["amount"]
				new_amt = old_amt + amount
				users[str(user.id)]["bag"][index]["amount"] = new_amt
				t = 1
				break
			index += 1
		if t == None:
			obj = {"item": item_name, "amount": amount}
			users[str(user.id)]["bag"].append(obj)
	except:
		obj = {"item": item_name, "amount": amount}
		users[str(user.id)]["bag"] = [obj]

	with open("bank2.json", "w") as f:
		json.dump(users, f)

	await update_bank(user, cost * -1, "wallet")

	return [True, "Worked"]


@bot.command()
async def sell(ctx, item, amount=1):
	await open_account(ctx.author)
  
	res = await sell_this(ctx.author, item, amount)

	if not res[0]:
		if res[1] == 1:
			await ctx.reply("That Item isn't there!")
			return
		if res[1] == 2:
			await ctx.reply(f"You don't have {amount} {item} in your bag.")
			return
		if res[1] == 3:
			await ctx.reply(f"You don't have {item} in your bag.")
			return

	embed = discord.Embed(
	    description=
	    f"{ctx.author.mention}, **You just sold {amount} - {item}**",
	    color=0xFFBA00)
	await ctx.reply(embed=embed)


async def sell_this(user, item_name, amount, price=None):
	item_name = item_name
	name_ = None
	for item in shopa:
		name = item["name"]
		if name == item_name:
			name_ = name
			if price == None:
				price = item["price"]
			break

	if name_ == None:
		return [False, 1]

	cost = price * amount

	users = await get_bank_data()

	bal = await update_bank(user)

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]["bag"]:
			n = thing["item"]
			if n == item_name:
				old_amt = thing["amount"]
				new_amt = old_amt - amount
				if new_amt < 0:
					return [False, 2]
				users[str(user.id)]["bag"][index]["amount"] = new_amt
				t = 1
				break
			index += 1
		if t == None:
			return [False, 3]
	except:
		return [False, 3]

	with open("bank2.json", "w") as f:
		json.dump(users, f)

	await update_bank(user, cost, "wallet")

	return [True, "Worked"]


@bot.command()
@commands.is_owner()
async def aahh(ctx):
	for i in range(0, 5):
		await ctx.send('guess')
		response = await bot.wait_for('message')
		if response.content == "0":
			await ctx.send("✓")
			return


@bot.command()
async def bag(ctx, member: discord.Member = None):
	if member == None:
		await open_account(ctx.author)
		user = ctx.author
		users = await get_bank_data()

		try:
			bag = users[str(user.id)]["bag"]
		except:
			bag = []

		em = discord.Embed(title="Bag 🎒", color=ctx.author.color)
		for item in bag:
			name = item["item"]
			amount = item["amount"]
			
			if amount!=0:
			  em.add_field(name=f"**__{name}__**", value=f"> **`{amount}`**")
			  
			  

		await ctx.reply(embed=em)
	else:
		await open_account(member)
		user = member
		users = await get_bank_data()

		try:
			bag = users[str(user.id)]["bag"]
		except:
			bag = []

		em9 = discord.Embed(
		    title="Bag 🎒",
		    color=ctx.author.color)
		for item in bag:
			name = item["item"]
			amount = item["amount"]

			em9.add_field(name=f"**__{name}__**", value=f"> **`{amount}`**")
		await ctx.reply(embed=em9)




@bot.command()
@commands.is_owner()
async def dropp(ctx, ken, *, mon):

	await ctx.message.delete()

	await ctx.channel.send(
	    f"Say **||__{mon}__||** to add `{ken}` 💰 to your wallet")

	for i in range(1, 10):

		msg = await bot.wait_for('message')
		if msg.content == mon:
			await open_account(msg.author)
			embed = discord.Embed(
			    title=
			    f"**{msg.author.name} - `{ken}` 💰 has been added to your __Wallet__**",
			    color=0x3498db)
			await ctx.send(embed=embed)
			amount = int(ken)

			await update_bank(msg.author, 1 * amount, "wallet")
			return

#@bot.command()
#@commands.cooldown(1, 86400, commands.BucketType.user)
#async def ughdaily(ctx):
   # with open("bank2.json", "r") as f:
        #data = json.load(f)
   # streak = data[f"{ctx.author.id}"]["streak"]
   # last_claim_stamp = data[f"{ctx.author.id}"]["last_claim"]
   # last_claim = datetime.fromtimestamp(float(last_claim_stamp)
    #now = datetime.datetime.now()
    #delta = now - last_claim
   # if delta > timedelta(hours=48):
        #print("reset streak")
       # streak = 1
 #   else:
        #print("increase streak")
      #  streak += 1
   # daily = 45 + (streak * 5)
   # amount_after = data[f"{ctx.author.id}"]["balance"] + daily
    #data[f"{ctx.author.id}"]["streak"] = streak
    #data[f"{ctx.author.id}"]["balance"] += daily
    #data[f"{ctx.author.id}"]["last_claim"] = str(now.timestamp())
   # with open("bank2.json", "w") as f:
       #json.dump(data, f, indent=2)
    #embed = discord.Embed(title="Daily", colour=random.randint(0, 0xffffff), description=f"You've claimed your daily of **{daily}**, now you have **{amount_after}**")
    #embed.set_footer(text=f"Your daily streak: {streak}")
    #await ctx.reply(embed=embed)

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx, member: discord.Member = None):

	if member == None:
		embed = discord.Embed(
		    title="Your Daily Coins!",
		    description=
		    f"**{ctx.author.mention}, You got `2500` coins in your bank**",
		    color=0xFCCAA1)
		await ctx.reply(embed=embed)
		amount = 2500
		await update_bank(ctx.author, 1 * amount, "bank")

	if member == ctx.author:
		await ctx.reply(f"{ctx.author.mention} i aint that dumb")
		return

	else:
		embed1 = discord.Embed(
		    title=f"{member}'s Daily Coins!",
		    description=
		    f"**{ctx.author.mention}, you gave {member.name} your daily `2500` coins**",
		    color=0xEE831B)
		await ctx.reply(embed=embed1)
		amount = 2500
		await update_bank(member, 1 * amount, "bank")


@daily.error
async def daily_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'This command is on cooldown, please try again in {:.2f}s'.format(
		    error.retry_after)
		await ctx.reply(msg)


@bot.command(aliases = ["lb"])
async def leaderboard(ctx, number = 1):
  users = await get_bank_data()
  leader_board = {}
  total = []
  for user in users:
    name=int(user)
    total_amount = users[user]["bank"] + users[user]["wallet"]
    
    leader_board[total_amount] = name
    total.append(total_amount)

  total = sorted(total,reverse=True)    

  em = discord.Embed(title = f"Top {number} Richest People", color = 0x7289da)
  em.set_thumbnail(url=f"{ctx.guild.icon.url}")
  index = 1
  for amt in total:
    if amt > 1:
      id_ = leader_board[amt]
      member = bot.get_user(id_)
      name = member.name
      em.add_field(name=f"{index}. {name} - **`{amt}` coins**", value=f"{member.id}", inline=False)
      if index == number:
        break
      else:
        index += 1

  await ctx.reply(embed = em)


@bot.command(aliases=["cbr"])
async def available(ctx, number=1):
	users = await get_bank_data()
	leader_board = {}
	total = []
	for user in users:
		name = int(user)
		total_amount = users[user]["wallet"]

		leader_board[total_amount] = name
		total.append(total_amount)

	total = sorted(total, reverse=True)

	em = discord.Embed(title=f"Wallet Money", color=0x7289da)
	em.set_thumbnail(url=f"{ctx.guild.icon.url}")
	index = 1
	for amt in total:
		if amt > 1:
			id_ = leader_board[amt]
			member = bot.get_user(id_)
			lol = member.name
			em.add_field(name=f"{index}. {lol} - **`{amt}` coins**",
			             value=f"{member.id}",
			             inline=False)
			if index == number:
				break
			else:
				index += 1

	await ctx.reply(embed=em)


async def open_account(user):

	users = await get_bank_data()

	if str(user.id) in users:
		return False

	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0

	with open("bank2.json", "w") as f:
		json.dump(users, f)
	return False


async def get_bank_data():
	with open("bank2.json", "r") as f:

		users = json.load(f)
		return users


async def update_bank(user, change=0, mode="wallet"):

	users = await get_bank_data()
	users[str(user.id)][mode] += change
	with open("bank2.json", "w") as f:
		json.dump(users, f)

	bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
	return bal

@bot.hybrid_command()
@commands.has_role(823558948980129792)
async def toggle(ctx, *, command):
  command = bot.get_command(command)
  if command is None:
    await ctx.reply("should i disable your life?")
  elif ctx.command == command:
    await ctx.reply("no u cant do it for this command")
  else:
    command.enabled = not command.enabled
    ternary = "enabled" if command.enabled else "disabled"
    await ctx.reply(f"{ctx.author.mention} **ive {ternary} `-{command.qualified_name}` for everyone**")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command(aliases=["math"])
async def calc(ctx, *, stuff):
        try:
            calcul = eval(stuff)
            embed = discord.Embed(title=f"**`{calcul}`**",color=ctx.author.color)
            await ctx.reply(embed=embed)
        except SyntaxError:
            await ctx.send("Sorry, I couldn't calculate that")
        except TypeError:
            await ctx.send("Sorry, I couldn't calculate that")

@bot.command()
async def tttr(ctx):
  embed=discord.Embed(title="Tic-tac-toe", description="**TICTACTOE GAME RULES\n\n__To start the game__ `-ttt @user`\n\n --> ok so basically it picks a random to start the match and to choose a position u do the command `-place <position>` like there's gonna be 9 you know right so `-place 1` like that, youre gonna get alternative chances**", color=ctx.author.color, timestamp=ctx.message.created_at)
  embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/794075957463351296/836519466397466644/unknown.png")
  await ctx.reply(embed=embed)

@bot.command(aliases=["ttt"])
async def tictactoe(ctx, member: discord.Member):
  if member==ctx.author:
    await ctx.reply("cunt")
    return
  else:
    global count
    global player1
    global player2
    global turn
    global gameOver
    pog=await ctx.send(f"**{member.mention}, `{ctx.author.name}` is ready whenever youre!**")
    await pog.add_reaction("✅")
    def check(reaction, user):
      return user==member and str(reaction.emoji)=="✅"
    await bot.wait_for('reaction_add', check=check)
    await pog.edit(content="challenge accepted")
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = ctx.author
        player2 = member

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send(f"It is {ctx.author.mention}'s turn")
        elif num == 2:
            turn = player2
            await ctx.send(f"It is {p2.mention}'s turn")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")



@bot.command(aliases=["pos"])
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.reply(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.reply("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.reply("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.reply("It is not your turn.")
    else:
        await ctx.reply("Please start a new game using the `-tictactoe` command")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@bot.command()
async def end(ctx):
  global count
  global player1
  global player2
  global turn
  global gameOver
       
  count = 0
  player1 = ""
  player2 = ""
  turn = ""
  gameOver=True
  if gameOver:
    myEmbed = discord.Embed(title= "All Games Ended!",description="**Start a new game using\n`-tictactoe` command**",color=0x2ecc71)
    await ctx.reply(embed=myEmbed)
    return

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.reply("Please make sure to enter an integer.")

snipe_message_author = {}
snipe_message_content = {}
snipe_message_avatar={}

@bot.listen('on_message_delete')
async def ye(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     snipe_message_avatar[message.channel.id] = message.author.avatar.url
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
     del snipe_message_avatar[message.channel.id]
     
@bot.command(name ='snipe')
async def snipe(ctx):
  channel = ctx.channel
  try:
    em=discord.Embed(description=snipe_message_content[channel.id], color=ctx.author.color, timestamp=ctx.message.created_at)
    em.set_author(name = f"{snipe_message_author[channel.id]}", icon_url=f"{snipe_message_avatar[channel.id]}")
    await ctx.reply(embed = em)
  except:
    await ctx.reply(f"there are no recently deleted messages in {channel.mention}")

@bot.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))
    bot.version = '1.7.2'
    embed = discord.Embed(title=f'{bot.user.name} Stats', color=ctx.author.color, timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value="Suprememeememe")
    embed.add_field(name='Node Version:', value=pythonVersion)
    embed.add_field(name='Node.js Version', value=dpyVersion)
    embed.add_field(name='Total Guilds:', value=serverCount)
    embed.add_field(name='Total Users:', value=memberCount)
    embed.add_field(name='Bot Developers:', value="YourMom#6969")

    embed.set_footer(text=f"{bot.user.name} | Credits: Dexter#4638")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    
    print(bot.user.name + " is ready.")


@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}

@bot.hybrid_command()
#@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    #if member is None:
       # return await ctx.reply("**`Member not found or u forgot to mention the member!`**")
    if member==ctx.author:
        return await ctx.reply("**shut up, i cant do that**")
    if reason is None:
        return await ctx.reply("Please provide a reason for warning this user.")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    embed=discord.Embed(title=f"Warned {member.name} for __{reason}__", color=discord.Color.blurple())
    embed.set_footer(text=f"{count} {'warning' if first_warning else 'warnings'}")
    await ctx.reply(embed=embed)

@bot.hybrid_command(aliases=["warns"])
#@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member==None:
        member=ctx.author
    embed = discord.Embed(description="", color=discord.Color.blurple())
    embed.set_author(name=f"{member.name}'s Warnings!",icon_url=member.avatar.url)
    embed.set_footer(text=ctx.guild.name)
    try:
        
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** by {admin.mention}/{admin.name}\n- {reason}\n"
            i += 1
     
        await ctx.reply(embed=embed)

    except KeyError: # no warnings
        await ctx.reply(f"**{member.name} was never warned!**")    


    
    
@bot.command()
async def atrivia(ctx, difficulty: str = None):
        """Test out your knowledge with trivia questions from nizcomix#7532"""
        difficulty = difficulty or random.choice(['easy', 'medium', 'hard'])
        try:
            question = await trivia.get_random_question(difficulty)
        except AiotriviaException:
            return await ctx.send(embed=discord.Embed(title='That is not a valid sort.',
                                                      description='Valid sorts are ``easy``, ``medium``, and ``hard``.',
                                                      color=0xFF0000))
        answers = question.responses
        d = difficulty.capitalize()
        random.shuffle(answers)
        final_answers = '\n'.join([f"{index}. {value}" for index, value in enumerate(answers, 1)])
        await ctx.send(embed=discord.Embed(
            title=f"{question.question}", description=f"\n{final_answers}\n\nQuestion about: **{question.category}"
                                                      f"**\nDifficulty: **{d}**",
            color=0x5643fd))
        answer = answers.index(question.answer) + 1
        try:
            while True:
                msg = await bot.wait_for('message', timeout=15, check=lambda m: m.author == ctx.message.author)
                if str(answer) in msg.content:
                    return await ctx.send(embed=discord.Embed(description=f"{answer} was correct ({question.answer})",
                                                              color=0x32CD32, title='Correct!'))
                if str(answer) not in msg.content:
                    return await ctx.send(embed=discord.Embed(description=f"Unfortunately **{msg.content}** was wrong. "
                                                                          f"The "
                                                                          f"correct answer was ``{question.answer}``.",
                                                              title='Incorrect', color=0xFF0000))
        except asyncio.TimeoutError:
            embed = discord.Embed(title='Time expired', color=0xFF0000,
                                  description=f"The correct answer was {question.answer}")
            await ctx.send(embed=embed)

@bot.command(aliases=["itt"])
@commands.is_owner()
async def itsthattime(ctx):
    ok = ["https://cdn.discordapp.com/attachments/532628715939561472/841322776375722004/20210510_163428.jpg", "https://media.discordapp.net/attachments/778985811189825589/874199215134343188/Screenshot_20210809-132516.jpg", "https://media.discordapp.net/attachments/778985811189825589/874515626331361362/unknown.gif", "https://media.discordapp.net/attachments/778985811189825589/876819288701407302/2641377267682380898_510093911_1629096727.jpg", "https://media.discordapp.net/attachments/778985811189825589/885951014753140746/CTm4F0ZIGJICBe2bcYLG0352ROAj0Axs3-F7JM0.jpg", "https://media.discordapp.net/attachments/778985811189825589/886651136130576384/Screenshot_20210912-220213.jpg", "https://media.discordapp.net/attachments/769785356320899132/877548556054048819/image0.jpg", "https://media.discordapp.net/attachments/769785356320899132/861109318270451782/SPOILER_jo_2.png", "https://media.discordapp.net/attachments/778985811189825589/996787546812063935/Picsart_22-07-13_20-07-13-054.jpg", "https://i.imgur.com/kM47YBh.jpg", "https://i.redd.it/7zf7nvqj3pb91.jpg", "https://i.redd.it/l291ppab9ia91.jpg", "https://v.redd.it/vztv16targs71/DASH_720.mp4?source=fallback", "https://media.discordapp.net/attachments/778985811189825589/929054125864419428/iamaishwaryaraju_1641574143227.jpg"]
    yk = random2.choice(ok)
    await ctx.reply(yk)
            
@bot.command(aliases=['gw', 'gstart'])
@commands.has_permissions(manage_guild=True)
async def giveaway(ctx):
    await ctx.send("Select the channel, you would like the giveaway to be in.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg1 = await bot.wait_for('message', check=check, timeout=30.0)

        channel_converter = discord.ext.commands.TextChannelConverter()
        try:
            giveawaychannel = await channel_converter.convert(ctx, msg1.content)
        except commands.BadArgument:
            return await ctx.send("This channel doesn't exist, please try again.")

    except asyncio.TimeoutError:
        await ctx.send("You took to long, please try again!")

    if not giveawaychannel.permissions_for(ctx.guild.me).send_messages or not giveawaychannel.permissions_for(
            ctx.guild.me).add_reactions:
        return await ctx.send(
            f"Bot does not have correct permissions to send in: {giveawaychannel}\n **Permissions needed:** ``Add reactions | Send messages.``")

    await ctx.send("How many winners to the giveaway would you like?")
    try:
        msg2 = await bot.wait_for('message', check=check, timeout=30.0)
        try:
            winerscount = int(msg2.content)
        except ValueError:
            return await ctx.send("You didn't specify a number of winners, please try again.")

    except asyncio.TimeoutError:
        await ctx.send("You took to long, please try again!")

    await ctx.send("Select an amount of time for the giveaway.")
    try:
        since = await bot.wait_for('message', check=check, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send("You took to long, please try again!")

    seconds = ("s", "sec", "secs", 'second', "seconds")
    minutes = ("m", "min", "mins", "minute", "minutes")
    hours = ("h", "hour", "hours")
    days = ("d", "day", "days")
    weeks = ("w", "week", "weeks")
    rawsince = since.content

    try:
        temp = re.compile("([0-9]+)([a-zA-Z]+)")
        if not temp.match(since.content):
            return await ctx.send("You did not specify a unit of time, please try again.")
        res = temp.match(since.content).groups()
        time = int(res[0])
        since = res[1]

    except ValueError:
        return await ctx.send("You did not specify a unit of time, please try again.")

    if since.lower() in seconds:
        timewait = time
    elif since.lower() in minutes:
        timewait = time * 60
    elif since.lower() in hours:
        timewait = time * 3600
    elif since.lower() in days:
        timewait = time * 86400
    elif since.lower() in weeks:
        timewait = time * 604800
    else:

        return await ctx.send("You did not specify a unit of time, please try again.")

    await ctx.send("What would you like the prize to be?")
    try:
        msg4 = await bot.wait_for('message', check=check, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send("You took to long, please try again.")

    logembed = discord.Embed(title="Giveaway Logged",
                             description=f"**Prize:** ``{msg4.content}``\n**Winners:** ``{winerscount}``\n**Channel:** {giveawaychannel.mention}\n**Host:** {ctx.author.mention}",
                             color=discord.Color.red())
    logembed.set_thumbnail(url=ctx.author.avatar.url)

    logchannel = ctx.guild.get_channel(794075957463351296)  # Put your channel, you would like to send giveaway logs to.
    await logchannel.send(content=f"<@304911836460089345>",embed=logembed)
    lm = ["<a:tadafgw:800412709316722698>", "<a:tada2:855440983608131655>", "<a:tada1:855440920102961152>"]
    ao=random2.choice(lm)
    futuredate = datetime.datetime.utcnow() + datetime.timedelta(seconds=timewait)
    embed1 = discord.Embed(color=discord.Color.random(),
                           title=f"🎁 **__{msg4.content}__**", timestamp=futuredate,
                           description=f'**React with {ao} to enter!\nHost: {ctx.author.mention}\nWinners: {winerscount}**')

    embed1.set_footer(text=f"Giveaway will end")
    msg = await giveawaychannel.send("**__GIVEAWAY!__**",embed=embed1)
    await msg.add_reaction(ao)
    await asyncio.sleep(timewait)
    message = await giveawaychannel.fetch_message(msg.id)
    for reaction in message.reactions:
        if str(reaction.emoji) == f"{ao}":
            users = [user async for user in reaction.users()]
            if len(users) == 1:
                return await msg.edit(embed=discord.Embed(title="Nobody has won the giveaway."))
    try:
        winners = random2.sample([user for user in users if not user.bot], k=winerscount)
    except:
        return await msg.reply(f"**imagine {winerscount} winners gw without {winerscount} members reactions!**")
    winnerstosend = " ".join([winner.mention for winner in winners])
    embed9=discord.Embed(title=f"🎁 **__{msg4.content}__**", description=f"**Winners: {winnerstosend}**", color=0xFF0000)
    await msg.edit(content="**__Giveaway Ended!__**", embed=embed9)
    win = await msg.reply(f"**{ctx.author.mention} Winners!\n\nCongrats to {winnerstosend} on winning `{msg4.content}`**")

def add_bio(member: discord.Member, text: str):
    if os.path.isfile("file.json"):
        with open("file.json", "r") as fp:
            data = json.load(fp)
        try:
            data[f"{member.id}"]["about"] = text
        except KeyError:
            data[f"{member.id}"] = {"about": "loser"}
    else:
        data = {f"{member.id}": {"about": text}}
    with open("file.json", "w+") as fp:
        json.dump(data, fp, sort_keys=True, indent=4)
        
        
        
def add_score(member: discord.Member, amount: int):
    if os.path.isfile("file.json"):
        with open("file.json", "r") as fp:
            data = json.load(fp)
        try:
            data[f"{member.id}"]["score"] += amount
        except KeyError: # if the user isn't in the file, do the following
            data[f"{member.id}"] = {"score": amount} # add other things you want to store
    else:
        data = {f"{member.id}": {"score": amount}}
    # saving the file outside of the if statements saves us having to write it twice
    with open("file.json", "w+") as fp:
        json.dump(data, fp, sort_keys=True, indent=4) # kwargs for beautification
   # you can also return the new/updated score here if you want

def get_score(member: discord.Member):
    with open("file.json", "r") as fp:
        data = json.load(fp)
    return data[f"{member.id}"]["score"]

def get_bio(member: discord.Member):
    with open("file.json", "r") as fp:
        data = json.load(fp)
    try:
        return data[f"{member.id}"]["about"]
    except:
        add_bio(member, "loser")
        return data[f"{member.id}"]["about"]


@bot.command()
async def addabout(ctx, *,text):
    #await ctx.reply(f"{get_bio(ctx.author)}")
    add_bio(ctx.author, text)
    await ctx.reply("done")


@bot.command()
async def checkscore(ctx, *,member:discord.Member=None):
    if member==None:
        member=ctx.author
    try:
        try:
            embed=discord.Embed(description=f"**__About:__ {get_bio(member)}**",color=0x5865f2)
        except:
            embed=discord.Embed(color=0x5865f2)
        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/794075957463351296/864173777574428702/unknown.png")
        embed.add_field(name="__Score:__", value=f"> **`{get_score(member)}` 💥**")
        embed.set_footer(text="-addabout")
        await ctx.reply(embed=embed)
    except:
        await ctx.reply("that loser still hasnt started")

@bot.command()
async def scorelb(ctx,x = 1):
    with open("file.json", "r") as f:
        data = json.load(f)
    leader_board = {}
    total = []
    for user in data:
        name = int(user)
        total_amount = data[user]["score"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} with high score!",color = 0x21FFD8)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.set_thumbnail(url="https://media.discordapp.net/attachments/794075957463351296/864795344604364840/unknown-3__01.png")
        em.add_field(name=f"**{index}. {name}**", value=f"**`{amt}` score!**")
        if index == x:

            break
        else:
            index += 1

    await ctx.reply(embed = em)


@bot.command(aliases=["ranklb"])
async def levellb(ctx,x = 1):
    with open("users.json", "r") as f:
        users = json.load(f)
    leader_board = {}
    total = []
    server = users[str(ctx.guild.id)]
    #user=discord.Member
    for user in server:
        name = int(user)
        total_amount = server[user]["level"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Level Leaderboard", color = discord.Color.random())
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"**`Level: {amt}`**")
        if index == x:
            break
        else:
            index += 1

    await ctx.reply(embed = em)
    
    
    
@bot.command()
async def ughlb(ctx):

    with open('file.json', 'r') as f:
        data = json.load(f)

    top_users = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

    names = ''
    for postion, user in enumerate(top_users):
        # add 1 to postion to make the index start from 1
        names += f'{postion+1} - {user.mention} with {top_users[user]}\n'

    embed = discord.Embed(title="Leaderboard")
    embed.add_field(name="Names", value=names, inline=False)
    await ctx.send(embed=embed)   
    
    
@bot.command()
#@commands.is_owner()
@commands.cooldown(1, 15, commands.BucketType.user)
async def score(ctx):
    #await ctx.reply("Play the game and get score\n Get started with `-wumpus`!")
   # return
    e=random2.randint(1, 100)
    add_score(ctx.author, e)
    embed=discord.Embed(title=f"**You now have `{get_score(ctx.author)} score!`**", color=0x5865f2)
    embed.set_footer(text=f"{e} new score added!")
    await ctx.reply(embed=embed)

@score.error
async def score_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Hold on, loser!",description=f"**Try again in `{error.retry_after:.2f} secs`**", color=0xFF0000)
            await ctx.reply(embed=em)
    
@bot.command()
@commands.has_permissions(manage_guild=True)
async def newreroll(ctx):
    async for message in ctx.channel.history(limit=100, oldest_first=False):
        if message.author.id == bot.user.id and message.embeds:
            #if message.content.startswith("**Giveaway Ended!**"):
                #await ctx.reply("e lmao")
            reroll = await ctx.fetch_message(message.id)
            users = await reroll.reactions[0].users().flatten()
            users.pop(users.index(bot.user))
            winner = random2.choice(users)
            await reroll.reply(f"The new winner is {winner.mention}")
            break
    else:
        await ctx.send("No giveaways going on in this channel.")        
        
def SearchByID():
    query = '''
    query($id: Int, $type: MediaType) {
        Media(id: $id, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    '''
    return query

def SearchByTitle():
    query = '''
    query($search: String, $type: MediaType) {
        Media(search: $search, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    '''
    return query


def GetByID(type, id):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type' : type,
        'id': id
    }
    return variables

def GetByTitle(type, title):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type' : type,
        'search' : title
    }
    return variables

def run_query(query, variables):
    request = requests.post('https://graphql.anilist.co', json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 404:
        print ("Invalid search.")
        return
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def removeTags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def cutLength(text):
    if len(text) > 900:
        return text[:900] + "..."
    return text


def replaceNone(text):
    if text is None:
        return 'N/A'
    return text        

def mangaSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('manga', title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('manga', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description=f"**There does not exist a manga with a title/ID of __`{title}`__ or api had an error**", color=discord.Color.red())

        embed = discord.Embed(
            color=0x5865f2,
            title=('{} ({}) {}'.format(result["data"]["Media"]["title"]["romaji"],
                                       result["data"]["Media"]["title"]["english"],
                                       result["data"]["Media"]["format"])),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace("&quot;", '"')
        )

        embed.add_field(name="Status", value=result["data"]["Media"]["status"].upper(), inline=True)
        embed.add_field(name="Start Date",
                        value='{}/{}/{}'.format(result["data"]["Media"]["startDate"]["day"],
                                                result["data"]["Media"]["startDate"]["month"],
                                                result["data"]["Media"]["startDate"]["year"]),
                        inline=True)
        embed.add_field(name="Number of Chapters", value=replaceNone(result["data"]["Media"]["chapters"]), inline=True)
        embed.add_field(name="Number of Volumes", value=replaceNone(result["data"]["Media"]["volumes"]), inline=True)
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score",
                        value='{}'.format(replaceNone(result["data"]["Media"]["averageScore"]), inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed

@bot.hybrid_command()
async def manga(ctx, *, title):
    embed = mangaSearch(title)
    await ctx.reply(embed=embed)
    
def reverseSearch(link):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    try:
        title = (tracemoe.search(link, is_url=True))
    except:
        return False

    for key, value in title["docs"][0].items():
        if key == "anilist_id":
            return value

def animeSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('anime', title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('anime', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist an anime with a title/ID of {}.".format(title))

        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title=('{} ({}) {}'.format(result["data"]["Media"]["title"]["romaji"],
                                       result["data"]["Media"]["title"]["english"],
                                       result["data"]["Media"]["format"])),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace("&quot;", '"')
        )
        embed.add_field(name="Status", value=result["data"]["Media"]["status"].upper(), inline=True)
        embed.add_field(name="Season",
                        value='{} {}'.format(result["data"]["Media"]["season"], result["data"]["Media"]["seasonYear"]),
                        inline=True)
        embed.add_field(name="Number of Episodes", value=result["data"]["Media"]["episodes"], inline=True)
        embed.add_field(name="Duration",
                        value='{} minutes/episode'.format(result["data"]["Media"]["duration"], inline=True))
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}%'.format(result["data"]["Media"]["averageScore"], inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed       
        
@bot.command()
async def reverse(ctx, *, link):
    if link.endswith(".jpg") or link.endswith(".png") or link.endswith(".jpeg"):
        await ctx.send(embed=animeSearch(title=str(reverseSearch(link))))
    else:
        await ctx.send(embed=discord.Embed(description="Link is not a .jpg or a .png file.", color=discord.Color.red()))
    
@bot.hybrid_command()
async def newanime(ctx, *, title):
    embed = animeSearch(title)
    await ctx.reply(embed=embed)

    
def searchChar():
    query = '''
    query ($search: String) {
      Character(search: $search) {
        siteUrl
        name {
          full
        }
        media(perPage: 1) {
          nodes {
            title {
                romaji
                english
            }
            siteUrl
          }
        }
        image {
          large
        }
        description(asHtml: true)
      }
    }
    '''
    return query    
    
def GetByChar(charname):
    variables = {
        'search' : charname
    }
    return variables    

def charSearch(charname):
    query = searchChar()
    variables = GetByChar(charname)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist a character with the name {}.".format(charname))

        embed = discord.Embed(
            colour=discord.Colour.dark_orange(),
            title=result["data"]["Character"]["name"]["full"],
            url=result["data"]["Character"]["siteUrl"]
        )

        desc = cutLength(removeTags(result["data"]["Character"]["description"]).replace("&quot;", '"'))
        for title in result["data"]["Character"]["media"]["nodes"]:
            embed.add_field(name="Title of Source", value='[{} ({})]({})'.format(title["title"]["romaji"], title["title"]["english"], title["siteUrl"], inline=False))
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_thumbnail(url=result["data"]["Character"]["image"]["large"])
        return embed
@bot.hybrid_command()
async def newchar(ctx, *, charname):
    embed = charSearch(charname)
    await ctx.reply(embed=embed)

@bot.command()
async def yknow(ctx, *,what):
    await ctx.trigger_typing()
    if what=="nhentai":
        lmao=Utils.get_random_id()
        doujin = Hentai(lmao)
        embed=discord.Embed(title=doujin.title(Format.Pretty), url=doujin.url, description=f"**__{lmao}__**",color=discord.Color.random())
        embed.set_image(url=doujin.thumbnail)
        await ctx.reply(embed=embed)
    if what=="hentai":
        lo=Utils.get_random_hentai()
        await ctx.reply(f"**{lo}**")
    
@bot.command(aliases=["nhentai"])
async def doujin(ctx, id: int=None):
	    if ctx.channel.is_nsfw():
            #if id is None:
                #id=Utils.get_random_id()
		    send = await ctx.reply(f"**😈 Searching for ```{id}```**")
		    if not Hentai.exists(id):
			    await ctx.send("404 not found")
		    else:
			
			    doujin = Hentai(id)
			    language = Tag.get(doujin.language, property_="name")
			    emoji = "🌐"
			    if language == "english, translated":
				    emoji = "English"
			    if language == "japanese, translated":
				    emoji = "Japanese"
			    if language == "chinese, translated":
				    emoji = "Chinese"
			    type_= Tag.get(doujin.category, property_="name")
			    close = []
			    for related in doujin.related:
				    hmm = str(related.id)
				    close.append(related.title(Format.Pretty))
				
			    embed = discord.Embed(title=doujin.title(Format.Pretty),
				 url=doujin.url, color=discord.Color.random())
			    embed.add_field(name="Language", value=f"{emoji} ")

			    embed.add_field(name="Author", value=Tag.get(doujin.artist, property_='name'))
			    embed.add_field(name="Type", value = type_)
			    if doujin.num_favorites == 0:
				    embed.add_field(name="Favorites", value=f"For some reason this is broken :(")
			    else:
				    embed.add_field(name="Favorites", value=f"❤ {(doujin.num_favorites)}")
			    embed.add_field(name="Pages", value=f"📕 {doujin.num_pages}")
			    embed.set_thumbnail(url=doujin.thumbnail)
			    thing= doujin.tag
			    tags = []
			    for tag in thing:
				    x = Tag.get(thing, property_="name")
					

			    embed.add_field(name="Tags",value=f"{x}", inline=False)
			    if close != None:
				    embed.add_field(name="Related",value=f" \n".join(close))
			    embed.description=f"**Click `Read` if you want to read this.**"
			    await send.delete()
			    x = await ctx.send(embed=embed)
			    #await x.add_reaction("<:nhentai:865543197118824508>")

    
@bot.command()
async def emojilist(ctx):
        emojis = sorted([e for e in ctx.guild.emojis if len(
            e.roles) == 0 and e.available], key=lambda e: e.name.lower())
        paginator = commands.Paginator(suffix='', prefix='')
        channel = ctx.channel

        for emoji in emojis:
            paginator.add_line(f'{emoji} ↳ `{emoji}`\n')

        for page in paginator.pages:
            await channel.send(page)

        await ctx.reply(ctx.tick(True))

        
@bot.hybrid_command()
async def movie(ctx, *, title):
		send = await ctx.send(f"**🎬 Searching for `{title}`**")
		embeds = []
		for page in range(1, 2):
			name = title
			url = "https://yts.mx/browse-movies/" + str(
				   name) + "/all/all/0/seeds/0/all"
			r = requests.get(url).text
			soup = BeautifulSoup(r, "lxml")
			for name in soup.findAll(
				   "div",
				   class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"):
				mov_name = name.find("div", class_="browse-movie-bottom")
				movie_name = mov_name.a.text
				movie_year = mov_name.div.text
				movie_name = movie_name + " " + movie_year
				rating = name.find("h4", class_="rating", text=True)
				if rating is not None:
					rating = rating.text
					rating = rating[:3]
				else:
					rating = "0.0"
				if rating[2] == "/":
					rating = rating[0:2]
				try:
					
					if movie_name[0] == "[" and movie_name[3] == "]":
						movie_name = movie_name[5:]
					movie_name = movie_name.replace(" ", "-")
					index = 0
					for char in movie_name:  #Handles Special Character In Url
						if char.isalnum() == False and char != "-":
							movie_name = movie_name.replace(char, "")
					for char in movie_name:
						if char == "-" and movie_name[index + 1] == "-":
							movie_name = movie_name[:index] + movie_name[index + 1:]
						if index < len(movie_name) - 1:
							index = index + 1
					if "--" in movie_name:  #Handles Movie Url Containing "--"
						movie_name = movie_name.replace("--", "-")
					movie_url = "https://yts.mx/movie/" + movie_name
					movie_url = movie_url.lower()
					request = requests.get(movie_url).text
					n_soup = BeautifulSoup(request, "lxml")
					info = n_soup.find("div", class_="bottom-info")
					torrent_info = n_soup.find("p", class_="hidden-xs hidden-sm")
					genre = n_soup.findAll("h2")[1].text
					likes = info.find("span", id="movie-likes").text
					imdb_link = info.find("a", title="IMDb Rating")["href"]
					for torrent in torrent_info.findAll("a"):
						if (torrent.text[:3] == "720"):
							torrent_720 = torrent["href"]
						if torrent.text[:4] == "1080":
							torrent_1080 = torrent["href"]
				except Exception as e:
					likes = None
					genre = None
					num_downloads = None
					imdb_link = None
					torrent_720 = None
					torrent_1080 = None
					pass
				movie_name = mov_name.a.text

				embed = discord.Embed(title=f"{movie_name}", color =discord.Color.random())
				#embed.description=f"{movie_name}"
				embed.add_field(name="Year", value=f"{movie_year}")
				embed.add_field(name="IMDb link", value=f"[Here]({imdb_link})")
				embed.add_field(name="Ratings", value=f"{rating}")
				embed.add_field(name=f"Genres", value=f"{genre}", inline=False)
				embed.add_field(name=f"Download", value=f"[720p]({torrent_720}) | "
														f"[1080p]({torrent_1080})")
				embeds.append(embed)

		paginator = BotEmbedPaginator(ctx, embeds)
		await send.delete()
		await paginator.run()
        
        # if(opponent=="" or opponent.find('help')!=-1):
           # em = discord.Embed()
           # em.title = f'Usage: /chess opponent'
           # em.description = f'Challenges opponent to a game of chess. The Opponent should be @mentoned to start\nOpponent will make the first move, and thus be controlling the white pieces.'
           # em.add_field(name="Example", value="/chess @Username", inline=False)
            #em.color = 0x22BBFF
           # await ctx.send(embed=em)
            #return
        #----------------------------------------------#
        # Remove challenge 
        
                 
                


        # Game variables
        
        #Castling check
        
        
        #Bunch of helper functio
@bot.command()
async def paginate(ctx):
    embed1 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 1")
    embed2 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 2")
    embed3 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 3")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('<:left:866313703832944640>', "back")
    #paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('🔢', "page")
    paginator.add_reaction('<:right:866313744380723221>', "next")
    paginator.add_reaction('⏭️', "last")
    paginator.add_reaction('⏹️', "clear")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)        
        
#tclient = aiopentdb.client()
        
@bot.command()
async def quiz(ctx):
        """Start an interactive quiz game"""
        try:
            lo = aiopentdb.Client()
            async with ctx.typing():
                question = lo.fetch_questions(
                    amount=1
                   # difficulty=aiopentdb.Difficulty.easy
                )
                question = question[0]
                if question.type.value == 'boolean':
                    options = ['True', 'False']
                else:
                    options = [question.correct_answer]
                    options.extend(question.incorrect_answers)
                    options = random2.sample(options, len(options)) # Shuffle
                answer = options.index(question.correct_answer)

                if len(options) == 2 and options[0] == 'True' and options[1] == 'False':
                    reactions = ['✅', '❌']
                else:
                    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']

                description = []
                for x, option in enumerate(options):
                    description += '\n {} {}'.format(reactions[x], option)

                embed = discord.Embed(title=question.content, description=''.join(description), color=0xFF9933)
                embed.set_footer(text='Answer using the reactions below⬇')
                quiz_message = await ctx.send(embed=embed)
                for reaction in reactions:
                    await quiz_message.add_reaction(reaction)

            def check(reaction, user):
                return user != bot.user and user == ctx.author and (str(reaction.emoji) == '1️⃣' or '2️⃣' or '3️⃣' or '4️⃣' or '✅' or '❌')

            try:
                reaction, _ = await bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(f"Time's Up! :stopwatch:\nAnswer is **{options[answer]}**")
            else:
                if str(reaction.emoji) == reactions[answer]:
                    await ctx.send("Correct answer:sparkles:")
                else:
                    await ctx.send(f"Wrong Answer :no_entry_sign:\nAnswer is **{options[answer]}**")
        except Exception as error:
            print(error)
            return await ctx.reply('Failed to start quiz :x:')

async def eplay(ctx):
	# Initialize the map array.

	world = [['  ' for _ in range(10)] for _ in range(7)]

	# Hide the wumpus (w).
	row = random2.randint(1, 5)
	col = random2.randint(1, 8)
	world[row][col] = 'w'

	# Hide the 2 pits (p).
	needit = True
	while needit:
		row = random2.randint(1, 5)
		col = random2.randint(1, 8)
		if world[row][col] == '  ':
			world[row][col] = 'p'
			needit = False
	needit = True
	while needit:
		row = random2.randint(1, 5)
		col = random2.randint(1, 8)
		if world[row][col] == '  ':
			world[row][col] = 'p'
			needit = False

	# Hide the 2 bats (b)
	needit = True
	while needit:
		row = random2.randint(1, 5)
		col = random2.randint(1, 8)
		if world[row][col] == '  ':
			world[row][col] = 'b'
			needit = False
	needit = True
	while needit:
		row = random2.randint(1, 5)
		col = random2.randint(1, 8)
		if world[row][col] == '  ':
			world[row][col] = 'b'
			needit = False
	# Place the user in a safe spot.
	needit = True
	while needit:
		row = random2.randint(1, 5)
		col = random2.randint(1, 8)
		if world[row][col] == '  ':
			userRow = row
			userCol = col
			needit = False

	# Initialize variables
	arrows = 5
	alive = True

	def printBoard(r, c):
		out = []
		w = [['  ' for _ in range(10)] for _ in range(7)]
		w[r][c] = '💂🏻‍♂️'
		for i in w:
			out.append('|'.join(i[1:-1]))
		return '```\n' + '\n--+--+--+--+--+--+--+--\n'.join(out[1:-1]) + '\n```'

	async def endBoard(r, c, sys_msg):
		out = []
		world[r][c] = '💂🏻‍♂️'
		for i in world:
			out.append('|'.join(i[1:-1]))
		await sys_msg.edit(content='```\n' + '\n--+--+--+--+--+--+--+--\n'.join(out[1:-1]).replace('w', '👹').replace('b', '🦇').replace('p', '⚫') + '\n```')
		return await p_msg.delete()

	# brd_msg 
	brd_msg = await ctx.send(printBoard(userRow, userCol))
	sys_msg = await ctx.send(f":bow_and_arrow:  `{arrows}`")
	# obs_msg
	p_msg = await ctx.send(":grinning:  `Loading...`")
	# addreactions
	reactions = ['🔼', '🔽', '<:left:866313703832944640>', '<:right:866313744380723221>', '🏹', '❌']
	# async with ctx.typing():
	for reaction in reactions:
		await p_msg.add_reaction(reaction)
	while alive:
		# Tell user where he is.
		# brd_msg
		await brd_msg.edit(content=printBoard(userRow, userCol))

		# Tells user if he is near the wumpus
		if world[userRow - 1][userCol] == 'w' or world[userRow + 1][userCol] == 'w' or world[userRow][userCol - 1] == 'w' or \
						world[userRow][userCol + 1] == 'w':
			# p_msg
			await p_msg.edit(content=':nauseated_face:  `I smell a Wumpus`')

		# Tells user if he is near a pit
		elif world[userRow - 1][userCol] == 'p' or world[userRow + 1][userCol] == 'p' or world[userRow][userCol - 1] == 'p' or \
						world[userRow][userCol + 1] == 'p':
			# p_msg
			await p_msg.edit(content=':dizzy_face:  `I feel a draft`')

		# Tell the user if he is near a bat
		elif world[userRow - 1][userCol] == 'b' or world[userRow + 1][userCol] == 'b' or world[userRow][userCol - 1] == 'b' or \
						world[userRow][userCol + 1] == 'b':
			# p_msg
			await p_msg.edit(content=':rolling_eyes:  `I hear wings flapping`')
		else:
			await p_msg.edit(content=':grinning:  `Nothing suspicious`')



		# Ask user what to do next (n/s/e/w/f).
		# sys_msg
		# 'What do you want to do next?'
		def check(reaction, user):
			# print(str(reaction.emoji))
			return user != bot.user and (str(reaction.emoji) == '🔼' or '🔽' or '<:left:866313703832944640>' or '<:right:866313744380723221>' or '🏹' or '❌')
		try:
			action, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
			action = str(action.emoji)
			await p_msg.remove_reaction(action, user)
		except asyncio.TimeoutError:
			await ctx.send(f"Time's Up! :stopwatch:\nGame over :coffin:")
			await endBoard(userRow, userCol, sys_msg)
			return

		# If direction, move
		if action == '🔼':
			userRow = userRow - 1
		if action == '🔽':
			userRow = userRow + 1
		if action == '<:right:866313744380723221>':
			userCol = userCol + 1
		if action == '<:left:866313703832944640>':
			userCol = userCol - 1

		# Do not allow user to walk off the face of the Earth.
		if userRow == 0:
			userRow = 1
		elif userRow == 6:
			userRow = 5

		if userCol == 9:
			userCol = 8
		elif userCol == 0:
			userCol = 1

		# If wumpus then user dies.
		if world[userRow][userCol] == 'w':
			await ctx.send('Chomp, chomp, chomp, you are dinner...')
			await endBoard(userRow, userCol, sys_msg)
			return

		# If pit then user dies.
		if world[userRow][userCol] == 'p':
			await ctx.send('"Aaaaaaaaaah," you scream as you fall to your death.')
			await endBoard(userRow, userCol, sys_msg)
			return

		# If bat then hyperspace.
		if world[userRow][userCol] == 'b':
			await ctx.send('You have been picked up by a bat.')
			await endBoard(userRow, userCol, sys_msg)
			return

		# Arrow/Shooting Stuff

		if action == '🏹':
			s_msg = await ctx.send("Where to shoot?", delete_after=12.0)
			# async with ctx.typing():
			for reaction in reactions[:-2]:
				await s_msg.add_reaction(reaction)

			def checkf(reaction, user):
				return user != bot.user and user == ctx.author and (str(reaction.emoji) == '🔼' or '🔽' or '<:left:866313703832944640>' or '<:right:866313744380723221>')
			try:
				flight, user = await bot.wait_for('reaction_add', timeout=10.0, check=checkf)
			except asyncio.TimeoutError:
				await ctx.send(f"Time's Up! :stopwatch:\nGame over :coffin:")
				await endBoard(userRow, userCol, sys_msg)
				return
			await s_msg.delete()

			flight = str(flight.emoji)
			# Check if the arrow hit the wumpus.
			if flight == '🔼':
				arrowRow = userRow - 1
				arrowCol = userCol
			if flight == '🔽':
				arrowRow = userRow + 1
				arrowCol = userCol
			if flight == '<:right:866313744380723221>':
				arrowRow = userRow
				arrowCol = userCol + 1
			if flight == '<:left:866313703832944640>':
				arrowRow = userRow
				arrowCol = userCol - 1

			# Do not allow the arrow to fly off the face of the Earth
			if arrowRow == 0:
				arrowRow = 1
			if arrowRow == 6:
				arrowRow = 5
			if arrowCol == 0:
				arrowCol = 1
			if arrowCol == 9:
				arrowCol = 8

			# Check what is in the spaces that he fired into.
			lookup = world[arrowRow][arrowCol]
			if lookup == 'w':
				try:
					await brd_msg.delete()
				except Exception:
					continue
				else:
					await ctx.send('You wumped the wumpus...\n**You win :trophy:**')
					await p_msg.edit(content=":star_struck:")
					await endBoard(userRow, userCol, sys_msg)
					return
			else:
				await ctx.send(':bow_and_arrow: Missed!', delete_after=1.5)

			arrows = arrows - 1
			await sys_msg.edit(content=f":bow_and_arrow:  `{arrows}`")
			if arrows==0:
				await ctx.send("You're out of arrows :bow_and_arrow:\nGame over :coffin:")
				await endBoard(userRow, userCol, sys_msg)
				return

		if action == '❌':
			await ctx.send('You quit :x:')
			await endBoard(userRow, userCol, sys_msg)
			return


@bot.command()
async def wumpus(ctx):
	await eplay(ctx)

        

@bot.command()
async def sauce(ctx, url=None):
        #https://github.com/FujiMakoto/pysaucenao Nice thing
        if url!= None:
            if is_url(url) != True:
                return await ctx.send("Your image url doesn't seem to be accurate. An image url should look like `https://danbooru.donmai.us/data/original/a2/d0/a2d093a060757d36d8a9f03bcbfbcd82.jpg`.")

        if url == None:
            await ctx.send("No url found in command, checking for attachments.", delete_after = 5)
            try:
                url = ctx.message.attachments[0].url
            except:
                url = None
        
        if url == None:
            await ctx.send("Couldn't find the url checking for the last message with image.", delete_after = 5)
            async for message in ctx.channel.history(limit=10):
                check = is_url(message.content)
                if check == True:
                    url = message.content
                    break
        if url == None:
            return await ctx.send("No image urls found in the last 10 messages please retry by uploading one.")
        try:
            google_url  = f"https://www.google.com/searchbyimage?image_url={url}&safe=off"
            yandex_url  = f"https://yandex.com/images/search?url={url}&rpt=imageview"
            saucenao_url = "https://saucenao.com/search.php?url={}".format(parse.quote_plus(url))
            #sauce = SauceNao(api_key = random2.choice(bot.saucenao_keys), results_limit = 6)
            sauce = SauceNao(results_limit=6)
            embed = discord.Embed(title="Here", color=discord.Color.random())
            results = await sauce.from_url(url)
            thumbnail = results[0].thumbnail if (results[0].thumbnail != None) else ctx.author.avatar.url
            similarity = results[0].similarity if (results[0].similarity != None) else 0
            embed.set_thumbnail(url = thumbnail)

            if isinstance(results[0], AnimeSource):
                await results[0].load_ids()
                embed.add_field(name="Anime Info", value=f"[AniList]({results[0].anilist_url})\n[MyAnimeList]({results[0].mal_url})")
            if isinstance(results[0], VideoSource):
                embed.add_field(name="Episode ", value=results[0].episode)
                embed.add_field(name= "TimeStamp", value=results[0].timestamp, inline=False)           

            if isinstance(results[0], MangaSource):
                embed.add_field(name="Chapter", value=results[0].chapter)
        
            try:
                source = results[0].url[0]
            except IndexError:
                source = "https://saucenao.com/search.php?url={}".format(parse.quote_plus(url))
            except TypeError:
                return await ctx.send("Nothing found in you request. Try not using a gif url if possible.")
            try:
                author = results[0].author_name
            except AttributeError:
                author = "Not given"
            try:
                title = results[0].title
            except AttributeError:
                title = "No title"
            index_id = results[0].index_id if (results[0].index_id != None) else "None"
            index_name = results[0].index_name if (results[0].index_name != None) else "None"
            if 50 >  similarity:
                return await ctx.send("Couldn't find any thing for the given query.")

            
            embed.description=f"Sucessfully found closest image(`{title}`) with the following information."
            embed.add_field(name="Similarity", value = similarity)
            embed.add_field(name="Author", value =author )
            embed.add_field(name="Source", value=source, inline=False)
            embed.add_field(name="Index", value=f"ID : `{index_id}` \nName : `{index_name}`")
            embed.add_field(name="Others", value=f"[Google]({google_url})\n[Yandex]({yandex_url})\n[SauceNao]({saucenao_url})",inline=False)
            await ctx.send(embed=embed)

        
        except UnknownStatusCodeException:
            url = "https://saucenao.com/search.php?url={}".format(parse.quote_plus(url))
            em = discord.Embed(title="ugh", description =f"Sorry nothing found you can try [here]({url}) if you'd like.", color=0x5865f2)
            em.set_footer(text="Also, make sure your url ends with an image format.")
            await ctx.send(embed = em)

        except InvalidImageException:
            return await ctx.send("Hey, it seems the url has no results. Also it seems your url is not an image url, please retry after checking that.")
        
def is_url(message):
        pattern =  re.compile(r"^https?://\S+(\.jpg|\.png|\.jpeg|\.webp]|\.gif)$")
        if not pattern.match(message):
            return False
        return True

@bot.command()
async def saucey(ctx, *,url):
    sauce = SauceNao()
    results = await sauce.from_url(url)

    if isinstance(results[0], AnimeSource):
        await results[0].load_ids()
        await ctx.reply(results[0].title)

@bot.command()
async def simon(ctx):
        """Start a game of Simon."""
        await ctx.send(
            "Starting game...\n**RULES:**\n```1. When you are ready for the sequence, click the green checkmark.\n2. Watch the sequence carefully, then repeat it back into chat.  For example, if the 1 then the 2 changed, I would type 12.\n3. You are given 10 seconds to repeat the sequence.\n4. When waiting for confirmation for next sequence, click the green check within 5 minutes of the bot being ready.\n5. Answer as soon as you can once the bot adds the stop watch emoji.```"
        )
        board = [[1, 2], [3, 4]]
        level = [1, 4]
        points = 0
        message = await ctx.send("```" + print_board(board) + "```")
        await message.add_reaction("\u2705")
        await message.add_reaction("\u274C")
        await ctx.send("Click the Green Check Reaction when you are ready for the sequence.")

        def check(reaction, user):
            return (
                (user.id == ctx.author.id)
                and (str(reaction.emoji) in ["\u2705", "\u274C"])
                and (reaction.message.id == message.id)
            )

        randoms = []
        for x in range(4):
            randoms.append(random2.randint(1, 4))

        while True:
            try:
                reaction, user = await bot.wait_for(
                    "reaction_add", check=check, timeout=300.0
                )
            except asyncio.TimeoutError:
                await message.delete()
                await ctx.send(
                    f"Game has ended due to no response for starting the next sequence.  You got {points} sequence{'s' if points != 1 else ''} correct!"
                )
                return
            else:
                if str(reaction.emoji) == "\u274C":
                    await message.delete()
                    await ctx.send(
                        f"Game has ended due to no response.  You got {points} sequence{'s' if points != 1 else ''} correct!"
                    )
                    return
                await message.remove_reaction("\u2705", bot.user)
                await message.remove_reaction("\u274C", bot.user)
                try:
                    await message.remove_reaction("\u2705", ctx.author)
                except discord.errors.Forbidden:
                    pass
                await message.add_reaction("\u26A0")
                for x in randoms:
                    await asyncio.sleep(1)
                    if x == 1:
                        board[0][0] = "-"
                        await message.edit(content="```" + print_board(board) + "```")
                        await asyncio.sleep(level[0])
                        board[0][0] = 1
                    elif x == 2:
                        board[0][1] = "-"
                        await message.edit(content="```" + print_board(board) + "```")
                        await asyncio.sleep(level[0])
                        board[0][1] = 2
                    elif x == 3:
                        board[1][0] = "-"
                        await message.edit(content="```" + print_board(board) + "```")
                        await asyncio.sleep(level[0])
                        board[1][0] = 3
                    elif x == 4:
                        board[1][1] = "-"
                        await message.edit(content="```" + print_board(board) + "```")
                        await asyncio.sleep(level[0])
                        board[1][1] = 4
                    await message.edit(content="```" + print_board(board) + "```")
                await message.remove_reaction("\u26A0", bot.user)
                answer = await "".join(list(map(str, randoms)))
                await message.add_reaction("\u23F1")

                def check_t(m):
                    return (m.author.id == ctx.author.id) and (m.content.isdigit())

                try:
                    user_answer = await bot.wait_for("message", check=check_t, timeout=10.0)
                except asyncio.TimeoutError:
                    await ctx.send(
                        f"Sorry {ctx.author.mention}!  You took too long to answer.  You got {points} sequence{'s' if points != 1 else ''} correct!"
                    )
                    await message.remove_reaction("\u23F1", bot.user)
                    return
                else:
                    try:
                        await user_answer.delete()
                    except discord.errors.Forbidden:
                        pass
                    await message.remove_reaction("\u23F1", bot.user)
                    if str(user_answer.content) == str(answer):
                        await message.add_reaction("\U0001F44D")
                    else:
                        await message.add_reaction("\U0001F6AB")
                        await ctx.send(
                            f"Sorry, but that was the incorrect pattern.  The pattern was {answer}.  You got {points} sequence{'s' if points != 1 else ''} correct!"
                        )
                        return
                    another_message = await ctx.send("Sequence was correct.")
                    points += 1
                    await asyncio.sleep(3)
                    await message.remove_reaction("\U0001F44D", bot.user)
                    await message.add_reaction("\u2705")
                    await message.add_reaction("\u274C")
                    await another_message.delete()
                level[0] *= 0.90
                randoms.append(random2.randint(1, 4))

def print_board(board):
        col_width = max(len(str(word)) for row in board for word in row) + 2  # padding
        whole_thing = ""
        for row in board:
            whole_thing += "".join(str(word).ljust(col_width) for word in row) + "\n"
        return whole_thing
    
@bot.command()
async def advmath(ctx, *expression):
    '''Advanced math command'''
        #if (expression == ""):
            #embed = discord.Embed(color = 0x5865f2, title = "Input A Expression")
            #await ctx.send(embed = embed)
            #return
    start = time.monotonic()
    api = "http://api.mathjs.org/v4/"
    params = {"expr": "".join(expression)}
    async with aiohttp.ClientSession() as cs:
        async with cs.get(api, params = params) as response:
            end = time.monotonic()
            embed = discord.Embed(color = 0xf34949, title = await response.text())
            embed.add_field(name = "Your Input:", value = f'`{"".join(expression)}`')
            embed.add_field(name = "Answer:", value = f"`{await response.text()}`")
            embed.set_footer(text = f"Calculated in {round((end - start) * 1000, 3)} ms")
            await ctx.reply(embed = embed)

async def get_result(ctx, operation, expression):
    if ("/" in expression):
        expression = expression.replace("/", "(over)")
        encoded_expression = parse.quote(expression)
        api = "https://newton.now.sh/api/v2"
        start = time.monotonic()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{api}/{operation}/{encoded_expression}") as response:
                data = await response.json()
                if ("error" in data.keys()):
                    embed = discord.Embed(title = f"Sorry! But the server was unable to solve the expression", color = 0xf34949)
                    return embed
                result = data["result"]
                end = time.monotonic()
                embed = discord.Embed(color = 0xf34949,title = result)
                embed.add_field(name = "Your Input:", value = f'`{expression.replace("(over)", "/")}`')
                embed.add_field(name = "Answer:",value = f"`{result}`")
                embed.set_footer(text = f"Calculated in {round((end - start) * 1000, 3)} ms")
                return embed

        
@bot.command()
async def derive(ctx, *,expression):
    expression = "".join(expression)
    loading = await ctx.send("Calculating...")
    await ctx.trigger_typing()
    lo = await get_result(ctx = ctx, operation = "derive", expression = expression)
    await loading.delete()
    await ctx.reply(embed = lo)

@bot.listen('on_message')
async def massage(message):
    #this=["710545224350302319", "710528916745617489", "794075864978817054"]
    if not message.author.bot:
        with open('users.json','r') as f:
            users = json.load(f)
        if message.channel.id == 710545224350302319:
            return
        if message.content=="-level":
            return
        if message.content=="-rank":
            return
        await update_data(users, message.author, message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author, message, message.guild)

        with open('users.json','w') as f:
            json.dump(users, f)

@bot.command()
@commands.is_owner()
async def fixbug(ctx, *,user:discord.Member=None):
    if user==None:
        user=ctx.author
    with open("users.json", "r") as f:
    #if user==None:
        #user = ctx.author
        users = json.load(f)
    lo = users[str(user.guild.id)][str(user.id)]['experience']
    ae = users[str(user.guild.id)][str(user.id)]['level']
    e = await ctx.reply(lo)
    ok1 = (ae + 1)
    ok2 = ok1**4
    ok3 = ok2 - 4
    ok4 = int(ok3)
    ok5 = ok2 - 1
    ok6 = int(ok5)
    a = await ctx.send("looking...")
    #await add_experience(users, user, 4, user.guild)
    ez = int(lo+8)
    ye = int(ez)
    pp = int(ae+1)
    ok = int(pp)
    if lo==ok4:
        await ctx.send("found a bug")
        users[str(user.guild.id)][str(user.id)]['experience'] = ye
        users[str(user.guild.id)][str(user.id)]['level'] = ok
        with open('users.json', 'w') as f:
            json.dump(users, f)
        await ctx.send("fixed it")
    elif lo==ok6:
        await ctx.send("found the usual bug")
        users[str(user.guild.id)][str(user.id)]['experience'] = ye
        users[str(user.guild.id)][str(user.id)]['level'] = ok
        with open('users.json', 'w') as f:
            json.dump(users, f)
        await ctx.send("done, bug fixed")
    else:
        await ctx.send("nope, no bug found")
     
    #new = await ctx.send("done")
   # await new.delete()
    await e.delete()
    await a.delete()

async def addnew_experience(users, member, exp, guild):
    users[str(member.guild.id)][str(member.id)]['experience'] = exp
    
async def update_data(users, user, guild):
    if not str(guild.id) in users:
        users[str(guild.id)] = {}
        if not str(user.id) in users[str(guild.id)]:
            users[str(guild.id)][str(user.id)] = {}
            users[str(guild.id)][str(user.id)]['experience'] = 0
            users[str(guild.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(guild.id)]:
            users[str(guild.id)][str(user.id)] = {}
            users[str(guild.id)][str(user.id)]['experience'] = 0
            users[str(guild.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, guild):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp   

async def level_up(users, user, message, guild):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if lvl_start < lvl_end:
    users[str(user.guild.id)][str(user.id)]['level'] = lvl_end
    experienceq = (lvl_start + 1)
    lonew = int(experience + 4)
    new = int(lonew)
    users[str(user.guild.id)][str(user.id)]['experience'] = new
    users[str(user.guild.id)][str(user.id)]['level'] = experienceq
    with open("users.json", "w") as f:
        json.dump(users, f)
    embed=discord.Embed(title="Level up!", description=f"**{message.author.mention}, you advanced to `Level {lvl_end}`**", color=discord.Color.random())
    #embed.set_footer(text="-level to check ur level")
    lo=await message.reply(embed=embed)
    #print('{} has leveled up to Level {}'.format(user.mention, lvl_end))
    #users[str(user.guild.id)][str(user.id)]['level'] = lvl_end
    #if (users[str(user.guild.id)][str(user.id)]['level'] == 2):
    if lvl_end == 10:
            var = discord.utils.get(message.guild.roles, id=710698976202063883)
            await user.add_roles(var)
    elif lvl_end == 20:
            var = discord.utils.get(message.guild.roles, id=710699108880351312)
            await user.add_roles(var)
    elif lvl_end == 30:
            var = discord.utils.get(message.guild.roles, id=710699186743541760)
            await user.add_roles(var)
    embed2=discord.Embed(title="Level up!", description=f"**{message.author.mention}, you advanced to `Level {lvl_end}`**", color=discord.Color.random())
    embed2.add_field(name="New Role", value=f"> **{var.mention}**")
    await lo.edit(content="**GG!**",embed=embed2)
            #await message.channel.send("u got the role!")

def image_search(query):
    r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 200,
        'q': query,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]

    image = urls[0]

    return image

@bot.command()
async def googimg(ctx, *,query):
    pic = image_search(query)
    await ctx.reply(pic)

@bot.command()
@commands.is_owner()
async def sync(ctx):
    synced = await bot.tree.sync(guild=ctx.guild)
    await ctx.reply(f"**Synced {len(synced)} commands**")
    
    
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def gasync(
  ctx, guilds: commands.Greedy[discord.Object], spec: typing.Optional[typing.Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
    
@bot.event
async def on_ready():
    await bot.load_extension('jishaku')
    #try:
        #synced = await bot.tree.sync()
        #print(f"Synced {len(synced)} command(s)")
    #except Exception as e:
        #print(e)

# This context menu command only works on members
@bot.tree.context_menu(name='Show Join Date')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')   
        
@bot.tree.context_menu(name="test")
#@app_commands.describe(text="Test command")
async def hello(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(f"Hey this is context menu command!", ephemeral=True)

@bot.tree.command(name="og")
async def og(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, you the og man!", ephemeral=True)
    
@bot.tree.command(name="sayy")
#@app_commands.describe(thing_to_say = "What should I say?")
async def sayy(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"{text}")

#@bot.tree.command(name="bh")
@bot.hybrid_command()
async def bh(interaction: discord.Interaction):
    pages = []
    page_content = ""
    
    for i in range(15):
        if (i > 0) and (i % 5 == 0):
            pages.append(page_content)
            page_content = ""

        page_content += f"{i+1}. Item `{i}`\n"

    if (page_content != "") and not (page_content in pages): pages.append(page_content)
        
    await Paginator(interaction, pages).start()
#bot.load_extension('dismusic')
#@bot.event
#async def on_ready():
    #await bot.load_extension('dispander')
    #await bot.load_extension('cog_reloader')
    #await bot.load_extension('CustomCommands')
    #await bot.load_extension('jishaku')

@bot.tree.command(name="mute", description="Admin command, you will not be able to run this")
async def mute(interaction: discord.Interaction, member: discord.Member, time: str, reason: str):
    desctime = time
    s=f"{member.name} has been unmuted"
    guild = bot.guilds
    role = discord.utils.get(member.guild.roles, name="Muted")
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    tempmute = int(time[0]) * time_convert[time[-1]]
    embed=discord.Embed(title="Muted", description=f"{member.name} has been muted", color=0x7892da)
    await interaction.response.send_message(embed=embed)
    await member.add_roles(role, reason=reason)
    await asyncio.sleep(tempmute)
    await interaction.user.remove_roles(role)
    await interaction.edit_original_response(f"{s}")

bot.run("OTE4MTg2MDk3NzY1NDAwNjU3.GeDirj.KcdnTSeIWbOpqwoEigIB8MJqPK_fHXZAc6elTo")