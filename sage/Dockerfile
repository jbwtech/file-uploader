FROM sagemath/sagemath:10.0 as base
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN apt update && apt install -y \
    rsync \
    vim \
    less \
    texlive-* \
    git

FROM base AS watcher
ADD sage/docker-entrypoint.sh /usr/local/bin/
USER sage
ADD sage/file-watcher.py /home/sage/
ADD sage/file-processor.sh /home/sage/
ADD sage/texmf /home/sage/texmf
RUN sudo chown -R sage:sage ~/texmf && rsync -avr sage/local/var/lib/sage/venv-python3.11.1/share/texmf/tex/latex/sagetex ~/texmf/tex/latex/
RUN sage -pip install watchdog pdflatex
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sage"]
