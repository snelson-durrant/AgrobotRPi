import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='agrobot',
            executable='agrobot_sm'),
        launch_ros.actions.Node(
            package='agrobot',
            executable='drive_sub'),
    ])