from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(environ.get(key='DATABASE_URL'))

meta = MetaData(engine)

Session = sessionmaker(bind=engine)

session = Session()