import sqlite3
from matplotlib import pyplot as plt

plt.style.use('ggplot')


def send_bg_color(color):
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    cur.execute(f"UPDATE colorChoice SET color = (:color) WHERE rowid = 1", {"color": color})
    connection.commit()
    connection.close()


def get_bg_color():
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM colorChoice")
    data = cur.fetchall()
    return data[0][0]


def send_data(query, data):
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    num_data = int(data)
    cur.execute(f"INSERT INTO {query} VALUES (:payed)", {"payed": num_data})
    connection.commit()
    connection.close()


def update_record(query, data):
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    num_data = int(data)
    cur.execute(f"UPDATE {query} SET userGoal = (:goal) WHERE rowid = 1", {"goal": num_data})
    connection.commit()
    connection.close()


def sum_partic_expense(query):
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    cur.execute(f"SELECT SUM(payed)  FROM {query}")
    d = cur.fetchall()
    connection.commit()
    connection.close()
    return d[0][0]


def get_total_spent():
    spent = 0
    spent_fun = sum_partic_expense("FUN")
    spent_transportation = sum_partic_expense("TRANSPORTATION")
    spent_food = sum_partic_expense("FOOD")
    spent_clothes = sum_partic_expense("CLOTHES")
    spent_bills = sum_partic_expense("BILLS")
    spent_other = sum_partic_expense("OTHER")

    if spent_fun is not None:
        spent += spent_fun

    if spent_transportation is not None:
        spent += spent_transportation

    if spent_food is not None:
        spent += spent_food

    if spent_clothes is not None:
        spent += spent_clothes

    if spent_bills is not None:
        spent += spent_bills

    if spent_other is not None:
        spent += spent_other

    return spent


def get_data(query):
    connection = sqlite3.connect("Finance.db")
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM {query}")
    c = cur.fetchall()
    connection.commit()
    connection.close()
    return c


def graph(graph_type):
    g_type = get_data(graph_type)
    plt.plot(range(1, len(g_type) + 1), g_type)
    plt.title(f"MONEY($) spent on category: {graph_type}")
    plt.xlabel("Number of purchases")
    plt.ylabel("CAD ($)")
    plt.show()


def graph_all():
    labels = []
    slices = []

    fun = sum_partic_expense("FUN")
    transport = sum_partic_expense("TRANSPORTATION")
    food = sum_partic_expense("FOOD")
    clothes = sum_partic_expense("CLOTHES")
    bills = sum_partic_expense("BILLS")
    other = sum_partic_expense("OTHER")

    if fun is not None:
        labels.append("FUN")
        slices.append(fun)

    if transport is not None:
        labels.append("TRANSPORT")
        slices.append(transport)

    if food is not None:
        labels.append("FOOD")
        slices.append(food)

    if clothes is not None:
        labels.append("CLOTHES")
        slices.append(clothes)

    if bills is not None:
        labels.append("BILLS")
        slices.append(bills)

    if other is not None:
        labels.append("OTHER")
        slices.append(other)

    colors = ("limegreen", "cyan", "yellow", "pink",
              "red", "lightblue")

    plt.pie(slices, labels=labels, shadow=True, wedgeprops={'edgecolor': 'black'}, autopct=f"%0.2f%%", colors=colors)
    plt.title("PIE CHART")
    plt.tight_layout()
    plt.show()


def get_count(query):
    con = sqlite3.connect("Finance.db")
    cur = con.cursor()
    cur.execute(f"SELECT COUNT (*) FROM {query}")
    count = cur.fetchall()
    con.commit()
    con.close()
    return count[0][0]


def delete_recent(query):
    con = sqlite3.connect("Finance.db")
    count = get_count(query)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {query} WHERE rowid= (:delete)", {"delete": count})
    con.commit()
    con.close()


"""
This will drop the table, 
then it will create a new table since there sqlite does not support truncate function
"""


def delete_data_in_table(query):
    con = sqlite3.connect("Finance.db")
    cur = con.cursor()
    cur.execute(f"DROP TABLE {query}")
    cur.execute(f"""CREATE TABLE {query}(
                payed real
                )""")
    con.commit()
    con.close()


def delete_all():
    delete_data_in_table("fun")
    delete_data_in_table("transportation")
    delete_data_in_table("food")
    delete_data_in_table("clothes")
    delete_data_in_table("bills")
    delete_data_in_table("other")


