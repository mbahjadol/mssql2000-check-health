# mssql2000-check-health
Check ancient MS SQL 2000 health in web service

# Build
$ docker build -t mssql2000-health-check .

# Run
$ docker run -d \
  -e MSSQL_USER=sa \
  -e MSSQL_PASS=SuperSecret123 \
  -e MSSQL_HOST=192.168.1.100 \
  -e MSSQL_DB=master \
  -e APP_PORT=8080 \
  -p 8080:8080 \
  mssql2000-health-check

# Check
curl http://localhost:8080/health
