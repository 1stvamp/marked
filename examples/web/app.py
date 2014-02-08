from __future__ import print_function

from sys import stdout
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.web import asynchronous, RequestHandler, Application

from marked import markup_to_markdown


class MainHandler(RequestHandler):
    def prepare(self):
        self.set_header('Content-Type', 'text/markdown; charset="utf-8"')

    @asynchronous
    def post(self):
        client = AsyncHTTPClient()
        client.fetch(
            request=self.get_argument('url'),
            method='GET',
            callback=self.handle_response,
        )
        self.flush()

    def handle_response(self, response):
        self.finish(markup_to_markdown(response.body))


application = Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    print('Service started on http://localhost:8888/', file=stdout)
    IOLoop.instance().start()
