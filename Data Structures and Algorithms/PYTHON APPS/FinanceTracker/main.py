import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import financeDataBase

mauve = "rgba(66, 39, 90, 1), stop:1 rgba(115, 75, 109, 1)"
green_blue = "rgba(67, 206, 162, 1), stop:1 rgba(24, 90, 157, 1)"
pink_orange = "rgba(221, 214, 243, 1), stop:1 rgba(250, 172, 168, 1)"

"""
    Method Name: verify
    Parameters: user_input
    @user_input: user entry is entered here
    Purpose: Makes sure user enters numerical digits
"""


def verify(user_input):
    try:
        float(user_input)
        print("Possible")
        return True
    except ValueError:
        print(f"Could not convert {user_input}!")
        return False


"""
    Method Name: go_help
    Parameters: None
    Purpose: Switches to help screen
"""


def go_help():
    help_window = Help()
    widget.addWidget(help_window)
    widget.setCurrentIndex(widget.currentIndex() + 1)


"""
    Method Name: go_home
    Parameters: None
    Purpose: Switches to home screen
"""


def go_home():
    financeapp = FinanceMenu()
    data = financeDataBase.get_bg_color()

    print(f"this is data {data}")
    financeapp.setStyleSheet(
        f"QDialog#Dialog {{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1,"
        f"y2:1, stop:0 {data}) }}")

    widget.addWidget(financeapp)
    widget.setCurrentIndex(widget.currentIndex() + 1)


"""
    Method Name: go_settings
    Parameters: None
    Purpose: Switches to settings screen
"""


def go_settings():
    settings_window = Settings()
    widget.addWidget(settings_window)
    widget.setCurrentIndex(widget.currentIndex() + 1)


"""
    Method Name: go_confirm
    Parameters: None
    Purpose: Switches to confirm screen
"""


def go_confirm():
    confirm = Confirm()
    widget.addWidget(confirm)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class FinanceMenu(QDialog):
    def __init__(self):
        super(FinanceMenu, self).__init__()
        loadUi("financeMenu.ui", self)
        self.enterAllDataButton.clicked.connect(self.send_all_data)
        self.viewTotalFunButton.clicked.connect(self.view_total_fun_expenses)
        self.viewTotalTransportationButton.clicked.connect(self.view_total_transport_expenses)
        self.viewTotalFoodButton.clicked.connect(self.view_total_food_expenses)
        self.viewTotalClothesButton.clicked.connect(self.view_total_clothes_expenses)
        self.viewTotalBillsButton.clicked.connect(self.view_total_bills_expenses)
        self.viewTotalOtherButton.clicked.connect(self.view_total_other_expenses)
        self.viewTotalExpenses.clicked.connect(self.view_all_expenses)
        self.viewFunGraph.clicked.connect(lambda: financeDataBase.graph("FUN"))
        self.viewTransportGraph.clicked.connect(lambda: financeDataBase.graph("TRANSPORTATION"))
        self.viewFoodGraph.clicked.connect(lambda: financeDataBase.graph("FOOD"))
        self.viewClothesGraph.clicked.connect(lambda: financeDataBase.graph("CLOTHES"))
        self.viewBillsGraph.clicked.connect(lambda: financeDataBase.graph("BILLS"))
        self.viewOtherGraph.clicked.connect(lambda: financeDataBase.graph("OTHER"))
        self.viewPieChart.clicked.connect(financeDataBase.graph_all)
        self.settingsButton.clicked.connect(lambda: go_settings())
        self.helpButton.clicked.connect(lambda: go_help())
        self.deletePrevFun.clicked.connect(lambda: financeDataBase.delete_recent("FUN"))
        self.deletePrevTransportation.clicked.connect(lambda: financeDataBase.delete_recent("TRANSPORTATION"))
        self.deletePrevFood.clicked.connect(lambda: financeDataBase.delete_recent("FOOD"))
        self.deletePrevClothes.clicked.connect(lambda: financeDataBase.delete_recent("CLOTHES"))
        self.deletePrevBills.clicked.connect(lambda: financeDataBase.delete_recent("BILLS"))
        self.deletePrevOther.clicked.connect(lambda: financeDataBase.delete_recent("OTHER"))
        self.del_table_fun.clicked.connect(lambda: financeDataBase.delete_data_in_table("fun"))
        self.del_table_transportation.clicked.connect(lambda: financeDataBase.delete_data_in_table("transportation"))
        self.del_table_food.clicked.connect(lambda: financeDataBase.delete_data_in_table("food"))
        self.del_table_clothes.clicked.connect(lambda: financeDataBase.delete_data_in_table("clothes"))
        self.del_table_bills.clicked.connect(lambda: financeDataBase.delete_data_in_table("bills"))
        self.del_table_other.clicked.connect(lambda: financeDataBase.delete_data_in_table("other"))
        self.enterGoalButton.clicked.connect(self.send_goal)
        self.checkGoalButton.clicked.connect(self.check_at_goal)
        self.setStyleSheet(f"QDialog#Dialog {{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1,"
                           f"y2:1, stop:0 {financeDataBase.get_bg_color()}) }})")

    """
    Method Name: send_all_data
    Parameters: None
    Purpose: Sends all of entered expenses to DB on their computer
    """

    def send_all_data(self):
        if verify(self.funEntry.text()):
            financeDataBase.send_data("FUN", float(self.funEntry.text()))
            print("Successful")
        if verify(self.transportationEntry.text()):
            financeDataBase.send_data("TRANSPORTATION", self.transportationEntry.text())
            print("Transportation was sent successfully")

        if verify(self.foodEntry.text()):
            financeDataBase.send_data("FOOD", self.foodEntry.text())
            print("Food was sent successfully")

        if verify(self.clothesEntry.text()):
            financeDataBase.send_data("CLOTHES", self.clothesEntry.text())
            print("Clothes sent successfully ")

        if verify(self.billsEntry.text()):
            financeDataBase.send_data("BILLS", self.billsEntry.text())
            print("Bills send successfully")

        if verify(self.otherEntry.text()):
            financeDataBase.send_data("OTHER", self.otherEntry.text())
            print("other sent successfully")

        # Clearing remaining text for user
        self.funEntry.setText("")
        self.transportationEntry.setText("")
        self.foodEntry.setText("")
        self.clothesEntry.setText("")
        self.billsEntry.setText("")
        self.otherEntry.setText("")

        goal = financeDataBase.get_data("GOAL")
        total_spent = financeDataBase.get_total_spent()
        if total_spent > goal[0][0]:
            trial = Trial()
            trial.warning.setText("You Are Over Budget Now!")
            trial.exec_()
        elif total_spent == goal[0][0]:
            trial = Trial()
            trial.warning.setText("You Have Hit Your Budget!")
            trial.exec_()

    """
    Method Name: send_goal
    Parameters: None
    Purpose: Sends user's goal to database so it is saved
    """

    def send_goal(self):
        if verify(self.goalEntry.text()):
            financeDataBase.update_record("GOAL", self.goalEntry.text())
        self.goalEntry.setText("")

    """
    Method Name: check_at_goal
    Parameters: None
    Purpose: Checks if user surpassed goal
    """

    def check_at_goal(self):
        goal = financeDataBase.get_data("GOAL")
        if financeDataBase.get_total_spent() > goal[0][0]:
            print("You have exceeded your budget!")
            self.spentSpecificLabel.setText(f"You are over budget, your budget was ${goal[0][0]}")
        elif 0 <= (goal[0][0] - financeDataBase.get_total_spent()) <= 500:
            self.spentSpecificLabel.setText(f"You are $500 within the budget, your budget is ${goal[0][0]}")
        elif financeDataBase.get_total_spent() < goal[0][0]:
            self.spentSpecificLabel.setText(f"You are under budget don't worry! Budget: ${goal[0][0]}")
        else:
            self.spentSpecificLabel.setText(f"You reached budget! Budget: ${goal[0][0]}")

    """
    Method Name: view_total_fun_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on fun category 
    """

    def view_total_fun_expenses(self):
        spent = financeDataBase.sum_partic_expense("FUN")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Fun")
        else:
            self.spentSpecificLabel.setText("Nothing spent on fun yet! Try entering something")

    """
    Method Name: view_total_transport_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on transport category 
    """

    def view_total_transport_expenses(self):
        spent = financeDataBase.sum_partic_expense("TRANSPORTATION")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Transportation")
        else:
            self.spentSpecificLabel.setText("Nothing spent on transportation yet! Try entering something")

    """
    Method Name: view_total_food_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on food category 
    """

    def view_total_food_expenses(self):
        spent = financeDataBase.sum_partic_expense("FOOD")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Food")
        else:
            self.spentSpecificLabel.setText("Nothing spent on food yet! Try entering something")

    """
    Method Name: view_total_clothes_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on clothes category 
    """

    def view_total_clothes_expenses(self):
        spent = financeDataBase.sum_partic_expense("CLOTHES")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Clothes")
        else:
            self.spentSpecificLabel.setText("Nothing spent on clothes yet! Try entering something")

    """
    Method Name: view_total_bills_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on bills category 
    """

    def view_total_bills_expenses(self):
        spent = financeDataBase.sum_partic_expense("BILLS")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Bills")
        else:
            self.spentSpecificLabel.setText("Nothing spent on bills yet! Try entering something")

    """
    Method Name: view_total_other_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on other category 
    """

    def view_total_other_expenses(self):
        spent = financeDataBase.sum_partic_expense("OTHER")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Other")
        else:
            self.spentSpecificLabel.setText("Nothing spent on other yet! Try entering something")

    """
    Method Name: view_all_expenses
    Parameters: None
    Purpose: Displays total amount of money spent on all categories 
    """

    def view_all_expenses(self):
        spent = financeDataBase.get_total_spent()
        self.spentSpecificLabel.setText(f"TOTAL Expenses: ${round(spent,2)}")


class Help(QDialog):
    def __init__(self):
        super(Help, self).__init__()
        loadUi("help.ui", self)
        self.homeButton1.clicked.connect(lambda: go_home())
        self.explain.setWordWrap(True)


class Trial(QDialog):
    def __init__(self):
        super(Trial, self).__init__()
        loadUi("trial.ui", self)
        self.setWindowTitle("Warning")
        self.exitButton.clicked.connect(self.close)


class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        loadUi("settings.ui", self)
        self.homeButton.clicked.connect(lambda: go_home())
        self.submitButton.clicked.connect(self.change_back_colour)  # this is defualt
        self.RGB_Button.clicked.connect(self.get_rgb_values)
        self.rSlider.valueChanged.connect(self.get_r_value)
        self.gSlider.valueChanged.connect(self.get_g_value)
        self.bSlider.valueChanged.connect(self.get_b_value)
        self.clearRecordsButton.clicked.connect(lambda: go_confirm())

    def get_r_value(self):
        red = str(self.rSlider.value())
        self.rValue.setText(red)
        return int(red)

    def get_rgb_values(self):
        red = str(self.rSlider.value())
        green = str(self.gSlider.value())
        blue = str(self.bSlider.value())
        rgb = f"rgb({red}, {green}, {blue})"
        financeDataBase.send_bg_color(rgb)

    def get_g_value(self):
        green = str(self.gSlider.value())
        self.gValue.setText(green)
        return int(green)

    def get_b_value(self):
        blue = str(self.bSlider.value())
        self.bValue.setText(blue)
        return int(blue)

    def change_back_colour(self):
        state = self.colorSelectBox.currentText()
        print(state)

        if state == "Mauve":
            financeDataBase.send_bg_color(mauve)
        elif state == "Green Blue":
            financeDataBase.send_bg_color(green_blue)
        else:
            financeDataBase.send_bg_color(pink_orange)


class Confirm(QDialog):
    def __init__(self):
        super(Confirm, self).__init__()
        loadUi("confirm.ui", self)
        self.warning.setWordWrap(True)
        self.cancelButton.clicked.connect(lambda: go_settings())
        self.proceedButton.clicked.connect(lambda: financeDataBase.delete_all())


app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
window = FinanceMenu()

widget.addWidget(window)

sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)

widget.setFixedWidth(sizeObject.width())
widget.setFixedHeight(sizeObject.height())
widget.show()
app.exec_()
