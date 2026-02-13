import discord # pyright: ignore[reportMissingImports]
from discord.ext import commands # pyright: ignore[reportMissingImports]

# Set up the bot's intents (permissions)
intents = discord.Intents.default()
intents.messages = True  # Ensure the bot can read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Store sent message IDs to prevent loops
sent_messages = {}

# Replace with actual channel IDs
CHANNEL_1_ID = 893588257948983359  # Server A, Channel 1 ID
CHANNEL_2_ID = 1365070296440115351  # Server B, Channel 2 ID

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent loops
    if message.author == bot.user:
        return

    # Check if the message has been forwarded already
    if message.id in sent_messages:
        return

    # Handle messages from Channel 1 (Server A) and forward to Channel 2 (Server B)
    if message.channel.id == CHANNEL_1_ID:
        target_channel = bot.get_channel(CHANNEL_2_ID)
        await target_channel.send(f"Forwarded from Server A: {message.content}")
        sent_messages[message.id] = "Server A to Server B"

    # Handle messages from Channel 2 (Server B) and forward to Channel 1 (Server A)
    elif message.channel.id == CHANNEL_2_ID:
        target_channel = bot.get_channel(CHANNEL_1_ID)
        await target_channel.send(f"Forwarded from Server B: {message.content}")
        sent_messages[message.id] = "Server B to Server A"

    # Always process other commands
    await bot.process_commands(message)

# Run the bot with your token
bot.run('MTQ3MTk5MzgyNzg5MDk1ODM2Ng.G-dVQ4.CMQoa_jo1k5utjnP0JvJ9m3Ij7c98s_U0qMLto')