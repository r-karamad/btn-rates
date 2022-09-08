FROM python:3.10-slim as build

WORKDIR /btn-rates

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /btn-rates/
RUN pip install -r requirements.txt

FROM python:3.10-slim as deploy

COPY --from=build /opt/venv /opt/venv

WORKDIR /btn-rates

COPY . /btn-rates/

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
