from types import MemberDescriptorType
import discord 
import Item_gen
from discord.ext import commands
import asyncio
from discord.ext.commands import CommandNotFound


pages = ['page1', 'page2', 'page3']

shops = ['Phauahevon', 'Weastberia', 'Eaqoria', 'phauahevon', 'weastberia', 'eaqoria', 'PHAUAHEVON', 'WEASTBERIA', 'EAQORIA']
item_types = ['Common', 'Uncommon', 'Rare', 'cCommon', 'cUncommon', 'cRare',
              'COMMON', 'UNCOMMON', 'RARE', 'CCOMMON', 'CUNCOMMON', 'CRARE',
               'common', 'uncommon', 'rare', 'ccommon', 'cuncommon', 'crare',
             ]
headerss = ['Item', 'Gold']

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print("Bot is ready")

@client.command() 
async def hello(ctx):
    await ctx.send('This works!')

@client.command()
async def Phauahevon(ctx, type):
    em = None
    if type == 'common' or type == 'Common' or type == 'COMMON': 
        em1 = discord.Embed(title = 'Phauahevon Common Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon Common Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.common_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon Common Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.common_list[26:len(Item_gen.Phauahevon_common)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'uncommon'or type == 'Uncommon' or type == 'UNCOMMON' : 
        em1 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.uncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.uncommon_list[26:len(Item_gen.Phauahevon_uncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'rare' or type == 'Rare' or type == 'RARE': 
        em1 = discord.Embed(title = 'Phauahevon rare Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon rare Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.rare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon rare Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.rare_list[26:len(Item_gen.Phauahevon_rare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'ccommon' or type == 'cCommon' or type == 'CCOMMON': 
        em1 = discord.Embed(title = 'Phauahevon common consumables Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon common consumables Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon common consumables Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.ccommon_list[26:len(Item_gen.Phauahevon_ccommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'cuncommon' or type == 'cUncommon' or type == 'CUNCOMMON': 
        em1 = discord.Embed(title = 'Phauahevon Uncommon Consumables Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.cuncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon Uncommon Consumables Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.cuncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon Uncommon Consumables Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.cuncommon_list[26:len(Item_gen.Phauahevon_cuncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'crare' or type == 'cRare' or type == 'CRARE': 
        em1 = discord.Embed(title = 'Phauahevon Rare Consumables Shop', description= 'Page 1')
        for item in Item_gen.Phauahevon.crare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon Rare Consumables Shop', description= 'Page 2')
        for item in Item_gen.Phauahevon.crare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon Rare Consumables Shop', description= 'Page 3')
        for item in Item_gen.Phauahevon.crare_list[26:len(Item_gen.Phauahevon_crare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")

    embeds = [em1, em2, em3]
    pages = 3
    cur_page = 1

    message = await ctx.send(embed=embeds[cur_page-1])
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        print("oh What the")
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            if reaction.emoji == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x second

@client.command()
async def Weastberia(ctx, type):
    em = None
    if type == 'common' or type == 'Common' or type == 'COMMON': 
        em1 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.common_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.common_list[26:len(Item_gen.Weastberia_common)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'uncommon'or type == 'Uncommon' or type == 'UNCOMMON' : 
        em1 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.uncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.uncommon_list[26:len(Item_gen.Weastberia_uncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'rare' or type == 'Rare' or type == 'RARE': 
        em1 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.rare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.rare_list[26:len(Item_gen.Weastberia_rare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'ccommon' or type == 'cCommon' or type == 'CCOMMON': 
        em1 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.ccommon_list[26:len(Item_gen.Weastberia_ccommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'cuncommon' or type == 'cUncommon' or type == 'CUNCOMMON': 
        em1 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.cuncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.cuncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.cuncommon_list[26:len(Item_gen.Weastberia_cuncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'crare' or type == 'cRare' or type == 'CRARE': 
        em1 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 1')
        for item in Item_gen.Weastberia.crare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 2')
        for item in Item_gen.Weastberia.crare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 3')
        for item in Item_gen.Weastberia.crare_list[26:len(Item_gen.Weastberia_crare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")

    embeds = [em1, em2, em3]
    pages = 3
    cur_page = 1

    message = await ctx.send(embed=embeds[cur_page-1])
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        print("oh What the")
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            if reaction.emoji == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x second

@client.command()
async def Eaqoria(ctx, type):
    em = None
    if type == 'common' or type == 'Common' or type == 'COMMON': 
        em1 = discord.Embed(title = 'Eaqoria Common Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Common Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.common_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria Common Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.common_list[26:len(Item_gen.Eaqoria_common)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'uncommon'or type == 'Uncommon' or type == 'UNCOMMON' : 
        em1 = discord.Embed(title = 'Eaqoria uncommon Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria uncommon Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.uncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria uncommon Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.uncommon_list[26:len(Item_gen.Eaqoria_uncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'rare' or type == 'Rare' or type == 'RARE': 
        em1 = discord.Embed(title = 'Eaqoria rare Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria rare Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.rare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria rare Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.rare_list[26:len(Item_gen.Eaqoria_rare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'ccommon' or type == 'cCommon' or type == 'CCOMMON': 
        em1 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.ccommon_list[26:len(Item_gen.Eaqoria_ccommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'cuncommon' or type == 'cUncommon' or type == 'CUNCOMMON': 
        em1 = discord.Embed(title = 'Eaqoria Uncommon Consumables Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.cuncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Uncommon Consumables Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.cuncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria Uncommon Consumables Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.cuncommon_list[26:len(Item_gen.Eaqoria_cuncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
    if type == 'crare' or type == 'cRare' or type == 'CRARE': 
        em1 = discord.Embed(title = 'Eaqoria Rare Consumables Shop', description= 'Page 1')
        for item in Item_gen.Eaqoria.crare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Rare Consumables Shop', description= 'Page 2')
        for item in Item_gen.Eaqoria.crare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria Rare Consumables Shop', description= 'Page 3')
        for item in Item_gen.Eaqoria.crare_list[26:len(Item_gen.Eaqoria_crare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")

    embeds = [em1, em2, em3]
    pages = 3
    cur_page = 1

    message = await ctx.send(embed=embeds[cur_page-1])
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        print("oh What the")
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            if reaction.emoji == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=embeds[cur_page-1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x second

@client.command()
async def buy(ctx, shop, gold, *item_name):
    res = await buy_this(shop, gold, *item_name)
    
    if res[0] == 0: 
        await ctx.send("Please check that the item is listed or that you inputted the correct amount of gold.")
    else:
         await ctx.send(f"{ctx.author} just bought {item_name} from {shop} for {gold}gp")
            
async def buy_this(shop, gold, item_name):
    gold = str(gold)
    thing = {'name': item_name, 'Gold':gold}
    itm_in_there = [0, 0, 0]
    if shop in shops:  
        if thing in Item_gen.Phauahevon.common_list: 
            indx_of_itm = Item_gen.Phauahevon.common_list.index(thing)
            Item_gen.Phauahevon.common_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Phauahevon.uncommon_list: 
            indx_of_itm = Item_gen.Phauahevon.uncommon_list.index(thing)
            Item_gen.Phauahevon.uncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Phauahevon.rare_list: 
            indx_of_itm = Item_gen.Phauahevon.rare_list.index(thing)
            Item_gen.Phauahevon.rare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Phauahevon.ccommon_list: 
            indx_of_itm = Item_gen.Phauahevon.ccommon_list.index(thing)
            Item_gen.Phauahevon.ccommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Phauahevon.cuncommon_list: 
            indx_of_itm = Item_gen.Phauahevon.cuncommon_list.index(thing)
            Item_gen.Phauahevon.cuncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Phauahevon.crare_list: 
            indx_of_itm = Item_gen.Phauahevon.crare_list.index(thing)
            Item_gen.Phauahevon.crare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.common_list: 
            indx_of_itm = Item_gen.Weastberia.common_list.index(thing)
            Item_gen.Weastberia.common_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.uncommon_list: 
            indx_of_itm = Item_gen.Weastberia.uncommon_list.index(thing)
            Item_gen.Weastberia.uncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.rare_list: 
            indx_of_itm = Item_gen.Weastberia.rare_list.index(thing)
            Item_gen.Weastberia.rare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.ccommon_list: 
            indx_of_itm = Item_gen.Weastberia.ccommon_list.index(thing)
            Item_gen.Weastberia.ccommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.cuncommon_list: 
            indx_of_itm = Item_gen.Weastberia.cuncommon_list.index(thing)
            Item_gen.Weastberia.cuncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Weastberia.crare_list: 
            indx_of_itm = Item_gen.Weastberia.crare_list.index(thing)
            Item_gen.Weastberia.crare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.common_list: 
            indx_of_itm = Item_gen.Eaqoria.common_list.index(thing)
            Item_gen.Eaqoria.common_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.uncommon_list: 
            indx_of_itm = Item_gen.Eaqoria.uncommon_list.index(thing)
            Item_gen.Eaqoria.uncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.rare_list: 
            indx_of_itm = Item_gen.Eaqoria.rare_list.index(thing)
            Item_gen.Eaqoria.rare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.ccommon_list: 
            indx_of_itm = Item_gen.Eaqoria.ccommon_list.index(thing)
            Item_gen.Eaqoria.ccommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.cuncommon_list: 
            indx_of_itm = Item_gen.Eaqoria.cuncommon_list.index(thing)
            Item_gen.Eaqoria.cuncommon_list.pop(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Item_gen.Eaqoria.crare_list: 
            indx_of_itm = Item_gen.Eaqoria.crare_list.index(thing)
            Item_gen.Eaqoria.crare_list.pop(indx_of_itm)
            itm_in_there[0] = 1
    return itm_in_there

@client.command(pass_context = True)
@commands.has_role('Data Member')
async def refresh(ctx): 
    Item_gen.refresh() 

