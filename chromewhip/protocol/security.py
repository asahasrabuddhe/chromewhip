# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# CertificateId: An internal certificate ID value.
CertificateId = int

# MixedContentType: A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories
MixedContentType = str

# SecurityState: The security level of a page or resource.
SecurityState = str

# SecurityStateExplanation: An explanation of an factor contributing to the security state.
class SecurityStateExplanation(ChromeTypeBase):
    def __init__(self,
                 securityState: Union['SecurityState'],
                 summary: Union['str'],
                 description: Union['str'],
                 hasCertificate: Union['bool'],
                 mixedContentType: Union['MixedContentType'],
                 ):

        self.securityState = securityState
        self.summary = summary
        self.description = description
        self.hasCertificate = hasCertificate
        self.mixedContentType = mixedContentType


# InsecureContentStatus: Information about insecure content on the page.
class InsecureContentStatus(ChromeTypeBase):
    def __init__(self,
                 ranMixedContent: Union['bool'],
                 displayedMixedContent: Union['bool'],
                 containedMixedForm: Union['bool'],
                 ranContentWithCertErrors: Union['bool'],
                 displayedContentWithCertErrors: Union['bool'],
                 ranInsecureContentStyle: Union['SecurityState'],
                 displayedInsecureContentStyle: Union['SecurityState'],
                 ):

        self.ranMixedContent = ranMixedContent
        self.displayedMixedContent = displayedMixedContent
        self.containedMixedForm = containedMixedForm
        self.ranContentWithCertErrors = ranContentWithCertErrors
        self.displayedContentWithCertErrors = displayedContentWithCertErrors
        self.ranInsecureContentStyle = ranInsecureContentStyle
        self.displayedInsecureContentStyle = displayedInsecureContentStyle


# CertificateErrorAction: The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request.
CertificateErrorAction = str

class Security(PayloadMixin):
    """ Security
    """
    @classmethod
    def enable(cls):
        """Enables tracking security state changes.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables tracking security state changes.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def showCertificateViewer(cls):
        """Displays native dialog with the certificate details.
        """
        return (
            cls.build_send_payload("showCertificateViewer", {
            }),
            None
        )

    @classmethod
    def handleCertificateError(cls,
                               eventId: Union['int'],
                               action: Union['CertificateErrorAction'],
                               ):
        """Handles a certificate error that fired a certificateError event.
        :param eventId: The ID of the event.
        :type eventId: int
        :param action: The action to take on the certificate error.
        :type action: CertificateErrorAction
        """
        return (
            cls.build_send_payload("handleCertificateError", {
                "eventId": eventId,
                "action": action,
            }),
            None
        )

    @classmethod
    def setOverrideCertificateErrors(cls,
                                     override: Union['bool'],
                                     ):
        """Enable/disable overriding certificate errors. If enabled, all certificate error events need to be handled by the DevTools client and should be answered with handleCertificateError commands.
        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        return (
            cls.build_send_payload("setOverrideCertificateErrors", {
                "override": override,
            }),
            None
        )



class SecurityStateChangedEvent(BaseEvent):

    js_name = 'Security.securityStateChanged'
    hashable = []
    is_hashable = False

    def __init__(self,
                 securityState: Union['SecurityState', dict],
                 schemeIsCryptographic: Union['bool', dict],
                 explanations: Union['[SecurityStateExplanation]', dict],
                 insecureContentStatus: Union['InsecureContentStatus', dict],
                 summary: Union['str', dict, None] = None,
                 ):
        if isinstance(securityState, dict):
            securityState = SecurityState(**securityState)
        self.securityState = securityState
        if isinstance(schemeIsCryptographic, dict):
            schemeIsCryptographic = bool(**schemeIsCryptographic)
        self.schemeIsCryptographic = schemeIsCryptographic
        if isinstance(explanations, dict):
            explanations = [SecurityStateExplanation](**explanations)
        self.explanations = explanations
        if isinstance(insecureContentStatus, dict):
            insecureContentStatus = InsecureContentStatus(**insecureContentStatus)
        self.insecureContentStatus = insecureContentStatus
        if isinstance(summary, dict):
            summary = str(**summary)
        self.summary = summary

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class CertificateErrorEvent(BaseEvent):

    js_name = 'Security.certificateError'
    hashable = ['eventId']
    is_hashable = True

    def __init__(self,
                 eventId: Union['int', dict],
                 errorType: Union['str', dict],
                 requestURL: Union['str', dict],
                 ):
        if isinstance(eventId, dict):
            eventId = int(**eventId)
        self.eventId = eventId
        if isinstance(errorType, dict):
            errorType = str(**errorType)
        self.errorType = errorType
        if isinstance(requestURL, dict):
            requestURL = str(**requestURL)
        self.requestURL = requestURL

    @classmethod
    def build_hash(cls, eventId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
