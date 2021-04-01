FROM python:3.8
LABEL MAINTAINER="Ali Moradi | ali.mrd318@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /alfax
WORKDIR /alfax
COPY . /alfax

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input


CMD ["gunicorn", "--chdir", "alfax", "--bind", ":8000", "alfax.wsgi:application"]
