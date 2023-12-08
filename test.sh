#!/bin/bash

cd ~/microros_ws
source install/setup.bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0 -b 6000000 &
sleep 5

cd ~/ros2_ws
source install/setup.bash

echo ""
echo "TESTING PROCESS_SRV SERVICE ON TEENSY..."
ros2 service call /process agro_interfaces/srv/Process "{target_x: 0.0, target_y: 0.0, target_z: 0.0}"

ros2 run agrobot agrobot_sm &

echo ""
echo "TESTING AGROBOT_SM PUBLISHER ON PI..."
ros2 topic echo --once /drive

killall agrobot_sm

ros2 run agrobot drive_sub &

echo ""
echo "TESTING DRIVER_SUB SUBSCRIBER ON PI..."
ros2 topic pub -1 /drive agro_interfaces/msg/Drive '{fl_motor: 0.0, fr_motor: 0.0, bl_motor: 0.0, br_motor: 0.0}'

killall drive_sub

echo ""
echo "TEST COMPLETE"

killall micro_ros_agent
wait