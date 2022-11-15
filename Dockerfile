FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]