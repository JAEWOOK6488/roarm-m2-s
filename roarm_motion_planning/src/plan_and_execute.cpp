#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

// Create the MoveIt MoveGroup Interface
using moveit::planning_interface::MoveGroupInterface;

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("roarm_motion_planning_node");
  rclcpp::executors::SingleThreadedExecutor executor;
  executor.add_node(node);
  std::thread([&executor]() { executor.spin(); }).detach();

  rclcpp::Logger logger = node->get_logger();

  MoveGroupInterface move_group_interface(node, "hand");

  // Set a target pose
  auto target_pose = [] {
    geometry_msgs::msg::Pose pose;
    pose.orientation.w = 1.0;
    pose.position.x = 0.1;
    pose.position.y = -0.2;
    pose.position.z = 0.3;
    return pose;
  }();

  move_group_interface.setPoseTarget(target_pose);

  // Create a plan to the target pose
  auto [success, plan] = [&move_group_interface] {
    MoveGroupInterface::Plan plan;
    bool ok = static_cast<bool>(move_group_interface.plan(plan));
    return std::make_pair(ok, plan);
  }();

  // Execute the plan
  if (success) {
    move_group_interface.execute(plan);
  } else {
    RCLCPP_ERROR(logger, "Planning failed!");
  }

  rclcpp::shutdown();
  return 0;
}
