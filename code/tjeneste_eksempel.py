#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.srv import TjenesteTest
class TjenesteNode(Node):
	def __init__(self):
		super().__init__('tjeneste_node')
		self.srv = self.create_service(TjenesteTest,
									   'test',
										self.handle_TjenesteTest)
	def handle_TjenesteTest(self, request, response):
		response.result = request.left + " " + request.right
		return response
def main():
	try:
		rclpy.init()
		tjeneste = TjenesteNode()
		rclpy.spin(tjeneste)
	except KeyboardInterrupt:
		print('\nStoppa av brukaren.')
	finally:
		pass
