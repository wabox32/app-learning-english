from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root_password@localhost:3307/learning")
conn = engine.connect()

meta_data = MetaData()