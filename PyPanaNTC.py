#!/usr/bin/python
from pathlib import Path
from socket import SOCK_STREAM, socket, AF_INET
from json import load as jsonload

s = socket(AF_INET, SOCK_STREAM)


def send_commands(ip, command, port=1024):
    global s
    try:
        s.connect((ip, port))
        received = s.recv(1024)
        if(b'NTCONTROL 0\r' in received):
            print(f"Connected to {ip}:{port}")
        elif(b'NTCONTROL 1' in received):
            print(f"{ip} needs password! {received}")
        else:
            print(f"Connection: Strange! {received}")
    except Exception as e:
        print(f"Connection: Exception! {e}")
        # s.close()
        pass
    try:
        bitstream = bytes(f"00{command}\r", 'ascii')
        print(f"Sending {str(bitstream)}")
        s.sendall(bitstream)
    except Exception as e:
        print(f"Sending: Exception! {e}")
        pass
    try:
        data = s.recv(1024)
        print(f'Received {repr(data)}')
    except Exception as e:
        print(f"Receiving: Exception! {e}")
        pass


# send_commands('192.168.1.7', "OSH:3")
with Path("./NTCtrls.json").open('r', encoding='utf-8') as file:
    all_commands = jsonload(file)

# Power:
for i in all_commands['Power']:
    print(all_commands['Power'][i]['Info'])

send_commands('127.0.0.1', "OSH:3", 50007)
send_commands('127.0.0.1', all_commands['Power']['ON']['Command_new'], 50007)
s.close()
