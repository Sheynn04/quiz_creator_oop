# 1. Import the needed library.
import random

# 2. Create a class for the question outputs.
class Question:

# 3. Define the variables we are going to include in this class.
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def display(self, number):
        print(f"Q{number}: {self.text}")
        print(f"A. {self.choices[0]}")
        print(f"B. {self.choices[1]}")
        print(f"C. {self.choices[2]}")
        print(f"D. {self.choices[3]}")

    def is_correct(self, user_answer):
        return user_answer.upper() == self.answer.upper()

# 4. Create a class for the quiz part.
class Quiz:

# 5. Define the functions necessary.
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def loading_questions(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()

        question_text = ""
        choices = []
        answer = ""

        for line in lines:
            if line.startswith("Question"):
                question_text = line.split(":", 1)[1].strip()
                choices = []

            elif line.startswith("Option"):
                choices.append(line.split(":", 1)[1].strip())

            elif line.startswith("Answer"):
                answer = line.split(":", 1)[1].strip()
                self.questions.append(Question(question_text, choices, answer))

    def start(self):
        random.shuffle(self.questions)
        score = 0

        for ques_itt, question in enumerate(self.questions, 1):
            question.display(ques_itt)
            user_answer = input("Choose the letter of your answer: ").upper()

            if question.is_correct(user_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question.answer}")

        print(f"\nYour final score is: {score} out of {len(self.questions)}")

# 6. Run the classes.
quiz = Quiz("quiz_creator.txt")
quiz.loading_questions()
quiz.start()