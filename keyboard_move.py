import keyboard
from urx import Robot
import numpy as np

# UR5 robot IP address
ROBOT_IP = "192.168.1.10"  # Replace with your robot's IP address

# Define Cartesian increment (adjust as needed)
CARTESIAN_INCREMENT = [0.0, 0.0, 0.01, 0.0, 0.0, 0.0]  # [dx, dy, dz, drx, dry, drz]

# Define keyboard control mappings
KEY_MAPPING = {
    "w": (0, 0, 1, 0, 0, 0),    # Move forward in Z-axis
    "s": (0, 0, -1, 0, 0, 0),   # Move backward in Z-axis
    "a": (0, -1, 0, 0, 0, 0),   # Move left in Y-axis
    "d": (0, 1, 0, 0, 0, 0),    # Move right in Y-axis
    "q": (0, 0, 0, 0, 0, -1),   # Rotate counterclockwise in Z-axis
    "e": (0, 0, 0, 0, 0, 1),    # Rotate clockwise in Z-axis
    "esc": None                # Exit program
}

def main():
    robot = Robot(ROBOT_IP)

    print("Cartesian Movement Control Script - Press 'esc' to exit.")

    # Continuous loop to capture keyboard inputs
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name.lower()

            if key in KEY_MAPPING:
                if key == "esc":
                    break

                # Get the Cartesian increment corresponding to the key
                cartesian_increment = np.array(KEY_MAPPING[key]) * CARTESIAN_INCREMENT

                # Get the current pose of the robot's end-effector
                current_pose = robot.getl()

                # Calculate the new pose
                new_pose = current_pose + cartesian_increment

                # Move the robot to the new pose
                robot.movel(new_pose, acc=0.1, vel=0.1)

    robot.close()
    print("Program terminated.")

if __name__ == "__main__":
    main()
