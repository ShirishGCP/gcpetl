FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV NAME gcpetl
CMD ["python", "./src/main_module.py"]