from sqlalchemy import create_engine, MetaData

url = 'sqlite:///Enterprise'
engine = create_engine(url, echo=True)

mdo = MetaData()
if __name__ == "__main__":

    mdo.create_all(engine)
