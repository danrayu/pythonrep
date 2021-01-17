import random


def GuessTheNumber():
    TargetNumber = 1  # random.randint(1, 100)
    UserNumber = 0
    Guesses = 0
    # print("I am thinking  of  the  number between 1 and 100")
    lang = 0

    language = input(("select your language (ru/eng)  "))
    if (language == "ru"):
        lang = 11
        print("Вы выбрали русский  язык.")

    elif (language == "eng"):
        print("You  selected english language.")
        lang = 12  # eng
    elif (language != "eng" and language != "ru"):
        print("Select eng or ru")
        GuessTheNumber()
        #lang = 0  # none
    while UserNumber != TargetNumber:

        if (lang == 11):
            UserNumber = int(input("О каком числе я думаю?  "))  # ru
        if (lang == 12):
            UserNumber = int(input("What number  am i  thinking of?  "))  # eng

        Guesses = Guesses + 1

        if UserNumber > 100 or UserNumber < 1 and lang == 11:
            print("Ведите число от 1  до 100")

        if UserNumber < TargetNumber and UserNumber >= 1 and lang == 11:  # ru
            print("Мое число  выше,чем", UserNumber)
            print()
        if UserNumber > TargetNumber and UserNumber <= 100 and lang == 11:  # ru
            print("Мое число ниже,чем", UserNumber)
            print()
        if UserNumber > TargetNumber and UserNumber <= 100 and lang == 12:  # eng
            print("My  number is lower,than", UserNumber)
            print()
        if UserNumber < TargetNumber and UserNumber >= 1 and lang == 12:  # eng
            print("My  number is higher,than", UserNumber)
            print()

        # if UserNumber == TargetNumber and lang == 12:
        #     print()
        #     print("Yep.It is", TargetNumber, "in", Guesses, "guesses")
        #     PlayAgain = input("1 more  game? Yes/No")
        #     if PlayAgain.lower() == "Yes":
        #         print()
        #         GuessTheNumber()
        #     else:
        #         exit()
        if UserNumber == TargetNumber and lang == 11: #ru
            print()
            print("Да.Это число:", TargetNumber, "Вы отгадали  его за", Guesses, "попытки")
            # PlayAgain = input("Сыграем еще раз?  Да/Нет")
        if UserNumber == TargetNumber and lang == 12: #eng
            print()
            print("Yep.It is number:", TargetNumber, "You  got it in", Guesses, "guesses")
    else:
        if(lang==12): #eng
         PlayAgain = input("1  more  game?(Yes/No)")
         if PlayAgain.lower() == "yes":
            print()
            GuessTheNumber()
         else:
            exit()
        if (lang == 11):  # ru
                PlayAgain = input("Еще одну игру? Да/Нет")
                if PlayAgain.lower() == "да":
                    print()
                    GuessTheNumber()
                # if PlayAgain.lower() != "да" and PlayAgain.lower() != "нет":
                #     print("Пожалуйста напишите Да или Нет")
                #     PlayAgain = input("Еще одну игру? Да/Нет")
                else:
                    exit()




# print("3")
GuessTheNumber()
