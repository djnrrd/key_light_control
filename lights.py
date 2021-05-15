import lifxlan
from lifxlan.errors import WorkflowException
import sys


def get_key_light():
    lan = lifxlan.LifxLAN(6)
    retry = 0
    while retry < 3:
        try:
            light = lan.get_device_by_name('Back Strip')
            if light:
                retry = 3
            else:
                retry += 1
        except WorkflowException as E:
            light = None
            retry += 1
    return light


def power_light(light, state):
    retry = 0
    ret_value = False
    while retry < 3:
        try:
            light.set_power(state)
            retry = 3
            ret_value = True
        except WorkflowException as E:
            retry += 1
    return ret_value


def set_blue_daylight(light):
    retry = 0
    ret_value = False
    while retry < 3:
        try:
            light.set_zone_color(0, 15, (35680, 0, 65535, 7500))
            retry = 3
            ret_value = True
        except WorkflowException as E:
            retry += 1
    return ret_value


def toggle_light(light):
    retry = 0
    ret_value = False
    while retry < 3:
        try:
            state = light.get_power()
            if state > 0:
                result = power_light(light, 'off')
            else:
                result = power_light(light, 'on')
            if result:
                retry = 3
                ret_value = True
            else:
                retry += 1
        except WorkflowException as E:
            retry += 1
    return ret_value


def main():
    # Get the light and make sure we found it
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


if __name__ == '__main__':
    main()
