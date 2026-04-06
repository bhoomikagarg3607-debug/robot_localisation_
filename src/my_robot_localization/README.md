# ROS2 Robot Localization using EKF

This project is based on robot localization using ROS2. The main goal is to improve the position and orientation estimation of a robot by combining data from multiple sensors.

I have used wheel odometry and IMU data and fused them using the Extended Kalman Filter (EKF) from the `robot_localization` package.



##  What this project does

- Takes input from:
  - `/odom` (wheel odometry)
  - `/imu` (IMU sensor)
- Uses EKF to combine both data
- Publishes filtered output on:
  - `/odometry/filtered`
- Uses TF to correct the IMU orientation (since it is mounted backwards)
- Visualizes everything in RViz



##  Concepts I learned

- How EKF works for sensor fusion
- Importance of TF (coordinate transformations)
- How different frames like `odom`, `base_link`, `imu_link` are connected
- Basic URDF for robot visualization
- Using RViz for debugging and visualization



##  How to run it 

1. Firstly build a workspace using
- cd ~/ros2_ws
- colcon build

2. Then source it using
- source /opt/ros/jazzy/setup.bash
- source ~/ros2_ws/install/setup.bash

3. Launch the project
- ros2 launch my_robot_localization ekf_launch.py




##  Topics used

/odom → odometry data
/imu → IMU data
/odometry/filtered → EKF output
/tf and /tf_static → frame transformations


## TF setup

I used a static transform between: 
         base_link → imu_link
with a rotation of 180°  to fix the IMU orientation.


## Visualisation

=> RViz is used to:

1. See the robot movement
2. Check TF frames
3. Visualize filtered odometry



## Final Result 

Successfully fused sensor data using EKF
Corrected IMU orientation using TF
Visualized robot motion in RViz


