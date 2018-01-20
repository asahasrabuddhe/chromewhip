# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import dom as DOM

# AXNodeId: Unique accessibility node identifier.
AXNodeId = str

# AXValueType: Enum of possible property types.
AXValueType = str

# AXValueSourceType: Enum of possible property sources.
AXValueSourceType = str

# AXValueNativeSourceType: Enum of possible native property sources (as a subtype of a particular AXValueSourceType).
AXValueNativeSourceType = str

# AXValueSource: A single source for a computed AX property.
class AXValueSource(ChromeTypeBase):
    def __init__(self,
                 type: Union['AXValueSourceType'],
                 value: Optional['AXValue'] = None,
                 attribute: Optional['str'] = None,
                 attributeValue: Optional['AXValue'] = None,
                 superseded: Optional['bool'] = None,
                 nativeSource: Optional['AXValueNativeSourceType'] = None,
                 nativeSourceValue: Optional['AXValue'] = None,
                 invalid: Optional['bool'] = None,
                 invalidReason: Optional['str'] = None,
                 ):

        self.type = type
        self.value = value
        self.attribute = attribute
        self.attributeValue = attributeValue
        self.superseded = superseded
        self.nativeSource = nativeSource
        self.nativeSourceValue = nativeSourceValue
        self.invalid = invalid
        self.invalidReason = invalidReason


# AXRelatedNode: 
class AXRelatedNode(ChromeTypeBase):
    def __init__(self,
                 backendDOMNodeId: Union['DOM.BackendNodeId'],
                 idref: Optional['str'] = None,
                 text: Optional['str'] = None,
                 ):

        self.backendDOMNodeId = backendDOMNodeId
        self.idref = idref
        self.text = text


# AXProperty: 
class AXProperty(ChromeTypeBase):
    def __init__(self,
                 name: Union['AXPropertyName'],
                 value: Union['AXValue'],
                 ):

        self.name = name
        self.value = value


# AXValue: A single computed AX property.
class AXValue(ChromeTypeBase):
    def __init__(self,
                 type: Union['AXValueType'],
                 value: Optional['Any'] = None,
                 relatedNodes: Optional['[AXRelatedNode]'] = None,
                 sources: Optional['[AXValueSource]'] = None,
                 ):

        self.type = type
        self.value = value
        self.relatedNodes = relatedNodes
        self.sources = sources


# AXPropertyName: Values of AXProperty name: from 'busy' to 'roledescription' - states which apply to every AXnode, from 'live' to 'root' - attributes which apply to nodes in live regions, from'autocomplete' to 'valuetext' - attributes which apply to widgets, from 'checked' to 'selected'- states which apply to widgets, from 'activedescendant' to 'owns' - relationships betweenelements other than parent/child/sibling.
AXPropertyName = str

# AXNode: A node in the accessibility tree.
class AXNode(ChromeTypeBase):
    def __init__(self,
                 nodeId: Union['AXNodeId'],
                 ignored: Union['bool'],
                 ignoredReasons: Optional['[AXProperty]'] = None,
                 role: Optional['AXValue'] = None,
                 name: Optional['AXValue'] = None,
                 description: Optional['AXValue'] = None,
                 value: Optional['AXValue'] = None,
                 properties: Optional['[AXProperty]'] = None,
                 childIds: Optional['[AXNodeId]'] = None,
                 backendDOMNodeId: Optional['DOM.BackendNodeId'] = None,
                 ):

        self.nodeId = nodeId
        self.ignored = ignored
        self.ignoredReasons = ignoredReasons
        self.role = role
        self.name = name
        self.description = description
        self.value = value
        self.properties = properties
        self.childIds = childIds
        self.backendDOMNodeId = backendDOMNodeId


class Accessibility(PayloadMixin):
    """ 
    """
    @classmethod
    def getPartialAXTree(cls,
                         nodeId: Union['DOM.NodeId'],
                         fetchRelatives: Optional['bool'] = None,
                         ):
        """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.
        :param nodeId: ID of node to get the partial accessibility tree for.
        :type nodeId: DOM.NodeId
        :param fetchRelatives: Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
        :type fetchRelatives: bool
        """
        return (
            cls.build_send_payload("getPartialAXTree", {
                "nodeId": nodeId,
                "fetchRelatives": fetchRelatives,
            }),
            cls.convert_payload({
                "nodes": {
                    "class": [AXNode],
                    "optional": False
                },
            })
        )

