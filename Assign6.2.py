print("         ADDITION TRAINER")

name = input("Name: ")
nickname = input ("Nickname: ")

print(f"    Thank You {nickname} for using Addition Trainer. Have fun and learn the Addition!")

import random

score = 0

for x in range(10):
    firstnum = random.randint(0,99)
    secondnum = random.randint(0,99)
    print(f"Add {firstnum} + {secondnum}")
    answer = int(input("    Enter your answer: "))
    answerf = firstnum + secondnum

    if answer == answerf:
        print("    CORRECT")
        score = score + 1
    else :
        print(f"    INCORRECT, The answer is {answerf}")

print(f"You obtained a score of {score}/10.")

if score > 6:
    print("    Job well done. Keep it up.")
else:
    print("    Better luck next time.")

print(f"Hopefully you learned something {name}. Thank you for using Addition Trainer.")
