from sshtunnel import open_tunnel
from time import sleep

SERVER_NAME = "SERVER_NAME"
USER_NAME = "USER_NAME"
PASSWORD = "PASSWORD"

with open_tunnel(
    (SERVER_NAME, 22),
    ssh_username=USER_NAME,
    ssh_password=PASSWORD,
    remote_bind_address=('127.0.0.1', 3306),
    local_bind_address=('127.0.0.1', 3306)
) as tunel:
    print("Local port: ", tunel.local_bind_port)
    print("press Ctrl-C for stopping")
    while True:
        sleep(1)

