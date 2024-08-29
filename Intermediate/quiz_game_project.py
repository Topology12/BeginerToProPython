"""Quiz game project"""

import random

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
                " you are free to take it home to eat.",
        "answer": "True"
    },
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Back rub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
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
        self.bank = [Question(question['text'], question['answer']) for question in question_data]

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
