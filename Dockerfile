FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./power_measuring_plugin.py"]
#CMD ["python", "./image_generating_plugin.py"]
CMD ["python", "./accuracy_measuring_plugin.py"]
