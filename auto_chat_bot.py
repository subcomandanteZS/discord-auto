import discord
import asyncio
import time

# Replace with your bot's token
TOKEN = 'YOUR_BOT_API_TOKEN'

# Channel ID where the bot will send messages
CHANNEL_ID = 123456789012345678  # Replace with your channel ID (must be an integer)

# Set the total run time in seconds for 24 hours (24 hours = 86400 seconds)
TOTAL_DURATION = 86400  # 24 hours in seconds

# Message to send repeatedly
MESSAGE = "Hello! This is an automated message."

# Interval in seconds between each message (2 hours = 7200 seconds)
INTERVAL = 7200  # Send message every 2 hours (2 hours = 7200 seconds)

class AutoChatBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

        # Get the channel by its ID
        channel = self.get_channel(CHANNEL_ID)

        # Check if the bot is in the correct channel
        if channel is None:
            print("Invalid channel ID.")
            return

        start_time = time.time()

        # Send messages at intervals for 24 hours
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            if elapsed_time >= TOTAL_DURATION:
                print(f"24 hours reached. Bot will stop chatting.")
                break
            
            # Send the message to the channel
            await channel.send(MESSAGE)
            print(f"Sent message: {MESSAGE}")

            # Wait for the interval before sending the next message
            await asyncio.sleep(INTERVAL)

        # Disconnect from Discord after 24 hours
        await self.close()

# Run the bot
intents = discord.Intents.default()
client = AutoChatBot(intents=intents)
client.run(TOKEN)
