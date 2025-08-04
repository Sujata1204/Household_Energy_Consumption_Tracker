import mysql.connector
from datetime import datetime

mycon=mysql.connector.connect(
             host="localhost",
             user="root",
             password="password",
             database= "Household_Energy_Consumption_Tracker"
             )
print(mycon)

mycursor=mycon.cursor()
# mycursor.execute("create database Household_Energy_Consumption_Tracker")

# mycursor.execute('''CREATE TABLE IF NOT EXISTS users
#                       (user_id int auto_increment primary key,
#                       name varchar(100),
#                       address varchar(200),
#                       email varchar(200))''')



# mycursor.execute ('''CREATE TABLE IF NOT EXISTS energy_usage
#                   (log_id INT auto_increment primary key,
#                   user_id INT,
#                   date DATE,
#                   units_consumed FLOAT,
#                   amount decimal(10,2),
#                   foreign key (user_id) REFERENCES users(user_id))''')


def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 6
    else:
        return (100 * 5) + (100 * 6) + (units - 200) * 7

def add_user():
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    if name and address and email:
        mycursor.execute("INSERT INTO users (name, address, email) VALUES (%s, %s, %s)", (name, address, email))
        mycon.commit()
        print("User added successfully!\n")
    else:
        print("All fields are required.\n")



def log_usage():
    try:
        user_id = int(input("Enter User ID: "))
        units = float(input("Enter Units Consumed: "))
        date = datetime.now().strftime("%Y-%m-%d")
        amount = calculate_bill(units)
        mycursor.execute("INSERT INTO energy_usage (user_id, date, units_consumed, amount) VALUES (%s, %s, %s, %s)",
                       (user_id, date, units, amount))
        mycon.commit()
        print(f" Usage logged. Bill Amount: ₹{amount:.2f}\n")
    except ValueError:
        print(" Please enter valid numeric values.\n")


def view_summary():
    user_id_input = input("Enter User ID to View Summary: ")
    if not user_id_input.isdigit():
        print("Please enter a valid numeric User ID.\n")
        return
    user_id = int(user_id_input)
    mycursor.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
    user = mycursor.fetchone()
    if not user:
        print("User not found.\n")
        return
    print(f"\nEnergy Consumption Summary for {user[0]}:")
    mycursor.execute("SELECT date, units_consumed, amount FROM energy_usage WHERE user_id = %s ORDER BY date", (user_id,))
    records = mycursor.fetchall()
    if not records:
        print("No energy usage records found.\n")
        return
    total_units = sum(row[1] for row in records)
    total_bill = sum(row[2] for row in records)
    for row in records:
        print(f"Date: {row[0]} | Units: {row[1]} | Bill: ₹{row[2]:.2f}")
    print(f"\nTotal Units Consumed: {total_units:.2f}")
    print(f"Total Bill Amount: ₹{total_bill:.2f}\n")


def view_all_users():
    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    if users:
        print("\n Registered Users:")
        for user in users:
            print(f"User ID: {user[0]} | Name: {user[1]} | Address: {user[2]} | Email: {user[3]}")
        print()
    else:
        print("No users found.\n")


def main():
    while True:
        print("==== Smart Energy Consumption Tracker ==================")
        print("1. Add New User")
        print("2. Log Energy Usage")
        print("3. View User Energy Summary")
        print("4. View All Users")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            log_usage()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            view_all_users()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
mycursor.close()
mycursor.close()