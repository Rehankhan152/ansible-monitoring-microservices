FROM ubuntu:22.04
RUN apt-get update && apt-get install -y wget tar adduser libfontconfig
RUN wget https://dl.grafana.com/oss/release/grafana-10.0.2.linux-amd64.tar.gz && \
    tar -zxvf grafana-*.tar.gz && mv grafana-10.0.2 /grafana && rm *.tar.gz
EXPOSE 3000
CMD ["/grafana/bin/grafana-server", "--homepath=/grafana"]