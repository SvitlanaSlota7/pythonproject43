from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """Головна сторінка курсу."""
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Сторінка реєстрації. Обробляє як показ форми, так і відправку даних."""
    if request.method == 'POST':
        # Отримуємо дані, які користувач ввів у форму
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Для демонстрації просто виведемо їх у консоль PyCharm
        print(f"Нова заявка на курс! Ім'я: {username}, Email: {email}, Тел: {phone}")

        # Після успішної реєстрації повертаємо користувача на головну
        return redirect(url_for('index'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)