# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime

# BreakpointId: Breakpoint identifier.
BreakpointId = str

# CallFrameId: Call frame identifier.
CallFrameId = str

# Location: Location in the source code.
class Location(ChromeTypeBase):
    def __init__(self,
                 scriptId: Union['Runtime.ScriptId'],
                 lineNumber: Union['int'],
                 columnNumber: Optional['int'] = None,
                 ):

        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber


# ScriptPosition: Location in the source code.
class ScriptPosition(ChromeTypeBase):
    def __init__(self,
                 lineNumber: Union['int'],
                 columnNumber: Union['int'],
                 ):

        self.lineNumber = lineNumber
        self.columnNumber = columnNumber


# CallFrame: JavaScript call frame. Array of call frames form the call stack.
class CallFrame(ChromeTypeBase):
    def __init__(self,
                 callFrameId: Union['CallFrameId'],
                 functionName: Union['str'],
                 location: Union['Location'],
                 scopeChain: Union['[Scope]'],
                 this: Union['Runtime.RemoteObject'],
                 functionLocation: Optional['Location'] = None,
                 returnValue: Optional['Runtime.RemoteObject'] = None,
                 ):

        self.callFrameId = callFrameId
        self.functionName = functionName
        self.functionLocation = functionLocation
        self.location = location
        self.scopeChain = scopeChain
        self.this = this
        self.returnValue = returnValue


# Scope: Scope description.
class Scope(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 object: Union['Runtime.RemoteObject'],
                 name: Optional['str'] = None,
                 startLocation: Optional['Location'] = None,
                 endLocation: Optional['Location'] = None,
                 ):

        self.type = type
        self.object = object
        self.name = name
        self.startLocation = startLocation
        self.endLocation = endLocation


# SearchMatch: Search match for resource.
class SearchMatch(ChromeTypeBase):
    def __init__(self,
                 lineNumber: Union['float'],
                 lineContent: Union['str'],
                 ):

        self.lineNumber = lineNumber
        self.lineContent = lineContent


# BreakLocation: 
class BreakLocation(ChromeTypeBase):
    def __init__(self,
                 scriptId: Union['Runtime.ScriptId'],
                 lineNumber: Union['int'],
                 columnNumber: Optional['int'] = None,
                 type: Optional['str'] = None,
                 ):

        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.type = type


class Debugger(PayloadMixin):
    """ Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing breakpoints, stepping through execution, exploring stack traces, etc.
    """
    @classmethod
    def enable(cls):
        """Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables debugger for given page.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def setBreakpointsActive(cls,
                             active: Union['bool'],
                             ):
        """Activates / deactivates all breakpoints on the page.
        :param active: New value for breakpoints active state.
        :type active: bool
        """
        return (
            cls.build_send_payload("setBreakpointsActive", {
                "active": active,
            }),
            None
        )

    @classmethod
    def setSkipAllPauses(cls,
                         skip: Union['bool'],
                         ):
        """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).
        :param skip: New value for skip pauses state.
        :type skip: bool
        """
        return (
            cls.build_send_payload("setSkipAllPauses", {
                "skip": skip,
            }),
            None
        )

    @classmethod
    def setBreakpointByUrl(cls,
                           lineNumber: Union['int'],
                           url: Optional['str'] = None,
                           urlRegex: Optional['str'] = None,
                           columnNumber: Optional['int'] = None,
                           condition: Optional['str'] = None,
                           ):
        """Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in <code>locations</code> property. Further matching script parsing will result in subsequent <code>breakpointResolved</code> events issued. This logical breakpoint will survive page reloads.
        :param lineNumber: Line number to set breakpoint at.
        :type lineNumber: int
        :param url: URL of the resources to set breakpoint on.
        :type url: str
        :param urlRegex: Regex pattern for the URLs of the resources to set breakpoints on. Either <code>url</code> or <code>urlRegex</code> must be specified.
        :type urlRegex: str
        :param columnNumber: Offset in the line to set breakpoint at.
        :type columnNumber: int
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        :type condition: str
        """
        return (
            cls.build_send_payload("setBreakpointByUrl", {
                "lineNumber": lineNumber,
                "url": url,
                "urlRegex": urlRegex,
                "columnNumber": columnNumber,
                "condition": condition,
            }),
            cls.convert_payload({
                "breakpointId": {
                    "class": BreakpointId,
                    "optional": False
                },
                "locations": {
                    "class": [Location],
                    "optional": False
                },
            })
        )

    @classmethod
    def setBreakpoint(cls,
                      location: Union['Location'],
                      condition: Optional['str'] = None,
                      ):
        """Sets JavaScript breakpoint at a given location.
        :param location: Location to set breakpoint in.
        :type location: Location
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        :type condition: str
        """
        return (
            cls.build_send_payload("setBreakpoint", {
                "location": location,
                "condition": condition,
            }),
            cls.convert_payload({
                "breakpointId": {
                    "class": BreakpointId,
                    "optional": False
                },
                "actualLocation": {
                    "class": Location,
                    "optional": False
                },
            })
        )

    @classmethod
    def removeBreakpoint(cls,
                         breakpointId: Union['BreakpointId'],
                         ):
        """Removes JavaScript breakpoint.
        :param breakpointId: 
        :type breakpointId: BreakpointId
        """
        return (
            cls.build_send_payload("removeBreakpoint", {
                "breakpointId": breakpointId,
            }),
            None
        )

    @classmethod
    def getPossibleBreakpoints(cls,
                               start: Union['Location'],
                               end: Optional['Location'] = None,
                               restrictToFunction: Optional['bool'] = None,
                               ):
        """Returns possible locations for breakpoint. scriptId in start and end range locations should be the same.
        :param start: Start of range to search possible breakpoint locations in.
        :type start: Location
        :param end: End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range.
        :type end: Location
        :param restrictToFunction: Only consider locations which are in the same (non-nested) function as start.
        :type restrictToFunction: bool
        """
        return (
            cls.build_send_payload("getPossibleBreakpoints", {
                "start": start,
                "end": end,
                "restrictToFunction": restrictToFunction,
            }),
            cls.convert_payload({
                "locations": {
                    "class": [BreakLocation],
                    "optional": False
                },
            })
        )

    @classmethod
    def continueToLocation(cls,
                           location: Union['Location'],
                           targetCallFrames: Optional['str'] = None,
                           ):
        """Continues execution until specific location is reached.
        :param location: Location to continue to.
        :type location: Location
        :param targetCallFrames: 
        :type targetCallFrames: str
        """
        return (
            cls.build_send_payload("continueToLocation", {
                "location": location,
                "targetCallFrames": targetCallFrames,
            }),
            None
        )

    @classmethod
    def stepOver(cls):
        """Steps over the statement.
        """
        return (
            cls.build_send_payload("stepOver", {
            }),
            None
        )

    @classmethod
    def stepInto(cls):
        """Steps into the function call.
        """
        return (
            cls.build_send_payload("stepInto", {
            }),
            None
        )

    @classmethod
    def stepOut(cls):
        """Steps out of the function call.
        """
        return (
            cls.build_send_payload("stepOut", {
            }),
            None
        )

    @classmethod
    def pause(cls):
        """Stops on the next JavaScript statement.
        """
        return (
            cls.build_send_payload("pause", {
            }),
            None
        )

    @classmethod
    def scheduleStepIntoAsync(cls):
        """Steps into next scheduled async task if any is scheduled before next pause. Returns success when async task is actually scheduled, returns error if no task were scheduled or another scheduleStepIntoAsync was called.
        """
        return (
            cls.build_send_payload("scheduleStepIntoAsync", {
            }),
            None
        )

    @classmethod
    def resume(cls):
        """Resumes JavaScript execution.
        """
        return (
            cls.build_send_payload("resume", {
            }),
            None
        )

    @classmethod
    def searchInContent(cls,
                        scriptId: Union['Runtime.ScriptId'],
                        query: Union['str'],
                        caseSensitive: Optional['bool'] = None,
                        isRegex: Optional['bool'] = None,
                        ):
        """Searches for given string in script content.
        :param scriptId: Id of the script to search in.
        :type scriptId: Runtime.ScriptId
        :param query: String to search for.
        :type query: str
        :param caseSensitive: If true, search is case sensitive.
        :type caseSensitive: bool
        :param isRegex: If true, treats string parameter as regex.
        :type isRegex: bool
        """
        return (
            cls.build_send_payload("searchInContent", {
                "scriptId": scriptId,
                "query": query,
                "caseSensitive": caseSensitive,
                "isRegex": isRegex,
            }),
            cls.convert_payload({
                "result": {
                    "class": [SearchMatch],
                    "optional": False
                },
            })
        )

    @classmethod
    def setScriptSource(cls,
                        scriptId: Union['Runtime.ScriptId'],
                        scriptSource: Union['str'],
                        dryRun: Optional['bool'] = None,
                        ):
        """Edits JavaScript source live.
        :param scriptId: Id of the script to edit.
        :type scriptId: Runtime.ScriptId
        :param scriptSource: New content of the script.
        :type scriptSource: str
        :param dryRun:  If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code.
        :type dryRun: bool
        """
        return (
            cls.build_send_payload("setScriptSource", {
                "scriptId": scriptId,
                "scriptSource": scriptSource,
                "dryRun": dryRun,
            }),
            cls.convert_payload({
                "callFrames": {
                    "class": [CallFrame],
                    "optional": True
                },
                "stackChanged": {
                    "class": bool,
                    "optional": True
                },
                "asyncStackTrace": {
                    "class": Runtime.StackTrace,
                    "optional": True
                },
                "exceptionDetails": {
                    "class": Runtime.ExceptionDetails,
                    "optional": True
                },
            })
        )

    @classmethod
    def restartFrame(cls,
                     callFrameId: Union['CallFrameId'],
                     ):
        """Restarts particular call frame from the beginning.
        :param callFrameId: Call frame identifier to evaluate on.
        :type callFrameId: CallFrameId
        """
        return (
            cls.build_send_payload("restartFrame", {
                "callFrameId": callFrameId,
            }),
            cls.convert_payload({
                "callFrames": {
                    "class": [CallFrame],
                    "optional": False
                },
                "asyncStackTrace": {
                    "class": Runtime.StackTrace,
                    "optional": True
                },
            })
        )

    @classmethod
    def getScriptSource(cls,
                        scriptId: Union['Runtime.ScriptId'],
                        ):
        """Returns source for the script with given id.
        :param scriptId: Id of the script to get source for.
        :type scriptId: Runtime.ScriptId
        """
        return (
            cls.build_send_payload("getScriptSource", {
                "scriptId": scriptId,
            }),
            cls.convert_payload({
                "scriptSource": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def setPauseOnExceptions(cls,
                             state: Union['str'],
                             ):
        """Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or no exceptions. Initial pause on exceptions state is <code>none</code>.
        :param state: Pause on exceptions mode.
        :type state: str
        """
        return (
            cls.build_send_payload("setPauseOnExceptions", {
                "state": state,
            }),
            None
        )

    @classmethod
    def evaluateOnCallFrame(cls,
                            callFrameId: Union['CallFrameId'],
                            expression: Union['str'],
                            objectGroup: Optional['str'] = None,
                            includeCommandLineAPI: Optional['bool'] = None,
                            silent: Optional['bool'] = None,
                            returnByValue: Optional['bool'] = None,
                            generatePreview: Optional['bool'] = None,
                            throwOnSideEffect: Optional['bool'] = None,
                            ):
        """Evaluates expression on a given call frame.
        :param callFrameId: Call frame identifier to evaluate on.
        :type callFrameId: CallFrameId
        :param expression: Expression to evaluate.
        :type expression: str
        :param objectGroup: String object group name to put result into (allows rapid releasing resulting object handles using <code>releaseObjectGroup</code>).
        :type objectGroup: str
        :param includeCommandLineAPI: Specifies whether command line API should be available to the evaluated expression, defaults to false.
        :type includeCommandLineAPI: bool
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
        :type silent: bool
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: bool
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: bool
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :type throwOnSideEffect: bool
        """
        return (
            cls.build_send_payload("evaluateOnCallFrame", {
                "callFrameId": callFrameId,
                "expression": expression,
                "objectGroup": objectGroup,
                "includeCommandLineAPI": includeCommandLineAPI,
                "silent": silent,
                "returnByValue": returnByValue,
                "generatePreview": generatePreview,
                "throwOnSideEffect": throwOnSideEffect,
            }),
            cls.convert_payload({
                "result": {
                    "class": Runtime.RemoteObject,
                    "optional": False
                },
                "exceptionDetails": {
                    "class": Runtime.ExceptionDetails,
                    "optional": True
                },
            })
        )

    @classmethod
    def setVariableValue(cls,
                         scopeNumber: Union['int'],
                         variableName: Union['str'],
                         newValue: Union['Runtime.CallArgument'],
                         callFrameId: Union['CallFrameId'],
                         ):
        """Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually.
        :param scopeNumber: 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually.
        :type scopeNumber: int
        :param variableName: Variable name.
        :type variableName: str
        :param newValue: New variable value.
        :type newValue: Runtime.CallArgument
        :param callFrameId: Id of callframe that holds variable.
        :type callFrameId: CallFrameId
        """
        return (
            cls.build_send_payload("setVariableValue", {
                "scopeNumber": scopeNumber,
                "variableName": variableName,
                "newValue": newValue,
                "callFrameId": callFrameId,
            }),
            None
        )

    @classmethod
    def setAsyncCallStackDepth(cls,
                               maxDepth: Union['int'],
                               ):
        """Enables or disables async call stacks tracking.
        :param maxDepth: Maximum depth of async call stacks. Setting to <code>0</code> will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        return (
            cls.build_send_payload("setAsyncCallStackDepth", {
                "maxDepth": maxDepth,
            }),
            None
        )

    @classmethod
    def setBlackboxPatterns(cls,
                            patterns: Union['[]'],
                            ):
        """Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        :type patterns: []
        """
        return (
            cls.build_send_payload("setBlackboxPatterns", {
                "patterns": patterns,
            }),
            None
        )

    @classmethod
    def setBlackboxedRanges(cls,
                            scriptId: Union['Runtime.ScriptId'],
                            positions: Union['[ScriptPosition]'],
                            ):
        """Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted.
        :param scriptId: Id of the script.
        :type scriptId: Runtime.ScriptId
        :param positions: 
        :type positions: [ScriptPosition]
        """
        return (
            cls.build_send_payload("setBlackboxedRanges", {
                "scriptId": scriptId,
                "positions": positions,
            }),
            None
        )



class ScriptParsedEvent(BaseEvent):

    js_name = 'Debugger.scriptParsed'
    hashable = ['scriptId', 'executionContextId']
    is_hashable = True

    def __init__(self,
                 scriptId: Union['Runtime.ScriptId', dict],
                 url: Union['str', dict],
                 startLine: Union['int', dict],
                 startColumn: Union['int', dict],
                 endLine: Union['int', dict],
                 endColumn: Union['int', dict],
                 executionContextId: Union['Runtime.ExecutionContextId', dict],
                 hash: Union['str', dict],
                 executionContextAuxData: Union['dict', dict, None] = None,
                 isLiveEdit: Union['bool', dict, None] = None,
                 sourceMapURL: Union['str', dict, None] = None,
                 hasSourceURL: Union['bool', dict, None] = None,
                 isModule: Union['bool', dict, None] = None,
                 length: Union['int', dict, None] = None,
                 stackTrace: Union['Runtime.StackTrace', dict, None] = None,
                 ):
        if isinstance(scriptId, dict):
            scriptId = Runtime.ScriptId(**scriptId)
        self.scriptId = scriptId
        if isinstance(url, dict):
            url = str(**url)
        self.url = url
        if isinstance(startLine, dict):
            startLine = int(**startLine)
        self.startLine = startLine
        if isinstance(startColumn, dict):
            startColumn = int(**startColumn)
        self.startColumn = startColumn
        if isinstance(endLine, dict):
            endLine = int(**endLine)
        self.endLine = endLine
        if isinstance(endColumn, dict):
            endColumn = int(**endColumn)
        self.endColumn = endColumn
        if isinstance(executionContextId, dict):
            executionContextId = Runtime.ExecutionContextId(**executionContextId)
        self.executionContextId = executionContextId
        if isinstance(hash, dict):
            hash = str(**hash)
        self.hash = hash
        if isinstance(executionContextAuxData, dict):
            executionContextAuxData = dict(**executionContextAuxData)
        self.executionContextAuxData = executionContextAuxData
        if isinstance(isLiveEdit, dict):
            isLiveEdit = bool(**isLiveEdit)
        self.isLiveEdit = isLiveEdit
        if isinstance(sourceMapURL, dict):
            sourceMapURL = str(**sourceMapURL)
        self.sourceMapURL = sourceMapURL
        if isinstance(hasSourceURL, dict):
            hasSourceURL = bool(**hasSourceURL)
        self.hasSourceURL = hasSourceURL
        if isinstance(isModule, dict):
            isModule = bool(**isModule)
        self.isModule = isModule
        if isinstance(length, dict):
            length = int(**length)
        self.length = length
        if isinstance(stackTrace, dict):
            stackTrace = Runtime.StackTrace(**stackTrace)
        self.stackTrace = stackTrace

    @classmethod
    def build_hash(cls, scriptId, executionContextId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ScriptFailedToParseEvent(BaseEvent):

    js_name = 'Debugger.scriptFailedToParse'
    hashable = ['scriptId', 'executionContextId']
    is_hashable = True

    def __init__(self,
                 scriptId: Union['Runtime.ScriptId', dict],
                 url: Union['str', dict],
                 startLine: Union['int', dict],
                 startColumn: Union['int', dict],
                 endLine: Union['int', dict],
                 endColumn: Union['int', dict],
                 executionContextId: Union['Runtime.ExecutionContextId', dict],
                 hash: Union['str', dict],
                 executionContextAuxData: Union['dict', dict, None] = None,
                 sourceMapURL: Union['str', dict, None] = None,
                 hasSourceURL: Union['bool', dict, None] = None,
                 isModule: Union['bool', dict, None] = None,
                 length: Union['int', dict, None] = None,
                 stackTrace: Union['Runtime.StackTrace', dict, None] = None,
                 ):
        if isinstance(scriptId, dict):
            scriptId = Runtime.ScriptId(**scriptId)
        self.scriptId = scriptId
        if isinstance(url, dict):
            url = str(**url)
        self.url = url
        if isinstance(startLine, dict):
            startLine = int(**startLine)
        self.startLine = startLine
        if isinstance(startColumn, dict):
            startColumn = int(**startColumn)
        self.startColumn = startColumn
        if isinstance(endLine, dict):
            endLine = int(**endLine)
        self.endLine = endLine
        if isinstance(endColumn, dict):
            endColumn = int(**endColumn)
        self.endColumn = endColumn
        if isinstance(executionContextId, dict):
            executionContextId = Runtime.ExecutionContextId(**executionContextId)
        self.executionContextId = executionContextId
        if isinstance(hash, dict):
            hash = str(**hash)
        self.hash = hash
        if isinstance(executionContextAuxData, dict):
            executionContextAuxData = dict(**executionContextAuxData)
        self.executionContextAuxData = executionContextAuxData
        if isinstance(sourceMapURL, dict):
            sourceMapURL = str(**sourceMapURL)
        self.sourceMapURL = sourceMapURL
        if isinstance(hasSourceURL, dict):
            hasSourceURL = bool(**hasSourceURL)
        self.hasSourceURL = hasSourceURL
        if isinstance(isModule, dict):
            isModule = bool(**isModule)
        self.isModule = isModule
        if isinstance(length, dict):
            length = int(**length)
        self.length = length
        if isinstance(stackTrace, dict):
            stackTrace = Runtime.StackTrace(**stackTrace)
        self.stackTrace = stackTrace

    @classmethod
    def build_hash(cls, scriptId, executionContextId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class BreakpointResolvedEvent(BaseEvent):

    js_name = 'Debugger.breakpointResolved'
    hashable = ['breakpointId']
    is_hashable = True

    def __init__(self,
                 breakpointId: Union['BreakpointId', dict],
                 location: Union['Location', dict],
                 ):
        if isinstance(breakpointId, dict):
            breakpointId = BreakpointId(**breakpointId)
        self.breakpointId = breakpointId
        if isinstance(location, dict):
            location = Location(**location)
        self.location = location

    @classmethod
    def build_hash(cls, breakpointId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PausedEvent(BaseEvent):

    js_name = 'Debugger.paused'
    hashable = []
    is_hashable = False

    def __init__(self,
                 callFrames: Union['[CallFrame]', dict],
                 reason: Union['str', dict],
                 data: Union['dict', dict, None] = None,
                 hitBreakpoints: Union['[]', dict, None] = None,
                 asyncStackTrace: Union['Runtime.StackTrace', dict, None] = None,
                 ):
        if isinstance(callFrames, dict):
            callFrames = [CallFrame](**callFrames)
        self.callFrames = callFrames
        if isinstance(reason, dict):
            reason = str(**reason)
        self.reason = reason
        if isinstance(data, dict):
            data = dict(**data)
        self.data = data
        if isinstance(hitBreakpoints, dict):
            hitBreakpoints = [](**hitBreakpoints)
        self.hitBreakpoints = hitBreakpoints
        if isinstance(asyncStackTrace, dict):
            asyncStackTrace = Runtime.StackTrace(**asyncStackTrace)
        self.asyncStackTrace = asyncStackTrace

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class ResumedEvent(BaseEvent):

    js_name = 'Debugger.resumed'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
