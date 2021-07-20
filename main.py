import json
import random
name=input("Enter your name")
print(name,":)Welcome to OLA Cabs","\U0001F600")
print("Your safety is our responsibility   you can belive")
print("Till your destination, we will make sure to be your best companion ")
print("your current location Halanayakahalli")
def Booking():
    Destination_place=["Huskur","Axis bank road","sai hanuman","Halnayakahalli","SaI baba mandir"]
    Drivers=[["nayak","sathish"],["vinod","mohan"],["ganni","akhila"],["Vinkya","sai kumar","srinu"],["umesh","Santhu"]]
    print("These are the places you can make an easy ride ")
    for i in Destination_place:
        print(i)
    limit=int(input("How many rides you can choose Here"))
    n=1
    dic={}
    books=int(input(" For Booking Click option :1 and for Cancling option:2 "))
    print("your currect location Halnayakahalli ")
    while n<=limit:
        select=input("enter your destination")
        i=0
        while i<len(Destination_place):
            if select==Destination_place[i]:
                j=0
                total=0
                while j<len(Drivers[i]):
                    a=random.choice(Drivers[j])
                    print("available drivers are there:",a)
                    j+=1
                select=input("enter any one rider")
                
                if books==1:
                    km=int(input("enter your kilometers"))
                    OTP=int(input("enter  your OTP"))
                    print(OTP,"\U0001F620")
                    fare=km*5
                    total+=fare
                else:
                    print("Canceling your ride")
                b=total
                dic[select]=b
                print(dic)
            i+=1
        n+=1
    with open("Rider_task.json","w+") as file:
            json.dump(dic,file,indent=3)
            M=json.dumps(dic)
            return M
Booking()