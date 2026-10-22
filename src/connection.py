import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from .env file
load_dotenv()

url = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
engine = create_engine(url) # Create a SQLAlchemy engine for the PostgreSQL database

# Test the connection to the database
with engine.connect() as conn:
    version = conn.execute(text("SELECT version();")).scalar() # Execute a SQL query to get the PostgreSQL version
    print("Successfully connected to:", version.split(",")[0])