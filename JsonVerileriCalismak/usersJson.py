

import  os
import json

with  open("users.txt","r") as users: # dosya açma işleminin farklı bir versiyonu burada açılan dosya iş bittikten sonra otomatik kapanır.

    data = json.load(users)
    for i in range(5):
        print(data[i]["name"])
        print(data[i]["id"])
        print(data[i]["address"]["street"])
        print(data[i]["address"]["geo"]["lat"])
        print("***********************************************")

