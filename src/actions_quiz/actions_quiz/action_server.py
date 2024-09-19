import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from actions_quiz_msg.action import Distance
from std_msgs import float64
import time
from nav_msgs.msg import Odometry
import numpy as np
from rclpy.qos import ReliabilityPolicy, QoSProfile


class MyActionServer(Node):

    def __init__(self):
        super().__init__('my_action_server')
        self._action_server = ActionServer(self, Distance, '/distance_as',self.execute_callback) 
        self.publisher_ = self.create_publisher(float64, '/total_distance', 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.odom_reading, QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE))
        self.old_position.x = 0.0
        self.old_position.y = 0.0
        self.current_distance = 0.0
        self.time_robot_on = 0
        self.create_timer(self.timer_period, self.timer)
        
    def timer(self):
        self.time_robot_on += self.timer_period
        self.get_logger().info(f"Updated Time Robot On={self.time_robot_on:.1f}")

    def odom_reading(self, msg):
        self.get_logger().info('odometry call back function is running!')
        self.new_position = msg.pose.pose.position
        self.distance_travelled = self.calculate_distance(self.new_position, self.old_position)
        self.update_position(self.new_position)
        self.current_distance += self.distance_travelled


    def update_position(self, new_position):
        self.old_position.x = new_position.x
        self.old_position.y = new_position.y

    def calculate_distance(self, new_position, old_position):
        x_new = new_position.x
        y_new = new_position.y
        x_old = old_position.x
        y_old = old_position.y
        distance = np.sqrt(((x_new-x_old)**2)+((y_new-y_old)**2))
        return distance

    def execute_callback(self, goal_handle):
        
        self.get_logger().info('Executing goal...')

        feedback_msg = Distance.Feedback()
        feedback_msg.current_dist = self.current_distance

        for i in range(1, goal_handle.request.seconds):
            
            self.get_logger().info('Feedback: {0} '.format(feedback_msg.current_dist))

            goal_handle.publish_feedback(feedback_msg)

            self.publisher_.publish(self.current_distance)
            time.sleep(1)

        goal_handle.succeed()

        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
            
        self.publisher_.publish(self.cmd)
        result = Distance.Result()
        result.status = True
        result.total_dist = self.current_distance
        self.get_logger().info('Result: {0}'.format(result.status))
        return result

def main(args=None):
    rclpy.init(args=args)

    my_action_server = MyActionServer()

    rclpy.spin(my_action_server)


if __name__ == '__main__':
    main()