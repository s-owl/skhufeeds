FROM debian:stretch-slim

ENV CADDYPATH="/usr/caddyfiles"

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install curl \
  && curl https://getcaddy.com | bash \
  && mkdir -p /usr/caddyfiles
WORKDIR /usr/caddyfiles

COPY Caddyfile /usr/caddyfiles/Caddyfile

EXPOSE 80 443 2015

CMD [ "caddy", "-conf", "/usr/caddyfiles/Caddyfile", "--log", "stdout"]
