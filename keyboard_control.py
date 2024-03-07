import keyboard
import sys


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
                print("Movement:", movement)  # Just print the movement for demonstration

    print("Program terminated.")

if __name__ == "__main__":
    main()
