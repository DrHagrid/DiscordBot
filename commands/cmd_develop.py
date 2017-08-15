

def ex(args, message, client, cmd):
    global msg
    if args[0] == 'channel_info':
        msg = """Name: {}
        ID: {}
        Server: {}
        Topic: {}
        Private: {}
        Position: {}
        Created: {}
        """.format(message.channel.name, message.channel.id, message.channel.server, message.channel.topic,
                   message.channel.is_private, message.channel.position, message.channel.created_at)
    yield from client.send_message(message.channel, msg)
