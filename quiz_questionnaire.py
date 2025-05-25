# 1. Import the needed library.
import random

# 2. Create a class for the question outputs.
class Question:

# 3. Define the variables we are going to include in this class.
    def __init__(self,questions,choices,answer):
        self.questions = questions
        self.choices = choices
        self.answer = answer

    def output(self):
        print(f"Q{ques_num +1}: {ques_contents['question']}")
        print(f"A. {ques_contents['choices'][0]}")
        print(f"B. {ques_contents['choices'][1]}")
        print(f"C. {ques_contents['choices'][2]}")
        print(f"D. {ques_contents['choices'][3]}")
    

# 4. Define each variables we listed.