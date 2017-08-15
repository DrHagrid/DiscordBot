

def ex(args, message, client, cmd):
    yield from client.send_message(message.channel, 'Понг!')
