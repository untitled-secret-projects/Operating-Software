from enum import Enum

# Enumerator class that captures the four commands we will use in the Raspberry PI.
# Enter, Back, Left, Right.
class Command(Enum):
    enter = "Enter"
    back = "Back"
    left = "Left"
    right = "Right"
    