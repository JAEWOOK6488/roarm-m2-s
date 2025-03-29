import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('roarm_description'),
                'launch',
                'robot_state_publisher.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo', '--verbose',
            PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'worlds', 'empty.world']),
            '-s', 'libgazebo_ros_factory.so',
            '-s', 'libgazebo_ros_init.so',
        ],
        output='screen'
    )

    spawn_entity = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('roarm_gazebo'),
                'launch',
                'spawn_robot.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    load_controllers = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('roarm_moveit_config'),
                'launch',
                'load_ros2_controllers.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        load_controllers,
    ])
