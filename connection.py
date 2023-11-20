from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
"""Databases are created in mysql using the syntax of "<dialect>+<db_engine>://<username>:<password@hostname>" the 
syntax is different for different dialects. when the database is not created it is required that the database name be 
omitted from the url
in using sqlalchemy to connect the session and the create_engine is used also literal text will not work except the text 
method is also used to add raw sql to the execute method."""


engine = create_engine("mysql+mysqlconnector://root:mistique@127.0.0.1", echo=True)

Session = sessionmaker(engine)
session = Session()

session.execute(text("CREATE DATABASE IF NOT EXISTS school"))
session.commit()
session.close()


