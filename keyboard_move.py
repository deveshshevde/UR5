import keyboard
from urx import Robot

# UR5 robot IP address
ROBOT_IP = "192.168.0.100"  # Replace with your robot's IP address

# Define keyboard control mappings
KEY_MAPPING = {
    "w": (0, 0, 0.01, 0, 0, 0),    # Move forward in Z-axis
    "s": (0, 0, -0.01, 0, 0, 0),   # Move backward in Z-axis
    "a": (0, -0.01, 0, 0, 0, 0),   # Move left in Y-axis
    "d": (0, 0.01, 0, 0, 0, 0),    # Move right in Y-axis
    "q": (0, 0, 0, 0, 0, 0.01),    # Rotate counterclockwise in Z-axis
    "e": (0, 0, 0, 0, 0, -0.01),   # Rotate clockwise in Z-axis
    "esc": None                   # Exit program
}

def main():
    # Connect to the UR5 robot
    robot = Robot(ROBOT_IP)

    print("Teleoperation Script - Press 'esc' to exit.")

    # Initial target pose
    target_pose = (0.5, 0.0, 0.5, 0, 0, 0)

    # Continuous loop to capture keyboard inputs
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name.lower()

            if key in KEY_MAPPING:
                if key == "esc":
                    break

                # Update target pose based on keyboard input
                movement = KEY_MAPPING[key]
                target_pose = tuple(x + y for x, y in zip(target_pose, movement))

                # Move the robot to the new target pose
                robot.movej(target_pose)

    # Close the connection to the UR5 robot
    robot.close()
    print("Program terminated.")

if __name__ == "__main__":
    main()
