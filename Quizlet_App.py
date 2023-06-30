import tkinter as tk
from tkinter import messagebox

quiz_questions = [
    {
        'question': 'What country has the highest life expectancy',
        'options': ['HongKong', 'India', 'China', 'England'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the most common surname in the United States',
        'options': ['Smith', 'Brown', 'Dilley', 'Matthews'],
        'answer': 'Leonardo da Vinci'
    },
    {
    'question': 'Who was the ancient Greek God of the Sun',
        'options': ['Apollo', 'Poseidon', 'Ares', 'Aphrodite'],
        'answer': 'Apollo'
    },
    {
        'question': 'What artist has the most streams on spotify',
        'options': ['Drake', 'S.Gomez', 'BlackPink', 'BTS'],
        'answer': 'Drake'
    }
    
]

class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self, text='')
        self.question_label.pack()

        self.options_frame = tk.Frame(self)
        self.options_frame.pack()

        for i in range(len(self.questions[0]['options'])):
            option_button = tk.Button(self.options_frame, text='', width=30, command=lambda i=i: self.check_answer(i))
            option_button.pack(pady=5)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question['question'])

            for i, option_button in enumerate(self.options_frame.winfo_children()):
                option_button.config(text=question['options'][i])

            self.current_question_index += 1
        else:
            self.show_score()

    def check_answer(self, selected_option):
        question = self.questions[self.current_question_index - 1]
        selected_answer = question['options'][selected_option]

        if selected_answer == question['answer']:
            self.score += 1

        self.next_question()

    def show_score(self):
        messagebox.showinfo('Quiz Completed', f'Quiz completed. Your score: {self.score}/{len(self.questions)}')
        self.destroy()


if __name__ == '__main__':
    app = QuizApp(quiz_questions)
    app.mainloop()
