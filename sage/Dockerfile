FROM sagemath/sagemath:10.0 as base
COPY sage/texmf /home/sage/texmf
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN apt update && apt install -y \
    rsync \
    vim \
    less \
    texlive-* \
    git

FROM base AS watcher
ENV UPLOAD_DIR=/files/uploads
ADD sage/docker-entrypoint.sh /usr/local/bin/
ADD sage/file-watcher.py /home/sage/
ADD sage/file-processor.sh /home/sage/
USER sage
RUN sage -pip install watchdog pdflatex
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sage"]