# import sqlite3

# def connect_to_database():
#     conn=sqlite3.connect('employee.db')
#     cursor = conn.cursor()
#     return conn, cursor

# connection = sqlite3.connect('employee.db')

# def create_table(id, first_name, last_name, email,contact):
#     connection = sqlite3.connect('employee.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS employee (
#                     id INTEGER PRIMARY KEY,
#                     first_name TEXT,
#                     last_name TEXT,
#                     email TEXT,
#                     contact INTEGER
#                 )
#                 ''' )

#     connection.commit()
#     connection.close()
#     result = insert_employee_data(id, first_name, last_name, email,contact)

# def insert_employee_data(id, first_name, last_name, email,contact):
#     conn, cursor = connect_to_database()
#     try:
#         insert_sql = "INSERT INTO employee (id, first_name, last_name, email, contact) VALUES (?,?,?,?,?)"
#         cursor.execute(insert_sql, (id, first_name, last_name, email, contact))
#         connection.commit()
#         connection.close()
#         print("Data inserted successfully")
#     except sqlite3.Error as e:
#         connection.commit()
#         connection.close()
#         print("Error in inserting data")
        
# def show_employees():
#     conn, cursor = connect_to_database()
#     try:
#         cursor.execute("SELECT id, first_name, last_name, email, contact FROM employee")
#         records = cursor.fetchall()
#         for record in records:
#             print(record)
#     except sqlite3.Error as e:
#         connection.commit()
#         connection.close()
#         print("Error in displaying data")
    

    