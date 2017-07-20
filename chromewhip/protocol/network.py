# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime
from chromewhip.protocol import security as Security

# LoaderId: Unique loader identifier.
LoaderId = str

# RequestId: Unique request identifier.
RequestId = str

# InterceptionId: Unique intercepted request identifier.
InterceptionId = str

# ErrorReason: Network level fetch failure reason.
ErrorReason = str

# TimeSinceEpoch: UTC time in seconds, counted from January 1, 1970.
TimeSinceEpoch = float

# MonotonicTime: Monotonically increasing time in seconds since an arbitrary point in the past.
MonotonicTime = float

# Headers: Request / response headers as keys / values of JSON object.
Headers = dict

# ConnectionType: Loading priority of a resource request.
ConnectionType = str

# CookieSameSite: Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies
CookieSameSite = str

# ResourceTiming: Timing information for the request.
class ResourceTiming(ChromeTypeBase):
    def __init__(self,
                 requestTime: Union['float'],
                 proxyStart: Union['float'],
                 proxyEnd: Union['float'],
                 dnsStart: Union['float'],
                 dnsEnd: Union['float'],
                 connectStart: Union['float'],
                 connectEnd: Union['float'],
                 sslStart: Union['float'],
                 sslEnd: Union['float'],
                 workerStart: Union['float'],
                 workerReady: Union['float'],
                 sendStart: Union['float'],
                 sendEnd: Union['float'],
                 pushStart: Union['float'],
                 pushEnd: Union['float'],
                 receiveHeadersEnd: Union['float'],
                 ):

        self.requestTime = requestTime
        self.proxyStart = proxyStart
        self.proxyEnd = proxyEnd
        self.dnsStart = dnsStart
        self.dnsEnd = dnsEnd
        self.connectStart = connectStart
        self.connectEnd = connectEnd
        self.sslStart = sslStart
        self.sslEnd = sslEnd
        self.workerStart = workerStart
        self.workerReady = workerReady
        self.sendStart = sendStart
        self.sendEnd = sendEnd
        self.pushStart = pushStart
        self.pushEnd = pushEnd
        self.receiveHeadersEnd = receiveHeadersEnd


# ResourcePriority: Loading priority of a resource request.
ResourcePriority = str

# Request: HTTP request data.
class Request(ChromeTypeBase):
    def __init__(self,
                 url: Union['str'],
                 method: Union['str'],
                 headers: Union['Headers'],
                 initialPriority: Union['ResourcePriority'],
                 referrerPolicy: Union['str'],
                 postData: Optional['str'] = None,
                 mixedContentType: Optional['Security.MixedContentType'] = None,
                 isLinkPreload: Optional['bool'] = None,
                 ):

        self.url = url
        self.method = method
        self.headers = headers
        self.postData = postData
        self.mixedContentType = mixedContentType
        self.initialPriority = initialPriority
        self.referrerPolicy = referrerPolicy
        self.isLinkPreload = isLinkPreload


# SignedCertificateTimestamp: Details of a signed certificate timestamp (SCT).
class SignedCertificateTimestamp(ChromeTypeBase):
    def __init__(self,
                 status: Union['str'],
                 origin: Union['str'],
                 logDescription: Union['str'],
                 logId: Union['str'],
                 timestamp: Union['TimeSinceEpoch'],
                 hashAlgorithm: Union['str'],
                 signatureAlgorithm: Union['str'],
                 signatureData: Union['str'],
                 ):

        self.status = status
        self.origin = origin
        self.logDescription = logDescription
        self.logId = logId
        self.timestamp = timestamp
        self.hashAlgorithm = hashAlgorithm
        self.signatureAlgorithm = signatureAlgorithm
        self.signatureData = signatureData


# SecurityDetails: Security details about a request.
class SecurityDetails(ChromeTypeBase):
    def __init__(self,
                 protocol: Union['str'],
                 keyExchange: Union['str'],
                 cipher: Union['str'],
                 certificateId: Union['Security.CertificateId'],
                 subjectName: Union['str'],
                 sanList: Union['[]'],
                 issuer: Union['str'],
                 validFrom: Union['TimeSinceEpoch'],
                 validTo: Union['TimeSinceEpoch'],
                 signedCertificateTimestampList: Union['[SignedCertificateTimestamp]'],
                 keyExchangeGroup: Optional['str'] = None,
                 mac: Optional['str'] = None,
                 ):

        self.protocol = protocol
        self.keyExchange = keyExchange
        self.keyExchangeGroup = keyExchangeGroup
        self.cipher = cipher
        self.mac = mac
        self.certificateId = certificateId
        self.subjectName = subjectName
        self.sanList = sanList
        self.issuer = issuer
        self.validFrom = validFrom
        self.validTo = validTo
        self.signedCertificateTimestampList = signedCertificateTimestampList


# BlockedReason: The reason why request was blocked.
BlockedReason = str

# Response: HTTP response data.
class Response(ChromeTypeBase):
    def __init__(self,
                 url: Union['str'],
                 status: Union['float'],
                 statusText: Union['str'],
                 headers: Union['Headers'],
                 mimeType: Union['str'],
                 connectionReused: Union['bool'],
                 connectionId: Union['float'],
                 securityState: Union['Security.SecurityState'],
                 encodedDataLength: Union['float'],
                 headersText: Optional['str'] = None,
                 requestHeaders: Optional['Headers'] = None,
                 requestHeadersText: Optional['str'] = None,
                 remoteIPAddress: Optional['str'] = None,
                 remotePort: Optional['int'] = None,
                 fromDiskCache: Optional['bool'] = None,
                 fromServiceWorker: Optional['bool'] = None,
                 timing: Optional['ResourceTiming'] = None,
                 protocol: Optional['str'] = None,
                 securityDetails: Optional['SecurityDetails'] = None,
                 ):

        self.url = url
        self.status = status
        self.statusText = statusText
        self.headers = headers
        self.headersText = headersText
        self.mimeType = mimeType
        self.requestHeaders = requestHeaders
        self.requestHeadersText = requestHeadersText
        self.connectionReused = connectionReused
        self.connectionId = connectionId
        self.remoteIPAddress = remoteIPAddress
        self.remotePort = remotePort
        self.fromDiskCache = fromDiskCache
        self.fromServiceWorker = fromServiceWorker
        self.encodedDataLength = encodedDataLength
        self.timing = timing
        self.protocol = protocol
        self.securityState = securityState
        self.securityDetails = securityDetails


# WebSocketRequest: WebSocket request data.
class WebSocketRequest(ChromeTypeBase):
    def __init__(self,
                 headers: Union['Headers'],
                 ):

        self.headers = headers


# WebSocketResponse: WebSocket response data.
class WebSocketResponse(ChromeTypeBase):
    def __init__(self,
                 status: Union['float'],
                 statusText: Union['str'],
                 headers: Union['Headers'],
                 headersText: Optional['str'] = None,
                 requestHeaders: Optional['Headers'] = None,
                 requestHeadersText: Optional['str'] = None,
                 ):

        self.status = status
        self.statusText = statusText
        self.headers = headers
        self.headersText = headersText
        self.requestHeaders = requestHeaders
        self.requestHeadersText = requestHeadersText


# WebSocketFrame: WebSocket frame data.
class WebSocketFrame(ChromeTypeBase):
    def __init__(self,
                 opcode: Union['float'],
                 mask: Union['bool'],
                 payloadData: Union['str'],
                 ):

        self.opcode = opcode
        self.mask = mask
        self.payloadData = payloadData


# CachedResource: Information about the cached resource.
class CachedResource(ChromeTypeBase):
    def __init__(self,
                 url: Union['str'],
                 type: Union['Page.ResourceType'],
                 bodySize: Union['float'],
                 response: Optional['Response'] = None,
                 ):

        self.url = url
        self.type = type
        self.response = response
        self.bodySize = bodySize


# Initiator: Information about the request initiator.
class Initiator(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 stack: Optional['Runtime.StackTrace'] = None,
                 url: Optional['str'] = None,
                 lineNumber: Optional['float'] = None,
                 ):

        self.type = type
        self.stack = stack
        self.url = url
        self.lineNumber = lineNumber


# Cookie: Cookie object
class Cookie(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 domain: Union['str'],
                 path: Union['str'],
                 expires: Union['float'],
                 size: Union['int'],
                 httpOnly: Union['bool'],
                 secure: Union['bool'],
                 session: Union['bool'],
                 sameSite: Optional['CookieSameSite'] = None,
                 ):

        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.expires = expires
        self.size = size
        self.httpOnly = httpOnly
        self.secure = secure
        self.session = session
        self.sameSite = sameSite


# AuthChallenge: Authorization challenge for HTTP status code 401 or 407.
class AuthChallenge(ChromeTypeBase):
    def __init__(self,
                 origin: Union['str'],
                 scheme: Union['str'],
                 realm: Union['str'],
                 source: Optional['str'] = None,
                 ):

        self.source = source
        self.origin = origin
        self.scheme = scheme
        self.realm = realm


# AuthChallengeResponse: Response to an AuthChallenge.
class AuthChallengeResponse(ChromeTypeBase):
    def __init__(self,
                 response: Union['str'],
                 username: Optional['str'] = None,
                 password: Optional['str'] = None,
                 ):

        self.response = response
        self.username = username
        self.password = password


class Network(PayloadMixin):
    """ Network domain allows tracking network activities of the page. It exposes information about http, file, data and other requests and responses, their headers, bodies, timing, etc.
    """
    @classmethod
    def enable(cls,
               maxTotalBufferSize: Optional['int'] = None,
               maxResourceBufferSize: Optional['int'] = None,
               ):
        """Enables network tracking, network events will now be delivered to the client.
        :param maxTotalBufferSize: Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :type maxTotalBufferSize: int
        :param maxResourceBufferSize: Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :type maxResourceBufferSize: int
        """
        return (
            cls.build_send_payload("enable", {
                "maxTotalBufferSize": maxTotalBufferSize,
                "maxResourceBufferSize": maxResourceBufferSize,
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables network tracking, prevents network events from being sent to the client.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def setUserAgentOverride(cls,
                             userAgent: Union['str'],
                             ):
        """Allows overriding user agent with the given string.
        :param userAgent: User agent to use.
        :type userAgent: str
        """
        return (
            cls.build_send_payload("setUserAgentOverride", {
                "userAgent": userAgent,
            }),
            None
        )

    @classmethod
    def setExtraHTTPHeaders(cls,
                            headers: Union['Headers'],
                            ):
        """Specifies whether to always send extra HTTP headers with the requests from this page.
        :param headers: Map with extra HTTP headers.
        :type headers: Headers
        """
        return (
            cls.build_send_payload("setExtraHTTPHeaders", {
                "headers": headers,
            }),
            None
        )

    @classmethod
    def getResponseBody(cls,
                        requestId: Union['RequestId'],
                        ):
        """Returns content served for the given request.
        :param requestId: Identifier of the network request to get content for.
        :type requestId: RequestId
        """
        return (
            cls.build_send_payload("getResponseBody", {
                "requestId": requestId,
            }),
            cls.convert_payload({
                "body": {
                    "class": str,
                    "optional": False
                },
                "base64Encoded": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def setBlockedURLs(cls,
                       urls: Union['[]'],
                       ):
        """Blocks URLs from loading.
        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        :type urls: []
        """
        return (
            cls.build_send_payload("setBlockedURLs", {
                "urls": urls,
            }),
            None
        )

    @classmethod
    def replayXHR(cls,
                  requestId: Union['RequestId'],
                  ):
        """This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password.
        :param requestId: Identifier of XHR to replay.
        :type requestId: RequestId
        """
        return (
            cls.build_send_payload("replayXHR", {
                "requestId": requestId,
            }),
            None
        )

    @classmethod
    def canClearBrowserCache(cls):
        """Tells whether clearing browser cache is supported.
        """
        return (
            cls.build_send_payload("canClearBrowserCache", {
            }),
            cls.convert_payload({
                "result": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def clearBrowserCache(cls):
        """Clears browser cache.
        """
        return (
            cls.build_send_payload("clearBrowserCache", {
            }),
            None
        )

    @classmethod
    def canClearBrowserCookies(cls):
        """Tells whether clearing browser cookies is supported.
        """
        return (
            cls.build_send_payload("canClearBrowserCookies", {
            }),
            cls.convert_payload({
                "result": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def clearBrowserCookies(cls):
        """Clears browser cookies.
        """
        return (
            cls.build_send_payload("clearBrowserCookies", {
            }),
            None
        )

    @classmethod
    def getCookies(cls,
                   urls: Optional['[]'] = None,
                   ):
        """Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
        :param urls: The list of URLs for which applicable cookies will be fetched
        :type urls: []
        """
        return (
            cls.build_send_payload("getCookies", {
                "urls": urls,
            }),
            cls.convert_payload({
                "cookies": {
                    "class": [Cookie],
                    "optional": False
                },
            })
        )

    @classmethod
    def getAllCookies(cls):
        """Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
        """
        return (
            cls.build_send_payload("getAllCookies", {
            }),
            cls.convert_payload({
                "cookies": {
                    "class": [Cookie],
                    "optional": False
                },
            })
        )

    @classmethod
    def deleteCookie(cls,
                     cookieName: Union['str'],
                     url: Union['str'],
                     ):
        """Deletes browser cookie with given name, domain and path.
        :param cookieName: Name of the cookie to remove.
        :type cookieName: str
        :param url: URL to match cooke domain and path.
        :type url: str
        """
        return (
            cls.build_send_payload("deleteCookie", {
                "cookieName": cookieName,
                "url": url,
            }),
            None
        )

    @classmethod
    def setCookie(cls,
                  url: Union['str'],
                  name: Union['str'],
                  value: Union['str'],
                  domain: Optional['str'] = None,
                  path: Optional['str'] = None,
                  secure: Optional['bool'] = None,
                  httpOnly: Optional['bool'] = None,
                  sameSite: Optional['CookieSameSite'] = None,
                  expirationDate: Optional['TimeSinceEpoch'] = None,
                  ):
        """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.
        :param url: The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
        :type url: str
        :param name: The name of the cookie.
        :type name: str
        :param value: The value of the cookie.
        :type value: str
        :param domain: If omitted, the cookie becomes a host-only cookie.
        :type domain: str
        :param path: Defaults to the path portion of the url parameter.
        :type path: str
        :param secure: Defaults ot false.
        :type secure: bool
        :param httpOnly: Defaults to false.
        :type httpOnly: bool
        :param sameSite: Defaults to browser default behavior.
        :type sameSite: CookieSameSite
        :param expirationDate: If omitted, the cookie becomes a session cookie.
        :type expirationDate: TimeSinceEpoch
        """
        return (
            cls.build_send_payload("setCookie", {
                "url": url,
                "name": name,
                "value": value,
                "domain": domain,
                "path": path,
                "secure": secure,
                "httpOnly": httpOnly,
                "sameSite": sameSite,
                "expirationDate": expirationDate,
            }),
            cls.convert_payload({
                "success": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def canEmulateNetworkConditions(cls):
        """Tells whether emulation of network conditions is supported.
        """
        return (
            cls.build_send_payload("canEmulateNetworkConditions", {
            }),
            cls.convert_payload({
                "result": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def emulateNetworkConditions(cls,
                                 offline: Union['bool'],
                                 latency: Union['float'],
                                 downloadThroughput: Union['float'],
                                 uploadThroughput: Union['float'],
                                 connectionType: Optional['ConnectionType'] = None,
                                 ):
        """Activates emulation of network conditions.
        :param offline: True to emulate internet disconnection.
        :type offline: bool
        :param latency: Additional latency (ms).
        :type latency: float
        :param downloadThroughput: Maximal aggregated download throughput.
        :type downloadThroughput: float
        :param uploadThroughput: Maximal aggregated upload throughput.
        :type uploadThroughput: float
        :param connectionType: Connection type if known.
        :type connectionType: ConnectionType
        """
        return (
            cls.build_send_payload("emulateNetworkConditions", {
                "offline": offline,
                "latency": latency,
                "downloadThroughput": downloadThroughput,
                "uploadThroughput": uploadThroughput,
                "connectionType": connectionType,
            }),
            None
        )

    @classmethod
    def setCacheDisabled(cls,
                         cacheDisabled: Union['bool'],
                         ):
        """Toggles ignoring cache for each request. If <code>true</code>, cache will not be used.
        :param cacheDisabled: Cache disabled state.
        :type cacheDisabled: bool
        """
        return (
            cls.build_send_payload("setCacheDisabled", {
                "cacheDisabled": cacheDisabled,
            }),
            None
        )

    @classmethod
    def setBypassServiceWorker(cls,
                               bypass: Union['bool'],
                               ):
        """Toggles ignoring of service worker for each request.
        :param bypass: Bypass service worker and load from network.
        :type bypass: bool
        """
        return (
            cls.build_send_payload("setBypassServiceWorker", {
                "bypass": bypass,
            }),
            None
        )

    @classmethod
    def setDataSizeLimitsForTest(cls,
                                 maxTotalSize: Union['int'],
                                 maxResourceSize: Union['int'],
                                 ):
        """For testing.
        :param maxTotalSize: Maximum total buffer size.
        :type maxTotalSize: int
        :param maxResourceSize: Maximum per-resource size.
        :type maxResourceSize: int
        """
        return (
            cls.build_send_payload("setDataSizeLimitsForTest", {
                "maxTotalSize": maxTotalSize,
                "maxResourceSize": maxResourceSize,
            }),
            None
        )

    @classmethod
    def getCertificate(cls,
                       origin: Union['str'],
                       ):
        """Returns the DER-encoded certificate.
        :param origin: Origin to get certificate for.
        :type origin: str
        """
        return (
            cls.build_send_payload("getCertificate", {
                "origin": origin,
            }),
            cls.convert_payload({
                "tableNames": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def setRequestInterceptionEnabled(cls,
                                      enabled: Union['bool'],
                                      ):
        """
        :param enabled: Whether or not HTTP requests should be intercepted and Network.requestIntercepted events sent.
        :type enabled: bool
        """
        return (
            cls.build_send_payload("setRequestInterceptionEnabled", {
                "enabled": enabled,
            }),
            None
        )

    @classmethod
    def continueInterceptedRequest(cls,
                                   interceptionId: Union['InterceptionId'],
                                   errorReason: Optional['ErrorReason'] = None,
                                   rawResponse: Optional['str'] = None,
                                   url: Optional['str'] = None,
                                   method: Optional['str'] = None,
                                   postData: Optional['str'] = None,
                                   headers: Optional['Headers'] = None,
                                   authChallengeResponse: Optional['AuthChallengeResponse'] = None,
                                   ):
        """Response to Network.requestIntercepted which either modifies the request to continue with any modifications, or blocks it, or completes it with the provided response bytes. If a network fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted event will be sent with the same InterceptionId.
        :param interceptionId: 
        :type interceptionId: InterceptionId
        :param errorReason: If set this causes the request to fail with the given reason. Must not be set in response to an authChallenge.
        :type errorReason: ErrorReason
        :param rawResponse: If set the requests completes using with the provided base64 encoded raw response, including HTTP status line and headers etc... Must not be set in response to an authChallenge.
        :type rawResponse: str
        :param url: If set the request url will be modified in a way that's not observable by page. Must not be set in response to an authChallenge.
        :type url: str
        :param method: If set this allows the request method to be overridden. Must not be set in response to an authChallenge.
        :type method: str
        :param postData: If set this allows postData to be set. Must not be set in response to an authChallenge.
        :type postData: str
        :param headers: If set this allows the request headers to be changed. Must not be set in response to an authChallenge.
        :type headers: Headers
        :param authChallengeResponse: Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
        :type authChallengeResponse: AuthChallengeResponse
        """
        return (
            cls.build_send_payload("continueInterceptedRequest", {
                "interceptionId": interceptionId,
                "errorReason": errorReason,
                "rawResponse": rawResponse,
                "url": url,
                "method": method,
                "postData": postData,
                "headers": headers,
                "authChallengeResponse": authChallengeResponse,
            }),
            None
        )



class ResourceChangedPriorityEvent(BaseEvent):

    js_name = 'Network.resourceChangedPriority'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 newPriority: Union['ResourcePriority', dict],
                 timestamp: Union['MonotonicTime', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(newPriority, dict):
            newPriority = ResourcePriority(**newPriority)
        self.newPriority = newPriority
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class RequestWillBeSentEvent(BaseEvent):

    js_name = 'Network.requestWillBeSent'
    hashable = ['loaderId', 'frameId', 'requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 loaderId: Union['LoaderId', dict],
                 documentURL: Union['str', dict],
                 request: Union['Request', dict],
                 timestamp: Union['MonotonicTime', dict],
                 wallTime: Union['TimeSinceEpoch', dict],
                 initiator: Union['Initiator', dict],
                 redirectResponse: Union['Response', dict, None] = None,
                 type: Union['Page.ResourceType', dict, None] = None,
                 frameId: Union['Page.FrameId', dict, None] = None,
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(loaderId, dict):
            loaderId = LoaderId(**loaderId)
        self.loaderId = loaderId
        if isinstance(documentURL, dict):
            documentURL = str(**documentURL)
        self.documentURL = documentURL
        if isinstance(request, dict):
            request = Request(**request)
        self.request = request
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(wallTime, dict):
            wallTime = TimeSinceEpoch(**wallTime)
        self.wallTime = wallTime
        if isinstance(initiator, dict):
            initiator = Initiator(**initiator)
        self.initiator = initiator
        if isinstance(redirectResponse, dict):
            redirectResponse = Response(**redirectResponse)
        self.redirectResponse = redirectResponse
        if isinstance(type, dict):
            type = Page.ResourceType(**type)
        self.type = type
        if isinstance(frameId, dict):
            frameId = Page.FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, loaderId, frameId, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class RequestServedFromCacheEvent(BaseEvent):

    js_name = 'Network.requestServedFromCache'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ResponseReceivedEvent(BaseEvent):

    js_name = 'Network.responseReceived'
    hashable = ['loaderId', 'frameId', 'requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 loaderId: Union['LoaderId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 type: Union['Page.ResourceType', dict],
                 response: Union['Response', dict],
                 frameId: Union['Page.FrameId', dict, None] = None,
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(loaderId, dict):
            loaderId = LoaderId(**loaderId)
        self.loaderId = loaderId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(type, dict):
            type = Page.ResourceType(**type)
        self.type = type
        if isinstance(response, dict):
            response = Response(**response)
        self.response = response
        if isinstance(frameId, dict):
            frameId = Page.FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, loaderId, frameId, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class DataReceivedEvent(BaseEvent):

    js_name = 'Network.dataReceived'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 dataLength: Union['int', dict],
                 encodedDataLength: Union['int', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(dataLength, dict):
            dataLength = int(**dataLength)
        self.dataLength = dataLength
        if isinstance(encodedDataLength, dict):
            encodedDataLength = int(**encodedDataLength)
        self.encodedDataLength = encodedDataLength

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class LoadingFinishedEvent(BaseEvent):

    js_name = 'Network.loadingFinished'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 encodedDataLength: Union['float', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(encodedDataLength, dict):
            encodedDataLength = float(**encodedDataLength)
        self.encodedDataLength = encodedDataLength

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class LoadingFailedEvent(BaseEvent):

    js_name = 'Network.loadingFailed'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 type: Union['Page.ResourceType', dict],
                 errorText: Union['str', dict],
                 canceled: Union['bool', dict, None] = None,
                 blockedReason: Union['BlockedReason', dict, None] = None,
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(type, dict):
            type = Page.ResourceType(**type)
        self.type = type
        if isinstance(errorText, dict):
            errorText = str(**errorText)
        self.errorText = errorText
        if isinstance(canceled, dict):
            canceled = bool(**canceled)
        self.canceled = canceled
        if isinstance(blockedReason, dict):
            blockedReason = BlockedReason(**blockedReason)
        self.blockedReason = blockedReason

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):

    js_name = 'Network.webSocketWillSendHandshakeRequest'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 wallTime: Union['TimeSinceEpoch', dict],
                 request: Union['WebSocketRequest', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(wallTime, dict):
            wallTime = TimeSinceEpoch(**wallTime)
        self.wallTime = wallTime
        if isinstance(request, dict):
            request = WebSocketRequest(**request)
        self.request = request

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):

    js_name = 'Network.webSocketHandshakeResponseReceived'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 response: Union['WebSocketResponse', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(response, dict):
            response = WebSocketResponse(**response)
        self.response = response

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketCreatedEvent(BaseEvent):

    js_name = 'Network.webSocketCreated'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 url: Union['str', dict],
                 initiator: Union['Initiator', dict, None] = None,
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(url, dict):
            url = str(**url)
        self.url = url
        if isinstance(initiator, dict):
            initiator = Initiator(**initiator)
        self.initiator = initiator

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketClosedEvent(BaseEvent):

    js_name = 'Network.webSocketClosed'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketFrameReceivedEvent(BaseEvent):

    js_name = 'Network.webSocketFrameReceived'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 response: Union['WebSocketFrame', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(response, dict):
            response = WebSocketFrame(**response)
        self.response = response

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketFrameErrorEvent(BaseEvent):

    js_name = 'Network.webSocketFrameError'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 errorMessage: Union['str', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(errorMessage, dict):
            errorMessage = str(**errorMessage)
        self.errorMessage = errorMessage

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class WebSocketFrameSentEvent(BaseEvent):

    js_name = 'Network.webSocketFrameSent'
    hashable = ['requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 response: Union['WebSocketFrame', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(response, dict):
            response = WebSocketFrame(**response)
        self.response = response

    @classmethod
    def build_hash(cls, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class EventSourceMessageReceivedEvent(BaseEvent):

    js_name = 'Network.eventSourceMessageReceived'
    hashable = ['eventId', 'requestId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 timestamp: Union['MonotonicTime', dict],
                 eventName: Union['str', dict],
                 eventId: Union['str', dict],
                 data: Union['str', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(timestamp, dict):
            timestamp = MonotonicTime(**timestamp)
        self.timestamp = timestamp
        if isinstance(eventName, dict):
            eventName = str(**eventName)
        self.eventName = eventName
        if isinstance(eventId, dict):
            eventId = str(**eventId)
        self.eventId = eventId
        if isinstance(data, dict):
            data = str(**data)
        self.data = data

    @classmethod
    def build_hash(cls, eventId, requestId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class RequestInterceptedEvent(BaseEvent):

    js_name = 'Network.requestIntercepted'
    hashable = ['interceptionId']
    is_hashable = True

    def __init__(self,
                 interceptionId: Union['InterceptionId', dict],
                 request: Union['Request', dict],
                 resourceType: Union['Page.ResourceType', dict],
                 redirectHeaders: Union['Headers', dict, None] = None,
                 redirectStatusCode: Union['int', dict, None] = None,
                 redirectUrl: Union['str', dict, None] = None,
                 authChallenge: Union['AuthChallenge', dict, None] = None,
                 ):
        if isinstance(interceptionId, dict):
            interceptionId = InterceptionId(**interceptionId)
        self.interceptionId = interceptionId
        if isinstance(request, dict):
            request = Request(**request)
        self.request = request
        if isinstance(resourceType, dict):
            resourceType = Page.ResourceType(**resourceType)
        self.resourceType = resourceType
        if isinstance(redirectHeaders, dict):
            redirectHeaders = Headers(**redirectHeaders)
        self.redirectHeaders = redirectHeaders
        if isinstance(redirectStatusCode, dict):
            redirectStatusCode = int(**redirectStatusCode)
        self.redirectStatusCode = redirectStatusCode
        if isinstance(redirectUrl, dict):
            redirectUrl = str(**redirectUrl)
        self.redirectUrl = redirectUrl
        if isinstance(authChallenge, dict):
            authChallenge = AuthChallenge(**authChallenge)
        self.authChallenge = authChallenge

    @classmethod
    def build_hash(cls, interceptionId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
