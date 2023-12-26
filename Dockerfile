FROM python:3.10

COPY ./requirements.txt /src/requirements.txt

RUN pip3 install --no-cache-dir -U -r /src/requirements.txt

COPY . /src
WORKDIR src
EXPOSE 8000

RUN python ./manage.py makemigrations
RUN python ./manage.py migrate
ENV C_FORCE_ROOT=1
CMD ["bash", "startup.sh"]
