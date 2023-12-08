import rclpy
from rclpy.node import Node
from agro_interfaces.msg import Drive
from agro_interfaces.srv import Process
import cam_handler

SERVICE_TIMEOUT = 1  # seconds
QOS_PROFILE = 10


class Agrobot_SM(Node):
    # Creates all of the publishers, subscriptions, services, and clients
    def __init__(self):
        super().__init__("agrobot_sm")

        # Create the publisher
        self.pub = self.create_publisher(Drive, "drive", QOS_PROFILE)

        # Create the client
        self.process_cli = self.create_client(Process, "process")
        while not self.process_cli.wait_for_service(timeout_sec=SERVICE_TIMEOUT):
            self.get_logger().info("Process service not available, waiting...")

        # Set initial variables
        self.drive_msg = Drive()
        self.process_req = Process.Request()

    # Sends a request to the process service
    def send_request(self, x, y, z):
        self.process_req.target_x = x
        self.process_req.target_y = y
        self.process_req.target_z = z
        self.future = self.cli.call_async(self.process_req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

    # Publishes a message to the drive topic
    def publish(self, front_left, front_right, back_left, back_right):
        self.drive_msg.fl_motor = front_left
        self.drive_msg.fr_motor = front_right
        self.drive_msg.bl_motor = back_left
        self.drive_msg.br_motor = back_right
        self.pub.publish(self.drive_msg)


def main(args=None):
    rclpy.init(args=args)

    agrobot_sm = Agrobot_SM()

    ##############################################################
    # ADD CAMERA INIT CODE HERE
    ##############################################################

    ##############################################################
    # END CAMERA INIT CODE HERE
    ##############################################################

    while 1:
        ##############################################################
        # START AGROBOT STATE MACHINE HERE
        ##############################################################

        process_resp = agrobot_sm.send_request(1, 2, 3)
        agrobot_sm.publish(1, 2, 3, 4)

        ##############################################################
        # END AGROBOT STATE MACHINE HERE
        ##############################################################

    agrobot_sm.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
