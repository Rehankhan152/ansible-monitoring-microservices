FROM ubuntu:22.04
RUN apt-get update && apt-get install -y wget tar
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz && \
    tar xvf prometheus-*.tar.gz && mv prometheus-2.45.0.linux-amd64 /prometheus && \
    rm *.tar.gz
EXPOSE 9090
CMD ["/prometheus/prometheus", "--config.file=/prometheus/prometheus.yml"]