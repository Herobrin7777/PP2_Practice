import csv
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Xmenpolo52428576jso_",
    host="localhost",
    port="5432"
)

cur = conn.cursor()



def insert_console():
    name=input("Enter name: ")
    phone=input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()


def insert_from_csv(file):
    with open(file, newline='') as f:
        reader=csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()


def update_user():
    name=input("Who to update: ")
    new_name=input("New name (or press enter): ")
    new_phone=input("New phone (or press enter): ")

    if new_name:
        cur.execute(
            "UPDATE phonebook SET username=%s WHERE first_name=%s",
            (new_name, name)
        )
    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE username=%s",
            (new_phone, name)
        )
    conn.commit()



def query_data():
    print("1 - all")
    print("2 - by name")
    print("3 - by phone")

    choice=input("Choose: ")

    if choice=="1":
        cur.execute("SELECT * FROM phonebook")
    elif choice=="2":
        name=input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE username=%s", (name,))
    elif choice=="3":
        phone=input("Phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone=%s", (phone,))

    rows=cur.fetchall()
    for row in rows:
        print(row)



def delete_user():
    choice = input("Delete by (1-name / 2-phone): ")

    if choice=="1":
        name=input("Name: ")
        cur.execute("DELETE FROM phonebook WHERE username=%s", (name,))
    else:
        phone=input("Phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()


while True:
    print("\n1.Insert console")
    print("2.Insert CSV")
    print("3.Update")
    print("4.Query")
    print("5.Delete")
    print("0.Exit")


    c=input(">> ")

    if c=="1":
        insert_console()
    elif c=="2":
        insert_from_csv("data.csv")
    elif c=="3":
        update_user()
    elif c=="4":
        query_data()
    elif c=="5":
        delete_user()
    elif c=="0":
        break

cur.close()
conn.close()