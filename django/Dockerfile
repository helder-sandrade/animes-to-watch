FROM python:3.10-bookworm
LABEL authors="helder"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=America/Sao_Paulo

# copy files
COPY ./app/ /app/
COPY requerimentos.txt /app/

WORKDIR /app/

# Default packege
RUN apt-get update && apt-get install -y  \
    wget \
    netcat-openbsd \
    mariadb-client \
    mlocate \
    python3-dev  \
    build-essential  \
    pkg-config \
    inetutils-ping

# configurando o python
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