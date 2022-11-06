from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ


SQLALCHEMY_DATABASE_URL = f"postgresql://streamlit_app:{environ['POSTAMAT_PG_PASS']}@135.181.97.90:25432/geo"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
