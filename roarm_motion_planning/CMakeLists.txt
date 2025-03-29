cmake_minimum_required(VERSION 3.8)
project(roarm_motion_planning)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

add_executable(motion_planner src/plan_and_execute.cpp)

ament_target_dependencies(motion_planner
  rclcpp
  std_msgs
  geometry_msgs
  moveit_ros_planning_interface
  tf2_geometry_msgs
)

install(TARGETS motion_planner
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
