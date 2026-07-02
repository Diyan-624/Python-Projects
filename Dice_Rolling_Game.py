# Write a program that simulates rolling a pair of dice. Each time the program runs, 
# it should randomly generate two numbers between 1 and 6 (inclusive), representing the result of each die
#  The program should then display the results and ask if the user would like to roll again.
import random
while True:
    option=input("Roll the dice (y/n): ").lower()
    if option=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    elif option=='n':
        print("Thanks For Playing")
        break
    else:
        print("Invalid Choice!")        

