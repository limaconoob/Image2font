FROM debian:jessie
LABEL name="debianimage2font"
MAINTAINER limaconoob <limaconoob@users.noreply.github.com>, adjivas <adjivas@users.noreply.github.com>
ENV USER root
ENV HOME /root
ENV LANG en_US.UTF-8
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends build-essential ca-certificates git fontforge python python-fontforge imagemagick potrace
RUN git clone --depth=50 --branch=master https://github.com/limaconoob/Image2font.git /root/image2font
ENTRYPOINT bash
WORKDIR $HOME/image2font
