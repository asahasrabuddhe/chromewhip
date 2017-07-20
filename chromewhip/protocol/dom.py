# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime

# NodeId: Unique DOM node identifier.
NodeId = int

# BackendNodeId: Unique DOM node identifier used to reference a node that may not have been pushed to the front-end.
BackendNodeId = int

# BackendNode: Backend node with a friendly name.
class BackendNode(ChromeTypeBase):
    def __init__(self,
                 nodeType: Union['int'],
                 nodeName: Union['str'],
                 backendNodeId: Union['BackendNodeId'],
                 ):

        self.nodeType = nodeType
        self.nodeName = nodeName
        self.backendNodeId = backendNodeId


# PseudoType: Pseudo element type.
PseudoType = str

# ShadowRootType: Shadow root type.
ShadowRootType = str

# Node: DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes. DOMNode is a base node mirror type.
class Node(ChromeTypeBase):
    def __init__(self,
                 nodeId: Union['NodeId'],
                 backendNodeId: Union['BackendNodeId'],
                 nodeType: Union['int'],
                 nodeName: Union['str'],
                 localName: Union['str'],
                 nodeValue: Union['str'],
                 parentId: Optional['NodeId'] = None,
                 childNodeCount: Optional['int'] = None,
                 children: Optional['[Node]'] = None,
                 attributes: Optional['[]'] = None,
                 documentURL: Optional['str'] = None,
                 baseURL: Optional['str'] = None,
                 publicId: Optional['str'] = None,
                 systemId: Optional['str'] = None,
                 internalSubset: Optional['str'] = None,
                 xmlVersion: Optional['str'] = None,
                 name: Optional['str'] = None,
                 value: Optional['str'] = None,
                 pseudoType: Optional['PseudoType'] = None,
                 shadowRootType: Optional['ShadowRootType'] = None,
                 frameId: Optional['Page.FrameId'] = None,
                 contentDocument: Optional['Node'] = None,
                 shadowRoots: Optional['[Node]'] = None,
                 templateContent: Optional['Node'] = None,
                 pseudoElements: Optional['[Node]'] = None,
                 importedDocument: Optional['Node'] = None,
                 distributedNodes: Optional['[BackendNode]'] = None,
                 isSVG: Optional['bool'] = None,
                 ):

        self.nodeId = nodeId
        self.parentId = parentId
        self.backendNodeId = backendNodeId
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.localName = localName
        self.nodeValue = nodeValue
        self.childNodeCount = childNodeCount
        self.children = children
        self.attributes = attributes
        self.documentURL = documentURL
        self.baseURL = baseURL
        self.publicId = publicId
        self.systemId = systemId
        self.internalSubset = internalSubset
        self.xmlVersion = xmlVersion
        self.name = name
        self.value = value
        self.pseudoType = pseudoType
        self.shadowRootType = shadowRootType
        self.frameId = frameId
        self.contentDocument = contentDocument
        self.shadowRoots = shadowRoots
        self.templateContent = templateContent
        self.pseudoElements = pseudoElements
        self.importedDocument = importedDocument
        self.distributedNodes = distributedNodes
        self.isSVG = isSVG


# RGBA: A structure holding an RGBA color.
class RGBA(ChromeTypeBase):
    def __init__(self,
                 r: Union['int'],
                 g: Union['int'],
                 b: Union['int'],
                 a: Optional['float'] = None,
                 ):

        self.r = r
        self.g = g
        self.b = b
        self.a = a


# Quad: An array of quad vertices, x immediately followed by y for each point, points clock-wise.
Quad = [float]

# BoxModel: Box model.
class BoxModel(ChromeTypeBase):
    def __init__(self,
                 content: Union['Quad'],
                 padding: Union['Quad'],
                 border: Union['Quad'],
                 margin: Union['Quad'],
                 width: Union['int'],
                 height: Union['int'],
                 shapeOutside: Optional['ShapeOutsideInfo'] = None,
                 ):

        self.content = content
        self.padding = padding
        self.border = border
        self.margin = margin
        self.width = width
        self.height = height
        self.shapeOutside = shapeOutside


# ShapeOutsideInfo: CSS Shape Outside details.
class ShapeOutsideInfo(ChromeTypeBase):
    def __init__(self,
                 bounds: Union['Quad'],
                 shape: Union['[]'],
                 marginShape: Union['[]'],
                 ):

        self.bounds = bounds
        self.shape = shape
        self.marginShape = marginShape


# Rect: Rectangle.
class Rect(ChromeTypeBase):
    def __init__(self,
                 x: Union['float'],
                 y: Union['float'],
                 width: Union['float'],
                 height: Union['float'],
                 ):

        self.x = x
        self.y = y
        self.width = width
        self.height = height


class DOM(PayloadMixin):
    """ This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object that has an <code>id</code>. This <code>id</code> can be used to get additional information on the Node, resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events only for the nodes that are known to the client. Backend keeps track of the nodes that were sent to the client and never sends the same node twice. It is client's responsibility to collect information about the nodes that were sent to the client.<p>Note that <code>iframe</code> owner elements will return corresponding document elements as their child nodes.</p>
    """
    @classmethod
    def enable(cls):
        """Enables DOM agent for the given page.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables DOM agent for the given page.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def getDocument(cls,
                    depth: Optional['int'] = None,
                    pierce: Optional['bool'] = None,
                    ):
        """Returns the root DOM node (and optionally the subtree) to the caller.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: int
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: bool
        """
        return (
            cls.build_send_payload("getDocument", {
                "depth": depth,
                "pierce": pierce,
            }),
            cls.convert_payload({
                "root": {
                    "class": Node,
                    "optional": False
                },
            })
        )

    @classmethod
    def getFlattenedDocument(cls,
                             depth: Optional['int'] = None,
                             pierce: Optional['bool'] = None,
                             ):
        """Returns the root DOM node (and optionally the subtree) to the caller.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: int
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: bool
        """
        return (
            cls.build_send_payload("getFlattenedDocument", {
                "depth": depth,
                "pierce": pierce,
            }),
            cls.convert_payload({
                "nodes": {
                    "class": [Node],
                    "optional": False
                },
            })
        )

    @classmethod
    def collectClassNamesFromSubtree(cls,
                                     nodeId: Union['NodeId'],
                                     ):
        """Collects class names for the node with given id and all of it's child nodes.
        :param nodeId: Id of the node to collect class names.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("collectClassNamesFromSubtree", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "classNames": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def requestChildNodes(cls,
                          nodeId: Union['NodeId'],
                          depth: Optional['int'] = None,
                          pierce: Optional['bool'] = None,
                          ):
        """Requests that children of the node with given id are returned to the caller in form of <code>setChildNodes</code> events where not only immediate children are retrieved, but all children down to the specified depth.
        :param nodeId: Id of the node to get children for.
        :type nodeId: NodeId
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: int
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false).
        :type pierce: bool
        """
        return (
            cls.build_send_payload("requestChildNodes", {
                "nodeId": nodeId,
                "depth": depth,
                "pierce": pierce,
            }),
            None
        )

    @classmethod
    def querySelector(cls,
                      nodeId: Union['NodeId'],
                      selector: Union['str'],
                      ):
        """Executes <code>querySelector</code> on a given node.
        :param nodeId: Id of the node to query upon.
        :type nodeId: NodeId
        :param selector: Selector string.
        :type selector: str
        """
        return (
            cls.build_send_payload("querySelector", {
                "nodeId": nodeId,
                "selector": selector,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def querySelectorAll(cls,
                         nodeId: Union['NodeId'],
                         selector: Union['str'],
                         ):
        """Executes <code>querySelectorAll</code> on a given node.
        :param nodeId: Id of the node to query upon.
        :type nodeId: NodeId
        :param selector: Selector string.
        :type selector: str
        """
        return (
            cls.build_send_payload("querySelectorAll", {
                "nodeId": nodeId,
                "selector": selector,
            }),
            cls.convert_payload({
                "nodeIds": {
                    "class": [NodeId],
                    "optional": False
                },
            })
        )

    @classmethod
    def setNodeName(cls,
                    nodeId: Union['NodeId'],
                    name: Union['str'],
                    ):
        """Sets node name for a node with given id.
        :param nodeId: Id of the node to set name for.
        :type nodeId: NodeId
        :param name: New node's name.
        :type name: str
        """
        return (
            cls.build_send_payload("setNodeName", {
                "nodeId": nodeId,
                "name": name,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def setNodeValue(cls,
                     nodeId: Union['NodeId'],
                     value: Union['str'],
                     ):
        """Sets node value for a node with given id.
        :param nodeId: Id of the node to set value for.
        :type nodeId: NodeId
        :param value: New node's value.
        :type value: str
        """
        return (
            cls.build_send_payload("setNodeValue", {
                "nodeId": nodeId,
                "value": value,
            }),
            None
        )

    @classmethod
    def removeNode(cls,
                   nodeId: Union['NodeId'],
                   ):
        """Removes node with given id.
        :param nodeId: Id of the node to remove.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("removeNode", {
                "nodeId": nodeId,
            }),
            None
        )

    @classmethod
    def setAttributeValue(cls,
                          nodeId: Union['NodeId'],
                          name: Union['str'],
                          value: Union['str'],
                          ):
        """Sets attribute for an element with given id.
        :param nodeId: Id of the element to set attribute for.
        :type nodeId: NodeId
        :param name: Attribute name.
        :type name: str
        :param value: Attribute value.
        :type value: str
        """
        return (
            cls.build_send_payload("setAttributeValue", {
                "nodeId": nodeId,
                "name": name,
                "value": value,
            }),
            None
        )

    @classmethod
    def setAttributesAsText(cls,
                            nodeId: Union['NodeId'],
                            text: Union['str'],
                            name: Optional['str'] = None,
                            ):
        """Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.
        :param nodeId: Id of the element to set attributes for.
        :type nodeId: NodeId
        :param text: Text with a number of attributes. Will parse this text using HTML parser.
        :type text: str
        :param name: Attribute name to replace with new attributes derived from text in case text parsed successfully.
        :type name: str
        """
        return (
            cls.build_send_payload("setAttributesAsText", {
                "nodeId": nodeId,
                "text": text,
                "name": name,
            }),
            None
        )

    @classmethod
    def removeAttribute(cls,
                        nodeId: Union['NodeId'],
                        name: Union['str'],
                        ):
        """Removes attribute with given name from an element with given id.
        :param nodeId: Id of the element to remove attribute from.
        :type nodeId: NodeId
        :param name: Name of the attribute to remove.
        :type name: str
        """
        return (
            cls.build_send_payload("removeAttribute", {
                "nodeId": nodeId,
                "name": name,
            }),
            None
        )

    @classmethod
    def getOuterHTML(cls,
                     nodeId: Union['NodeId'],
                     ):
        """Returns node's HTML markup.
        :param nodeId: Id of the node to get markup for.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("getOuterHTML", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "outerHTML": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def setOuterHTML(cls,
                     nodeId: Union['NodeId'],
                     outerHTML: Union['str'],
                     ):
        """Sets node HTML markup, returns new node id.
        :param nodeId: Id of the node to set markup for.
        :type nodeId: NodeId
        :param outerHTML: Outer HTML markup to set.
        :type outerHTML: str
        """
        return (
            cls.build_send_payload("setOuterHTML", {
                "nodeId": nodeId,
                "outerHTML": outerHTML,
            }),
            None
        )

    @classmethod
    def performSearch(cls,
                      query: Union['str'],
                      includeUserAgentShadowDOM: Optional['bool'] = None,
                      ):
        """Searches for a given string in the DOM tree. Use <code>getSearchResults</code> to access search results or <code>cancelSearch</code> to end this search session.
        :param query: Plain text or query selector or XPath search query.
        :type query: str
        :param includeUserAgentShadowDOM: True to search in user agent shadow DOM.
        :type includeUserAgentShadowDOM: bool
        """
        return (
            cls.build_send_payload("performSearch", {
                "query": query,
                "includeUserAgentShadowDOM": includeUserAgentShadowDOM,
            }),
            cls.convert_payload({
                "searchId": {
                    "class": str,
                    "optional": False
                },
                "resultCount": {
                    "class": int,
                    "optional": False
                },
            })
        )

    @classmethod
    def getSearchResults(cls,
                         searchId: Union['str'],
                         fromIndex: Union['int'],
                         toIndex: Union['int'],
                         ):
        """Returns search results from given <code>fromIndex</code> to given <code>toIndex</code> from the sarch with the given identifier.
        :param searchId: Unique search session identifier.
        :type searchId: str
        :param fromIndex: Start index of the search result to be returned.
        :type fromIndex: int
        :param toIndex: End index of the search result to be returned.
        :type toIndex: int
        """
        return (
            cls.build_send_payload("getSearchResults", {
                "searchId": searchId,
                "fromIndex": fromIndex,
                "toIndex": toIndex,
            }),
            cls.convert_payload({
                "nodeIds": {
                    "class": [NodeId],
                    "optional": False
                },
            })
        )

    @classmethod
    def discardSearchResults(cls,
                             searchId: Union['str'],
                             ):
        """Discards search results from the session with the given id. <code>getSearchResults</code> should no longer be called for that search.
        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        return (
            cls.build_send_payload("discardSearchResults", {
                "searchId": searchId,
            }),
            None
        )

    @classmethod
    def requestNode(cls,
                    objectId: Union['Runtime.RemoteObjectId'],
                    ):
        """Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of <code>setChildNodes</code> notifications.
        :param objectId: JavaScript object id to convert into node.
        :type objectId: Runtime.RemoteObjectId
        """
        return (
            cls.build_send_payload("requestNode", {
                "objectId": objectId,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def highlightRect(cls):
        """Highlights given rectangle.
        """
        return (
            cls.build_send_payload("highlightRect", {
            }),
            None
        )

    @classmethod
    def highlightNode(cls):
        """Highlights DOM node.
        """
        return (
            cls.build_send_payload("highlightNode", {
            }),
            None
        )

    @classmethod
    def hideHighlight(cls):
        """Hides any highlight.
        """
        return (
            cls.build_send_payload("hideHighlight", {
            }),
            None
        )

    @classmethod
    def pushNodeByPathToFrontend(cls,
                                 path: Union['str'],
                                 ):
        """Requests that the node is sent to the caller given its path. // FIXME, use XPath
        :param path: Path to node in the proprietary format.
        :type path: str
        """
        return (
            cls.build_send_payload("pushNodeByPathToFrontend", {
                "path": path,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def pushNodesByBackendIdsToFrontend(cls,
                                        backendNodeIds: Union['[BackendNodeId]'],
                                        ):
        """Requests that a batch of nodes is sent to the caller given their backend node ids.
        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: [BackendNodeId]
        """
        return (
            cls.build_send_payload("pushNodesByBackendIdsToFrontend", {
                "backendNodeIds": backendNodeIds,
            }),
            cls.convert_payload({
                "nodeIds": {
                    "class": [NodeId],
                    "optional": False
                },
            })
        )

    @classmethod
    def setInspectedNode(cls,
                         nodeId: Union['NodeId'],
                         ):
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).
        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("setInspectedNode", {
                "nodeId": nodeId,
            }),
            None
        )

    @classmethod
    def resolveNode(cls,
                    nodeId: Optional['NodeId'] = None,
                    backendNodeId: Optional['DOM.BackendNodeId'] = None,
                    objectGroup: Optional['str'] = None,
                    ):
        """Resolves the JavaScript node object for a given NodeId or BackendNodeId.
        :param nodeId: Id of the node to resolve.
        :type nodeId: NodeId
        :param backendNodeId: Backend identifier of the node to resolve.
        :type backendNodeId: DOM.BackendNodeId
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: str
        """
        return (
            cls.build_send_payload("resolveNode", {
                "nodeId": nodeId,
                "backendNodeId": backendNodeId,
                "objectGroup": objectGroup,
            }),
            cls.convert_payload({
                "object": {
                    "class": Runtime.RemoteObject,
                    "optional": False
                },
            })
        )

    @classmethod
    def getAttributes(cls,
                      nodeId: Union['NodeId'],
                      ):
        """Returns attributes for the specified node.
        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("getAttributes", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "attributes": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def copyTo(cls,
               nodeId: Union['NodeId'],
               targetNodeId: Union['NodeId'],
               insertBeforeNodeId: Optional['NodeId'] = None,
               ):
        """Creates a deep copy of the specified node and places it into the target container before the given anchor.
        :param nodeId: Id of the node to copy.
        :type nodeId: NodeId
        :param targetNodeId: Id of the element to drop the copy into.
        :type targetNodeId: NodeId
        :param insertBeforeNodeId: Drop the copy before this node (if absent, the copy becomes the last child of <code>targetNodeId</code>).
        :type insertBeforeNodeId: NodeId
        """
        return (
            cls.build_send_payload("copyTo", {
                "nodeId": nodeId,
                "targetNodeId": targetNodeId,
                "insertBeforeNodeId": insertBeforeNodeId,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def moveTo(cls,
               nodeId: Union['NodeId'],
               targetNodeId: Union['NodeId'],
               insertBeforeNodeId: Optional['NodeId'] = None,
               ):
        """Moves node into the new container, places it before the given anchor.
        :param nodeId: Id of the node to move.
        :type nodeId: NodeId
        :param targetNodeId: Id of the element to drop the moved node into.
        :type targetNodeId: NodeId
        :param insertBeforeNodeId: Drop node before this one (if absent, the moved node becomes the last child of <code>targetNodeId</code>).
        :type insertBeforeNodeId: NodeId
        """
        return (
            cls.build_send_payload("moveTo", {
                "nodeId": nodeId,
                "targetNodeId": targetNodeId,
                "insertBeforeNodeId": insertBeforeNodeId,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def undo(cls):
        """Undoes the last performed action.
        """
        return (
            cls.build_send_payload("undo", {
            }),
            None
        )

    @classmethod
    def redo(cls):
        """Re-does the last undone action.
        """
        return (
            cls.build_send_payload("redo", {
            }),
            None
        )

    @classmethod
    def markUndoableState(cls):
        """Marks last undoable state.
        """
        return (
            cls.build_send_payload("markUndoableState", {
            }),
            None
        )

    @classmethod
    def focus(cls,
              nodeId: Optional['NodeId'] = None,
              backendNodeId: Optional['BackendNodeId'] = None,
              objectId: Optional['Runtime.RemoteObjectId'] = None,
              ):
        """Focuses the given element.
        :param nodeId: Identifier of the node.
        :type nodeId: NodeId
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: BackendNodeId
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Runtime.RemoteObjectId
        """
        return (
            cls.build_send_payload("focus", {
                "nodeId": nodeId,
                "backendNodeId": backendNodeId,
                "objectId": objectId,
            }),
            None
        )

    @classmethod
    def setFileInputFiles(cls,
                          files: Union['[]'],
                          nodeId: Optional['NodeId'] = None,
                          backendNodeId: Optional['BackendNodeId'] = None,
                          objectId: Optional['Runtime.RemoteObjectId'] = None,
                          ):
        """Sets files for the given file input element.
        :param files: Array of file paths to set.
        :type files: []
        :param nodeId: Identifier of the node.
        :type nodeId: NodeId
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: BackendNodeId
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Runtime.RemoteObjectId
        """
        return (
            cls.build_send_payload("setFileInputFiles", {
                "files": files,
                "nodeId": nodeId,
                "backendNodeId": backendNodeId,
                "objectId": objectId,
            }),
            None
        )

    @classmethod
    def getBoxModel(cls,
                    nodeId: Optional['NodeId'] = None,
                    backendNodeId: Optional['BackendNodeId'] = None,
                    objectId: Optional['Runtime.RemoteObjectId'] = None,
                    ):
        """Returns boxes for the currently selected nodes.
        :param nodeId: Identifier of the node.
        :type nodeId: NodeId
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: BackendNodeId
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Runtime.RemoteObjectId
        """
        return (
            cls.build_send_payload("getBoxModel", {
                "nodeId": nodeId,
                "backendNodeId": backendNodeId,
                "objectId": objectId,
            }),
            cls.convert_payload({
                "model": {
                    "class": BoxModel,
                    "optional": False
                },
            })
        )

    @classmethod
    def getNodeForLocation(cls,
                           x: Union['int'],
                           y: Union['int'],
                           includeUserAgentShadowDOM: Optional['bool'] = None,
                           ):
        """Returns node id at given location.
        :param x: X coordinate.
        :type x: int
        :param y: Y coordinate.
        :type y: int
        :param includeUserAgentShadowDOM: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :type includeUserAgentShadowDOM: bool
        """
        return (
            cls.build_send_payload("getNodeForLocation", {
                "x": x,
                "y": y,
                "includeUserAgentShadowDOM": includeUserAgentShadowDOM,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )

    @classmethod
    def getRelayoutBoundary(cls,
                            nodeId: Union['NodeId'],
                            ):
        """Returns the id of the nearest ancestor that is a relayout boundary.
        :param nodeId: Id of the node.
        :type nodeId: NodeId
        """
        return (
            cls.build_send_payload("getRelayoutBoundary", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "nodeId": {
                    "class": NodeId,
                    "optional": False
                },
            })
        )



class DocumentUpdatedEvent(BaseEvent):

    js_name = 'Dom.documentUpdated'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class SetChildNodesEvent(BaseEvent):

    js_name = 'Dom.setChildNodes'
    hashable = ['parentId']
    is_hashable = True

    def __init__(self,
                 parentId: Union['NodeId', dict],
                 nodes: Union['[Node]', dict],
                 ):
        if isinstance(parentId, dict):
            parentId = NodeId(**parentId)
        self.parentId = parentId
        if isinstance(nodes, dict):
            nodes = [Node](**nodes)
        self.nodes = nodes

    @classmethod
    def build_hash(cls, parentId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AttributeModifiedEvent(BaseEvent):

    js_name = 'Dom.attributeModified'
    hashable = ['nodeId']
    is_hashable = True

    def __init__(self,
                 nodeId: Union['NodeId', dict],
                 name: Union['str', dict],
                 value: Union['str', dict],
                 ):
        if isinstance(nodeId, dict):
            nodeId = NodeId(**nodeId)
        self.nodeId = nodeId
        if isinstance(name, dict):
            name = str(**name)
        self.name = name
        if isinstance(value, dict):
            value = str(**value)
        self.value = value

    @classmethod
    def build_hash(cls, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AttributeRemovedEvent(BaseEvent):

    js_name = 'Dom.attributeRemoved'
    hashable = ['nodeId']
    is_hashable = True

    def __init__(self,
                 nodeId: Union['NodeId', dict],
                 name: Union['str', dict],
                 ):
        if isinstance(nodeId, dict):
            nodeId = NodeId(**nodeId)
        self.nodeId = nodeId
        if isinstance(name, dict):
            name = str(**name)
        self.name = name

    @classmethod
    def build_hash(cls, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class InlineStyleInvalidatedEvent(BaseEvent):

    js_name = 'Dom.inlineStyleInvalidated'
    hashable = ['nodeIds']
    is_hashable = True

    def __init__(self,
                 nodeIds: Union['[NodeId]', dict],
                 ):
        if isinstance(nodeIds, dict):
            nodeIds = [NodeId](**nodeIds)
        self.nodeIds = nodeIds

    @classmethod
    def build_hash(cls, nodeIds):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class CharacterDataModifiedEvent(BaseEvent):

    js_name = 'Dom.characterDataModified'
    hashable = ['nodeId']
    is_hashable = True

    def __init__(self,
                 nodeId: Union['NodeId', dict],
                 characterData: Union['str', dict],
                 ):
        if isinstance(nodeId, dict):
            nodeId = NodeId(**nodeId)
        self.nodeId = nodeId
        if isinstance(characterData, dict):
            characterData = str(**characterData)
        self.characterData = characterData

    @classmethod
    def build_hash(cls, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ChildNodeCountUpdatedEvent(BaseEvent):

    js_name = 'Dom.childNodeCountUpdated'
    hashable = ['nodeId']
    is_hashable = True

    def __init__(self,
                 nodeId: Union['NodeId', dict],
                 childNodeCount: Union['int', dict],
                 ):
        if isinstance(nodeId, dict):
            nodeId = NodeId(**nodeId)
        self.nodeId = nodeId
        if isinstance(childNodeCount, dict):
            childNodeCount = int(**childNodeCount)
        self.childNodeCount = childNodeCount

    @classmethod
    def build_hash(cls, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ChildNodeInsertedEvent(BaseEvent):

    js_name = 'Dom.childNodeInserted'
    hashable = ['previousNodeId', 'parentNodeId']
    is_hashable = True

    def __init__(self,
                 parentNodeId: Union['NodeId', dict],
                 previousNodeId: Union['NodeId', dict],
                 node: Union['Node', dict],
                 ):
        if isinstance(parentNodeId, dict):
            parentNodeId = NodeId(**parentNodeId)
        self.parentNodeId = parentNodeId
        if isinstance(previousNodeId, dict):
            previousNodeId = NodeId(**previousNodeId)
        self.previousNodeId = previousNodeId
        if isinstance(node, dict):
            node = Node(**node)
        self.node = node

    @classmethod
    def build_hash(cls, previousNodeId, parentNodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ChildNodeRemovedEvent(BaseEvent):

    js_name = 'Dom.childNodeRemoved'
    hashable = ['nodeId', 'parentNodeId']
    is_hashable = True

    def __init__(self,
                 parentNodeId: Union['NodeId', dict],
                 nodeId: Union['NodeId', dict],
                 ):
        if isinstance(parentNodeId, dict):
            parentNodeId = NodeId(**parentNodeId)
        self.parentNodeId = parentNodeId
        if isinstance(nodeId, dict):
            nodeId = NodeId(**nodeId)
        self.nodeId = nodeId

    @classmethod
    def build_hash(cls, nodeId, parentNodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ShadowRootPushedEvent(BaseEvent):

    js_name = 'Dom.shadowRootPushed'
    hashable = ['hostId']
    is_hashable = True

    def __init__(self,
                 hostId: Union['NodeId', dict],
                 root: Union['Node', dict],
                 ):
        if isinstance(hostId, dict):
            hostId = NodeId(**hostId)
        self.hostId = hostId
        if isinstance(root, dict):
            root = Node(**root)
        self.root = root

    @classmethod
    def build_hash(cls, hostId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ShadowRootPoppedEvent(BaseEvent):

    js_name = 'Dom.shadowRootPopped'
    hashable = ['rootId', 'hostId']
    is_hashable = True

    def __init__(self,
                 hostId: Union['NodeId', dict],
                 rootId: Union['NodeId', dict],
                 ):
        if isinstance(hostId, dict):
            hostId = NodeId(**hostId)
        self.hostId = hostId
        if isinstance(rootId, dict):
            rootId = NodeId(**rootId)
        self.rootId = rootId

    @classmethod
    def build_hash(cls, rootId, hostId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PseudoElementAddedEvent(BaseEvent):

    js_name = 'Dom.pseudoElementAdded'
    hashable = ['parentId']
    is_hashable = True

    def __init__(self,
                 parentId: Union['NodeId', dict],
                 pseudoElement: Union['Node', dict],
                 ):
        if isinstance(parentId, dict):
            parentId = NodeId(**parentId)
        self.parentId = parentId
        if isinstance(pseudoElement, dict):
            pseudoElement = Node(**pseudoElement)
        self.pseudoElement = pseudoElement

    @classmethod
    def build_hash(cls, parentId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PseudoElementRemovedEvent(BaseEvent):

    js_name = 'Dom.pseudoElementRemoved'
    hashable = ['parentId', 'pseudoElementId']
    is_hashable = True

    def __init__(self,
                 parentId: Union['NodeId', dict],
                 pseudoElementId: Union['NodeId', dict],
                 ):
        if isinstance(parentId, dict):
            parentId = NodeId(**parentId)
        self.parentId = parentId
        if isinstance(pseudoElementId, dict):
            pseudoElementId = NodeId(**pseudoElementId)
        self.pseudoElementId = pseudoElementId

    @classmethod
    def build_hash(cls, parentId, pseudoElementId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class DistributedNodesUpdatedEvent(BaseEvent):

    js_name = 'Dom.distributedNodesUpdated'
    hashable = ['insertionPointId']
    is_hashable = True

    def __init__(self,
                 insertionPointId: Union['NodeId', dict],
                 distributedNodes: Union['[BackendNode]', dict],
                 ):
        if isinstance(insertionPointId, dict):
            insertionPointId = NodeId(**insertionPointId)
        self.insertionPointId = insertionPointId
        if isinstance(distributedNodes, dict):
            distributedNodes = [BackendNode](**distributedNodes)
        self.distributedNodes = distributedNodes

    @classmethod
    def build_hash(cls, insertionPointId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
