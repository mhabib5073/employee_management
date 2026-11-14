from sqlalchemy.engine import URL

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",  
    username="postgres",
    password="admin1234",
    host="localhost",
    port=5432,
    database="employee_db"
)