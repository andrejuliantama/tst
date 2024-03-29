import http.server
import socketserver
import ssl

PORT = 9875
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.socket = ssl.wrap_socket(httpd.socket, 
                                   keyfile = "privatekey.key", 
                                   certfile = "certificate.crt", 
                                   server_side=True)
    httpd.serve_forever()
