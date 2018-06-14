@manager.command
def resetdb():
    """ Drop & create a database with all of the tables defined in
        your SQLAlchemy models.
        DO NOT USE IN PRODUCTION.
    """
    if env == "dev":
        db.drop_all()
        db.create_all()
        seed()
        print("Dropped")


if __name__ == "__main__":
