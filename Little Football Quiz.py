print("Welcome to ny computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, Game on! :)")
score = 0

answer = input("Who is the premier league's all time top goal scorer? ")
if answer.lower() == "alan shearer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the highest goal scoring midfielder in the premier league? ")
if answer.lower() == "frank lampard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many champions league titles have Chelsea won? ")
if answer.lower() == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is Henry better than Drogba? ")
if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")


    