from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CUSTOMERS_DATA = Path(BASE_DIR, 'homework-1', 'north_data', 'customers_data.csv')
EMPLOYEES_DATA = Path(BASE_DIR, 'homework-1', 'north_data', 'employees_data.csv')
ORDERS_DATA = Path(BASE_DIR, 'homework-1', 'north_data', 'orders_data.csv')