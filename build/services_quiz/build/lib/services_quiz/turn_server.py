# import the Twist module from geometry_msgs messages interface
from geometry_msgs.msg import Twist
# import the MyCustomServiceMessage module from custom_interfaces package
from services_quiz_srv.srv import Turn
# import the ROS2 Python client libraries
import rclpy
from rclpy.node import Node
import time

class Service(Node):

    def __init__(self):
        # Here you have the class constructor

        # call the class constructor to initialize the node as service_stop
        super().__init__('movement_server')
        # create the Service Server object
        # defines the type, name, and callback function
        self.srv = self.create_service(Turn, '/turn', self.custom_service_callback)
        # create the Publisher object
        # in this case, the Publisher will publish on /cmd_vel topic with a queue size of 10 messages.
        # use the Twist module
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        

    def custom_service_callback(self, request, response):
        # The callback function receives the self-class parameter, 
        # received along with two parameters called request and response
        # - receive the data by request
        # - return a result as a response
        self.get_logger().info(f'Received request: direction={request.direction}, angular_velocity={request.angular_velocity}, time={request.time}')

        # create a Twist message
        msg = Twist()
        
        if request.direction == "left":
            # define the linear x-axis velocity of /cmd_vel topic parameter to 0.1
            # define the angular z-axis velocity of /cmd_vel topic parameter to -0.5 to turn right
            msg.angular.z = float(request.angular_velocity)
            # Publish the message to the topic
            self.publisher_.publish(msg)
            self.get_logger().info('Turning to left direction!!')
            time.sleep(request.time)
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            # print a pretty message
            
            # response state
            response.success = True
        elif request.direction == "right":
            # define the linear x-axis velocity of /cmd_vel topic parameter to 0.1
            # define the angular z-axis velocity of /cmd_vel topic parameter to 0.5 to turn left
            msg.angular.z = -float(request.angular_velocity)
            # Publish the message to the topic
            self.publisher_.publish(msg)
            self.get_logger().info('Turning to right direction!!')
            time.sleep(request.time)
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            # print a pretty message
            
            # response state
            response.success = True
        else:
            # response state
            response.success = False
        
        # return the response parameter
        return response


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor  
    service = Service()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(service)
    # shutdown the ROS communication
    rclpy.shutdown()


if __name__ == '__main__':
    main()