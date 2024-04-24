class ConnectionError(Exception):
    def __init__(self, message):
        super(ConnectionError, self).__init__(message)

class InvalidRepositoryResponse(Exception):
    def __init__(self, message):
        super(InvalidRepositoryResponse, self).__init__(message)

class RepositoryResponseParseError(Exception):
    def __init__(self, message):
        super(RepositoryResponseParseError, self).__init__(message)

class RepositoryEndpointError(Exception):
    def __init__(self, message):
        super(RepositoryEndpointError, self).__init__(message)

class RepositoryNotFound(Exception):
    def __init__(self, message):
        super(RepositoryNotFound, self).__init__(message)