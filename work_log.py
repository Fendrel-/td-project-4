from Entry import db, Entry

if __name__ == "__main__":
    db.connect()
    db.create_tables([Entry])
