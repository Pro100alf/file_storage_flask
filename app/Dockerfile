FROM python:3.10.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV WORKDIR=/app

RUN mkdir -p ./logs

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry==1.3.2
RUN poetry config virtualenvs.create false

COPY poetry.lock* pyproject.toml ./
ARG INSTALL_DEV=false
RUN echo Install dev packages: $INSTALL_DEV
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install ; else poetry install --no-dev ; fi"

COPY ./ $WORKDIR

CMD bash -c "gunicorn -b 0.0.0.0:5000 'app:create_app()'"