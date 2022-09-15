#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

initial_extensions = [
    'modules.sarasa'
]
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix=">",
    description="Botardo",
    intents=intents
)


@bot.event
async def on_message(message):
    """
    The code in this event is executed every time someone sends a message, with or without the prefix

    :param message: The message that was sent.
    """
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)


@bot.event
async def on_command_completion(context):
    """
    The code in this event is executed every time a normal command has been *successfully* executed
    :param context: The context of the command that has been executed.
    """
    full_command_name = context.command.qualified_name
    split = full_command_name.split(" ")
    executed_command = str(split[0])
    if context.guild is not None:
        print(
            f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})")
    else:
        print(f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs")


async def load_modules() -> None:
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"./modules"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"modules.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


asyncio.run(load_modules())
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
