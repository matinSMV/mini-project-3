import sqlite3

connect = sqlite3.connect('database\database.db')
my_cursor = connect.cursor()


def employees():
    my_cursor.execute('SELECT * FROM employee')
    result = my_cursor.fetchall()
    return result

def employee_detail(id):
    my_cursor.execute(f'SELECT * FROM employee WHERE id={id}')
    result = my_cursor.fetchall()
    return result


def add_employee(id, firstname, lastname, birthday, code, img_path):
    my_cursor.execute(f'INSERT INTO employee(id, firstname, lastname, birthday, code, img_path) VALUES("{id}", "{firstname}", "{lastname}", "{birthday}", "{code}", "{img_path}")')
    connect.commit()


def delete(id):
    my_cursor.execute(f'DELETE FROM employee WHERE id={id}')
    connect.commit()


def update(id, firstname, lastname, birthday, code, img_path):
    my_cursor.execute(f'UPDATE employee SET (id, firstname, lastname, birthday, code, edit)VALUES("{id}", "{firstname}", "{lastname}", "{birthday}", "{code}", "{img_path}") WHERE id={id}')
    connect.commit()


def checkPWD(username , password):
    my_cursor.execute('SELECT * FROM admin')
    result = my_cursor.fetchall()
    if result[0][1] == username and result[0][2] == password:
        return True
    else:
        return False
    

def counter():
    my_cursor.execute('SELECT * FROM employee')
    result = my_cursor.fetchall()
    return len(result)