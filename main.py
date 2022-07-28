'''
Credit to OnlyEli#8144 on discord for the JuiceWRLD era database
Eliza was developed by me, y9#8009
Feel free to use this code, but please give credit if you do
'''

from pydoc import describe
import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
eliza = commands.Bot(command_prefix=";", intents=intents, case_insensitive=True)
eliza.remove_command('help')

with open('juicewrld-era-db.json', 'r') as file:
    data = json.load(file)


@eliza.command(brief="Song Era Information", description="Displays the era for specified song.")
async def era(ctx, *, song = None) -> None:
    if song is None:
        embed = discord.Embed(title="❌ No song title provided", color=0)
        await ctx.reply(embed=embed)
        return
    
    eras = ['wod', 'drfl', 'gbgr', 'outsiders', 'juicethekidd', 'nineninenine']
    the_era = None
    for era in eras:

        if song.lower() in data['eras'][era]:
            the_era = era
            if era == 'wod':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value=f"{era.upper()}")
                embed.add_field(name="Era Timeline", value="May 24th, 2018 - October 19th, 2018", inline=False)
                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/0/02/Wrld_on_Drugs.jpg/220px-Wrld_on_Drugs.jpg")
                await ctx.reply(embed=embed)
                break

            elif era == 'drfl':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value=f"{era.upper()}")
                embed.add_field(name="Era Timeline", value="October 20th, 2018 - March 8th, 2019", inline=False)
                embed.set_thumbnail(url="https://media.pitchfork.com/photos/5c7fe8f08a62e1373c014204/1:1/w_450%2Cc_limit/JuiceWLRD_DeathRaceForLove.jpg")
                await ctx.reply(embed=embed)
                break

            elif era == 'gbgr':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value=f"{era.upper()}")
                embed.add_field(name="Era Timeline", value="June 16th, 2017 - May 23rd, 2018", inline=False)
                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg")
                await ctx.reply(embed=embed)
                break

            elif era =='outsiders':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value="JW3")
                embed.add_field(name="Era Timeline", value="March 9th, 2019 - December 8th, 2019", inline=False)
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/juice-wrld/images/7/7b/Outsiderscover3.PNG/revision/latest/scale-to-width-down/250?cb=20200317030834")
                await ctx.reply(embed=embed)
                break

            elif era == 'juicethekidd':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value="JuiceTheKidd")
                embed.add_field(name="Era Timeline", value="Pre March 2017", inline=False)
                embed.set_thumbnail(url="https://i.pinimg.com/736x/d0/d4/74/d0d474e4cd36837c948709fdc03e21c7.jpg")
                await ctx.reply(embed=embed)
                break
 
            elif era == 'nineninenine':
                embed = discord.Embed(color=0)
                embed.add_field(name=f"{song.title()}'s era is", value="999")
                embed.add_field(name="Era Timeline", value="March 2017- June 15th, 2017", inline=False)
                embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000228668625-4m8ren-t500x500.jpg")
                await ctx.reply(embed=embed)
                break
    if the_era is None:
        embed = discord.Embed(color=0)
        embed.add_field(name="Error", value=f"I couldn't find the song {song.title()} in __any__ eras. Please check spelling and retry")
        await ctx.reply(embed=embed)


@eliza.command(brief="All Eras", description="Displays all eras.")
async def eras(ctx) -> None:
    embed = discord.Embed(color=0)
    embed.add_field(name="JuiceTheKidd", value="Timeline:\nPre March 2017", inline=False)
    embed.add_field(name="999", value="Timeline:\nMarch 2017 - June 15th, 2017", inline=False)
    embed.add_field(name="Goodbye & Good Riddance", value="Timeline:\nJune 16th, 2017 - May 23rd, 2018", inline=False)
    embed.add_field(name="Wrld On Drugs", value="Timeline:\nMay 24th, 2018 - October 19th, 2018", inline=False)
    embed.add_field(name="Death Race For Love", value="Timeline:\nOctober 20th, 2018 - March 8th, 2019", inline=False)
    embed.add_field(name="JW3", value="Timeline:\nMarch 9th, 2019 - December 8th, 2019", inline=False)
    embed.set_thumbnail(url="https://images.fineartamerica.com/images/artworkimages/medium/3/1-juice-wrld-999-original-merch-sania-wadika-transparent.png")
    await ctx.reply(embed=embed)

@eliza.command(brief="Help", description="Displays all commands")
async def help(ctx) -> None:
    embed = discord.Embed(title="Help Menu", color=0)
    embed.add_field(name=";era <song title>", value="Search for a songs era", inline=True)
    embed.add_field(name=";eras", value="Display all eras", inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text="<> = required")
    await ctx.reply(embed=embed)


eliza.run("TokenGoesHere")
