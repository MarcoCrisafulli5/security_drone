from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='security_drone', executable='camera_node', name='camera'),
        Node(package='security_drone', executable='yolo_node', name='yolo'),
    ])