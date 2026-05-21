import rclpy

from rclpy.node import Node
from example_interfaces.msg import Velocity

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(Velocity, 'velocity', 10)
        timer_period = 5.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.drive_forwards = True
    def timer_callback(self):
        if self.drive_forwards:
            # drive forwards
            self.get_logger().info('Driving forwards')
            self.publisher_.publish(Velocity(left=5.0, right=-5.0))
        else:
            # turn on the spot
            self.get_logger().info('Turning')
            self.publisher_.publish(Velocity(left=2.5, right=2.5))
        # toggle mode
        self.drive_forwards = not self.drive_forwards
        
rclpy.init()
velocity_publisher = VelocityPublisher()
rclpy.spin(velocity_publisher)
velocity_publisher.destroy_node()
rclpy.shutdown()