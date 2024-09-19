from geometry_msgs.msg import Twist
# import the MyCustomServiceMessage module from custom_interfaces package
from services_quiz_srv.srv import Turn
# import the ROS2 Python client libraries
import rclpy
from rclpy.node import Node
import time


class Client(Node):

    def __init__(self):
        # Here you have the class constructor

        # call the class constructor to initialize the node as movement_client
        super().__init__('movement_client')
        # create the Service Client object
        # defines the name and type of the Service Server you will work with.
        self.client = self.create_client(Turn, '/turn')
        # checks once per second if a Service matching the type and name of the client is available.
        while not self.client.wait_for_service(timeout_sec=1.0):
            # if it is not available, a message is displayed
            self.get_logger().info('service not available, waiting again...')
        
        # create an Empty request
        self.req = Turn.Request()
        

    def send_request(self):
        
        # send the request
        self.req.direction = 'right'
        self.req.angular_velocity = 0.2
        self.req.time = 10
        # uses sys.argv to access command line input arguments for the request.
        self.future = self.client.call_async(self.req)
        self.get_logger().info('Sending request: direction=right, angular_velocity=0.2, time=10')

        # to print in the console


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    client = Client()
    # run the send_request() method
    client.send_request()

    while rclpy.ok():
        # pause the program execution, waits for a request to kill the node (ctrl+c)
        rclpy.spin_once(client)
        if client.future.done():
            try:
                # checks the future for a response from the Service
                # while the system is running. 
                # if the Service has sent a response, the result will be written
                # to a log message.
                response = client.future.result()
            except Exception as e:
                # Display the message on the console
                client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                # Display the message on the console
                client.get_logger().info(
                    'Response state %r' % (response.success,))
            break

    client.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()


if __name__ == '__main__':
    main()