FROM python:3.10-slim
WORKDIR /app
RUN pip install ecdsa
# copy the mining script into the container
COPY mine.py /app/mine.py
#now run the mining script
CMD ["python", "/app/mine.py"]
