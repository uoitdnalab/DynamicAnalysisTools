FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install git python perl libwww-perl mitmproxy iputils-ping
RUN apt-get -y install python-requests
RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
RUN git clone https://github.com/commixproject/commix.git commix
RUN git clone https://github.com/wireghoul/dotdotpwn.git dotdotpwn
COPY run_commix_tests.sh /
COPY run_sqlmap_tests.sh /
COPY run_dotdotpwn_tests.sh /dotdotpwn
COPY test_url.py /dotdotpwn
