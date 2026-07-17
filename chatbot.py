from datetime import datetime
import random

# ============================
# RULE-BASED AI CHATBOT
# Created by: Christoph T Tuahuku
# ============================


print("=" * 55)
print("             🤖 WELCOME TO RULEBOT AI")
print("=" * 55)

name = input("Bot: Hello! What is your name? ")

print(f"\nBot: Nice to meet you, {name}! 😊")
print("Bot: I am RuleBot AI, a simple rule-based chatbot.")
print("Bot: Please choose an option below.\n")


message_count = 0


jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Java developers wear glasses? Because they don't C#!",
    "Debugging is like being a detective in a crime movie where you are also the criminal.",
    "There are only 10 types of people: those who understand binary and those who don't."
]


quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Never stop learning because life never stops teaching.",
    "Believe in yourself and all that you are.",
    "Every expert was once a beginner."
]


def show_menu():
    print("""
================ MENU ================

1. Say hello
2. How are you?
3. What is your name?
4. Who created you?
5. Current time
6. Current date
7. Date and time
8. Tell me a joke
9. Give motivation
10. Calculator
11. What is AI?
12. Best programming language
13. Message count
14. Exit

======================================
""")


show_menu()


while True:

    user = input(f"{name}: ").lower().strip()

    message_count += 1


    # Option 1
    if user == "1" or user in ["hello", "hi", "hey"]:

        greetings = [
            f"Hello {name}! 😊",
            f"Hi {name}! How can I help you?",
            f"Nice to see you again {name}!"
        ]

        print("Bot:", random.choice(greetings))


    # Option 2
    elif user == "2" or user == "how are you":

        print("Bot: I'm doing great! Thanks for asking.")


    # Option 3
    elif user == "3" or user == "what is your name":

        print("Bot: My name is RuleBot AI.")


    # Option 4
    elif user == "4" or user == "who created you":

        print("Bot: I was created by Christoph T Tuahuku using Python.")


    # Option 5
    elif user == "5" or user == "time":

        print(
            "Bot: Current time is",
            datetime.now().strftime("%H:%M:%S")
        )


    # Option 6
    elif user == "6" or user == "date":

        print(
            "Bot: Today's date is",
            datetime.now().strftime("%d/%m/%Y")
        )


    # Option 7
    elif user == "7" or user == "datetime":

        print(
            "Bot:",
            datetime.now().strftime("%A %d %B %Y %H:%M:%S")
        )


    # Option 8
    elif user == "8" or user == "joke":

        print("Bot:", random.choice(jokes))


    # Option 9
    elif user == "9" or user in ["motivation", "motivate me"]:

        print("Bot:", random.choice(quotes))


    # Option 10 Calculator
    elif user == "10" or user == "calculator":

        try:

            number1 = float(input("Enter first number: "))
            operator = input("Enter operator (+ - * /): ")
            number2 = float(input("Enter second number: "))


            if operator == "+":

                answer = number1 + number2


            elif operator == "-":

                answer = number1 - number2


            elif operator == "*":

                answer = number1 * number2


            elif operator == "/":

                if number2 != 0:
                    answer = number1 / number2

                else:
                    answer = "Cannot divide by zero"


            else:

                answer = "Invalid operator"


            print("Bot: Answer =", answer)


        except ValueError:

            print("Bot: Please enter valid numbers.")



    # Option 11
    elif user == "11" or user == "what is ai":

        print(
            "Bot: Artificial Intelligence allows computers "
            "to perform tasks that normally require human intelligence."
        )


    # Option 12
    elif user == "12" or user == "best programming language":

        print(
            "Bot: Python is one of the best languages for AI, "
            "automation, and data science."
        )


    # Option 13
    elif user == "13" or user == "count":

        print(
            f"Bot: We have exchanged {message_count} messages."
        )


    # Option 14 Exit
    elif user == "14" or user in ["bye", "exit", "quit"]:

        print(f"\nBot: Goodbye {name}! 👋")
        print(f"Bot: Total messages: {message_count}")
        break


    # Unknown input
    else:

        print(
            "Bot: I don't understand that yet."
        )

        print(
            "Bot: Please choose a number from the menu."
        )


    # Show menu after every conversation
    print("\nBot: What else can I help you with?")
    show_menu()