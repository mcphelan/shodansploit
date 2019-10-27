FROM python:3.8.0-alpine3.10

RUN apk add git
RUN git clone https://github.com/mcphelan/shodansploit.git  /tmp/mcphelanshodansploit

WORKDIR /tmp/mcphelanshodansploit
RUN pip install requests

ENTRYPOINT ["python", "shodansploit.py"]
