# NQueensA_DBK.py
import random
from itertools import permutations

NQ_solutions = 0 
NQ_conflicts = 0
iterations = 0 

N = int (input("Input an 'N' value (must be larger than 3): ")) 

while (NQ_solutions is 0):
    cols = [random.randint(0,N-1) for cols in range(N)] # Generate a candidate NQ solution [random.randint(0,n-1) for x in range(n)]
    for combo in permutations(cols): #Row conflicts
        if (NQ_solutions is 0): 
            if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)): # Diagonal conflicts
                NQ_solutions += 1 # How many solutions?
                iterations += 1 # How many iterations?
                print('Solution '+str(NQ_solutions)+': '+str(combo)+'\n')
                print("\n".join(' - ' * i + ' Q ' + ' - ' * (N-i-1) for i in combo) + "\n\n\n\n") 
            else:
                NQ_conflicts += 1 # How many conflicts?
                iterations += 1 # How many iterations?

if (N <= 3):
    print("Your number needs to be greater than 3 to make a reasonable board size")

print("The # of solutions was: ", NQ_solutions) 
print("The # of conflicts was: ", NQ_conflicts) 
print("The # of iterations was: ", iterations) 
