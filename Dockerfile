FROM python:3.7-slim
RUN mkdir /app
COPY req_deploy.txt /app
RUN pip3 install -r /app/req_deploy.txt --no-cache-dir
COPY api_yamdb/ /app
WORKDIR /app
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
