FROM miktex/miktex

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get -y install python3-pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]