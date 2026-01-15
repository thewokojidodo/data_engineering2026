To set up a data pipeline, the steps are :
    1. Set up an ideal / lean dockerize Virtual Environment image
    2. Using dockerize VE Create a dockerize postgresql
    3. Create a data ingestion script, this may be accomplished by using jupyter notebook/panda/sqlalchemy
    4. Data clean up/scripting via jupyter notebook into postgresql is quite powerful

All steps above can be dockerized.

To query and check out table/data use pgadmin or pgcli to some extent

jupyter notebook is standard to add/drop postgres table

Everything may be simplified via docker-compose