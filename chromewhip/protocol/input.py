# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# TouchPoint: 
class TouchPoint(ChromeTypeBase):
    def __init__(self,
                 state: Union['str'],
                 x: Union['int'],
                 y: Union['int'],
                 radiusX: Optional['int'] = None,
                 radiusY: Optional['int'] = None,
                 rotationAngle: Optional['float'] = None,
                 force: Optional['float'] = None,
                 id: Optional['float'] = None,
                 ):

        self.state = state
        self.x = x
        self.y = y
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.rotationAngle = rotationAngle
        self.force = force
        self.id = id


# GestureSourceType: 
GestureSourceType = str

# TimeSinceEpoch: UTC time in seconds, counted from January 1, 1970.
TimeSinceEpoch = float

class Input(PayloadMixin):
    """ 
    """
    @classmethod
    def setIgnoreInputEvents(cls,
                             ignore: Union['bool'],
                             ):
        """Ignores input events (useful while auditing page).
        :param ignore: Ignores input events processing when set to true.
        :type ignore: bool
        """
        return (
            cls.build_send_payload("setIgnoreInputEvents", {
                "ignore": ignore,
            }),
            None
        )

    @classmethod
    def dispatchKeyEvent(cls,
                         type: Union['str'],
                         modifiers: Optional['int'] = None,
                         timestamp: Optional['TimeSinceEpoch'] = None,
                         text: Optional['str'] = None,
                         unmodifiedText: Optional['str'] = None,
                         keyIdentifier: Optional['str'] = None,
                         code: Optional['str'] = None,
                         key: Optional['str'] = None,
                         windowsVirtualKeyCode: Optional['int'] = None,
                         nativeVirtualKeyCode: Optional['int'] = None,
                         autoRepeat: Optional['bool'] = None,
                         isKeypad: Optional['bool'] = None,
                         isSystemKey: Optional['bool'] = None,
                         ):
        """Dispatches a key event to the page.
        :param type: Type of the key event.
        :type type: str
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: int
        :param timestamp: Time at which the event occurred.
        :type timestamp: TimeSinceEpoch
        :param text: Text as generated by processing a virtual key code with a keyboard layout. Not needed for for <code>keyUp</code> and <code>rawKeyDown</code> events (default: "")
        :type text: str
        :param unmodifiedText: Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: "").
        :type unmodifiedText: str
        :param keyIdentifier: Unique key identifier (e.g., 'U+0041') (default: "").
        :type keyIdentifier: str
        :param code: Unique DOM defined string value for each physical key (e.g., 'KeyA') (default: "").
        :type code: str
        :param key: Unique DOM defined string value describing the meaning of the key in the context of active modifiers, keyboard layout, etc (e.g., 'AltGr') (default: "").
        :type key: str
        :param windowsVirtualKeyCode: Windows virtual key code (default: 0).
        :type windowsVirtualKeyCode: int
        :param nativeVirtualKeyCode: Native virtual key code (default: 0).
        :type nativeVirtualKeyCode: int
        :param autoRepeat: Whether the event was generated from auto repeat (default: false).
        :type autoRepeat: bool
        :param isKeypad: Whether the event was generated from the keypad (default: false).
        :type isKeypad: bool
        :param isSystemKey: Whether the event was a system key event (default: false).
        :type isSystemKey: bool
        """
        return (
            cls.build_send_payload("dispatchKeyEvent", {
                "type": type,
                "modifiers": modifiers,
                "timestamp": timestamp,
                "text": text,
                "unmodifiedText": unmodifiedText,
                "keyIdentifier": keyIdentifier,
                "code": code,
                "key": key,
                "windowsVirtualKeyCode": windowsVirtualKeyCode,
                "nativeVirtualKeyCode": nativeVirtualKeyCode,
                "autoRepeat": autoRepeat,
                "isKeypad": isKeypad,
                "isSystemKey": isSystemKey,
            }),
            None
        )

    @classmethod
    def dispatchMouseEvent(cls,
                           type: Union['str'],
                           x: Union['float'],
                           y: Union['float'],
                           modifiers: Optional['int'] = None,
                           timestamp: Optional['TimeSinceEpoch'] = None,
                           button: Optional['str'] = None,
                           clickCount: Optional['int'] = None,
                           ):
        """Dispatches a mouse event to the page.
        :param type: Type of the mouse event.
        :type type: str
        :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
        :type x: float
        :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
        :type y: float
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: int
        :param timestamp: Time at which the event occurred.
        :type timestamp: TimeSinceEpoch
        :param button: Mouse button (default: "none").
        :type button: str
        :param clickCount: Number of times the mouse button was clicked (default: 0).
        :type clickCount: int
        """
        return (
            cls.build_send_payload("dispatchMouseEvent", {
                "type": type,
                "x": x,
                "y": y,
                "modifiers": modifiers,
                "timestamp": timestamp,
                "button": button,
                "clickCount": clickCount,
            }),
            None
        )

    @classmethod
    def dispatchTouchEvent(cls,
                           type: Union['str'],
                           touchPoints: Union['[TouchPoint]'],
                           modifiers: Optional['int'] = None,
                           timestamp: Optional['TimeSinceEpoch'] = None,
                           ):
        """Dispatches a touch event to the page.
        :param type: Type of the touch event.
        :type type: str
        :param touchPoints: Touch points.
        :type touchPoints: [TouchPoint]
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: int
        :param timestamp: Time at which the event occurred.
        :type timestamp: TimeSinceEpoch
        """
        return (
            cls.build_send_payload("dispatchTouchEvent", {
                "type": type,
                "touchPoints": touchPoints,
                "modifiers": modifiers,
                "timestamp": timestamp,
            }),
            None
        )

    @classmethod
    def emulateTouchFromMouseEvent(cls,
                                   type: Union['str'],
                                   x: Union['int'],
                                   y: Union['int'],
                                   timestamp: Union['TimeSinceEpoch'],
                                   button: Union['str'],
                                   deltaX: Optional['float'] = None,
                                   deltaY: Optional['float'] = None,
                                   modifiers: Optional['int'] = None,
                                   clickCount: Optional['int'] = None,
                                   ):
        """Emulates touch event from the mouse event parameters.
        :param type: Type of the mouse event.
        :type type: str
        :param x: X coordinate of the mouse pointer in DIP.
        :type x: int
        :param y: Y coordinate of the mouse pointer in DIP.
        :type y: int
        :param timestamp: Time at which the event occurred.
        :type timestamp: TimeSinceEpoch
        :param button: Mouse button.
        :type button: str
        :param deltaX: X delta in DIP for mouse wheel event (default: 0).
        :type deltaX: float
        :param deltaY: Y delta in DIP for mouse wheel event (default: 0).
        :type deltaY: float
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: int
        :param clickCount: Number of times the mouse button was clicked (default: 0).
        :type clickCount: int
        """
        return (
            cls.build_send_payload("emulateTouchFromMouseEvent", {
                "type": type,
                "x": x,
                "y": y,
                "timestamp": timestamp,
                "button": button,
                "deltaX": deltaX,
                "deltaY": deltaY,
                "modifiers": modifiers,
                "clickCount": clickCount,
            }),
            None
        )

    @classmethod
    def synthesizePinchGesture(cls,
                               x: Union['float'],
                               y: Union['float'],
                               scaleFactor: Union['float'],
                               relativeSpeed: Optional['int'] = None,
                               gestureSourceType: Optional['GestureSourceType'] = None,
                               ):
        """Synthesizes a pinch gesture over a time period by issuing appropriate touch events.
        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param scaleFactor: Relative scale factor after zooming (>1.0 zooms in, <1.0 zooms out).
        :type scaleFactor: float
        :param relativeSpeed: Relative pointer speed in pixels per second (default: 800).
        :type relativeSpeed: int
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: GestureSourceType
        """
        return (
            cls.build_send_payload("synthesizePinchGesture", {
                "x": x,
                "y": y,
                "scaleFactor": scaleFactor,
                "relativeSpeed": relativeSpeed,
                "gestureSourceType": gestureSourceType,
            }),
            None
        )

    @classmethod
    def synthesizeScrollGesture(cls,
                                x: Union['float'],
                                y: Union['float'],
                                xDistance: Optional['float'] = None,
                                yDistance: Optional['float'] = None,
                                xOverscroll: Optional['float'] = None,
                                yOverscroll: Optional['float'] = None,
                                preventFling: Optional['bool'] = None,
                                speed: Optional['int'] = None,
                                gestureSourceType: Optional['GestureSourceType'] = None,
                                repeatCount: Optional['int'] = None,
                                repeatDelayMs: Optional['int'] = None,
                                interactionMarkerName: Optional['str'] = None,
                                ):
        """Synthesizes a scroll gesture over a time period by issuing appropriate touch events.
        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param xDistance: The distance to scroll along the X axis (positive to scroll left).
        :type xDistance: float
        :param yDistance: The distance to scroll along the Y axis (positive to scroll up).
        :type yDistance: float
        :param xOverscroll: The number of additional pixels to scroll back along the X axis, in addition to the given distance.
        :type xOverscroll: float
        :param yOverscroll: The number of additional pixels to scroll back along the Y axis, in addition to the given distance.
        :type yOverscroll: float
        :param preventFling: Prevent fling (default: true).
        :type preventFling: bool
        :param speed: Swipe speed in pixels per second (default: 800).
        :type speed: int
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: GestureSourceType
        :param repeatCount: The number of times to repeat the gesture (default: 0).
        :type repeatCount: int
        :param repeatDelayMs: The number of milliseconds delay between each repeat. (default: 250).
        :type repeatDelayMs: int
        :param interactionMarkerName: The name of the interaction markers to generate, if not empty (default: "").
        :type interactionMarkerName: str
        """
        return (
            cls.build_send_payload("synthesizeScrollGesture", {
                "x": x,
                "y": y,
                "xDistance": xDistance,
                "yDistance": yDistance,
                "xOverscroll": xOverscroll,
                "yOverscroll": yOverscroll,
                "preventFling": preventFling,
                "speed": speed,
                "gestureSourceType": gestureSourceType,
                "repeatCount": repeatCount,
                "repeatDelayMs": repeatDelayMs,
                "interactionMarkerName": interactionMarkerName,
            }),
            None
        )

    @classmethod
    def synthesizeTapGesture(cls,
                             x: Union['float'],
                             y: Union['float'],
                             duration: Optional['int'] = None,
                             tapCount: Optional['int'] = None,
                             gestureSourceType: Optional['GestureSourceType'] = None,
                             ):
        """Synthesizes a tap gesture over a time period by issuing appropriate touch events.
        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param duration: Duration between touchdown and touchup events in ms (default: 50).
        :type duration: int
        :param tapCount: Number of times to perform the tap (e.g. 2 for double tap, default: 1).
        :type tapCount: int
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: GestureSourceType
        """
        return (
            cls.build_send_payload("synthesizeTapGesture", {
                "x": x,
                "y": y,
                "duration": duration,
                "tapCount": tapCount,
                "gestureSourceType": gestureSourceType,
            }),
            None
        )

