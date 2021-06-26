import random

min_bound = int(input("Enter the min number of range :-"))
max_bound= int(input("Enter the max number of range:-"))

m_no = random.randint(min_bound,max_bound)
print("You have 4 lives to predict the number")
live = 0
while live < 4:
    g_no = int(input("Enter your Guess :-"))
    if live == 3 :
        print("Oops! All you chances are finished. Better luck next time!")
        break
    else :
        if g_no == m_no:
            print( "Yeah! You identified the number" )
            break
        elif g_no < m_no:
            print( "Please try again! The number you guessed is too small")
            live += 1
        elif g_no > m_no:
            print( "Please try again! The number you guessed is too high")
            live += 1

