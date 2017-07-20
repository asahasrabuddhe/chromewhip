# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# ServiceWorkerRegistration: ServiceWorker registration.
class ServiceWorkerRegistration(ChromeTypeBase):
    def __init__(self,
                 registrationId: Union['str'],
                 scopeURL: Union['str'],
                 isDeleted: Union['bool'],
                 ):

        self.registrationId = registrationId
        self.scopeURL = scopeURL
        self.isDeleted = isDeleted


# ServiceWorkerVersionRunningStatus: 
ServiceWorkerVersionRunningStatus = str

# ServiceWorkerVersionStatus: 
ServiceWorkerVersionStatus = str

# ServiceWorkerVersion: ServiceWorker version.
class ServiceWorkerVersion(ChromeTypeBase):
    def __init__(self,
                 versionId: Union['str'],
                 registrationId: Union['str'],
                 scriptURL: Union['str'],
                 runningStatus: Union['ServiceWorkerVersionRunningStatus'],
                 status: Union['ServiceWorkerVersionStatus'],
                 scriptLastModified: Optional['float'] = None,
                 scriptResponseTime: Optional['float'] = None,
                 controlledClients: Optional['[Target.TargetID]'] = None,
                 targetId: Optional['Target.TargetID'] = None,
                 ):

        self.versionId = versionId
        self.registrationId = registrationId
        self.scriptURL = scriptURL
        self.runningStatus = runningStatus
        self.status = status
        self.scriptLastModified = scriptLastModified
        self.scriptResponseTime = scriptResponseTime
        self.controlledClients = controlledClients
        self.targetId = targetId


# ServiceWorkerErrorMessage: ServiceWorker error message.
class ServiceWorkerErrorMessage(ChromeTypeBase):
    def __init__(self,
                 errorMessage: Union['str'],
                 registrationId: Union['str'],
                 versionId: Union['str'],
                 sourceURL: Union['str'],
                 lineNumber: Union['int'],
                 columnNumber: Union['int'],
                 ):

        self.errorMessage = errorMessage
        self.registrationId = registrationId
        self.versionId = versionId
        self.sourceURL = sourceURL
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber


class ServiceWorker(PayloadMixin):
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
    def unregister(cls,
                   scopeURL: Union['str'],
                   ):
        """
        :param scopeURL: 
        :type scopeURL: str
        """
        return (
            cls.build_send_payload("unregister", {
                "scopeURL": scopeURL,
            }),
            None
        )

    @classmethod
    def updateRegistration(cls,
                           scopeURL: Union['str'],
                           ):
        """
        :param scopeURL: 
        :type scopeURL: str
        """
        return (
            cls.build_send_payload("updateRegistration", {
                "scopeURL": scopeURL,
            }),
            None
        )

    @classmethod
    def startWorker(cls,
                    scopeURL: Union['str'],
                    ):
        """
        :param scopeURL: 
        :type scopeURL: str
        """
        return (
            cls.build_send_payload("startWorker", {
                "scopeURL": scopeURL,
            }),
            None
        )

    @classmethod
    def skipWaiting(cls,
                    scopeURL: Union['str'],
                    ):
        """
        :param scopeURL: 
        :type scopeURL: str
        """
        return (
            cls.build_send_payload("skipWaiting", {
                "scopeURL": scopeURL,
            }),
            None
        )

    @classmethod
    def stopWorker(cls,
                   versionId: Union['str'],
                   ):
        """
        :param versionId: 
        :type versionId: str
        """
        return (
            cls.build_send_payload("stopWorker", {
                "versionId": versionId,
            }),
            None
        )

    @classmethod
    def inspectWorker(cls,
                      versionId: Union['str'],
                      ):
        """
        :param versionId: 
        :type versionId: str
        """
        return (
            cls.build_send_payload("inspectWorker", {
                "versionId": versionId,
            }),
            None
        )

    @classmethod
    def setForceUpdateOnPageLoad(cls,
                                 forceUpdateOnPageLoad: Union['bool'],
                                 ):
        """
        :param forceUpdateOnPageLoad: 
        :type forceUpdateOnPageLoad: bool
        """
        return (
            cls.build_send_payload("setForceUpdateOnPageLoad", {
                "forceUpdateOnPageLoad": forceUpdateOnPageLoad,
            }),
            None
        )

    @classmethod
    def deliverPushMessage(cls,
                           origin: Union['str'],
                           registrationId: Union['str'],
                           data: Union['str'],
                           ):
        """
        :param origin: 
        :type origin: str
        :param registrationId: 
        :type registrationId: str
        :param data: 
        :type data: str
        """
        return (
            cls.build_send_payload("deliverPushMessage", {
                "origin": origin,
                "registrationId": registrationId,
                "data": data,
            }),
            None
        )

    @classmethod
    def dispatchSyncEvent(cls,
                          origin: Union['str'],
                          registrationId: Union['str'],
                          tag: Union['str'],
                          lastChance: Union['bool'],
                          ):
        """
        :param origin: 
        :type origin: str
        :param registrationId: 
        :type registrationId: str
        :param tag: 
        :type tag: str
        :param lastChance: 
        :type lastChance: bool
        """
        return (
            cls.build_send_payload("dispatchSyncEvent", {
                "origin": origin,
                "registrationId": registrationId,
                "tag": tag,
                "lastChance": lastChance,
            }),
            None
        )



class WorkerRegistrationUpdatedEvent(BaseEvent):

    js_name = 'Serviceworker.workerRegistrationUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 registrations: Union['[ServiceWorkerRegistration]', dict],
                 ):
        if isinstance(registrations, dict):
            registrations = [ServiceWorkerRegistration](**registrations)
        self.registrations = registrations

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class WorkerVersionUpdatedEvent(BaseEvent):

    js_name = 'Serviceworker.workerVersionUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 versions: Union['[ServiceWorkerVersion]', dict],
                 ):
        if isinstance(versions, dict):
            versions = [ServiceWorkerVersion](**versions)
        self.versions = versions

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class WorkerErrorReportedEvent(BaseEvent):

    js_name = 'Serviceworker.workerErrorReported'
    hashable = []
    is_hashable = False

    def __init__(self,
                 errorMessage: Union['ServiceWorkerErrorMessage', dict],
                 ):
        if isinstance(errorMessage, dict):
            errorMessage = ServiceWorkerErrorMessage(**errorMessage)
        self.errorMessage = errorMessage

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
