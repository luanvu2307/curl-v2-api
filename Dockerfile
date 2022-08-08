FROM ubuntu

ENV PYTHONDONTWRITEBYTECODE=1
RUN apt-get update
RUN apt install -y build-essential pkg-config cmake ninja-build curl autoconf automake libtool wget
RUN apt install -y golang-go unzip
RUN apt install -y software-properties-common

ARG DEBIAN_FRONTEND=noninteractive 
ENV TZ=Asia/UTC

ENV LANG=C.UTF-8


# set locale
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
ENV TZ=Asia/Ho_Chi_Minh
RUN apt install --no-install-recommends -y tk-dev apt-utils tzdata locales
RUN locale-gen en_US.UTF-8
RUN apt update
RUN apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev
RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
RUN tar -xf Python-3.9.1.tgz
WORKDIR /Python-3.9.1
RUN bash configure --enable-optimizations
RUN make -j 12
RUN make altinstall

COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

COPY curl-install /home/
WORKDIR /home/
RUN bash run.sh
ENV PYTHONUNBUFFERED=1
ENV PORT 2307
EXPOSE 2307

COPY gunicorn-config.py ./
CMD exec gunicorn main:app -c ./gunicorn-config.py
# CMD ["/bin/bash"]