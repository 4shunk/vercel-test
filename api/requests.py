from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    res = requests.get('https://vercel-test-jade-nu.vercel.app/api/date')
    body = res.text
    self.wfile.write(body)
    return