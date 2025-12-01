from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres_123",
    host="localhost",
    database="crud_tutorial",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
