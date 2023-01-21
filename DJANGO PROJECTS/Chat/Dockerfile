FROM python:3.10
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /app
COPY . /app
RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver"]
