FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN mkdir __logger

RUN apt-get update && apt-get install wget

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN google-chrome --version

# set display port to avoid crash
ENV DISPLAY=:99

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install --upgrade chromedriver-autoinstaller

CMD ["python", "./3_actual_code_test.py"]