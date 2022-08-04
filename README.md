# TCP_SUBSERVERS

A system that allows the user to search for a file in a remote database concurrently using multiple subservers for load balancing.

Used TCP sockets for connection and threading for asynchronous requests.

## How to run the project:
- Run initalize.py and specify the number of subservers you want. This will create a separate directory for each subserver and fill it with random files.
- First of all, run the main server, followed the sub servers.
- Run the client and provide a file name you want to search. If found, the details will be returned.

![system diagram](https://github.com/AhsanAAR/TCP_SUBSERVERS/blob/master/subservers_architecture.jpg)
