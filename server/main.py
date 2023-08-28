from _socket import _RetAddress
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import _RequestType, BaseServer
from ..repository import message_memory
from ..repository import user_memory
from ..domain import message
from ..domain import user

class HandleRequests(BaseHTTPRequestHandler):

	def __init__(self, request: _RequestType, client_address: _RetAddress, server: BaseServer) -> None:
		super().__init__(request, client_address, server)
		self.message_repository = message_memory.Repository()
		self.user_repository = user_memory.Repository()

	def _set_headers(self, tipo = 'text/plain'):
		self.send_response(200)
		self.send_header('Content-type', tipo)
		self.send_header('Access-Control-Allow-Credentials', 'true')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
		self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
		self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
		self.end_headers()

	def _set_response(self, response):
		if isinstance(response, bytes):#si el parametro es binario
			self.wfile.write(response)
		else:#si no se convierte a bytes
			self.wfile.write(bytes(response, 'utf-8'))


	def do_GET(self):
		match self.path:
			case "/message":
				self.message_repository.Get()
			case "/message/getAll":
				self.message_repository.GetAll()
			case "/user":
				self.user_repository.Get()
			case "/user/getAll":
				self.user_repository.GetAll()

	def do_POST(self):
		match self.path:
			case "/message":
				newMessage = message.Domain(0, 0, "msg")
				self.message_repository.Save(newMessage)
			case "/user":
				newUser = user.Domain("name")
				self.user_repository.Save(newUser)

