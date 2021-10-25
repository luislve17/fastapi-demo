FROM python:3.8.10

RUN mkdir /source
WORKDIR /source

RUN pip install --upgrade pip
COPY ./backend/source/requirements.txt /source/
RUN pip3 install -r requirements.txt

COPY ./backend/source/start.sh /source/
RUN chmod +x start.sh
CMD ["bash", "/source/start.sh"]