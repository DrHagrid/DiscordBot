from random import randrange


def ex(args, message, client, cmd):
    if len(args) > 0:
        num = randrange(0, len(args))
        yield from client.send_message(message.channel, args[num])
