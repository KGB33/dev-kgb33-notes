FROM python
RUN apt-get update && \
        apt-get upgrade -y

RUN python -m pip install --upgrade pip

ENV FLASK_APP "notes"
ENV APP_CONFIG "${FLASK_APP}.configs.Production"

COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY notes ./notes

COPY ./prod/gunicorn_config.py .

EXPOSE 5000
