import couchdb
import logging


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
            # Load the database
            db = self.get_or_create_db(name)

            # Try the get the document from the database
            try:
                # Return the document if it exists in the database
                return db[doc]
            except Exception:
                # We have no document with that id, report
                logging.warning("Tried to get document with id '%s' that does not exist" % (doc))

                # Return None since we do not have any document
                return None
        else:
            # Since the database does not exit the document doesn't exist either
            logging.warning("Tried to fetch document from non-existing database %s, possibly misspelled" % (name))

            # Return None since we do not have any document
            return None

    def add(self, name, docs):
        """Preforms an bulk update or insert to the database"""

        if name in self.couch:
            # Load the database
            db = self.get_or_create_db(name)

            # List containing any failed documents
            failed_docs = list()

            # Save the documents to the database
            for doc in db.update(docs):
                # Check so that all inserts or updates went okay
                if not doc[0]:
                    # Store the '_id' for the document that failed
                    failed_docs.append(doc[1])

            # Return failed_docs when done
            return failed_docs
