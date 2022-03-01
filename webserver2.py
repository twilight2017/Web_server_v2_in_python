import io
import socket
import sys


class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(self.address_family, self.socket_type)
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind
        listen_socket.bind(server_address)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = host
        self.sever_port = port
        # Return headers set by Web framework/Web application
        self.headers_set = []

    # 绑定Web应用
    def set_app(self, application):
        self.application = application

    # 一直接收服务
    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            client_connection, client_address = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        request_data = self.client_connection.receive(1024)
        self.request_data = request_data = request_data.decode('utf-8')
        # print formatted request data
        print(''.join(
            f'< {line}\n' for line in request_data.splitlines()
        ))
        self.parse_request(request_data)
        # Construct environment dictionary using request data
        env = self.get_environ()
        # call our application callable and get back a result that can become HTTP response body
        result = self.application(env, self.start_response)
        # Construct a response and send it back to the client
        self.finish_response(result)

    # 解析请求
    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line into the components
        (
            self.request_method,  # GET
            self.path,  # url
            self.request_version,  #HTTP 1.1
        )=request_line.split()

    # 获得环境
    def get_environ(self) -> dict:
        env={ }
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = io.StringIO(self.request_data)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocecss'] = False
        env['wsgi.run_once'] = False
        # Required CDI variables
        env['REQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT'] = self.sever_port
        return env
