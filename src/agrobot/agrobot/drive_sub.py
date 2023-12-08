import rclpy
from rclpy.node import Node
from agro_interfaces.msg import Drive
from rclpy.qos import qos_profile_sensor_data


class DriveSubscriber(Node):
    def __init__(self):
        super().__init__("drive_sub")
        self.subscription = self.create_subscription(
            Drive, "drive", self.listener_callback, qos_profile_sensor_data
        )
        self.subscription  # prevent unused variable warning

        ##############################################################
        # ADD MOTOR INIT CODE HERE
        ##############################################################

        ##############################################################
        # END MOTOR INIT CODE HERE
        ##############################################################

    def listener_callback(self, msg):
        ##############################################################
        # ADD CODE HERE TO EXECUTE WHEN A MESSAGE IS RECEIVED
        ##############################################################

        front_left = msg.fl_speed
        front_right = msg.fr_speed
        back_left = msg.bl_speed
        back_right = msg.br_speed

        ##############################################################
        # END CODE HERE TO EXECUTE WHEN A MESSAGE IS RECEIVED
        ##############################################################


def main(args=None):
    rclpy.init(args=args)

    drive_sub = DriveSubscriber()

    rclpy.spin(drive_sub)

    drive_sub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
