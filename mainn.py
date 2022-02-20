#Mass Dm By Szordrin6870
import discord

client = discord.Client()
Token = input("gt") 
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send("discord.gg/fr1ends")#ADD HERE THAT YOU WANNA SEND TO YOUR FRIENDS
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run(token, bot=False)#ADD YOUR TOKEN HERE NOT ANY BOT TOKEN
