import random
import os
import shutil

print("How many sub servers do you want: ")
no_of_servers = int(input())

for i in range(1, no_of_servers+1):
    os.mkdir(f"sub_server_{i}/") 

    for _ in range(10):
        r = random.randint(1000,9999)
        with open(f"sub_server_{i}/{r}", 'w') as f:
            f.write(str(hash(r)))
    
    shutil.copy("sub_server.py", f"sub_server_{i}/sub_server_{i}.py")
    