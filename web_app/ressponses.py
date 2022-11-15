import json
import logging

from django.http import HttpResponse


class Result(object):
    def __init__(self, code, status, message, extra_fields=None):
        """
        Base Result class for API responses.
        code - numeric status code, similar to HTTP status code
        status - short status code
        message - descriptive message.
        """
        self.code = code
        self.status = status
        self.message = message
        self.extra_fields = extra_fields

    def to_json_dict(self):
        """Convert to a dict for serializing to JSON."""
        result = {"code": self.code, "status": self.status, "message": self.message}
        if self.extra_fields:
            result.update(self.extra_fields)
        return result

    def to_json(self, pretty=0):
        """Serialize to JSON."""
        if pretty == 1:
            return json.dumps(self.to_json_dict(), indent=2)
        return json.dumps(self.to_json_dict())

    def http_response(self, pretty=0, status_code=200):
        response = HttpResponse(self.to_json(pretty), content_type='application/json')
        response.status_code = status_code
        response['Access-Control-Allow-Origin'] = '*'
        return response
