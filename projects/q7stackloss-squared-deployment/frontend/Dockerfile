FROM python:3.11

WORKDIR /app/

COPY ./requirements.txt /app/
COPY ./.env /app/
RUN pip install --no-cache-dir -r ./requirements.txt

ENV ENVIRONMENT production

COPY ./app.py /app/

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

  