FROM python:3.6

WORKDIR /usr/src/app

COPY requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY requirements.txt ./
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes
RUN pip install --no-cache-dir -r requirements.txt

RUN airflow initdb

COPY . .

CMD [ "python", "./setup.py", "develop" ]