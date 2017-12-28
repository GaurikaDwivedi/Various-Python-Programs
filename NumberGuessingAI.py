range = int (input("What is the maximum range, 1 to ___?"))

theMax = range
theMin = range-range
guess = (theMax + theMin) // 2

computerGuessing= True
while computerGuessing:
    print ("Is it " + str(guess) + "?")    
    choice = input("Tell me too high with >, too low with <, or y if I got it")
        
    if choice == '>':
        theMax=guess
        guess = (theMax + theMin) // 2

    elif choice == '<':
        theMin=guess +1
        guess = (theMax + theMin) // 2

    if choice =='y':
        computerGuessing = False
print ('Your number is ' + str(guess) + ".")
