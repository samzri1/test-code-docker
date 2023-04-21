# Dockerfile
FROM postgres:latest
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydatabase
# Dockerfile
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD mypassword
ENV MYSQL_DATABASE mydatabase
ENV MYSQL_USER myuser
ENV MYSQL_PASSWORD mypassword
# Dockerfile
FROM mongo:latest
ENV MONGO_INITDB_ROOT_USERNAME myuser
ENV MONGO_INITDB_ROOT_PASSWORD mypassword
ENV MONGO_INITDB_DATABASE mydatabase
