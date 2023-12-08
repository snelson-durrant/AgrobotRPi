#!/bin/bash

# syncs changes made in the agro_interfaces package with the teensy_ws
rsync -avu --delete ~/ros2_ws/src/agro_interfaces ~/teensy_ws/agrobot/extra_packages