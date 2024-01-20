REM 'https://www.dbvis.com/thetable/how-to-set-up-postgres-using-docker/'

@echo off
REM Script to set up PostgreSQL and Spark using Docker

REM Start PostgreSQL
echo Starting PostgreSQL container...
@REM REM docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres
docker run -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres

REM End of script
