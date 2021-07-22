import random
import json
name=input("Enter your name")
print(name,"=:)Welcome to OLA Cabs","\U0001F600")
print("Your safety is our responsibility   you can belive")
print("Till your destination, we will make sure to be your best companion ")
def Booking():
    Destination_place=["Huskur","Axis bank road","sai hanuman","Halnayakahalli","SaI baba mandir"]
    Drivers=[["nayak","sathish"],["vinod","mohan"],["ganni","akhila"],["Vinkya","sai kumar","srinu"],["umesh","Santhu"]]
    limit=int(input("How many rides you want you can choose"))
    index=1
    dic={}
    Book_cab=int(input("for Booking Click on  option :)1"))
    print("your current location Halanayakahalli")
    for i in Destination_place:
        print(i)
    print("These are the places you can make an easy ride!")
    while index<=limit:
        select=input("enter your destination")
        i=0
        while i<len(Destination_place):
            if select==Destination_place[i]:
                j=0
                while j<len(Drivers[i]):
                    a=random.choice(Drivers[j])
                    print("available drivers are here:",a)
                    j+=1
                choose=input("enter any one rider")
                total=0
                if Book_cab==1:
                    kil=int(input("enter your kilometers"))
                    Dis=kil*5
                    total+=Dis
                X=total
                dic[choose]=X
                print(dic)
            i+=1
        index+=1
    Rate_number=int(input("How was your ride rate by giving us numbers upto 5"))
    if Rate_number<=1:
        print("Give us Feedback")
    elif Rate_number<=2:
        print("you need work good")
    elif Rate_number<=3:
        print("You need to work more on safety")
    elif Rate_number<=4:
        print(" It was good and just focus on journey ")
    elif Rate_number<=5:
        print("It was good ride Thankyou ")
    with open("Total.json","w+")as file:
        json.dump(dic,file,indent=2)
        s=json.dumps(dic)
        return s
Booking()
def Ride():
    while True:
        again=input("Do you want to cancle your cab press y for yes and n for no") 
        if again=="y":
            print("Thank you For riding with us")
            break
        else:
             Booking()
Ride()