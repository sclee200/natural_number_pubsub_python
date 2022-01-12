import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class BasicSubscriber(Node):

    def __init__(self):
        super().__init__('sum_calculator')
        self.subscription = self.create_subscription(
            Int64,
            'natural_number_signal',
            self.listener_callback,
            10)
        self.sum = 0 

    def listener_callback(self, msg):
        self.sum += msg.data
        self.get_logger().info('Received : "%d" and sum : "%d"' % (msg.data, self.sum))
         


def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber)

    basic_subcriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()