import sys
from key_light_switch.lifx import get_key_light, toggle_light, set_blue_daylight


def main() -> None:
    key_light = get_key_light()
    if key_light:
        power_state = toggle_light(key_light)
        if power_state:
            blue = set_blue_daylight(key_light)
            if blue:
                sys.exit(0)
            else:
                sys.exit(3)
        else:
            sys.exit(2)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
