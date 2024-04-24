import requests
from urllib import parse
import json
from .exceptions import  RepositoryResponseParseError, InvalidRepositoryResponse, RepositoryEndpointError
import os
class RestRepository(object):

    HEADER_CONTENT_TYPE = 'Content-Type'
    HEADERS = {HEADER_CONTENT_TYPE : 'application/json',}

    def __init__(self,version):
        self.repository_url = None
        self.version = version
        self.endpoints = None

    def set_repository_url(self,repository_url):
        self.repository_url = repository_url
        return self

    def set_endpoints(self,endpoints):
        self.endpoints = endpoints
        return self

    def get_service_endpoint(self,service_name,absolute=True):
        try:
            return self.endpoints[self.version].get(service_name)
        except KeyError:
            raise RepositoryEndpointError('%s service endpoint not defined' % service_name)

    @property
    def default_headers(self):
        return self.HEADERS

    def format_headers(self,headers):
        if headers:
            self.HEADERS.update(headers)
        return self.HEADERS

    def request(self,type,endpoint,data=None,headers=None):
        if type.lower()=='post':
            return self.post(endpoint,data,headers)
        if type.lower()=='put':
            return self.put(endpoint,data,headers)
        if type.lower()=='delete':
            return self.put(endpoint,data,headers)
        return self.get(endpoint,data,headers)

    def get(self,endpoint,data=None,headers=None,params=None):
        headers = self.format_headers(headers)
        response = requests.get(url=endpoint, headers=headers, data=json.dumps(data),params=params)
        return self.process_response(response)

    def post(self,endpoint, data=None, headers=None, files=None):
        headers = self.format_headers(headers)
        if files:
            response = requests.post(url=endpoint, files=files, data=None)
            return self.process_response(response)
        else:
            response = requests.post(url=endpoint, headers=headers, data=json.dumps(data))
            return self.process_response(response)

    def put(self, endpoint, data=None, files=None, headers=None):
        headers = self.format_headers(headers)
        if files:
            response = requests.put(url=endpoint, files=files, data=data)
            return self.process_response(response)
        else:
            response = requests.put(url=endpoint, headers=headers, data=json.dumps(data, default=str))
            return self.process_response(response)

    def patch(self,endpoint, data=None, headers=None):
        headers = self.format_headers(headers)
        response = requests.patch(url=endpoint, headers=headers, data=json.dumps(data))
        return self.process_response(response)


    def delete(self,endpoint, data=None, headers=None):
        headers = self.format_headers(headers)
        response = requests.delete(url=endpoint, headers=headers, data=json.dumps(data))
        return self.process_response(response)

    def process_response(self,response):
        if response.status_code == requests.codes.ok:
            try:
                response_obj = response.json()
                status =requests.codes.ok
                if 'status' in response_obj:
                    status = response_obj.pop('status')
                if 'response' in response_obj:
                    response_obj = response_obj['response']
                return {'data': response_obj, 'status': status}
            except ValueError:
                raise RepositoryResponseParseError('Could not parse response')
        else:
            raise InvalidRepositoryResponse('Repository response code is not valid %s (%s)' % (response.status_code, response.url))

    def get_absulute_url(self,endpoint):
        if not self.repository_url:
            raise RepositoryEndpointError('Repository endpoint not defined')
        return parse.urljoin(self.repository_url, endpoint)

    def get_wallet_url(self,endpoint):
        if not os.environ.get('EWALLMOB_USER_WALLET_SERVICE'):
            raise RepositoryEndpointError('Repository endpoint not defined')
        return parse.urljoin(os.environ.get('EWALLMOB_USER_WALLET_SERVICE'), endpoint)
    
    def get_absolute_url(self, endpoint):
        if not self.repository_url:
            raise RepositoryEndpointError('Respository endpoint not defined')
        return parse.urljoin(self.repository_url, endpoint)