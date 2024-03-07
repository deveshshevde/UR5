import keyboard
from urx import Robot

# UR5 robot IP address
ROBOT_IP = "192.168.1.10"  # Replace with your robot's IP address

# Define robot movement increments (adjust as needed)
MOVEMENT_INCREMENT = 0.01  # in meters

# Define keyboard control mappings
KEY_MAPPING = {
    "w": (MOVEMENT_INCREMENT, 0, 0, 0, 0, 0),   # Move forward
    "s": (-MOVEMENT_INCREMENT, 0, 0, 0, 0, 0),  # Move backward
    "a": (0, -MOVEMENT_INCREMENT, 0, 0, 0, 0),  # Move left
    "d": (0, MOVEMENT_INCREMENT, 0, 0, 0, 0),   # Move right
    "q": (0, 0, MOVEMENT_INCREMENT, 0, 0, 0),   # Move up
    "e": (0, 0, -MOVEMENT_INCREMENT, 0, 0, 0),  # Move down
    "r": (0, 0, 0, 0, 0, MOVEMENT_INCREMENT),   # Rotate counterclockwise
    "f": (0, 0, 0, 0, 0, -MOVEMENT_INCREMENT),  # Rotate clockwise
    "esc": None  # Exit program
}

def main():
    # Connect to the UR5 robot
    robot = Robot(ROBOT_IP)

    print("Teleoperation Script - Press 'esc' to exit.")

    # Continuous loop to capture keyboard inputs
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name.lower()

            if key in KEY_MAPPING:
                if key == "esc":
                    break

                movement = KEY_MAPPING[key]
                if movement:
                    robot.translate_tool(movement, acc=0.1, vel=0.1)

    # Close the connection to the UR5 robot
    robot.close()
    print("Program terminated.")

if __name__ == "__main__":
    main()
