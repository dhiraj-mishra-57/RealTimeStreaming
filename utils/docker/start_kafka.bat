@echo off
REM Script to set up Kafka & Zookeeper

REM Start Kafka & Zookeeper
echo Starting Kafka & Zookeeper container...
docker-compose -f ./docker-compose.yml up -d

REM End of script
