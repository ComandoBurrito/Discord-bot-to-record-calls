import discord
import os

from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        await message.channel.send(message.content)

client = MyClient()

load_dotenv()

TOKEN = os.getenv("TOKEN")

client.run(TOKEN)