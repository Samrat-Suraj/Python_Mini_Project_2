import random

guess= int(input("Enter Number to Guess-Number \n"))
random=random.randint(1,10)
attemt=0

while(True):
    if guess==random:
        print("You Win !")
        print(f"Total attemp is : {attemt}")
        break
    if guess=="quit":
        print("You Loss Game quiting .....")
        break
    elif guess>random:
        guess=int(input("Your Guess is to large Plese Enter lesser "))
        attemt +=1

    elif guess<random:
        guess=int(input("Your Guess To Less please Enter large number "))
        attemt +=1
    else:
        guess=input("Enter Please Enter Number only")
        break