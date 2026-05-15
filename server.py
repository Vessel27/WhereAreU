from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

print(f"Running at http://localhost:{PORT}")

server.serve_forever()
