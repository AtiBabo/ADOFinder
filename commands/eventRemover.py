import os
import sys
import nextcord
from nextcord.ext import commands

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from info import INFO

class eventRemoverCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(name="이벤트제거", description=".adofai 파일의 이벤트를 제거합니다.")
    async def eventRemover(
            self, interaction: nextcord.Interaction
        ):
        
        embed = nextcord.Embed(
            title=":ping_pong: Pong! (" + str((round(self.client.latency * 1000, 2))) + "ms)", 
            description="", 
            color=INFO.default_color
        )
        
        embed.add_field(name="✅ 업타임", value="<t:" + str(INFO.uptime) + ":R>")
        embed.add_field(name="🏠 현재 참가중인 서버", value=f"{str(len(self.client.guilds))} 개")
        embed.set_footer(text="현재 버전 : V" + str(INFO.version))
        await interaction.send(embed=embed, ephemeral=False)

def setup(client):
    client.add_cog(eventRemoverCog(client))