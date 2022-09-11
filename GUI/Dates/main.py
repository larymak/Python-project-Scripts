"""
Dates - a simple graphic dates calculator
Demonstrates the use of PySimpleGui as an interface
and date arithmetics using module datetime and numpy.
2022 Eduardo C. - https://github.com/ehcelino
"""
from datetime import datetime
import PySimpleGUI as sg
import numpy as np

DATE_FRMT = '%m-%d-%Y'

def days_between(date_one, date_two):
    """
    Determines how many days between dates.
    :param date_one: date (us format) as string
    :param date_two: date (us format) as string
    :return: days as string
    """
    result = ''
    try:
        tmp_one = datetime.strptime(date_one, DATE_FRMT)
        tmp_two = datetime.strptime(date_two, DATE_FRMT)
    except ValueError as exc:
        sg.popup('Error:', exc)
    else:
        mytimedelta = tmp_one - tmp_two
        result = mytimedelta.days
    return result

def workdays_between(date_one, date_two):
    """
    Determines how many workdays between dates.
    :param date_one: date (us format) as string
    :param date_two: date (us format) as string
    :return: days as int
    """
    result = ''
    try:
        tmp_one = datetime.strptime(date_one, DATE_FRMT)
        tmp_two = datetime.strptime(date_two, DATE_FRMT)
    except ValueError as exc:
        sg.popup('Error:', exc)
    else:
        result = np.busday_count(tmp_one.strftime('%Y-%m-%d'), tmp_two.strftime('%Y-%m-%d'))
    return result

def main_window():
    """
    Defines the main window.
    :return: PySimpleGUI Window object.
    """
    tsz = (8, 1) # Makes easier to define sizes to multiple elements.
    isz = (15, 1)
    # Everything bound by []'s goes on one line.
    layout = [
        [sg.Text('Date calculator', font='_ 12 bold')],
        [sg.Text('Date format: US (mm-dd-yyyy', font='_ 10 italic')],
        [sg.Text('Date one:', size=tsz),
         sg.Input('', size=isz, key='-DATE01-')],
        [sg.Text('Date two:', size=tsz),
         sg.Input('', size=isz, key='-DATE02-')],
        [sg.Text('Answer:', size=tsz),
         sg.Input('', size=isz, key='-OUTPUT-')],
        [sg.Push(), sg.Button('Days between dates', key='-BETWEEN-'), sg.Push()],
        [sg.Push(), sg.Button('Working days bt. dates', key='-WORKING-'), sg.Push()],
        [sg.Push(), sg.Button('Exit', key='-EXIT-')]
    ]

    return sg.Window('Date calculator!', layout, finalize=True)

window = main_window()

while True:  # This is the main loop.
    event, values = window.read()

    if event == '-BETWEEN-':
        try:
            window['-OUTPUT-'].update(value=str(abs(
                days_between(values['-DATE01-'], values['-DATE02-']))))
        except TypeError as err:
            sg.popup('Error:', err)

    if event == '-WORKING-':
        try:
            window['-OUTPUT-'].update(value=str(abs(
                workdays_between(values['-DATE01-'], values['-DATE02-']))))
        except TypeError as err:
            sg.popup('Error:', err)

    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break

window.close()
