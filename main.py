import socket
import os
from dotenv import load_dotenv, dotenv_values, find_dotenv

load_dotenv(find_dotenv(".dev.env"))

HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Halla server!")
    data = s.recv(1024)
    print(f"Fekk data: {data!r}")