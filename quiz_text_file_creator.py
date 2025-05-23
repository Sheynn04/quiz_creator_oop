# 1. Create a class for the functions. 
class QuizCreator:

# 2. Define the variables that we are going to use.
    def __init__(self):
        self.title = ""
        self.item_quantity = 0   #These are the relevant datas in my previous code. 
        self.quiz_data = []

# 3. Define the initial inputs.
    def get_title(self):
        self.title = input("What is the title of this quiz?: ").title()    

    def get_item_quantity(self):
        while True:
            try:
                self.item_quantity = int(input("How many questions will be on this quiz?: "))
            except ValueError:
                print("Please input a proper value!")

# 4. Define the question and answer inputs.
    def collect_questions(self):
        for quesnum in range(self.item_quantity):
            print(f"Queztion {quesnum+1}: ")
            question = input("Input your question: ").strip()

            choices = []
            for option in ["A", "B", "C", "D"]:
                choice = input(f"Enter option{option}: ").strip()
                choices.append(choice)
            while True:
                answer = input("Which letter is the correct answer?: ").upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Answer not in the options! Please input A, B, C, or D.")

            self.quiz_data.append({
                "question": question,
                "choices": choices,
                "answer": answer
            })


# 5. Define the file it is going to be saved as.


# 6. Make a variable storage for the class.