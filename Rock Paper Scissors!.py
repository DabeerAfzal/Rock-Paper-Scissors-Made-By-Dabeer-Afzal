import random

greetings_demo = ["Hello Dear Sir!", "Hello There!", "Hi There!"]
greetings = random.choice(greetings_demo)
print(f"{greetings} Welcome To Rock, Paper And Scissors! Please Enter You're Choice: \n")

while True:
    answer_of_bot = random.choice (["Rock", "Paper", "Scissors"])
    answer_of_human = str(input())
    print(f"You're Answer: {answer_of_human}\n")

# Bot's All Possible Answers

    if "Rock" in answer_of_human:
        print(f"Bot's Answer: {answer_of_bot}\n")

    elif "Paper" in answer_of_human:
        print(f"Bot's Answer: {answer_of_bot}\n")

    elif "Scissors" in answer_of_human:
        print(f"Bot's Answer: {answer_of_bot}\n")

# Winning Techniques For Us

    if "Paper" in answer_of_human and "Rock" in answer_of_bot:
        print("You Won!\n")
    
    if "Scissors" in answer_of_human and "Paper" in answer_of_bot:
        print("You've Won!\n")
    
    if "Rock" in answer_of_human and "Scissors" in answer_of_bot:
        print("You've Won!\n")
    
    elif answer_of_human == answer_of_bot:
        print("It's A Tie!\n")

# Winning Techniques For The Bot   
 
    if "Paper" in answer_of_bot and "Rock" in answer_of_human:
        print("You've Lost!\n")
    
    if "Scissors" in answer_of_bot and "Paper" in answer_of_human:
        print("You've Lost!\n")
    
    if "Rock" in answer_of_bot and "Scissors" in answer_of_human:
        print("You've Lost!\n")
