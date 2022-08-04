import socket
import json
import pickle

def main():
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1009)
    s_tcp.connect(server_address)
    print(f"client created at {s_tcp.getsockname()}")

    print("Enter the name of file you want:")
    query = input()
    msg = json.dumps({"type": "client", "query": query})

    s_tcp.send(msg.encode())
    msg = s_tcp.recv(2000)

    print(pickle.loads(msg))

if __name__ == "__main__":
    main()
