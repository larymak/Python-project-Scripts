"""
PyQuiz - a simple graphical quiz software
Demonstrates the use of PySimpleGui as an interface
and simple dictionary interaction
"""
import PySimpleGUI as sg

# The dictionary containing our questions and answers (can come from a file, a database...)
datatable = {
    "1": {
        "question": "10 + 10",
        "answers": {
            "a": "20",
            "b": "100",
            "c": "1010",
        },
        "correct_answer": "a",
    },
    "2": {
        "question": "5 * 5",
        "answers": {
            "a": "55",
            "b": "25",
            "c": "500",
        },
        "correct_answer": "b",
    },
    "3": {
        "question": "3 ** 2",
        "answers": {
            "a": "3",
            "b": "32",
            "c": "9",
        },
        "correct_answer": "c",
    },
}

# Our window definition.
def main_window():
    """
    Defines the main window.
    :return: PySimpleGUI Window object.
    """
    # Everything bound by []'s goes on one line.
    layout = [
        [sg.Text('Quiz!', font='_ 12 bold')],
        [sg.Text('Question:')],
        [sg.Input('', size=(30, 1), key='-QUESTION-')],
        [sg.Text('Answers:')],
        [sg.Multiline('', size=(30, 8), key='-OPTIONS-')],
        [sg.Radio('a', group_id='-RADIO-', key='a'),
         sg.Radio('b', group_id='-RADIO-', key='b'),
         sg.Radio('c', group_id='-RADIO-', key='c'),],
        [sg.Button('Start', key='-START-'), sg.Button('Answer', key='-ANSWER-'),
         sg.Button('Exit', key='-EXIT-')]
    ]

    return sg.Window('Quiz!', layout, finalize=True)

window = main_window()

# variables
QUESTIONS_INDEX = 1
END = False  # To keep track of the end of the game
ANSWERED = False  # If the question is still unanswered
QUESTIONING = False  # If there's an active question
CORRECT = 0

# aliases
question = window['-QUESTION-']
answers = window['-OPTIONS-']

while True:  # This is the main loop.
    event, values = window.read()

    if event == '-START-':
        if not END:
            QUESTIONING = True
            answers.update(value='')
            question.update(value=f'{datatable[str(QUESTIONS_INDEX)]["question"]}')
            for answer, answer_data in datatable[str(QUESTIONS_INDEX)]["answers"].items():
                answers.print(f'({answer}): {answer_data}')
            correct_answer = datatable[str(QUESTIONS_INDEX)]["correct_answer"]
            ANSWERED = False
        else:
            QUESTIONING = False
            sg.popup('End of Quiz.')

    if event == '-ANSWER-':
        if (values['a'] or values['b'] or values['c']) and QUESTIONING:
            for idx in ('a', 'b', 'c'):
                if values[idx]:
                    USER_CHOICE = idx
            if not ANSWERED:
                if USER_CHOICE == correct_answer:
                    sg.popup('Correct!')
                    CORRECT += 1
                else:
                    sg.popup('Wrong.')
            if not ANSWERED:
                QUESTIONS_INDEX += 1
                ANSWERED = True
            if QUESTIONS_INDEX > len(datatable):
                END = True
                sg.popup(f'The end. You got {CORRECT} of {len(datatable)}.')
            if not END:
                window.write_event_value('-START-', '')

    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break


window.close()
