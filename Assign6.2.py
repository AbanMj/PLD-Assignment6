

import random

score = 0

for x in range(10):
    firstnum = random.randint(0,99)
    secondnum = random.randint(0,99)
    print(f"Add {firstnum} + {secondnum}")
    answer = int(input("Enter your answer: "))
    answerf = firstnum + secondnum

    if answer == answerf:
        print("CORRECT")
        score = score + 1
    else :
        print(f"INCORRECT, The answer is {answerf}")

print(f"Your score is {score}/10.")

