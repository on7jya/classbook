from django.urls import reverse
from rest_framework.test import force_authenticate


class UrlMixin:
    URL = None

    def get_url(self, kwargs=None):
        assert self.URL is not None, \
            ('Expected class %s should contain `URL` to get right url for tests.' % (self.__class__.__name__,))
        return reverse(self.URL, kwargs=kwargs)


class GetResponseMixin(UrlMixin):
    VIEW = None

    def get_response(self, request_factory, url_kwargs=None, data=None, user=None, force_auth=True):
        assert self.VIEW is not None, \
            ('Expected class %s should contain `VIEW` to get response for request.' % (self.__class__.__name__,))
        url_kwargs = url_kwargs or {}
        url = self.get_url(kwargs=url_kwargs)
        request = request_factory.get(url, data=data)
        if force_auth and user:
            force_authenticate(request, user=user)
        view = self.VIEW.as_view()
        return view(request, **url_kwargs)
