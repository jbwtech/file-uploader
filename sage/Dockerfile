FROM sagemath/sagemath:10.0
ADD sage/docker-entrypoint.sh /usr/local/bin/
ADD sage/file-watcher.py /home/sage/
COPY sage/texmf /home/sage/texmf
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    rsync \
    vim \
    less \
    git
USER sage
RUN pip3 install watchdog
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sage"]