
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Position and orientation
    # [X, Y, Z]
    position = [0.0, 0.0, 0.05]
    # [Roll, Pitch, Yaw]
    orientation = [0.0, 0.0, -3.14]
    # Base Name or robot
    robot_base_name = "roarm"

    entity_name = robot_base_name+"-"+str(int(random.random()*1000))

    # Spawn ROBOT Set Gazebo
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_entity',
        output='screen',
        arguments=['-entity',
                   entity_name,
                   '-x', str(position[0]), '-y', str(position[1]), '-z', str(position[2]),
                   '-R', str(orientation[0]), '-P', str(orientation[1]), '-Y', str(orientation[2]),
                   '-topic', '/robot_description'
                   ]
    )

    # create and return launch description object
    return LaunchDescription([
            spawn_robot,
    ])
