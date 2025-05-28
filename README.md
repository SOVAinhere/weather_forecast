# Прогноз погоды 🌤️

Небольшое Django-приложение, которое показывает текущую погоду по введённому городу, используя бесплатное API Open-Meteo.

Технологии

- Django
- Bootstrap 5
- JavaScript (автодополнение)
- Open-Meteo API (геолокация + погода)

Что умеет

- Ввод города и получение прогноза
- Автодополнение при вводе (реализовано через JS)
- Уведомление, если город не найден

Установка


git clone ...
cd weather_project
python -m venv venv
source venv/bin/activate  или venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
