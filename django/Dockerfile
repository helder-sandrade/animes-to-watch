FROM python:3.10-bookworm
LABEL authors="helder"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy files
COPY ./app/ /app/
COPY requerimentos.txt /app/

WORKDIR /app/

# Instalando o python3 e o pip
RUN apt-get update && apt-get install -y  \
    wget \
    netcat-openbsd \
    xvfb \
    mariadb-client \
    mlocate \
    python3-dev  \
    build-essential  \
    pkg-config


# configurando o python
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN rm -rf google-chrome-stable_current_amd64.deb
RUN python -m venv /venv
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install --no-cache-dir -r /app/requerimentos.txt
RUN chmod -R +x /app/docker_scripts
RUN mkdir -p /data/static
RUN mkdir -p /data/media

# add path
ENV PATH="/app/docker_scripts:/venv/bin:$PATH"

#exec commands
CMD ["commands.sh"]
#CMD ["top", "-b"]