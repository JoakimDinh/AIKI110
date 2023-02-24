#!/usr/bin/env python3

import rclpy			
from rclpy.node import Node	
from std_msgs.msg import String 


class MinimalSubscriber(Node):  
    def __init__(self):
        super().__init__("abc123_subscriber") 
        self.subscription = self.create_subscription(String,
                                                     "abc123",
                                                     self.lytter_callback,
                                                     10)				

    def lytter_callback(self, string_data): 
        mottatt = string_data.data 	
        print("Mottok: %s" % mottatt)


def main():
    try:
        rclpy.init() 	
        min_instans = MinimalSubscriber() 
        rclpy.spin(min_instans)
    except:
        KeyboardInterrupt()
        print('Program stoppa av brukaren')
    finally:
        min_instans.destroy_node()


if __name__ == '__main__':
    main()
