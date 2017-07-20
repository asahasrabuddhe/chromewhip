# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime
from chromewhip.protocol import debugger as Debugger

# ProfileNode: Profile node. Holds callsite information, execution statistics and child nodes.
class ProfileNode(ChromeTypeBase):
    def __init__(self,
                 id: Union['int'],
                 callFrame: Union['Runtime.CallFrame'],
                 hitCount: Optional['int'] = None,
                 children: Optional['[]'] = None,
                 deoptReason: Optional['str'] = None,
                 positionTicks: Optional['[PositionTickInfo]'] = None,
                 ):

        self.id = id
        self.callFrame = callFrame
        self.hitCount = hitCount
        self.children = children
        self.deoptReason = deoptReason
        self.positionTicks = positionTicks


# Profile: Profile.
class Profile(ChromeTypeBase):
    def __init__(self,
                 nodes: Union['[ProfileNode]'],
                 startTime: Union['float'],
                 endTime: Union['float'],
                 samples: Optional['[]'] = None,
                 timeDeltas: Optional['[]'] = None,
                 ):

        self.nodes = nodes
        self.startTime = startTime
        self.endTime = endTime
        self.samples = samples
        self.timeDeltas = timeDeltas


# PositionTickInfo: Specifies a number of samples attributed to a certain source position.
class PositionTickInfo(ChromeTypeBase):
    def __init__(self,
                 line: Union['int'],
                 ticks: Union['int'],
                 ):

        self.line = line
        self.ticks = ticks


# CoverageRange: Coverage data for a source range.
class CoverageRange(ChromeTypeBase):
    def __init__(self,
                 startOffset: Union['int'],
                 endOffset: Union['int'],
                 count: Union['int'],
                 ):

        self.startOffset = startOffset
        self.endOffset = endOffset
        self.count = count


# FunctionCoverage: Coverage data for a JavaScript function.
class FunctionCoverage(ChromeTypeBase):
    def __init__(self,
                 functionName: Union['str'],
                 ranges: Union['[CoverageRange]'],
                 isBlockCoverage: Union['bool'],
                 ):

        self.functionName = functionName
        self.ranges = ranges
        self.isBlockCoverage = isBlockCoverage


# ScriptCoverage: Coverage data for a JavaScript script.
class ScriptCoverage(ChromeTypeBase):
    def __init__(self,
                 scriptId: Union['Runtime.ScriptId'],
                 url: Union['str'],
                 functions: Union['[FunctionCoverage]'],
                 ):

        self.scriptId = scriptId
        self.url = url
        self.functions = functions


class Profiler(PayloadMixin):
    """ 
    """
    @classmethod
    def enable(cls):
        """
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def setSamplingInterval(cls,
                            interval: Union['int'],
                            ):
        """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.
        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        return (
            cls.build_send_payload("setSamplingInterval", {
                "interval": interval,
            }),
            None
        )

    @classmethod
    def start(cls):
        """
        """
        return (
            cls.build_send_payload("start", {
            }),
            None
        )

    @classmethod
    def stop(cls):
        """
        """
        return (
            cls.build_send_payload("stop", {
            }),
            cls.convert_payload({
                "profile": {
                    "class": Profile,
                    "optional": False
                },
            })
        )

    @classmethod
    def startPreciseCoverage(cls,
                             callCount: Optional['bool'] = None,
                             ):
        """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters.
        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: bool
        """
        return (
            cls.build_send_payload("startPreciseCoverage", {
                "callCount": callCount,
            }),
            None
        )

    @classmethod
    def stopPreciseCoverage(cls):
        """Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code.
        """
        return (
            cls.build_send_payload("stopPreciseCoverage", {
            }),
            None
        )

    @classmethod
    def takePreciseCoverage(cls):
        """Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started.
        """
        return (
            cls.build_send_payload("takePreciseCoverage", {
            }),
            cls.convert_payload({
                "result": {
                    "class": [ScriptCoverage],
                    "optional": False
                },
            })
        )

    @classmethod
    def getBestEffortCoverage(cls):
        """Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection.
        """
        return (
            cls.build_send_payload("getBestEffortCoverage", {
            }),
            cls.convert_payload({
                "result": {
                    "class": [ScriptCoverage],
                    "optional": False
                },
            })
        )



class ConsoleProfileStartedEvent(BaseEvent):

    js_name = 'Profiler.consoleProfileStarted'
    hashable = ['id']
    is_hashable = True

    def __init__(self,
                 id: Union['str', dict],
                 location: Union['Debugger.Location', dict],
                 title: Union['str', dict, None] = None,
                 ):
        if isinstance(id, dict):
            id = str(**id)
        self.id = id
        if isinstance(location, dict):
            location = Debugger.Location(**location)
        self.location = location
        if isinstance(title, dict):
            title = str(**title)
        self.title = title

    @classmethod
    def build_hash(cls, id):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ConsoleProfileFinishedEvent(BaseEvent):

    js_name = 'Profiler.consoleProfileFinished'
    hashable = ['id']
    is_hashable = True

    def __init__(self,
                 id: Union['str', dict],
                 location: Union['Debugger.Location', dict],
                 profile: Union['Profile', dict],
                 title: Union['str', dict, None] = None,
                 ):
        if isinstance(id, dict):
            id = str(**id)
        self.id = id
        if isinstance(location, dict):
            location = Debugger.Location(**location)
        self.location = location
        if isinstance(profile, dict):
            profile = Profile(**profile)
        self.profile = profile
        if isinstance(title, dict):
            title = str(**title)
        self.title = title

    @classmethod
    def build_hash(cls, id):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
