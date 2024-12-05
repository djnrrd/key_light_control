from typing import Union
import lifxlan
from lifxlan.errors import WorkflowException
from lifxlan.multizonelight import MultiZoneLight


def get_key_light() -> Union[MultiZoneLight, None]:
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


def power_light(light: MultiZoneLight, state: str) -> bool:
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


def set_blue_daylight(light: MultiZoneLight) -> bool:
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


def toggle_light(light: MultiZoneLight) -> bool:
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
