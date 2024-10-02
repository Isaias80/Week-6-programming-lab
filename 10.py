import random

# Function to generate the quiz and check the answer
def math_quiz():
    # Generate two random numbers
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)

    # Display the problem to the user
    print(f"What is {num1} + {num2}?")
    
    # Input: the user's answer
    user_answer = int(input("Your answer: "))

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

def main():
    math_quiz()

main()
# FINAL OUTPUT FOR LABS:
# What is 186 + 435?
# Your answer: 621
# Congratulations! Your answer is correct.