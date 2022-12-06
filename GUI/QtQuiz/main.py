r"""
QtQuiz - Qt graphical quiz software.
Demonstrates the use of PyQT5 as an interface, and
simple dictionary interaction.

The interface was designed using QT Designer (https://build-system.fman.io/qt-designer-download).
To convert from designer's .ui to .py use the command 'pyuic5 .\design.ui >> design.py' (Windows
powershell). Then proceed by importing the new module into your code. A few errors may occur,
usually related to the codepage of the .py file or invalid characters found in it.
For both I use Notepad++ to make the necessary corrections.

I've noticed that PyQt5 prevents python from throwing errors as expected,
instead showing minimal cryptic messages. So I make use of the PyCharm's debugger function
to extract and correct these errors.

2022 Eduardo C. - https://github.com/ehcelino
"""
import sys
# import QtQuiz.design
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from QtQuiz.design import *

datatable = {
    "1": {
        "question": "The statement: 'print((10+10) / 2) will result in:'",
        "answers": {
            "a": "an error",
            "b": "10.0",
            "c": "10",
            "d": "(10+10) / 2",
        },
        "correct_answer": "b",
    },
    "2": {
        "question": "What's the result of print(type(5.0))?",
        "answers": {
            "a": "True",
            "b": "Integer",
            "c": "False",
            "d": "class 'float'",
        },
        "correct_answer": "d",
    },
    "3": {
        "question": "How do you define a function in Python?",
        "answers": {
            "a": "function myfunction():",
            "b": "def myfunction():",
            "c": "set myfunction as function",
            "d": "myfunction():",
        },
        "correct_answer": "b",
    },
}

CORRECT = 0

class ReportWindow(QWidget):
    """
    This is actually a QWidget, that will appear floating as a window.
    It shows the user how many questions he got right compared to the total.
    The button in it quits the whole application, same as the exit button on main window.
    Notice that instead of using a design file, we are creating this window on the fly.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label1 = QLabel("Your result:")
        layout.addWidget(self.label1)
        self.label1.setStyleSheet('font: 15px Calibri')  # The style is set using css rules
        self.label2 = QLabel(f"You got {CORRECT} from {len(datatable)}")
        self.label2.setStyleSheet('font: 15px Calibri')
        layout.addWidget(self.label2)
        self.button = QPushButton('Exit')
        self.button.setStyleSheet('font: 15px Calibri')
        layout.addWidget(self.button)
        self.button.clicked.connect(QApplication.quit)
        self.setLayout(layout)

class QuizApp(QMainWindow, Ui_MainWindow):
    """
    Main application window. All the logic goes here.
    """
    index = 1
    started = False

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.txtResult.setStyleSheet('border: 1px solid red; font: bold')
        self.btnStart.clicked.connect(self.start)
        self.btnAnswer.clicked.connect(self.answer)
        self.btnExit.clicked.connect(QApplication.quit)

    def start(self):
        """
        Start the questions.
        :return: None.
        """
        self.started = True
        self.txtOne.setText(str(self.index))
        self.txtN.setText(str(len(datatable)))
        self.txtQuestion.setText(f'{datatable[str(self.index)]["question"]}')
        self.txtAnswerA.setText(f'{datatable[str(self.index)]["answers"]["a"]}')
        self.txtAnswerB.setText(f'{datatable[str(self.index)]["answers"]["b"]}')
        self.txtAnswerC.setText(f'{datatable[str(self.index)]["answers"]["c"]}')
        self.txtAnswerD.setText(f'{datatable[str(self.index)]["answers"]["d"]}')


    def answer(self):
        """
        This function is called whenever the answer button is pressed.
        :return: None.
        """
        global CORRECT
        if self.started and (self.radA.isChecked() or self.radB.isChecked()
                             or self.radC.isChecked() or self.radD.isChecked()):
            # couldn't find a better way to do this. If you do please drop me a line.
            if self.radA.isChecked():
                choice = 'a'
            elif self.radB.isChecked():
                choice = 'b'
            elif self.radC.isChecked():
                choice = 'c'
            elif self.radD.isChecked():
                choice = 'd'
            # started = False
            if choice == datatable[str(self.index)]["correct_answer"]:
                self.txtResult.setText('Correct!')
                CORRECT += 1
            else:
                self.txtResult.setText('Wrong!')
            if self.index < len(datatable):
                self.index += 1
                self.start()
            else:
                # self.txtResult.setText(f'End! You got {self.CORRECT_ANSWERS} of {len(datatable)}')
                self.show_report_window()

    def show_report_window(self):
        """
        Opens the report window at the end of the run.
        :return: None.
        """
        self.win = ReportWindow()
        self.win.show()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    qtquiz = QuizApp()
    qtquiz.show()
    qt.exec_()
