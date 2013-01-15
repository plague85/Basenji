# The amount of days back we should scan when adding new groups
NEW_GROUP_SCAN_DAYS = 1

# The amount of messages we should download at a time
HEADER_DOWNLOAD_AMOUNT = 20000

# Using compressed headers will reduce bandwidth but increase
# processing time.
USE_COMPRESSED_HEADERS = True

# Here you configure all the providers that you want to use,
# more providers means that you can have even more workers running.
providers = dict(
    # A sample provider configuration for AstraWeb with SSL
    astra = dict(
        # Host address to the server
        host = "ssl-eu.astraweb.com",

        # Port for the server
        port = 443,

        # Secure access to the provider, make sure the port
        # is the correct on if you set to True.
        secure = True,

        # Credentials for accessing the provider
        username = "...",
        password = "...",

        # The amount of connections each worker should use, more connetions
        # mens that more groups can simultaniously be updated.
        connections = 10
    )
)

# Configuration for the NoSQL database we should use, currently only
# CouchDB is available as an adaptor.
database = dict(
    # The adaptor for the NoSQL database Basenji should use
    adaptor = "couchdb",

    # Host address to the database server
    host = "http://localhost:8984/",

    # Name of all the databases we should use for each task
    databases = dict(
        # Name of the database were we store releases
        releases = "releases",

        # Name of the database were we store binaries
        binaries = "binaries"
    )
)