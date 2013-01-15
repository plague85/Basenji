import couchdb


class CouchDBAdaptor:
    """CouchDB adaptor for Basenji"""

    def __init__(self):
        self.couch = couchdb.Server()

    def get_or_create_db(self, name):
        """Gets an database or creates it should it not exist"""
        try:
            db = self.couch.create(name)
        except Exception:
            db = self.couch[name]

        return db

    def get(self, name, doc):
        """Gets the document associated with the ID from the given database"""

        if name in self.couch:
            # Load the database or create it if not existing
            db = self.get_or_create_db(name)

            # Try the get the document from the database
            try:
                # Return the document if it exists in the database
                return db[doc]
            except Exception:
                # We have no document with that id, report
                print("Tried to get document with id '%s' that does not exist" % (doc))

                # Return None since we do not have any document
                return None
        else:
            # Since the database does not exit the document doesn't exist either
            print("Tried to fetch document from non-existing database %s, possibly misspelled" % (name))

            # Return None since we do not have any document
            return None
