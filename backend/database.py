# set up database connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///./auth_project.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} # for multithreaded app
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# create db
def init_db():
    try:
        print("initializing db")
        Base.metadata.create_all(bind=engine)
        print("created db")
    except Exception as e:
        print(e)

# get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
