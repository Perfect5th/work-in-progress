import re

from django.conf import settings
from django.http import HttpResponseRedirect


class Wiki2RedirectMiddleware:
    WIKI2_REGEX = r'^wiki2'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if re.match(self.WIKI2_REGEX, host):
            return HttpResponseRedirect(
                f'https://{settings.SITE_URL}/sunday-primers/')

        response = self.get_response(request)

        return response
