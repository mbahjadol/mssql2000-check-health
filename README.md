# mssql2000-check-health
Check ancient MS SQL 2000 health in web service

### Build
    $ docker build -t mbahjadol/mssql2000-health-check .

### Run
    $ docker run -d \
    -e MSSQL_USER=sa \
    -e MSSQL_PASS=SuperSecret123 \
    -e MSSQL_HOST=192.168.1.100 \
    -e MSSQL_DB=master \
    -e APP_PORT=8080 \
    -p 8080:8080 \
    mssql2000-health-check

### Check
    $ curl http://localhost:8080/health

#### It will result OK with:
    {
        "result": 1,
        "status": "ok"
    }

#### If not OK then:
    will response http status 500 or else

### Docker Image:
    build container image that ready to use can be pull at
    https://hub.docker.com/r/mbahjadol/mssql2000-health-check