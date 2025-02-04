import os
import socket

os.system('cls')

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input("Enter the ipaddress: ")
port = int(input("Enter the port: "))

def portScanner():
    if sock.connect_ex((ip,port)):
        print(f"Port {port} is closed :(")
    else:
        print(f"Port {port} is open :)")

portScanner()