#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.srv import TjenesteTest
from time import sleep
class KlientNode(Node):
	def __init__(self):
		super().__init__('klient_node')
		self.cli = self.create_client(TjenesteTest, 'test')
		
		while not self.cli.wait_for_service(timeout_sec=1.0):
			print('Tjeneste utilgjengelig, venter...')
			
	def send_request(self):
		request = TjenesteTest.Request()
		request.left = 'Hello'
		request.right = 'world!'
		#left and right should correspond to whatever is in your srv file
		
		self.future = self.cli.call_async(request)
		rclpy.spin_until_future_complete(self, self.future)
		result = self.future.result()
		print(result.result)
		
	def main():
		try:
			rclpy.init()
			klient = KlientNode()
			while rclpy.ok():
			klient.send_request()
			sleep(1)
		except KeyboardInterrupt:
			print('\nStoppa av brukaren.')
		finally:
			pass
		
if __name__ == '__main__':
	main()
