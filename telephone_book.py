import psycopg2

while True:
    info = int(input(f'1.Создать таблицу\n'
                     f'2.Добавить пользователя\n'
                     f'3.Изменить значения пользователя\n'
                     f'4.Изменить номер\n'
                     f'5.Удалить пользователя\n'
                     f'6.Вывести всю информацию\n'
                     f'Введите цифру для начала работы: '))
    if info == 1:

        def funcone():
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("CREATE TABLE Telephone_book"
                           "(id SERIAL PRIMARY KEY,"
                           "name VARCHAR(50),"
                           "lastname VARCHAR(50),"
                           "email VARCHAR(20),"
                           "numphone VARCHAR(30) )")
            conn.commit()
            conn.close()
            cursor.close()


        funcone()


    elif info == 2:
        a = input('Введите имя пользователя: ')
        b = input('Введите фамилию: ')
        c = input('Введите email пользователя: ')
        f = input('Введите телефон пользователя: ')


        def funcone(a, b, c, f):
            cortegh = (a, b, c, f)
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("INSERT INTO Telephone_book(name,lastname,email,numphone) VALUES (%s,%s,%s,%s)", cortegh)

            conn.commit()
            conn.close()
            cursor.close()


        funcone(a, b, c, f)
    elif info == 3:
        id1 = int(input('id пользователя: '))
        a = input('Введите имя пользователя: ')
        b = input('Введите фамилию: ')
        c = input('Введите email пользователя: ')
        f = input('Введите телефон пользователя: ')


        def funcone(id, a, b, c, f):
            cortegh = (a, b, c, f, id)
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("UPDATE Telephone_book SET name=%s, lastname=%s ,email = %s, numphone=%s WHERE id=%s", cortegh)

            conn.commit()
            conn.close()
            cursor.close()


        funcone(id1, a, b, c, f)
    elif info == 4:
        id1 = int(input('id пользователя: '))
        f = input('телефон пользователя: ')


        def funcone(f, id1):
            cortegh = (f, id1)
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("UPDATE Telephone_book SET numphone=%s WHERE id=%s", cortegh)

            conn.commit()
            conn.close()
            cursor.close()


        funcone(f, id1)
    elif info == 5:
        id1 = int(input('id пользователя: '))


        def funcone(id1, ):
            cortegh = (id1,)
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("DELETE FROM Telephone_book WHERE id=%s", cortegh)

            conn.commit()
            conn.close()
            cursor.close()


        funcone(id1)

    elif info == 6:
        def funcone():
            cortegh = ()
            conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Telephone_book",
                           cortegh)
            print(cursor.fetchall())

            conn.commit()
            conn.close()
            cursor.close()

        funcone()
