from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from mysql_url import url

"""the imported modules enables for the creation of an engine and to support  raw sql  code using text
the sessionmaker creates sessions for execution and other numerous actions especially in  DDL related
actions. the url is kept in a separate module for security purposes"""
# converts the function into a string object to be passed in the engine
url = url()
# create an sql statement for execution
stmt = "CREATE DATABASE montessori"

# create an engine to enable the connection between the database and the client
engine = create_engine(url, echo=True)
# create a session responsible for DDL related actions on the database
Session = sessionmaker(engine)
session = Session()
# execute DDL codes on the db from the client
session.execute(text(stmt))
# commits actions to the db
session.commit()
# ends the connection to the db
session.close()
