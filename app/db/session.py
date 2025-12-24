from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine("postgresql://user:secret123@localhost:5434/mydb")
MySession = sessionmaker(bind = engine)

def get_db():
    db = MySession()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
