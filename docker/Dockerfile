FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /DeporterDEV/


COPY ../requirements/base.txt ../requirements/base.txt
RUN pip install --no-cache-dir -r ../requirements/base.txt


COPY . .


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ReporterDEV.ReporterDEV.wsgi:application"]
