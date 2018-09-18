import requests
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


def forumPost(data , section, user):
    delm = 0
    title = ''
    content = ''
    for word in data:
        if delm == 0 and word != ';':
            title += word
            title += ' '
        elif delm == 1:
            content += word
            content += " "
        if word == ';':
            delm = 1
    
    content += " **- Submitted By "
    content += user
    content += "**"

    if title != '' and content != '':
        userdata = {"title": title, "message": content, "section": section}
        resp = requests.post('https://imperials.io/api/thread.php', params=userdata)
        return True
    else:
        return False

@client.event
async def on_ready():
    print('Bot initiated')


@client.command(pass_context=True)
async def method(ctx, *args):
    author = str(ctx.message.author)
    status=forumPost(args, 21, author)
    if status:
        await client.say("The title has been posted Successfully")
    else:
        await client.say("Wrong Format kindly use this format: .SectionName Thread Title ; Thread Content")


@client.command(pass_context=True)
async def method1(ctx, *args):
    author = str(ctx.message.author)
    status = forumPost(args, 23, author)
    if status:
        await client.say("The title has been posted Successfully")
    else:
        await client.say("Wrong Format kindly use this format: .SectionName Thread Title ; Thread Content")


@client.command(pass_context=True)
async def method2(ctx, *args):
    author = str(ctx.message.author)
    status = forumPost(args, 24, author)
    if status:
        await client.say("The title has been posted Successfully")
    else:
        await client.say("Wrong Format kindly use this format: .SectionName Thread Title ; Thread Content")


@client.command(pass_context=True)
async def method3(ctx, *args):
    author = str(ctx.message.author)
    status = forumPost(args, 25, author)
    if status:
        await client.say("The title has been posted Successfully")
    else:
        await client.say("Wrong Format kindly use this format: .SectionName Thread Title ; Thread Content")

client.run(os.getenv('TOKEN'))
