from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine("postgresql://app_user:app_pass@db:5432/app_db")
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
