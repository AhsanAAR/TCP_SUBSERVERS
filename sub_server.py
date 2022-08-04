import threading
import socket
import json
import os
import pickle
from datetime import datetime

def handle_query(s: socket.socket, query: str):
    result = None
    if query in os.listdir():
        date_of_creation = datetime.fromtimestamp(os.path.getctime(query))
        file_path = os.getcwd() + "\\" + query
        file_size = os.path.getsize(query)
        result = {
            "date_of_creation": date_of_creation,
            "file_path": file_path,
            "file_size": file_size,
        }

    s.send(pickle.dumps(result))
    print(f"{result} result sent for query {query}")

def main():
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1009)
    s_tcp.connect(server_address) 

    print(f"subserver created at {s_tcp.getsockname()}")

    msg = json.dumps({"type": "sub_server"})
    s_tcp.send(msg.encode())

    while True:
        query = s_tcp.recv(200)
        query = query.decode()

        t = threading.Thread(target=handle_query, args=(query, ))
        t.start()

if __name__ == "__main__":
    main()