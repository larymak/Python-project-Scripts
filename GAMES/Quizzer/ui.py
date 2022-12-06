from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.title('Quizzer')
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(self, text="Score: 0", bg=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(self, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(self, image=true_img, command=self.true_press, highlightthickness=0)
        self.true.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false = Button(self, image=false_img, command=self.false_press, highlightthickness=0)
        self.false.grid(row=2, column=1)

        self.question_box()
        self.mainloop()

    def question_box(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true.destroy()
            self.false.destroy()

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.after(1000, self.question_box)
