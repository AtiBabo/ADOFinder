import os
import sys
import nextcord
from nextcord.ext import commands

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from info import INFO

class curvedChartCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(name="곡선채보", description="N각형의 각도와 BPM을 구해줍니다.")
    async def curvedChart(
            self, interaction: nextcord.Interaction,
            angular: int = nextcord.SlashOption(
                name = "angular",
                description = "몇 각형을 만들지 정합니다.",
                min_value = 3,
                required = True),
            bpm: float = nextcord.SlashOption(
                name = "bpm",
                description = "곡선채보를 만들 위치의 BPM을 입력해주세요.",
                required = True),
            direction: str = nextcord.SlashOption(
                name = "direction",
                description = "곡선채보에서 공이 돌 방향을 구합니다.",
                choices = {"내각": "in", "외각": "out"},
                required = True)
            ):
        if direction == "in":
            embed = nextcord.Embed(title="정**" + str(angular) + "**각형의 한 내각", description="", color=INFO.default_color)
            embed.add_field(name="각도", value="**" + str(round(180 * (angular-2) / angular, 8)) + "**°", inline=False)
            embed.add_field(name="BPM", value="**" + str(round(bpm * (180 * (angular-2) / angular) / 180, 8)) + "**BPM", inline=False)
            embed.add_field(name="승수", value="**" + str(round((180 * (angular - 2) / angular) / 180, 8)) + "**X", inline=False)
            await interaction.send(embed=embed, ephemeral=False)
        elif direction == "out":
            embed = nextcord.Embed(title="정**" + str(angular) + "**각형의 한 외각", description="", color=INFO.default_color)
            embed.add_field(name="각도", value="**" + 180 * str(round(((360 - angular) - 2) / (360 - angular), 8)) + "**°", inline=False)
            embed.add_field(name="BPM", value="**" + str(round(bpm * (360-(((360 - angular) - 2) / (360-angular))) / 180, 8)) + "**BPM", inline=False)
            embed.add_field(name="승수", value="**" + str(round(180 / (180 * (angular - 2) / angular), 8)) + "**X", inline=False)
            await interaction.send(embed=embed, ephemeral=False)

def setup(client):
    client.add_cog(curvedChartCog(client))