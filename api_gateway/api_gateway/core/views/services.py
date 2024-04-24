from rest_framework.views import APIView
from rest_framework.response import Response
from api_gateway.core.services.base.exceptions import RepositoryNotFound


class ServiceAPIView(APIView):
    repository_class = None
    api_verison = None

    def get_repository_class(self):
        if self.repository_class:
            return self.repository_class
        raise RepositoryNotFound('%s repository not found' % self.__class__)

    def get_repository_object(self):
        repository = self.repository_class(self.api_verison)
        repository.format_headers({
            "Accept-Language": self.request.META.get(
                'HTTP_ACCEPT_LANGUAGE', 'en')
        })
        return repository

    def get_response(self, request, *args, **kwargs):
        setattr(request, 'repository', self.get_repository_object())
        response = self.call_service(request, *args, **kwargs)
        return Response(**response)

    def call_service(self, request, *args, **kwargs):
        raise NotImplementedError()


class ServicePostAPIView(ServiceAPIView):

    def post(self, request, *args, **kwargs):
        return self.get_response(request, *args, **kwargs)


class ServiceGetAPIView(ServiceAPIView):

    def get(self, request, *args, **kwargs):
        return self.get_response(request, *args, **kwargs)


class ServicePutAPIView(ServiceAPIView):

    def put(self, request, *args, **kwargs):
        return self.get_response(request, *args, **kwargs)


class ServicePatchAPIView(ServiceAPIView):

    def patch(self, request, *args, **kwargs):
        return self.get_response(request, *args, **kwargs)