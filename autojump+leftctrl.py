import keyboard
import time
import threading

def main():
    # Ask user for the interval in milliseconds for space bar presses
    try:
        space_interval_ms = float(input("Enter the interval between space bar presses (in milliseconds): "))
        if space_interval_ms <= 0:
            print("Interval must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Convert intervals to seconds for time.sleep
    space_interval = space_interval_ms / 1000.0
    ctrl_interval = 0.5  # 500ms for left Ctrl presses

    print("Hold the space bar to start auto-pressing space and left Ctrl. Press 'q' to quit.")

    def press_keys():
        last_ctrl_press = 0
        while True:
            # Check if space bar is held
            if keyboard.is_pressed('space'):
                # Simulate space bar press
                keyboard.press('space')
                keyboard.release('space')
                
                # Simulate left Ctrl press every 500ms
                current_time = time.time()
                if current_time - last_ctrl_press >= ctrl_interval:
                    keyboard.press('left ctrl')
                    keyboard.release('left ctrl')
                    last_ctrl_press = current_time
                
                time.sleep(space_interval)
            else:
                time.sleep(0.01)  # Small sleep to prevent high CPU usage
            # Check for quit condition
            if keyboard.is_pressed('q'):
                print("Exiting...")
                break

    # Run the key presser in a separate thread
    thread = threading.Thread(target=press_keys)
    thread.start()
    thread.join()  # Wait for the thread to finish

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
