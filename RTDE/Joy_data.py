import pygame


def main():
    # Initialize pygame
    pygame.init()

    # Initialize joystick
    pygame.joystick.init()
    
    # Check if any joystick is connected
    if pygame.joystick.get_count() == 0:
        print("No joystick connected.")
        return
    
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    # Print joystick information
    print("Joystick Name:", joystick.get_name())
    print("Number of Axes:", joystick.get_numaxes())
    print("Number of Buttons:", joystick.get_numbuttons())
    
    try:
        # Variables to store axis values
        axis_0 = 0.0
        axis_1 = 0.0
        axis_2 = 0.0
        axis_3 = 0.0
        axis_4 = 0.0
        axis_5 = 0.0
        
        # Continuous loop to read joystick data
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    # Update axis values
                    if event.axis == 0:
                        axis_0 = round(event.value, 2)
                    elif event.axis == 1:
                        axis_1 = round(event.value, 2)
                    elif event.axis == 2:
                        axis_2 = round(event.value, 2)
                    elif event.axis == 3:
                        axis_3 = round(event.value, 2)
                    elif event.axis == 4:
                        axis_4 = round(event.value, 2)
                    elif event.axis == 5:
                        axis_5 = round(event.value, 2)
                
                # Print button and hat events
                elif event.type == pygame.JOYBUTTONDOWN:
                    print("Button", event.button, "Pressed")
                elif event.type == pygame.JOYBUTTONUP:
                    print("Button", event.button, "Released")
                elif event.type == pygame.JOYHATMOTION:
                    print("Hat", event.hat, "Value:", event.value)
                else:
                    print("Other Event:", event)
            
            # Print axis values
            print("Axis 0:", axis_0)
            print("Axis 1:", axis_1)
            print("Axis 2:", axis_2)
            print("Axis 3:", axis_3)
            print("Axis 4:", axis_4)
            print("Axis 5:", axis_5)
        

    
    except KeyboardInterrupt:
        pass
    
    finally:
        # Clean up
        pygame.joystick.quit()
        pygame.quit()

if __name__ == "__main__":
    main()