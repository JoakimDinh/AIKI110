#!/usr/bin/env python3

import rclpy
from rclpy.node import Node	
from std_msgs.msg import String	#Built in datatype from ROS which it can publish, regular python strings cannot be published in the ROs channels

class MinimalPublisher(Node):	
    def __init__(self):
        super().__init__("abc123_publisher")     
        self.publisher = self.create_publisher(String, #Datatype which your publisher will accept
        	                                    "abc123", #name on the channel
                                               10) #Queue size
        #create variables here to easily access them later
        self.fortegnelse = {} 
        self.liste = []
        self.timer = self.create_timer(1, self.si_hei) #Call the second argument function 
        
    def si_hei(self):
        msg = String() #Set datatype of the message
        msg.data = "Hei, fra abc123_publisher.py!" #set content of the message
        self.publisher.publish(msg) #publish the message
    
def main():
    try:
        rclpy.init()
        min_instans = MinimalPublisher()
        rclpy.spin(min_instans)
    except:
        KeyboardInterrupt()
        print("Program stoppa av brukaren.")
    finally:
        min_instans.destroy_node() 	     

if __name__ == '__main__': #call main function
    main() 
