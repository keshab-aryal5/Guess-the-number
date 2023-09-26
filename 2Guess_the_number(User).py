import random
def check_the_guess(x):
    global random_number,count
    count+=1
    if random_number==x:
        mesg=f"Congratulations!!! you guessed it right at {count} atttempts"
        print(mesg.center(100))
        return True
    else:
        if(x > random_number):
            print(f"{x} is greater than the actual number, make a try again. ")
        else:
            print(f"{x} is smaller than the acutal number, make a try again. ")
            
        return False
    
    
while True:
    a=int(input("Enter the least number you want to guess. "))
    b=int(input("Enter the maximum number you want to guess. "))
    random_number=random.randint(a,b)
    count=0
    while True:
        guess=int(input("Guess the number "))
        result=check_the_guess(guess)
        if result:
            break
        else:
            continue
        
    next=int(input("Do you want to play again? \n1----------->Yes \n0----------->No\n"))
    if not next:
        break