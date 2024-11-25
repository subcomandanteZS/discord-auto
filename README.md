
To modify the script so that the bot sends messages every 2 hours instead of every few seconds, you can simply change the INTERVAL to 2 hours in seconds (which is 7200 seconds). The bot will send a message every 2 hours and run for a total of 24 hours.

Here is the updated script:

Updated Python Script (Send Messages Every 2 Hours):
python
Copy code
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
Key Changes:
Interval of 2 Hours:
The INTERVAL variable is set to 7200 seconds (2 hours).
Duration of 24 Hours:
The bot will run for 24 hours (TOTAL_DURATION = 86400 seconds).
How the Bot Works:
Every 2 Hours: The bot sends a message (MESSAGE) to the specified channel every 2 hours.
Stops After 24 Hours: After 24 hours, the bot stops and disconnects from the server.
Steps to Run:
Set the Token: Replace 'YOUR_BOT_API_TOKEN' with your actual Discord bot token.
Set the Channel ID: Replace CHANNEL_ID = 123456789012345678 with the target channel's ID.
Run the Script:
Save the script in a .py file (e.g., auto_chat_bot.py).
Open a terminal and run the script with:
bash
Copy code
python auto_chat_bot.py
How to Calculate the Interval for Different Durations:
1 hour = 3600 seconds.
2 hours = 7200 seconds (used in the script).
3 hours = 10,800 seconds.
4 hours = 14,400 seconds.
