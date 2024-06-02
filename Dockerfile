FROM python:3.9-slim
WORKDIR /gcpetl
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN ls -l
EXPOSE 5000
ENV FLASK_APP=src/app.py
CMD ["flask", "run", "--host=0.0.0.0"]
