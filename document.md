## Headers

In order to make headers searchable instead of releases Basenji stores the headers
in the database.

**Format**

```json
{
    "_id"         : "base64 encoded string of message-id",
    "subject"     : "string containing the subject of the header",
    "date"        : "the date of the header",
    "group"       : "group the header was fetched from",
    "message-id"  : "the message-id for this post",
    "bytes"       : "the size of the header"
}
```

**Example**

```json
{
   "_id": "NTBmNDc0NTIkMCQxMTQzMyRjMDBiN2VjNkA5NC4yMzIuMTE2Ljcx",
   "subject": "[3/3] - THVVDZEDKVDWP2HV.rar.vol0+1.PAR2 (2/2)",
   "date": "14 Jan 2013 21:10:45 GMT",
   "group": "alt.binaries.ebooks",
   "message-id": "50f47452$0$11433$c00b7ec6@94.232.116.71",
   "bytes": "224051"
}
```

## Relases

The Basenji platform works by creating releases of the headers. With these we can get information
from imdb, thetvdb, tvrage and others. All releases are stored in the following json format. 

**Format**

```json
{
    "_id"         : "base64 encoded string of the first message-id",
    "name"        : "name for the release",
    "date"        : "date the last header past posted",
    "group"       : "group the headers was posted to",
    "headers"     : [
        "list of all the headers in this release"
    ],
    "bytes"       : "size of the release in bytes",
    "category"    : "category for this release",
    "information" : {
        "json": "a json document containing information fetched from external resources"
    }
}
```