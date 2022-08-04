from itertools import repeat
import json
import pickle
from typing import List
import socket
from multiprocessing.pool import ThreadPool
import threading


sub_servers_list: List[socket.socket] = []
SERVER_PORT = 1009

def query_subserver(subserver_conn: socket.socket, query: str):
    subserver_conn.send(query.encode())
    response_bytes = subserver_conn.recv(200)
    return pickle.loads(response_bytes)

def handle_query(client_socket: socket.socket, query: str, addr):
    pool = ThreadPool()
    results_list = pool.starmap(query_subserver, zip(sub_servers_list, repeat(query)))
    pool.close()

    filtered_list = list(filter(None, results_list))
    response = filtered_list if filtered_list else None

    client_socket.send(pickle.dumps(response))
    print(f"response {response} made to {addr}")

def main():
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_tcp.bind(("localhost", SERVER_PORT)) 
    print(f"Server started at {s_tcp.getsockname()}\n")
    s_tcp.listen()

    while True:
        conn, addr = s_tcp.accept()

        # all new connections will send a dictionary as the first message
        # the dictionary will have a 'type' field that will specify either client or subserver connection
        msg = conn.recv(200)
        msg = json.loads(msg)

        if msg["type"] == "sub_server":
            sub_servers_list.append(conn)
            print(f"sub_server connected {addr}")

        elif msg["type"] == "client":
            query = msg['query']
            print(f"{addr} requested for file {query}")

            thread = threading.Thread(target=handle_query, args=(conn, query, addr))
            thread.start()

if __name__ == "__main__":
    main()
