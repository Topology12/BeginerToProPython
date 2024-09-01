"""Quiz game project"""

import random

question_data = [
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "&quot;Windows NT&quot; is a monolithic kernel.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The HTML5 standard was published in 2014.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "A Boolean value of &quot;0&quot; represents which of these words?",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "AMD created the first consumer 64-bit processor.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "Linus Sebastian is the creator of the Linux kernel,"
                 " which went on to be used in Linux, Android, and Chrome OS.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Time on Computers is measured via the EPOX System.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "To bypass US Munitions Export Laws,"
                 " the creator of the PGP published all the source code in book form. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The open source program Redis is a relational database server.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The first computer bug was formed by faulty wires.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
     "question": "DHCP stands for Dynamic Host Configuration Port.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
     "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "Android versions are named in alphabetical order.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "MacOS is based on Linux.", "correct_answer": "False",
     "incorrect_answers": ["True"]}
]


class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def plus_score(self):
        self.score += 1

    def get_score(self) -> int:
        return self.score


class Question:

    def __init__(self, question, answer):
        self.text = question
        self.answer = answer


class QuestionBank:
    def __init__(self):
        self.bank = [Question(question['question'], question['correct_answer']) for question in question_data]

    def get_question(self) -> Question:
        question = random.choice(self.bank)
        self.bank.remove(question)
        return question


class QuizGame:
    def __init__(self, user: User, question_bank: QuestionBank):
        self.user = user
        self.question_bank = question_bank
        self.question_number = 0
        self.total_questions = len(self.question_bank.bank)

    def next_question(self):
        question = self.question_bank.get_question()
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text}")
        self.check_answer(question, user_answer)

    def still_has_question(self):
        if len(self.question_bank.bank) == 0:
            return False
        return True

    def check_answer(self, question, answer):
        if question.answer == answer:
            print("You got it right!")
            self.user.plus_score()
        else:
            print("That 's wrong.")
        print(f"Your current score is {self.user.score}/{self.question_number}")


user = User("Bé tập đi")
question_bank = QuestionBank()
game = QuizGame(user, question_bank)
while game.still_has_question():
    game.next_question()

print("\n")
print("You completed the quiz")
print(f"Final your score is {game.user.score}/{game.total_questions}")
