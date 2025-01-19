from flask import Flask, jsonify, render_template
from faker import Faker

app = Flask(__name__)
fake = Faker()

# Генерация данных
def generate_fake_data():
    return {
        "name": fake.name(),
        "gender": fake.random_element(elements=("Male", "Female")),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "email": fake.email(),
        "credit_card": fake.credit_card_full(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y"),
    }

# API для генерации данных
@app.route('/api/generate', methods=['GET'])
def generate():
    return jsonify(generate_fake_data())

# Отображение веб-страницы
@app.route('/')
def home():
    return render_template('htmlfilename')

if __name__ == "__main__":
    app.run(debug=True)
