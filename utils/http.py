import json
import urllib.parse
from abc import ABCMeta, abstractmethod
from enum import auto, Enum

import requests.exceptions


class HTTPException(Exception):
    def __init__(self, message=None, code=None, http_status=None, *args, **kwargs):
        self.message = message
        self.code = code
        self.http_status = http_status
        super().__init__(*args, **kwargs)


class HTTPVerb(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()


class HTTPRequest:
    def __init__(
        self,
        verb,
        url,
        *,
        headers=None,
        params=None,
        body=None,
        use_json=True,
        **kwargs
    ):
        self.verb = verb
        self.url = url
        self.headers = headers
        self.params = params
        self.body = body
        self.use_json = use_json
        self.kwargs = kwargs

    def execute(self):
        kwargs = {
            **{
                k: v
                for k, v in {
                    "headers": self.headers,
                    "params": self.params,
                    "json" if self.use_json else "data": self.body,
                }.items()
                if v is not None
            },
            **self.kwargs,
        }

        if not isinstance(self.verb, HTTPVerb):
            raise TypeError("Expected verb to be of type HTTPVerb")

        response = requests.request(self.verb.name, self.url, **kwargs)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            message = str(e)
            code = None
            try:
                content = json.loads(response.content)
                if content.get("error"):
                    message = content.get("message", str(e))
                    code = content.get("code", None)
            except json.JSONDecodeError:
                pass
            raise HTTPException(message, code, response.status_code)

        if "application/json" in response.headers.get("content-type", ""):
            return response.json()
        return response.text


class HTTPClient(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def base_url(self):
        pass

    @property
    def injected_headers(self):
        return None

    def process_request(self, *args, **kwargs):
        return HTTPRequest(*args, **kwargs).execute()

    def get_url(self, path):
        return urllib.parse.urljoin(self.base_url, path)

    def get_headers(self, headers, inject=False):
        if inject:
            if self.injected_headers and headers:
                return {**self.injected_headers, **headers}
            elif self.injected_headers:
                return self.injected_headers
        return headers

    def get(self, path, headers=None, params=None, inject_headers=True, **kwargs):
        return self.process_request(
            HTTPVerb.GET,
            self.get_url(path),
            headers=self.get_headers(headers, inject=inject_headers),
            params=params,
            **kwargs,
        )

    def post(self, path, headers=None, body=None, inject_headers=True, **kwargs):
        return self.process_request(
            HTTPVerb.POST,
            self.get_url(path),
            headers=self.get_headers(headers, inject=inject_headers),
            body=body,
            **kwargs,
        )

    def put(self, path, headers=None, body=None, inject_headers=True, **kwargs):
        return self.process_request(
            HTTPVerb.PUT,
            self.get_url(path),
            headers=self.get_headers(headers, inject=inject_headers),
            body=body,
            **kwargs,
        )

    def patch(self, path, headers=None, body=None, inject_headers=True, **kwargs):
        return self.process_request(
            HTTPVerb.PATCH,
            self.get_url(path),
            headers=self.get_headers(headers, inject=inject_headers),
            body=body,
            **kwargs,
        )

    def delete(self, path, headers=None, params=None, inject_headers=True, **kwargs):
        return self.process_request(
            HTTPVerb.DELETE,
            self.get_url(path),
            headers=self.get_headers(headers, inject=inject_headers),
            params=params,
            **kwargs,
        )
