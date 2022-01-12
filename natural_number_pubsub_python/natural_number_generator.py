import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64

class BasicPublisher(Node):

    def __init__(self):
        super().__init__('natural_number_generator')
        self.publisher_ = self.create_publisher(Int64, 'natural_number_signal', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 1

    def timer_callback(self):
        msg = Int64()
        # listcnt = []
        # listcnt[0] ='Count: '
        # listcnt[1] = self.count
        msg.data = self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Generating: "%s"' % msg.data)
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    basic_publisher = BasicPublisher()
    rclpy.spin(basic_publisher)

    basic_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()