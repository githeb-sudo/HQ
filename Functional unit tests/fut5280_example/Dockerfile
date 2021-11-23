# Using clean debian9 image
FROM debian:9


# Installing all essentials
RUN apt-get update && \
 apt-get install -y \
 build-essential \
 zlib1g-dev \
 dpkg \
 unzip \
 libncurses5-dev \
 libgdbm-dev \
 libnss3-dev \
 libssl-dev \
 libreadline-dev \
 libffi-dev \
 curl \
 procps \
 ssh \
 sshpass \
 virtualenv

# Installing python 3.7.3
RUN curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz && \
 tar -xf Python-3.7.3.tar.xz && \
 cd Python-3.7.3 && \
 ./configure --enable-optimizations && \
 make altinstall && \
 curl -O https://bootstrap.pypa.io/get-pip.py && \
 python3.7 get-pip.py && \
 update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.7 1 && \
 cd .. && rm -rf Python-3*

# JDK required for Allure generation
RUN mkdir -p /usr/share/man/man1 && \
 apt-get install -y openjdk-8-jdk && \
 apt-get autoremove -y

RUN apt-get install sudo \
 wget

# Install allure
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.10.0/allure-commandline-2.10.0.zip && \
 unzip allure-*.zip && rm allure-*.zip && mv allure-* allure && mv allure /usr/local/lib/
ARG allure_bin_arg=/usr/local/lib/allure/bin/allure
ENV ALLURE_BIN_FILE=$allure_bin_arg

RUN curl -O --location http://netfilter.org/pub/iptables/iptables-1.8.4.tar.bz2 && \
    tar -xf iptables-1.8.4.tar.bz2 && \
    cd iptables-1.8.4 && \
    ./configure --prefix=/usr \
        --sbindir=/sbin \
        --disable-nftables \
        --enable-libipq \
        --with-xtlibdir=/lib/xtables && \
    make
RUN cd iptables-1.8.4 && \
 make install && \
 ln -sfv ../../sbin/xtables-legacy-multi /usr/bin/iptables-xml

RUN for file in ip4tc ip6tc ipq xtables; do mv -v /usr/lib/lib${file}.so.* /lib && ln -sfv ../../lib/$(readlink /usr/lib/lib${file}.so) /usr/lib/lib${file}.so; done
RUN cd .. && rm -rf iptables*

RUN apt-get install -y liblua5.3-0 libpcre2-8-0
ARG haproxy_package=haproxy_1.8.19-1+deb10u2~bpo9+1_armhf.deb
RUN wget http://ftp.de.debian.org/debian/pool/main/h/haproxy/$haproxy_package
RUN yes | dpkg -i $haproxy_package

RUN apt-get update && \
 apt-get install -y nginx
#COPY ./data/etc/nginx/sites-available/default /etc/nginx/sites-available/default

# Install Mosquitto
RUN apt-get update && \
 apt-get install -y mosquitto

# Installing PIP libraries
#  butterfly          3.2.5
#  butterfly[themes]
#  butterfly[systemd]
#  flask              1.1.2
#  flask-cors         3.0.1
#  pexpect            4.8.0
#  psutil             5.8.0
#  mock               4.0.3
#  responses          0.12.1
#  requests           2.25.1
#  filelock           3.0.12
#  PyYAML             5.3.1
#  xmltodict          0.12.
#  pytest             6.2.1
#  pytest-timeout     1.4.2
#  paramiko           2.7.2
#  allure-pytest      2.8.3
#  pytest-dependency  0.5.1
#  pytest-ordering    0.6


RUN pip install \
 cryptography \
 butterfly==3.2.5 \
 butterfly[themes] \
 butterfly[systemd] \
 flask==1.1.2 \
 flask-cors==3.0.10

RUN pip install \
 pexpect==4.8.0 \
 psutil==5.8.0 \
 mock==4.0.3 \
 responses==0.12.1 \
 requests==2.25.1 \
 filelock==3.0.12 \
 PyYAML==5.3.1 \
 xmltodict==0.12.0

RUN pip install \
 pytest==6.2.1 \
 pytest-timeout==1.4.2 \
 paramiko==2.7.2 \
 allure-pytest==2.8.31

RUN pip install \
 pytest-dependency==0.5.1 \
 pytest-ordering==0.6

# Settings - Need root for butterfly server
COPY ./data/.bashrc /root/.bashrc
COPY ./data/.ssh/config /root/.ssh/config
COPY ./data/scripts/ /root/scripts/
RUN \
 chown root:root -R /root/.ssh && \
 chown root:root /root/.bashrc && \
 chown root:root -R /root/scripts && \
 echo "root:root" | chpasswd

RUN addgroup ---- && useradd -rm -d /home/dir -s /bin/bash -g ---- -G sudo -u 1000 ---- -p ------
COPY ./data/.bashrc /home/dir/.bashrc
COPY ./data/.ssh/config /home/dir/.ssh/config
COPY ./data/scripts/ /home/dir/scripts/
RUN \
 chown ----:---- -R /home/dir/.ssh && \
 chown ----:---- /home/dir/.bashrc && \
 chown ----:---- -R /home/dir/scripts && \
 echo "----:----" | chpasswd

RUN echo "%----:----     ALL=NOPASSWD: ALL" >> /etc/sudoers 

RUN mkdir -p /var/www/app/logs/
