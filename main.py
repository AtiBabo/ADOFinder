import configparser
import itertools
import nextcord
import platform
import sqlite3
from info import CCO
from info import INFO
from nextcord.ext import tasks
from nextcord.ext import commands

extensions = ["commands.ping", "commands.curvedChart", "commands.eventRemover"]

config = configparser.ConfigParser()
config.read(INFO.now_directory + '/config.ini')

token = str(config['CREDENTIALS']['token'])
owner_id = str(config['CREDENTIALS']['owner_id'])
client_secret = str(config['CREDENTIALS']['client_secret'])
client_id = str(config['CREDENTIALS']['client_id'])

print(f'{CCO.CHECK}Setting check.')

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.AutoShardedBot(command_prefix=' ', intents=intents, status='dnd')

@client.event
async def on_ready():
    print(f'{CCO.CHECK}Authentication to Discord.')
    
    owner_name = await client.fetch_user(owner_id)
    print('======================================')
    print(f'Logged in as {CCO.BLUE}{client.user.name}#{client.user.discriminator} {CCO.RESET}({CCO.BLUE}{client.user.id}{CCO.RESET})')
    print(f"Owner: {CCO.BLUE}{str(owner_name)}{CCO.RESET} {CCO.RESET}({CCO.BLUE}{owner_id}{CCO.RESET})")
    print(f'Currenly running nextcord {CCO.BLUE}{nextcord.__version__}{CCO.RESET} on python {CCO.BLUE}{platform.python_version()}{CCO.RESET}')
    print('======================================')
    
    changeStatus.start()

statusMessage = itertools.cycle([
        "개발자는 바보입니다.",
        "개의 서버에 참가 중"
    ])

@tasks.loop(seconds = 10)
async def changeStatus():
    next_status = next(statusMessage)
    status = 'idle'
    
    if next_status == "개의 서버에 참가 중": next_status = str(len(client.guilds)) + "개의 서버에 참가 중"
    
    await client.change_presence(activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=next_status), status=status)

def cogReloader():
    '''cog들을 다시 로드'''
    
    for extension in extensions:
        if extension in client.extensions:
            client.unload_extension(extension)
    
    for extension in extensions:
        client.load_extension(extension)

cogReloader()

client.run(token)