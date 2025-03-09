FROM python:3.11

WORKDIR /app/

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r ./requirements.txt

ENV ENVIRONMENT production

COPY ./app /app/

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

