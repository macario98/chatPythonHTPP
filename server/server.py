import json
from server import base_handler
from repository import message_memory
from repository import user_memory
from domain import message
from domain import user

class ServerAPI(base_handler.HandleRequests):
	def __init__(self, request, client_address, server) -> None:
		self.message_repository = message_memory.Repository()
		self.user_repository = user_memory.Repository()
		super().__init__(request, client_address, server)

	def do_GET(self):
		self._set_headers()

		match self.path:
			case "/message":
				params = self._get_params("GET", True)
				r = self.message_repository.Get(params.get("id", ""))
				bin = json.dumps(r, default=base_handler.myconverter).encode('utf-8')
				self.wfile.write(bin)
			case "/message/getAll":
				r = self.message_repository.GetAll()
			case "/user":
				self.user_repository.Get()
				params = self._get_params("GET", True)
			case "/user/getAll":
				self.user_repository.GetAll()

	def do_POST(self):
		self._set_headers()
		match self.path:
			case "/message":
				newMessage = message.Domain(0, 0, "msg")
				self.message_repository.Save(newMessage)
			case "/user":
				newUser = user.Domain("name")
				self.user_repository.Save(newUser)