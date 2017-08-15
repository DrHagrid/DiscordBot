# -*- coding: utf-8 -*-
import asyncio as asyncio

import STATICS
import discord
from commands import cmd_ping, cmd_random, cmd_help, cmd_weather
from discord import Game, Embed

client = discord.Client()

commands = {

    "помощь": cmd_help,
    "пинг": cmd_ping,
    "рандом": cmd_random,
    "погода": cmd_weather

}

if STATICS.BANNED_CONTENT:
    with open(STATICS.BANNED_LIST_DIR) as file:
        ban_list = [row.strip() for row in file]
    print('A list with banned content has been uploaded')


# Проверка строки на содержание запрещённого контента
def check_for_banned_content(msg):
    for element in ban_list:
        if element in msg.lower():
            return True
    return False


@client.event
@asyncio.coroutine
def on_ready():
    print('Bot successfully launched')
    yield from client.change_presence(game=Game(name="бота"))


@client.event
@asyncio.coroutine
def on_message(message):
    # Если сообщение начинается с префикса команды и автор НЕ бот
    if (message.content.startswith(STATICS.PREFIX)) and (message.author.name != STATICS.BOT_NAME) and \
            not (check_for_banned_content(message.content)):
        cmd = message.content[len(STATICS.PREFIX):].split(' ')[0].lower()
        args = message.content.split(' ')[1:]
        if STATICS.PRINT_LOG:
            print('Cmd call ||| Author: {} | Channel: {} | Cmd: {} | Args: {}'.format(message.author, message.channel, cmd, args.__str__()))
        if commands.__contains__(cmd):
            yield from commands.get(cmd).ex(args, message, client, cmd)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description="Команды `%s` не существует" % cmd))
    # Удаление сообщений с запрещённым контентом
    if check_for_banned_content(message.content):
        yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description="Сообщение %s было удалено" % message.author.name))
        yield from client.delete_message(message)

print('Launch bot has started...')
client.run(STATICS.ACCESS_TOKEN)  # Запуск бота по токену
