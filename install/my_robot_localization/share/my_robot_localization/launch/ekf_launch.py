from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    ekf_config = os.path.join(
        get_package_share_directory("my_robot_localization"),
        'config',
        'ekf.yaml'
    )

    rviz_config = os.path.join(
        get_package_share_directory("my_robot_localization"),
        'rviz',
        'ekf_config.rviz'
    )

    return LaunchDescription([

        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config]
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0','0','0','0','0','3.14159','base_link','imu_link']
        ),

        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
        ),

        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen'
        )   

    ])