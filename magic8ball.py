import random
import time
def start():
    answer = random.choice(
        ["Yes.", "Without a doubt.", "It is recommended.", "Extremely agree.", "Perhaps.", "Extremely Recommended.",
         "No.", "Never.", "I do not recommend it.", "Extremely disagree.", "You should not consider doing that."])
    input("What would you like to ask the magic 8 ball? ")
    print("Shaking the magic 8 ball...")
    time.sleep(1)
    print(answer)
    question = input("Would you like to use the magic 8 ball again? (y/n) ")
    if question == "y":
        start()
    elif question == "n":
        print("Thank you for using the magic 8 ball.")
        time.sleep(0.5)
        exit()

start()
