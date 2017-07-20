# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

class DeviceOrientation(PayloadMixin):
    """ 
    """
    @classmethod
    def setDeviceOrientationOverride(cls,
                                     alpha: Union['float'],
                                     beta: Union['float'],
                                     gamma: Union['float'],
                                     ):
        """Overrides the Device Orientation.
        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        return (
            cls.build_send_payload("setDeviceOrientationOverride", {
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
            }),
            None
        )

    @classmethod
    def clearDeviceOrientationOverride(cls):
        """Clears the overridden Device Orientation.
        """
        return (
            cls.build_send_payload("clearDeviceOrientationOverride", {
            }),
            None
        )

