import discord
client = discord.Client()
keywords = ["krish", "help", "pyautogui", "hello", "hi"]


@client.event
async def on_message(message):
      for i in range(len(keywords)):
          if keywords[i] in message.content:
              for i in range(1000):
                  await message.channel.send("type anything u want to spam ")

client.run('bot token')

#install pyautogui and discord.py before running the bot.
#for more information contact- Krish#0003.
