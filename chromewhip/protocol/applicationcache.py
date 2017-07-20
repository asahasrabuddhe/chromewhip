# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# ApplicationCacheResource: Detailed application cache resource information.
class ApplicationCacheResource(ChromeTypeBase):
    def __init__(self,
                 url: Union['str'],
                 size: Union['int'],
                 type: Union['str'],
                 ):

        self.url = url
        self.size = size
        self.type = type


# ApplicationCache: Detailed application cache information.
class ApplicationCache(ChromeTypeBase):
    def __init__(self,
                 manifestURL: Union['str'],
                 size: Union['float'],
                 creationTime: Union['float'],
                 updateTime: Union['float'],
                 resources: Union['[ApplicationCacheResource]'],
                 ):

        self.manifestURL = manifestURL
        self.size = size
        self.creationTime = creationTime
        self.updateTime = updateTime
        self.resources = resources


# FrameWithManifest: Frame identifier - manifest URL pair.
class FrameWithManifest(ChromeTypeBase):
    def __init__(self,
                 frameId: Union['Page.FrameId'],
                 manifestURL: Union['str'],
                 status: Union['int'],
                 ):

        self.frameId = frameId
        self.manifestURL = manifestURL
        self.status = status


class ApplicationCache(PayloadMixin):
    """ 
    """
    @classmethod
    def getFramesWithManifests(cls):
        """Returns array of frame identifiers with manifest urls for each frame containing a document associated with some application cache.
        """
        return (
            cls.build_send_payload("getFramesWithManifests", {
            }),
            cls.convert_payload({
                "frameIds": {
                    "class": [FrameWithManifest],
                    "optional": False
                },
            })
        )

    @classmethod
    def enable(cls):
        """Enables application cache domain notifications.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def getManifestForFrame(cls,
                            frameId: Union['Page.FrameId'],
                            ):
        """Returns manifest URL for document in the given frame.
        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: Page.FrameId
        """
        return (
            cls.build_send_payload("getManifestForFrame", {
                "frameId": frameId,
            }),
            cls.convert_payload({
                "manifestURL": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def getApplicationCacheForFrame(cls,
                                    frameId: Union['Page.FrameId'],
                                    ):
        """Returns relevant application cache data for the document in given frame.
        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: Page.FrameId
        """
        return (
            cls.build_send_payload("getApplicationCacheForFrame", {
                "frameId": frameId,
            }),
            cls.convert_payload({
                "applicationCache": {
                    "class": ApplicationCache,
                    "optional": False
                },
            })
        )



class ApplicationCacheStatusUpdatedEvent(BaseEvent):

    js_name = 'Applicationcache.applicationCacheStatusUpdated'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['Page.FrameId', dict],
                 manifestURL: Union['str', dict],
                 status: Union['int', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = Page.FrameId(**frameId)
        self.frameId = frameId
        if isinstance(manifestURL, dict):
            manifestURL = str(**manifestURL)
        self.manifestURL = manifestURL
        if isinstance(status, dict):
            status = int(**status)
        self.status = status

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NetworkStateUpdatedEvent(BaseEvent):

    js_name = 'Applicationcache.networkStateUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 isNowOnline: Union['bool', dict],
                 ):
        if isinstance(isNowOnline, dict):
            isNowOnline = bool(**isNowOnline)
        self.isNowOnline = isNowOnline

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
