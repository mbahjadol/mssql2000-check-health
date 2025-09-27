FROM python:3.11-slim

# Install deps untuk pyodbc + FreeTDS (driver SQL Server lama)
RUN apt-get update && apt-get install -y \
    gcc g++ unixodbc-dev freetds-bin freetds-dev tdsodbc \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip install flask pyodbc

# Copy app
WORKDIR /app
COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
