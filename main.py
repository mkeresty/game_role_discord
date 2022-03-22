import discord

from discord.ext import commands

TOKEN='OTU1OTY0NTkwMzEzODQwNjYx.YjpVZw.b-SoCMYiAQP_LZ2_8yZFsQoWBB0'

client = discord.Client()

bot = commands.Bot(command_prefix="!", description="invite bot")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def invite(ctx): #!upgrade
    person= ctx.message.author
    user = ctx.message.author.id
    
    rolelist=[]
    for role in person.roles:
        rolelist.append(role.name)
    print(rolelist)
    x = await ctx.guild.invites()
    print(x)
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            print(i.inviter)
            totalInvites += i.uses
    print(totalInvites)        
    if totalInvites > 1:
        if "CannaDAO cultivator" not in rolelist:
            ogrole = discord.utils.get(person.guild.roles, name = "CannaDAO cultivator")
            await person.add_roles(ogrole, atomic=True)
            embed = discord.Embed(title = person, description = str(person) + ", congrats! You are now an CannaDAO cultivator.")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
            
        else:
            embed = discord.Embed(title = person, description = str(person) + ", you already have CannaDAO cultivator role.")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
        
    else:     
        embed = discord.Embed(title = person, description= 'Not enough invites!')
        embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
        await ctx.channel.send(embed = embed)
        


    
#client.run(TOKEN)
bot.run(TOKEN)   
