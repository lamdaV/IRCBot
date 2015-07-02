"""
A conceptual bot that is to be implented in a desired IRC server and channel.

Created on Jun 27, 2015.
Written by: lamd.
"""
import socket
import datetime as dt  # Could be used to determine which assignment to display.

def main():
    """ 
        The main function of the IRCbot.
    """
    # Constants.
    global IRC_SOCKET
    global SERVER
    global PORT
    global CHANNEL
    global NICKNAME
    global RESPONSES

    # DataList location constants.
    SERVER_DATA = 0
    PORT_DATA = 1
    CHANNEL_DATA = 2
    NICKNAME_DATA = 3
    HINT_DATA = 4

    # Logging.
    verbose = True

    # Obtain data.
    file = open("data.txt")
    dataList = file.read().split("\n")
    file.close()

    # Update on use.
    IRC_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER = dataList[SERVER_DATA]
    PORT = int(dataList[PORT_DATA])
    CHANNEL = dataList[CHANNEL_DATA]
    NICKNAME = dataList[NICKNAME_DATA]

    # Add commands here.
    RESPONSES = {'!help' : 'The available commands are "!help", "!assignments", and "!hint"',
                 '!assignments' : 'Assignments can be found here: https://www.rose-hulman.edu/class/csse/csse120/201540/',
                 '!hint' : dataList[HINT_DATA]};

    connect()

    # Main loop.
    while True:
        ircMessage = IRC_SOCKET.recv(2048).decode()
        ircMessage = ircMessage.strip("\n\r")

        file = open("data.txt")
        dataList = file.read().split("\n")
        file.close()
        updateHint = {'!hint' : dataList[HINT_DATA]}
        RESPONSES.update(updateHint)

        if (verbose):
            print(ircMessage)

        if (ircMessage.find(":Hello " + NICKNAME) != -1):
            hello()

        if (ircMessage.find("PING :") != -1):
            ping()

        if (ircMessage.find("!") != -1):
            respondant = ircMessage.split("!")[0][1:]
            commands(respondant, ircMessage)

def connect():
    """
        Connects the bot to the desired channel.
    """
    IRC_SOCKET.connect((SERVER, PORT))

    userMessage = "USER {0} {1} {2} : This is a test bot!\r\n".format(NICKNAME, NICKNAME, NICKNAME)
    IRC_SOCKET.send(userMessage.encode())

    nickMessage = "NICK {0}\r\n".format(NICKNAME)
    IRC_SOCKET.send(nickMessage.encode())

    joinMessage = "JOIN {0}\r\n".format(CHANNEL)
    IRC_SOCKET.send(joinMessage.encode())

    testMessage = "PRIVMSG {0} :Hello. Please type '!help' for more commands.\r\n".format(CHANNEL)
    IRC_SOCKET.send(testMessage.encode())

def ping():
    """
        Responds to server ping when requested.
    """
    pingMessage = "PONG :Pong\r\n"
    IRC_SOCKET.send(pingMessage.encode())

def sendMessage(message):
    """
        Send messages directly to the channel.
    """
    decodedMessage = "PRIVMSG {0} :{1}\r\n".format(CHANNEL, message)
    IRC_SOCKET.send(decodedMessage.encode())

def hello():
    """
        A test function that will respond if a user enters "Hello <BotName>."
    """
    helloMessage = "PRIVMSG {0} :Hello!\r\n".format(CHANNEL)
    IRC_SOCKET.send(helloMessage.encode())

def commands(respondant, ircMessage):
    """
        A function that will respond to commands issued by members of the channel. 
        It will call the appropriate function.
    """
    for key in RESPONSES:
        if (ircMessage.find(key) != -1):
            returnMessage = "PRIVMSG {0} :{1}: {2}\r\n".format(CHANNEL, respondant, RESPONSES[key])
            IRC_SOCKET.send(returnMessage.encode())

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
