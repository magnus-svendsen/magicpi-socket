#THIS FILE IS ONLY USED TO TEST THE CLIENT
import socket
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(".dev.env"))

HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)