# store of the connector url
def url():
    string = "mysql+mysqlconnector://root:mistique@127.0.0.1"
    return string


def url_connect(db_name):
    url = f"mysql+mysqlconnector://root:mistique@127.0.0.1/{db_name}"
    return url
