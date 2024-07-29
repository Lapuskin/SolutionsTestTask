FROM python:3.12.3

RUN mkdir SolutionsTestTask

WORKDIR /SolutionsTestTask

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR apitask

RUN python3 manage.py migrate

RUN python3 manage.py test

RUN python3 manage.py < scripts/load_database.py

CMD python3 manage.py runserver 0.0.0.0:8000