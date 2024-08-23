from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import engine, meta_data

chat =  Table("chats", meta_data,
    Column('id', Integer ,primary_key=True),
    Column('class_id', Integer),
    Column('question', Text, nullable=False),
    Column('response', Text, nullable=False),
)

meta_data.create_all(engine)