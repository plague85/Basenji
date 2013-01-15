# The amount of days back we should scan when adding new groups
NEW_GROUP_SCAN_DAYS = 1

# The amount of messages we should download at a time
HEADER_DOWNLOAD_AMOUNT = 20000

# Using compressed headers will reduce bandwidth but increase
# processing time.
USE_COMPRESSED_HEADERS = True

# Here you configure all the providers that you want to use,
# more providers means that you can have even more workers running.
providers = {
    # A sample provider configuration for AstraWeb with SSL
    "astra": {
        # Host address to the server
        "host": "ssl-eu.astraweb.com",

        # Port for the server
        "port": 443,

        # Secure access to the provider, make sure the port
        # is the correct on if you set to True.
        "secure": True,

        # Credentials for accessing the provider
        "username": "...",
        "password": "...",

        # The amount of connections each worker should use, more connetions
        # mens that more groups can simultaniously be updated.
        "connections": 10
    }
}


# Configuration for the NoSQL database we should use, currently only
# CouchDB is available as an adaptor.
database = {
    # The adaptor for the NoSQL database Basenji should use
    "adaptor": "database.CouchDBAdaptor",

    # Host address to the database server
    "host": "http://localhost:8984/",

    # Name of all the databases we should use for each task
    "databases": {
        # Name of the database were we store releases
        "releases": "releases",

        # Name of the database were we store headers
        "headers": "headers"
    }
}

# Configuration for the Python logging module
logging = {
    # Do not change this since this can only have 1 as value
    'version': 1,

    # Configuration for logging formatters
    'formatters': {

        # Simple formatter that is used by Basenji
        'simple': {
            # Message formatting
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',

            # Format for all printed datetimes
            'datefmt': '%m/%d/%Y %H:%M:%S'
        }
    },

    # Configuration for output handlers, can add more advanced handlers
    # if needed.
    'handlers': {

        # Handler for all console output, to easily disable any output
        'console': {

            # Handler class
            'class': "logging.StreamHandler",

            # The formatter to use
            'formatter': "simple",

            # The minimum level we should print
            "level": "DEBUG",

            # The stream we should send to
            "stream": "ext://sys.stdout"
        },

        # Handler for logging to file
        'file': {

            # Handler class, rotates files based on size
            'class': 'logging.handlers.RotatingFileHandler',

            # The formatter to use
            'formatter': 'simple',

            # Minimum level we should output
            'level': 'WARN',

            # The name of the log file we should write to
            'filename': 'basenji.log',

            # Max size of one log file
            'maxBytes': 1024,

            # The amount of backup log files we should keep
            'backupCount': 3
        }
    },

    # Loggers that we can use
    "loggers": {
        # The default basenji logger
        "basenji": {
            # Minimum level to log
            "level": "DEBUG",

            # Handlers we should send the log message to
            "handlers": ["console", "file"]
        }
    },

    # Root logger
    'root': {
        # Minimum level to log
        'level': 'DEBUG',

        # Handlers we should send the log message to
        'handlers': ['console', 'file']
    }
}
