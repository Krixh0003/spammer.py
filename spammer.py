import discord
client = discord.Client()
keywords = ["krish", "help", "pyautogui", "hello", "hi"]


@client.event
async def on_message(message):
      for i in range(len(keywords)):
          if keywords[i] in message.content:
              for i in range(1000):
                  await message.channel.send("type anything u want to spam ")

client.run('Nzc3ODY3ODEzOTcxOTUxNjY2.GmMazr.wGOB-1iTOOCYyuIdZJw1E6XiBQMeVPMU0-hWYg')

#install pyautogui and discord.py before running the bot.
#for more information contact- Krish#0003.
