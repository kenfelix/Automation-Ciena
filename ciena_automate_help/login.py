from netmiko import ConnectHandler
from getpass import getpass
from animate import Loader
from time import sleep


def login():
    host = input("host: ")
    username = input("username: ")
    password = getpass()


    ciena = {
        'device_type': 'ciena_saos',
        'host': host,
        'username': username,
        'password': password,
        'port' : 22,          # optional, defaults to 22
    }

    try:
        net_connect = ConnectHandler(**ciena)
        loader = Loader("connecting to node......", "That was fast!", 0.05).start()
        if net_connect:
            loader.stop()
            print("connected to node")
    except Exception:
        print(Exception)

    return net_connect
    

if __name__ == "__main__":
    login()