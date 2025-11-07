from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    world_path = os.path.join(
        'share', 'security_drone', 'worlds', 'factory.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path],
            output='screen'
        ),
        Node(
            package='security_drone',
            executable='camera_node',
            name='camera'
        ),
        Node(
            package='security_drone',
            executable='yolo_node',
            name='yolo'
        ),
    ])