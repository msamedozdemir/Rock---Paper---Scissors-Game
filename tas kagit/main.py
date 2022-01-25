import random

your_score = 0
computers_score =0

a = ["rock", "paper", "scissors"]

while True:

    your_chose = input("pls type rock, paper or scissors ").lower()
    comp_chose = random.choice(a)
    if your_chose not in a:
        print("pls type valid chose")
    if (your_chose == "rock" and comp_chose == "scissors") or (your_chose == "paper" and comp_chose == "rock") or (your_chose == "scissors" and comp_chose == "paper"):
        print("computers chose was: "+comp_chose)
        your_score +=1
        print("goood! you win\n your score: " + str(your_score) )
    elif (comp_chose == "rock" and your_chose == "scissors") or (comp_chose == "paper" and your_chose == "rock") or (comp_chose == "scissors" and your_chose == "paper"):
        print("computers chose was: " + comp_chose)
        computers_score +=1
        print("Hahahaa! you lose\n computers score: " + str(computers_score))
    elif your_chose == comp_chose:
        print("computers chose was: " + comp_chose)
        print("again!!")
    else:
        print("something went wrong")

    if (your_score == 5) or (computers_score == 5):
        print("end of the game")
        break

