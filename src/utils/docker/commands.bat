REM 'https://www.dbvis.com/thetable/how-to-set-up-postgres-using-docker/'

@echo off
REM Script to set up PostgreSQL and Spark using Docker

REM Start PostgreSQL
echo Starting PostgreSQL container...
@REM REM docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres
docker run -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres


REM Wait for a moment for PostgreSQL to start
timeout /t 5 /nobreak >nul

REM Start Spark container
echo Starting Spark container...
docker run -d -p 4040:4040 -it spark:python3 /opt/spark/bin/pyspark

REM End of script
