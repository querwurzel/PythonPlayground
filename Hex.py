#!/bin/python

__author__ = 'stefan'

import sys

def main():
    args = sys.argv[1:]

    # file hex mode
    if len(args) == 1:
        hex_file(args[0])
    # file re-hex mode
    elif len(args) == 3:
        mod_file(args[0], args[1], args[2])
    else:
        print("Mode of operation unsupported")

def hex_file(file):
    try:
        with open(file, "rb") as f:
            octets = f.read()

        block = 0
        for octet in octets:
            block += 1
            if block < 31:
                hex_octet(octet)
                print(' ', end='')
            else:
                hex_octet(octet)
                print()
                block = 0
    except IOError as e:
        print(e)

def hex_octet(octet):
    print("{0:02X}".format(octet), sep='', end='')

def mod_file(file, old, new):
    try:
        with open(file, "r+b") as f:
            data = f.read()
            data = data.replace(bytes.fromhex(old), bytes.fromhex(new))

            f.seek(0)
            f.write(data)
            f.close()
    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()
