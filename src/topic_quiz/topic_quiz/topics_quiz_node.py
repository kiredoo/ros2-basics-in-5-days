import rclpy
import time
import numpy as np
# import the ROS2 python libraries
from rclpy.node import Node
# import the Twist interface from the geometry_msgs package
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class topics_quiz_node(Node):

    def __init__(self):
        # Here you have the class constructor
        # call super() in the constructor to initialize the Node object
        # the parameter you pass is the node name
        super().__init__('topics_quiz_node')
        # create the publisher object
        # in this case, the publisher will publish on /cmd_vel Topic with a queue size of 10 messages.
        # use the Twist module for /cmd_vel Topic
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', self.movement, 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.euler_from_quaternion, 10)
        self.cmd = Twist()
        self.target_yaw = 1.57

    def euler_from_quaternion(self, quaternion):
        """
        Converts quaternion (w in last place) to euler roll, pitch, yaw
        quaternion = [x, y, z, w]
        Below should be replaced when porting for ROS2 Python tf_conversions is done.
        """
        x = quaternion[0]
        y = quaternion[1]
        z = quaternion[2]
        w = quaternion[3]

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        self.yaw = np.arctan2(siny_cosp, cosy_cosp)

        

    def straight_movement(self, msg):

        self.cmd.linear.x = 0.5
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        time.sleep(2)
        self.cmd.linear.x = 0
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        self.turn(msg)
        
    def turn(self,msg):
        self.cmd.angular.z = 0.5
        self.publisher_.publish(self.cmd)
        self.get_logger().info('Publishing: "%s"' % self.cmd)
        while True:
            self.get_logger().info('yaw: "%s" radians' % self.yaw)
            if self.yaw > self.target_yaw:
                break
            

                      


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    topic_quiz = topic_quiz()       
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(topic_quiz)
    # Explicity destroy the node
    topic_quiz.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()