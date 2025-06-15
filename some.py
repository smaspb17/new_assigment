from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('SELECT id, price, discount FROM new_app_book')
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Посмотрим сырые данные из базы