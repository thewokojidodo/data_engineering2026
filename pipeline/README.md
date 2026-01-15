To set up a data pipeline, the steps are :
    1. Set up an ideal / lean dockerize Virtual Environment image
    2. Using dockerize VE Create a dockerize postgresql
    3. Create a data ingestion script, this may be accomplished by using jupyter notebook/panda/sqlalchemy
    4. Data clean up/scripting via jupyter notebook into postgresql is quite powerful

All steps above can be dockerized.

To query and check out table/data use pgadmin or pgcli to some extent

jupyter notebook is standard to add/drop postgres table

Everything may be simplified via docker-compose

to clean up docker after use check
    1. https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/10-cleanup.md

## Stop All Running Containers

```bash
docker-compose down
```

## Remove Specific Containers

```bash
# List all containers
docker ps -a

# Remove specific container
docker rm <container_id>

# Remove all stopped containers
docker container prune
```

## Remove Docker Images

```bash
# List all images
docker images

# Remove specific image
docker rmi taxi_ingest:v001

# Remove all unused images
docker image prune -a
```

## Remove Docker Volumes

```bash
# List volumes
docker volume ls

# Remove specific volumes
docker volume rm ny_taxi_postgres_data
docker volume rm pgadmin_data

# Remove all unused volumes
docker volume prune
```

## Remove Docker Networks

```bash
# List networks
docker network ls

# Remove specific network
docker network rm pg-network

# Remove all unused networks
docker network prune
```

## Complete Cleanup

Removes ALL Docker resources - use with caution!

```bash
# ⚠️ Warning: This removes ALL Docker resources!
docker system prune -a --volumes
```

## Clean Up Local Files

```bash
# Remove parquet files
rm *.parquet

# Remove Python cache
rm -rf __pycache__ .pytest_cache

# Remove virtual environment (if using venv)
rm -rf .venv
```
