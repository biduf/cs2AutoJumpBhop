import keyboard
import time
import threading

def main():
    # Ask user for the interval in milliseconds
    try:
        interval_ms = float(input("Enter the interval between space bar presses (in milliseconds): "))
        if interval_ms <= 0:
            print("Interval must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Convert interval to seconds for time.sleep
    interval = interval_ms / 1000.0

    print("Hold the space bar to start auto-pressing. Press 'q' to quit.")

    def press_space():
        while True:
            # Check if space bar is held
            if keyboard.is_pressed('space'):
                keyboard.press('space')
                keyboard.release('space')
                time.sleep(interval)
            else:
                time.sleep(0.01)  # Small sleep to prevent high CPU usage
            # Check for quit condition
            if keyboard.is_pressed('q'):
                print("Exiting...")
                break

    # Run the space presser in a separate thread
    thread = threading.Thread(target=press_space)
    thread.start()
    thread.join()  # Wait for the thread to finish

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
