FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY service.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python3", "service.py"]