"""
Create a tkinter app in Python 3.10 that allows you to connect to the web to chat.
"""


import socket
from tkinter import *

class Config:
    port = 58489  # define port for this chat
    host = '196.248.34.72'
    ip = socket.gethostbyname(host)
    buffer_size = 4096  # set buffer size that server and client use
    messages = []
    subs = []


Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_object = Socket.connect((Config.ip, Config.port))


class Client:
    def __init__(self, master):
        """
        Define frames for connecting, disconnecting, chatting, and subbing.
        """
        self.master = master

        one = Frame(master)
        one.pack()

        two = Frame(master)
        two.pack()

        three = Frame(master)
        three.pack()

        four = Frame(master)
        four.pack()

        self.l1 = Label(one, text='Server'.format(Config.host, Config.port))
        self.l1.pack()

        self.display_subs = Text(three, height=10)
        self.display_subs.pack()

        self.display_chat = Text(three, height=8)
        self.display_chat.pack()

        self.e1 = Entry(two)
        self.e1.bind('<Return>', lambda x: self.sub())
        self.e1.pack(side=LEFT)

        self.b1 = Button(two, text='Sub', command=lambda: self.sub())
        self.b1.pack(side=LEFT)

        self.e2 = Entry(one)
        self.e2.bind('<Return>', lambda x: self.send())
        self.e2.pack(side=LEFT)

        self.b2 = Button(one, text='Send', command=lambda: self.send())
        self.b2.pack(side=LEFT)

        self.b4 = Button(one, text='Fetch', command=lambda: self.fetch_chat())
        self.b4.pack(side=LEFT)

        self.b3 = Button(one, text='Disconnect', command=lambda: self.leave())
        self.b3.pack(side=LEFT)

        self.message_len = Label(four, justify=LEFT)
        self.message_len.pack()
        self.message_len.configure(text='You have {} messages!'.format(len(Config.messages)))

        self.subbed_len = Label(two, justify=LEFT)
        self.subbed_len.pack()
        self.subbed_len.configure(text='You have {} subs!'.format(len(Config.subs)))

    def sub(self) -> None:
        """
        Get input from a user in label two and sub using said input.
        """
        get = self.e1.get()
        if get != '':
            command = 'sub'.encode('utf-8')
            sub = get.encode('utf-8')
            Socket.send(command + b'\n' + sub)
            self.e1.delete(0, END)
            Config.subs.append(get)
            self.display_subs.insert(END, '\n{}'.format(get))
            self.subbed_len.configure(text='You have {} subs!'.format(len(Config.subs)))

        return 'null'

    def send(self) -> None:
        """
        Send input in text provided on label one.
        """
        get = self.e2.get()
        command = 'sendall'.encode('utf-8')
        message = get.encode('utf-8')
        if len(get) <= 400:  # prevents user from sending more than 400 characters
            Socket.send(command + b'\n' + message)
            self.e2.delete(0, END)
            Config.messages.append(message)
            self.message_len.configure(text='You have {} messages!'.format(len(Config.messages)))

        return 'null'

    def leave(self) -> None:
        """
        Closes the socket.
        """
        Socket.close()
        master.destroy()

    def fetch_chat(self) -> None:
        """
        Fetch messages not yet posted to server.
        """
        data = Socket.recv(Config.buffer_size)
        if data:  # check for empty data
            content = data.decode('utf-8')
            if content == 'null':
                print('No match found')
                return 'null'
            else:
                responses = content.split('\n')
                responses.reverse()
                breakpoint()
            if Config.messages[-1] != data.decode('utf-8'):
                # self.display_chat.insert(END, '\r' + data.decode('utf-8'))
                self.message_len.configure(text='You have {} messages!'.format(len(Config.messages)))


if __name__ == '__main__':
    master = Tk()
    master.geometry("500x500")
    app = Client(master)
    master.mainloop()