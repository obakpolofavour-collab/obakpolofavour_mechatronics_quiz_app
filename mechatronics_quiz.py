# Mechatronics Quiz App
# A beginner-friendly Python quiz about mechatronics and basic engineering.

# A list of dictionaries stores each question, its options, correct answer, and explanation.
questions = [
    {
        "question": "What does PLC stand for?",
        "options": ["1. Programmable Logic Controller", "2. Power Line Connection",
                    "3. Program Level Computer", "4. Process Logic Cable"],
        "answer": 1,
        "explanation": "PLC means Programmable Logic Controller. It is used to control machines and industrial processes."
    },
    {
        "question": "Which component converts electrical energy into mechanical motion?",
        "options": ["1. Sensor", "2. Actuator", "3. Resistor", "4. Fuse"],
        "answer": 2,
        "explanation": "An actuator converts energy into movement, such as the movement of a motor."
    },
    {
        "question": "What is the main function of a sensor?",
        "options": ["1. To store data", "2. To produce sound",
                    "3. To detect or measure a physical quantity", "4. To stop every machine"],
        "answer": 3,
        "explanation": "A sensor detects or measures conditions such as temperature, pressure, or position."
    },
    {
        "question": "Which programming language are you using for this project?",
        "options": ["1. HTML", "2. Python", "3. CSS", "4. SQL"],
        "answer": 2,
        "explanation": "Python is the programming language used to write this quiz application."
    },
    {
        "question": "What does CPU stand for?",
        "options": ["1. Central Processing Unit", "2. Computer Power Utility",
                    "3. Control Program User", "4. Central Programming Use"],
        "answer": 1,
        "explanation": "CPU means Central Processing Unit. It executes instructions in a computer."
    },
    {
        "question": "Which device is commonly used to measure temperature?",
        "options": ["1. Thermistor", "2. Relay", "3. Switch", "4. Transformer"],
        "answer": 1,
        "explanation": "A thermistor is a temperature-sensitive resistor whose resistance changes with temperature."
    },
    {
        "question": "What is the purpose of a motor?",
        "options": ["1. To convert mechanical energy to light",
                    "2. To convert electrical energy into mechanical energy",
                    "3. To measure voltage", "4. To store programmes"],
        "answer": 2,
        "explanation": "An electric motor converts electrical energy into mechanical energy."
    },
    {
        "question": "Which of these is an example of an input device?",
        "options": ["1. Sensor", "2. Loudspeaker", "3. Motor", "4. Lamp"],
        "answer": 1,
        "explanation": "A sensor provides input to a control system by detecting a condition."
    },
    {
        "question": "What does SCADA commonly help operators do?",
        "options": ["1. Design posters", "2. Monitor and control industrial processes",
                    "3. Charge batteries", "4. Browse social media"],
        "answer": 2,
        "explanation": "SCADA systems are used to supervise, monitor, and control industrial processes."
    },
    {
        "question": "Which statement best describes a robot?",
        "options": ["1. A device that can be programmed to perform tasks",
                    "2. A type of resistor", "3. A computer password",
                    "4. A measuring unit"],
        "answer": 1,
        "explanation": "A robot is a programmable machine that can carry out tasks automatically or semi-automatically."
    }
]


def ask_question(question_number, question_data):
    """Display one question and return True if the user's answer is correct."""
    print("\n" + str(question_number) + ". " + question_data["question"])

    # Display all four answer options.
    for option in question_data["options"]:
        print(option)

    # Keep asking until the user enters a valid option from 1 to 4.
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))

            if answer >= 1 and answer <= 4:
                break
            else:
                print("Please choose a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number, not a letter.")

    # Give feedback and an explanation immediately after each answer.
    if answer == question_data["answer"]:
        print("Correct! Well done.")
        return True
    else:
        print("Incorrect. The correct answer is option " +
              str(question_data["answer"]) + ".")
        print("Explanation: " + question_data["explanation"])
        return False


def calculate_result(score, total_questions):
    """Calculate and return the percentage and grade."""
    percentage = (score / total_questions) * 100

    if percentage >= 80:
        grade = "A - Excellent"
    elif percentage >= 60:
        grade = "B - Very Good"
    elif percentage >= 50:
        grade = "C - Good"
    else:
        grade = "Needs Improvement"

    return percentage, grade


def run_quiz():
    """Run the quiz, keep the score, and display the final result."""
    print("=" * 45)
    print("          MECHATRONICS QUIZ APP")
    print("=" * 45)
    print("Test your knowledge of mechatronics and engineering.")
    print("There are", len(questions), "questions. Each question carries 1 mark.")

    name = input("\nEnter your name: ").strip()
    if name == "":
        name = "Student"

    score = 0

    # The loop moves through every question in the questions list.
    for number, question_data in enumerate(questions, start=1):
        if ask_question(number, question_data):
            score += 1

    # Display the final score, percentage, and grade.
    percentage, grade = calculate_result(score, len(questions))

    print("\n" + "=" * 45)
    print("                 QUIZ RESULT")
    print("=" * 45)
    print("Student:", name)
    print("Score:", str(score) + "/" + str(len(questions)))
    print("Percentage: " + str(round(percentage, 1)) + "%")
    print("Grade:", grade)
    print("Thank you for taking the Mechatronics Quiz!")
    print("=" * 45)


# Start the application.
if __name__ == "__main__":
    run_quiz()
