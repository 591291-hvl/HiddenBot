import discord
import os
import countInfo

import art


from keepAlive import keepAlive

intents = discord.Intents(messages=True, guilds=True, members=True)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	activity = discord.Game(name="!help for list of commands")
	await client.change_presence(status=discord.Status.offline, activity=activity)

#Text responses
@client.event
async def on_message(message):
	if message.author == client.user or not message.author.id == 223112835671130112:
		return

	elif message.content.lower().startswith(".test"):
		await message.channel.send("I work")

	elif message.content.lower().startswith("!counttxt"):
		async with message.channel.typing():
			await message.channel.send("```\n" + await countInfo.get_txt(client, message) + "\n```")

	elif message.content.lower().startswith("!countimg"):
		async with message.channel.typing():
			await message.channel.send(file=await countInfo.get_img(client, message))

	elif message.content.lower().startswith("!countall"):
		async with message.channel.typing():
			await message.reply(await countInfo.get_countAll(client,message), mention_author=True)

	elif message.content.lower().startswith("!count"):
		async with message.channel.typing():
			await message.reply(await countInfo.get_count(message.content[7:],client, message), mention_author=True)
	
	elif message.content.lower().startswith("!wordcountchannel"):
		async with message.channel.typing():
			await message.reply(await countInfo.get_wordchannel(message.content[18:],client, message), mention_author=True)

	elif message.content.lower().startswith("!wordcounttxt"):
		async with message.channel.typing():
			await message.channel.send("```\n" + await countInfo.get_wordTxt(client, message) + "\n```")

	elif message.content.lower().startswith("!wordcountimg"):
		async with message.channel.typing():
			await message.channel.send(file=await countInfo.get_wordImg(client, message))

	elif message.content.lower().startswith("!wordcountall"):
		async with message.channel.typing():
			await message.reply(await countInfo.get_wordCountAll(client,message), mention_author=True)

	elif message.content.lower().startswith("!wordcount"):
		async with message.channel.typing():
			await message.reply(await countInfo.get_wordCount(message.content[11:],client, message),mention_author=True)


  #Not relevant to main function
  
	elif message.content.lower().startswith("!art"):
		async with message.channel.typing():
			await message.channel.send("```\n" + art.text2art(message.content[5:]) + "\n```")

	elif message.content.lower().startswith("!github"):
		async with message.channel.typing():
			await message.channel.send("https://github.com/591291-hvl/dpsharkBot")

	elif (client.user.mentioned_in(message) or "<@" in message.content):
		async with message.channel.typing():
			await message.add_reaction("<:blobping:917804967350399059>")

	elif "pog" in message.content.lower():
		async with message.channel.typing():
			await message.add_reaction("<:pog:917817711982182570")
  
      
	else:
		print("nothing")


keepAlive()
client.run(os.environ['TOKEN'])