import turtle


# Set up the turtle screen
wn = turtle.Screen()
wn.title("Simple Quiz App")
wn.bgcolor("lightblue")


# Function to ask a question and check the answer (procedural abstraction)
def ask_question(question, correct_answer):
    user_answer = wn.textinput("Quiz Question", question)  # Input using turtle's textinput
    if user_answer and user_answer.lower() == correct_answer.lower():  # Algorithmic logic
        return 1
    else:
        return 0


# Main program
def main():
    score = 0
    questions = [  # List of questions and answers (list processing)
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("What is the largest planet in the solar system?", "Jupiter")
    ]


    # Iterate through the list of questions
    for question, answer in questions:
        score += ask_question(question, answer)  # Procedural abstraction


    # Display the final score using turtle
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write(f"Your final score is {score}/{len(questions)}.", align="center", font=("Arial", 16, "normal"))


# Run the program
wn.mainloop()


if __name__ == "__main__":
    main()
    turtle.mainloop()  # Keep the turtle window open
