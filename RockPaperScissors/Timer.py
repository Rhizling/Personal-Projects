import time


def countdown(time_sec) -> None:
    # Delays the system a specified amount of seconds in the parameter
    while time_sec:
        time.sleep(1)
        time_sec -= 1
