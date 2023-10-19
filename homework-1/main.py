"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from csv import DictReader
import settings

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Irgvel"
)

cur = conn.cursor()


#Заполнение таблицы customers
with open(settings.CUSTOMERS_DATA, encoding="utf-8") as file:
    dict_obj = DictReader(file)
    for row in dict_obj:
        customer_id = row['customer_id']
        company_name = row['company_name']
        contact_name = row['contact_name']
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer_id, company_name, contact_name))


#Заполнение таблицы employees
with open(settings.EMPLOYEES_DATA, encoding="utf-8") as file:
    dict_obj = DictReader(file)
    for row in dict_obj:
        employee_id = row['employee_id']
        first_name = row['first_name']
        last_name = row['last_name']
        title = row['title']
        birth_date = row['birth_date']
        notes = row['notes']
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee_id, first_name, last_name,
                                                                              title, birth_date, notes))


#Заполнение таблицы orders
with open(settings.ORDERS_DATA, encoding="utf-8") as file:
    dict_obj = DictReader(file)
    for row in dict_obj:
        order_id = row['order_id']
        customer_id = row['customer_id']
        employee_id = row['employee_id']
        order_date = row['order_date']
        ship_city = row['ship_city']
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order_id, customer_id, employee_id,
                                                                          order_date, ship_city))
conn.commit()

cur.close()
conn.close()