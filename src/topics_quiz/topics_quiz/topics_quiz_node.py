import rclpy
import time
import numpy as np
# import the ROS2 python libraries
from rclpy.node import Node
# import the Twist interface from the geometry_msgs package
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.qos import ReliabilityPolicy, QoSProfile

class topics_quiz_node(Node):

    def __init__(self):
        # Here you have the class constructor
        # call super() in the constructor to initialize the Node object
        # the parameter you pass is the node name
        super().__init__('topics_quiz_node')
        # create the publisher object
        # in this case, the publisher will publish on /cmd_vel Topic with a queue size of 10 messages.
        # use the Twist module for /cmd_vel Topic
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.euler_from_quaternion, QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE))
        self.cmd = Twist()
        self.target_yaw = 1.30
        self.straight_movement()

    def euler_from_quaternion(self, msg):
        """
        Converts quaternion (w in last place) to euler roll, pitch, yaw
        quaternion = [x, y, z, w]
        Below should be replaced when porting for ROS2 Python tf_conversions is done.
        """
        self.get_logger().info('quaternion call back function is running!')
        quaternion = msg.pose.pose.orientation
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        # sinr_cosp = 2 * (w * x + y * z)
        # cosr_cosp = 1 - 2 * (x * x + y * y)
        # roll = np.arctan2(sinr_cosp, cosr_cosp)

        # sinp = 2 * (w * y - z * x)
        # pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        self.yaw = np.arctan2(siny_cosp, cosy_cosp)

        

    def straight_movement(self):

        self.cmd.linear.x = 0.5
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        time.sleep(9.5)
        self.cmd.linear.x = 0.0
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        self.cmd.angular.z = 0.5
        self.publisher_.publish(self.cmd)
        self.timer = self.create_timer(0.1, self.check_yaw)
        
    def check_yaw(self):
        if self.yaw is not None:
            self.get_logger().info(f'yaw: {self.yaw} radians')
            if self.yaw > self.target_yaw:
                self.cmd.angular.z = 0.0
                self.publisher_.publish(self.cmd)
                self.get_logger().info(f'Publishing: {self.cmd}')
                self.destroy_timer(self.timer)
                self.straight_movement2()
    
    def straight_movement2(self):
        self.cmd.linear.x = 0.8
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        time.sleep(8)
        self.cmd.linear.x = 0.0
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        

            
def main(args=None):
    rclpy.init(args=args)
    node = topics_quiz_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


