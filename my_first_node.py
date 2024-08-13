#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #import node class

def main(args=None):
    rclpy.init(args=args) #initiate communication
    # the node is created inside :
    node = Node("py_test") # import node class
    node.get_logger().info("Hello Ros2")
    rclpy.shutdown() #last line of code

if __name__ == "__main__":
    main()