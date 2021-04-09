FROM ubuntu:20.04

# install requirements
COPY . /opt/
RUN pip install -r requirements.txt


CMD [python3 testbotmsg.py]
