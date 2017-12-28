import random
rand = random.randint(1,1000)
# print(rand) #For testing purposes

response = input("Would you like to play guess the number? Y/N")
 
if response =="n":
    quit()
while response == "y":
    num = int (input("enter a number between 1 and 1000: "))
    while response != rand: 
        if num>rand:
            #print(rand) #For testing purposes
            print("Wrong, Go lower!")
            num = int(input("enter a number between 1 and 1000: "))
        elif num<rand:
            #print(rand) #For testing purposes
            print("Wrong, Go higher!")
            num = int(input("enter a number between 1 and 1000: "))
        elif num == rand:
            print("You are right!")
            response = input("Would you like to play again? Y/N")
            if response =="n":
                quit()
            if response =="y":
                rand = random.randint(1,1000)
            break
