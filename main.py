from __future__ import print_function

import discord
from discord.ext import commands
import time
from config import *

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate(firebaseconfig)
databaseApp = firebase_admin.initialize_app(cred,{'databaseURL':databaseURL})

#client = discord.Client()

bot = commands.Bot(command_prefix="!", description="game bot")


# @client.event
# async def on_message(message):

#     if message.content.startswith('!whitelist'):
#         personid = str(message.author.id)
#         person=str(message.author.name)
#         rows = read_range()
#         print(rows)
#         addy=str(message.content).split(" ",1)[1]
#         print('addy is: '+str(addy))
#         if str(personid) not in rows:

#           DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + [str(message.content).split(" ",1)[1]]
#           add(SPREADSHEET_ID, RANGE_NAME, DATA)
#           await message.channel.send(str(person) + ': ' + str(addy) +' has been whitelisted!')

#         if str(personid) in rows:
#           print('already registered')
#           await message.channel.send(str(person)+': is already whitelisted!')
#         #await message.channel.send("hello!")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# @bot.command(pass_context=True)
# async def write(ctx): # !write
#     #color = input("pick a color")
#     person= ctx.message.author
#     user = ctx.message.id
#     print(user, " is user id")
#     ref = db.reference(f"/")
#     ref.update({
#         user: "nope"
#         }
#     )
#     await message.channel.send(str(person)+", your login code is: "str(user))

@bot.command(pass_context=True)
async def play(ctx): # !play
    #color = input("pick a color")
    person= ctx.message.author
    user = ctx.message.author.id
    print(user, " is user id")
    ref = db.reference(f"/")
    ref2 = db.reference(f"/"+str(user))    
    status2 = ref2.get()
    #print(status2)
    if status2 == None:
        ref.update({
            user: "nope"
            }
    )
    await ctx.channel.send(str(person)+", your login code is: "+str(user))

def letsee():
    ref2 = db.reference(f"/"+"bobby") 
    status2 = ref2.get()
    print(status2)
    if status2 == None:
        print("caught")


letsee()

@bot.command(pass_context=True)
async def upgrade(ctx): #!upgrade
    person= ctx.message.author
    user = ctx.message.author.id
    ref = db.reference(f"/"+str(user))    
    status = ref.get()
    print("status: "+ str(status))

    rolelist=[]
    for role in person.roles:
        rolelist.append(role.name)
    print(rolelist)

    if status == "nope":
        await ctx.channel.send(str(person) + ", you haven't reached the score threshold!")
    if int(status) >=15:
        if "bear" not in rolelist:
            ogrole = discord.utils.get(person.guild.roles, name = "OG DEGENETICIST")
            await person.add_roles(ogrole, atomic=True)
            await ctx.channel.send(str(person) + ", congrats! Your role is now OG.")
        else:
            await ctx.channel.send(str(person) + ", You already have OG role")
    else:        
        await ctx.channel.send(str(person)+ ", please use the !play command to get your game code.")    
    

bot.run(TOKEN)    
