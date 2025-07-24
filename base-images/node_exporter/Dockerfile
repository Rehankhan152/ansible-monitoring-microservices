FROM ubuntu:22.04
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz && \
    tar xvf node_exporter-*.tar.gz && mv node_exporter-1.7.0.linux-amd64 /node_exporter && \
    rm *.tar.gz
EXPOSE 9100
CMD ["/node_exporter/node_exporter"]