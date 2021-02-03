import random

def GuessTheNumber():
    TargetNumber=random.randint(1,100)
    UserNumber=0
    maxNumber=100
    minNumber=1
    Guesses=0
    print("I am thinking  of  the  number between 1 and 100")

    while UserNumber != TargetNumber :
     try:
        UserNumber=int(input("What number am i thinking of?"))
     except:
        print("isn't a number")
        continue
        
     Guesses=Guesses+1
     if UserNumber>maxNumber or UserNumber<minNumber:
         print("You should type  a  number between 1 and 100")
         continue

     if UserNumber<TargetNumber and UserNumber>=minNumber:
        print("My  number is higher,than",UserNumber)
        print()
     if UserNumber>TargetNumber and UserNumber<=maxNumber:
        print("My  number is lower,than",UserNumber)
        print()

     if  UserNumber==TargetNumber:
        print()
        print("Yep.It is",TargetNumber,"in",Guesses,"guesses")
    else:
        PlayAgain=input("1  more  game?(Yes/No)")
        if PlayAgain.lower()=="yes":
            print()
            GuessTheNumber()
        else:
            exit()


GuessTheNumber()
