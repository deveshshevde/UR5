from urx import Robot

# IP address of the UR5 robot
ROBOT_IP = "192.168.0.100"  # Replace with your robot's IP address

def main():
    # Connect to the UR5 robot
    robot = Robot(ROBOT_IP)

    # Move the robot to a specific pose (x, y, z, rx, ry, rz)
    target_pose = (0.5, 0.0, 0.5, 0, 0, 0)
    robot.movej(target_pose)

    # Send custom URScript commands
    custom_script = "textmsg(\"Hello from URScript!\")"
    robot.send_program(custom_script)

    # Close the connection
    robot.close()

if __name__ == "__main__":
    main()
