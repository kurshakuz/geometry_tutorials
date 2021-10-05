from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():
    turtlesim_world1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtle_tf2_py'), 'launch'),
            '/turtlesim1.launch.py'])
        )
    turtlesim_world2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtle_tf2_py'), 'launch'),
            '/turtlesim2.launch.py'])
        )
    demo_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtle_tf2_py'), 'launch'),
            '/turtle_tf2_demo.launch.py']),
        launch_arguments={'target_frame': 'carrot1'}.items(),
        )
    mimic_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtle_tf2_py'), 'launch'),
            '/mimic.launch.py'])
        )
    fixed_frame_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtle_tf2_py'), 'launch'),
            '/turtle_tf2_fixed_frame_demo.launch.py'])
        )

    return LaunchDescription([
        turtlesim_world1,
        turtlesim_world2,
        demo_nodes,
        mimic_nodes,
        fixed_frame_node
    ])