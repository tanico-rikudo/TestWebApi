FROM python:3.9

WORKDIR /app
RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install -r /app/requirements.txt
RUN python -m pip uninstall python-dotenv
RUN python -m pip install python-dotenv


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

