import requests
import json


#write
def write():           
        a="http://indianiotcloud.com/update1.php?id=4RMVHUG81PHTM8YKIKT8&field1="
        b=input("message::-")
        a=a+b
        requests.get(a)
        print("----MESSAGE SENT----")
        read()

#read
def read():
        c=" http://indianiotcloud.com/retrieve.php?id=4RMVHUG81PHTM8YKIKT8"
        d=requests.get(c)
        e=d.json()
        f=e["result"][0]["field1"]
        print("---RECIVED MESSAGE---")
        print(f)
        write()
write()

