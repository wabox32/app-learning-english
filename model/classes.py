from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import engine, meta_data

classes =  Table("classes", meta_data,
    Column('id', Integer ,primary_key=True),
    Column('level_id', Integer),
    Column('name',  String('255'), nullable=False),
    Column('description', Text, nullable=False),
    Column('prompt_question', Text, nullable=False),
    Column('prompt_response', Text, nullable=False)
)

meta_data.create_all(engine)