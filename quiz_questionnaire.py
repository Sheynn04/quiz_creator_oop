# 1. Import the needed library.
import random

# 2. Create a class for the question outputs.
class Question:

# 3. Define the variables we are going to include in this class.
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def output(self):
        print(f"Q{ques_num +1}: {ques_contents['question']}")
        print(f"A. {ques_contents['choices'][0]}")
        print(f"B. {ques_contents['choices'][1]}")
        print(f"C. {ques_contents['choices'][2]}")
        print(f"D. {ques_contents['choices'][3]}")
    

# 4. Create a class for the quiz part.

class Quiz:
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

