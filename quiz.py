print("Welcome to quiz!")

playing = input("Would you like to play? ")

if playing.lower().strip() != "yes":
    quit()

print("Here we go!!!")
score = 0

answer = input('What does GPU stand for? ')
if answer.lower().strip() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does RAM stand for? ')
if answer.lower().strip() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does PSU stand for? ')
if answer.lower().strip() == "power supply unit":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')

print("Total score: " + str(score) + ".")
print("total score: " + str((score / 3) * 100) + "%.")