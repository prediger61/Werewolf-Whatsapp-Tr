import pywhatkit
import random
from roles import roleList
import datetime as time
x = time.datetime.now()
timeList= x.strftime("%X").split(":")#21:30:00
sendHour = int(timeList[0])
sendMinute = int(timeList[1])+1 #for send 1 minutes later

numberList = ["+90xxxxxxxxxx","+90xxxxxxxxxx","+90xxxxxxxxxx",
              "+90xxxxxxxxxx","+90xxxxxxxxxx","+90xxxxxxxxxx",
              "+90xxxxxxxxxx","+90xxxxxxxxxx","+90xxxxxxxxxx"]

PlayerList=[[],[],[],[],[],[],[],[],[],[],[],[],[]]

for gamecount in range(3):
    random.shuffle(roleList)
    for _ in range(len(roleList)):
        PlayerList[_].append(roleList[_])

for player in range(len(numberList)):

    pywhatkit.sendwhatmsg(numberList[player],
                          "Senin 1. Oyundaki Rolün "+PlayerList[player][0]+
                          "Senin 2. Oyundaki Rolün "+PlayerList[player][1]+
                          "Senin 3. Oyundaki Rolün "+PlayerList[player][2], sendHour, sendMinute,15 ,True,2)#pywhatkit.sendwhatmsg(phonenumber, message as a string , hour , minute)
    sendMinute += 1 # to send next player 1 minutes later.