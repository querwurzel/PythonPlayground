#!/bin/python

import socket
from os import linesep

def loop():
    try:
        s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_in.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_in.bind(("localhost", 4711))
        s_in.listen(5)
        print("Starting server .. up!")

        while True:
            #(s_out, addr) = s_in.accept()
            tup = s_in.accept()
            s_out = tup[0]
            addr  = tup[1]
            if s_out:
                greeting = "Hi & Bye, {0}!{1}".format(addr[0], linesep)
                print("{0}:{1}".format(addr[0], addr[1]), "has connected.")
                print(greeting, end='')
                s_out.send(greeting.encode("utf-8"))
                s_out.close()
    except OSError as e:
        print("Port currently in use.")
        print(e)
    except KeyboardInterrupt as e:
        print("Shutting server .. down!")
        print(e)
    finally:
        s_in.close()

if __name__ == "__main__":
    loop()
