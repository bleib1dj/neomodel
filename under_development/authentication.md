# Authentication
In the release of Neo4j 2.2 authentication has been turned on by default. If you wish to continue interacting
with the database without it you'll need to deactivate it manually. You can use the steps outlined in the
[security server auth](http://neo4j.com/docs/stable/security-server.html#security-server-auth) docs to do so
although it is not recommended.

Please also note that before utilizing neomodel to connect with the server you'll need to change the default
password or you'll see 403 errors thrown by the Neo4j REST interface. To do this you can follow the steps
outlined in py2neo's [Authentication](http://py2neo.org/2.0/essentials.html?highlight=authenticate#py2neo.authenticate)
docs. As the docs outline you can run the following command to update your password:

```
neoauth neo4j neo4j my-p4ssword
```



# Logging
You can access the neomodel logs by creating a handler for `neomodel.util`.


def __init__(self, _url):
        if hasattr(self, 'session'):
            raise SystemError('__init__ called too many times')

        parse_result = urlparse(_url)
        if parse_result.netloc.find('@') > -1:
            credentials, self.host = parse_result.netloc.split('@')
            self.user, self.password, = credentials.split(':')
            authenticate(self.host, self.user, self.password)
        else:
            self.url = _url
        self.graph = Graph(_url)