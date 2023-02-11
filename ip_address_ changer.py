import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet OTO IP")
print("""

automatic ip address change tool, enter value in seconds >
""")

ip_time =int( input("enter the ip change time(second) : "))

os.system("anonsurf start")
os.system("clear")
print("new ip address :")
print("-----------------------------")
os.system("curl icanhazip.com")
print("-----------------------------")

while True:
        time.sleep(ip_time)
        os.system("anonsurf restart")
        os.system("clear")
        print("new ıp Addres :")
        print("-----------------------------")
        os.system("curl icanhazip.com")
        print("-----------------------------")
