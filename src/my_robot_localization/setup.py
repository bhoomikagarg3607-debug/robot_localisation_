from setuptools import find_packages, setup

package_name = 'my_robot_localization'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/ekf_launch.py']),
        ('share/' + package_name + '/config', ['config/ekf.yaml']),
        ('share/' + package_name + '/urdf', ['urdf/robot.urdf']),
        ('share/' + package_name + '/rviz', ['rviz/ekf_config.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hoomika_arg',
    maintainer_email='hoomika_arg@todo.todo',
    description='ROS2 EKF localization package',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [],
    },
)