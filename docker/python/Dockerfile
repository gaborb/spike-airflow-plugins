FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./setup.py", "test" ]