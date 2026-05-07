from flask import Flask, render_template
import sqlalchemy
from extensions import db

# Імпорт моделей обов'язковий перед db.create_all()
import models 

from api.courses import courses_bp
from api.disciplines import disciplines_bp
from api.groups import groups_bp
from api.students import students_bp
from api.teachers import teachers_bp

app = Flask(__name__)

# Використовуємо 127.0.0.1 замість localhost для Mac
connection_string = 'mssql+pyodbc://sa:Kikorik9!@127.0.0.1:14330/university?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Реєстрація Blueprint
app.register_blueprint(courses_bp)
app.register_blueprint(disciplines_bp)
app.register_blueprint(groups_bp)
app.register_blueprint(students_bp)
app.register_blueprint(teachers_bp)

# --- АВТОМАТИЧНЕ СТВОРЕННЯ БАЗИ ТА ТАБЛИЦЬ ---
def setup_database():
    # 1. Тимчасово підключаємось до системної бази master, щоб створити university
    master_uri = connection_string.replace('/university', '/master')
    engine = sqlalchemy.create_engine(master_uri)
    
    with engine.connect() as conn:
        conn.execution_options(isolation_level="AUTOCOMMIT")
        # Перевіряємо чи є база, якщо нема - створюємо
        exists = conn.execute(sqlalchemy.text("SELECT database_id FROM sys.databases WHERE name = 'university'")).fetchone()
        if not exists:
            conn.execute(sqlalchemy.text("CREATE DATABASE university"))
            print("База даних 'university' створена успішно!")

    # 2. Створюємо всі таблиці на основі моделей
    with app.app_context():
        db.create_all()
        print("Всі таблиці створені!")

# Запускаємо налаштування перед стартом
setup_database()

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)