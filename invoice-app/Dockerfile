FROM python:3.10

WORKDIR /app/

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv

RUN pipenv install --system --deploy

COPY . /app/

EXPOSE 80

CMD ["python", "-m", "entrypoint"]