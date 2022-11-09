FROM python:3.8

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt #встановлюємо наші requirements внашому випадку тільки flask

CMD ./wait-for-it.sh database:3306 -- python app.py