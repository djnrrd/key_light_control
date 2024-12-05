from typing import Union
import lifxlan
from lifxlan.errors import WorkflowException
from lifxlan.multizonelight import MultiZoneLight


def get_key_light() -> Union[MultiZoneLight, None]:
    """
    Get the object representing the key light, currently hard coded to 'Back Strip')

    :return: The light object or None
    """
    lan = lifxlan.LifxLAN(6)
    retry = 0
    light = None
    while retry < 3:
        try:
            light = lan.get_device_by_name("Back Strip")
            if light:
                retry = 3
            else:
                retry += 1
        except WorkflowException as E:
            retry += 1
    return light


def power_light(light: MultiZoneLight, state: str) -> bool:
    """
    Set the power state of the light object to either 'On' or 'Off'

    :param light: The key light object
    :param state: 'on' or 'off'
    :return: Success state
    """
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
    """
    Set the colour and brightness of the key light object to Blue Daylight

    :param light: The key light object
    :return: Success state
    """
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
    """
    Toggle the power status of the key light object between 'On' and 'Off'

    :param light: The key light object
    :return: Success state
    """
    retry = 0
    ret_value = False
    while retry < 3:
        try:
            state = light.get_power()
            if state > 0:
                result = power_light(light, "off")
            else:
                result = power_light(light, "on")
            if result:
                retry = 3
                ret_value = True
            else:
                retry += 1
        except WorkflowException as E:
            retry += 1
    return ret_value
