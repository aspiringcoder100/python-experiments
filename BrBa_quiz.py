print("Hello and welcome to the Los Pollos Hermanos family! My name is Gustavo "
      "but you can call me Gus")

playing = input("Do you wish to play this game? ")

if playing.lower() != "yes":
    quit()

print("You wanna get nuts? Let's get nuts")

score = 0

answer1 = input("Which episode is the highest-rated on IMDB? ")
if answer1.lower() == "ozymandias":
    print("Correct!")
    score += 1
else:
    print("Incorrect. Try again")

answer2 = input("How many episodes are in Breaking Bad? ")
if answer2.lower() == "62":
    print("Correct!")
    score += 1
else:
    print("Incorrect. Try again")

answer3 = input("Who dies in the end of Br Ba Season 3? ")
if answer3.lower() == "gale":
    print("Correct!")
    score += 1
else:
    print("Incorrect. Try again")

answer4 = input("What is the name of the Season 4 finale? ")
if answer4.lower() == "face off":
    print("Correct!")
    score += 1
else:
    print("Incorrect. Try again")

answer5 = input("Did Season 5 have 13 episodes like the previous two seasons? ")
if answer5.lower() == "no":
    print("Correct! You have officially completed the quiz! ")
    score += 1
else:
    print("Incorrect. Try again")

print("You got " + str(score) + "/5 on this quiz!")