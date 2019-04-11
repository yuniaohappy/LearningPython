import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print(self.client_address)


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever()
