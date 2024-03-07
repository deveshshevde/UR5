import keyboard
from urx import Robot
import numpy as np

# UR5 robot IP address
ROBOT_IP = "192.168.1.10"  # Replace with your robot's IP address

# Define joint angle increments (adjust as needed)
JOINT_INCREMENT = np.radians(1)  # in radians

# Define keyboard control mappings
KEY_MAPPING = {
    "q": (0, 1, 2, 3, 4, 5),    # Rotate joint 1 counterclockwise
    "a": (0, -1, -2, -3, -4, -5),   # Rotate joint 1 clockwise
    "w": (1,),   # Rotate joint 2 counterclockwise
    "s": (-1,),  # Rotate joint 2 clockwise
    "e": (2,),   # Rotate joint 3 counterclockwise
    "d": (-2,),  # Rotate joint 3 clockwise
    "r": (3,),   # Rotate joint 4 counterclockwise
    "f": (-3,),  # Rotate joint 4 clockwise
    "t": (4,),   # Rotate joint 5 counterclockwise
    "g": (-4,),  # Rotate joint 5 clockwise
    "y": (5,),   # Rotate joint 6 counterclockwise
    "h": (-5,),  # Rotate joint 6 clockwise
    "esc": None   # Exit program
}

def main():
    # Connect to the UR5 robot
    robot = Robot(ROBOT_IP)

    print("Joint Rotation Control Script - Press 'esc' to exit.")

    # Continuous loop to capture keyboard inputs
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name.lower()

            if key in KEY_MAPPING:
                if key == "esc":
                    break

                # Get the joint indices to be rotated and their respective directions
                joint_indices = KEY_MAPPING[key]

                # Calculate the new joint angles
                current_joint_angles = robot.getj()
                new_joint_angles = list(current_joint_angles)
                for idx in joint_indices:
                    new_joint_angles[idx] += JOINT_INCREMENT

                # Move the robot to the new joint angles
                robot.movej(new_joint_angles)

    # Close the connection to the UR5 robot
    robot.close()
    print("Program terminated.")

if __name__ == "__main__":
    main()
