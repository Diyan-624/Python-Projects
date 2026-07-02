#Random num 1 to 100
#if wrong please enter valid number
#if computer random number is higher should print too high
#if computer random number is lower should print too low
#after guessing number print congratulations you guessed number
import random   
rand=random.randint(1,100)
while True:
 try:

    choice=int(input("Enter The Number: "))
    if choice ==rand:
        print("Congratulation You Guessed THe Number")
        
    elif choice>rand:
        print("Too high")
    elif choice<rand:
        print("Too low")
    else:
        print("Please Enter Valid Input")
        break 
 except ValueError:
    print('Please Enter a valid number')