FROM python:3.10-alpine3.13
LABEL authors="helder"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy files
COPY ./app/ /app/
COPY requerimentos.txt /app/


WORKDIR /app/

# port container
#EXPOSE 8000

#config
RUN ls -la
RUN apk update
RUN apk upgrade
RUN apk add pkgconfig
RUN apk add --no-cache gcc musl-dev mariadb-dev mariadb-connector-c-dev
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