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
                break
            except ValueError:
                print("Please input a proper value!")

# 4. Define the question and answer inputs.
    def collect_questions(self):
        for quesnum in range(self.item_quantity):
            print(f"Queztion {quesnum+1}: ")
            question = input("Input your question: ").strip()

            choices = []
            for option in ["A", "B", "C", "D"]:
                choice = input(f"Enter option {option}: ").strip()
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
    def save_to_file(self, filename="quiz_creator.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Quiz Title: {self.title.title()}\n\n")
            f.write(f"Quiz Item Quantity: {self.item_quantity}\n\n")

            for i, item in enumerate(self.quiz_data):
                f.write(f"Question {i+1}: {item['question']}\n")
                f.write(f"Option A: {item['choices'][0]}\n")
                f.write(f"Option B: {item['choices'][1]}\n")
                f.write(f"Option C: {item['choices'][2]}\n")
                f.write(f"Option D: {item['choices'][3]}\n")
                f.write(f"Answer: {item['answer']}\n\n")

        print(f"\nQuiz saved to '{filename}' successfully!")

    def run(self):
        self.get_title()
        self.get_item_quantity()
        self.collect_questions()
        self.save_to_file()
# 6. Make a variable storage for the class.
creator = QuizCreator()
creator.run()
