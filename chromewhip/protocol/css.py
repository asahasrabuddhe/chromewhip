# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import dom as DOM

# StyleSheetId: 
StyleSheetId = str

# StyleSheetOrigin: Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets.
StyleSheetOrigin = str

# PseudoElementMatches: CSS rule collection for a single pseudo style.
class PseudoElementMatches(ChromeTypeBase):
    def __init__(self,
                 pseudoType: Union['DOM.PseudoType'],
                 matches: Union['[RuleMatch]'],
                 ):

        self.pseudoType = pseudoType
        self.matches = matches


# InheritedStyleEntry: Inherited CSS rule collection from ancestor node.
class InheritedStyleEntry(ChromeTypeBase):
    def __init__(self,
                 matchedCSSRules: Union['[RuleMatch]'],
                 inlineStyle: Optional['CSSStyle'] = None,
                 ):

        self.inlineStyle = inlineStyle
        self.matchedCSSRules = matchedCSSRules


# RuleMatch: Match data for a CSS rule.
class RuleMatch(ChromeTypeBase):
    def __init__(self,
                 rule: Union['CSSRule'],
                 matchingSelectors: Union['[]'],
                 ):

        self.rule = rule
        self.matchingSelectors = matchingSelectors


# Value: Data for a simple selector (these are delimited by commas in a selector list).
class Value(ChromeTypeBase):
    def __init__(self,
                 text: Union['str'],
                 range: Optional['SourceRange'] = None,
                 ):

        self.text = text
        self.range = range


# SelectorList: Selector list data.
class SelectorList(ChromeTypeBase):
    def __init__(self,
                 selectors: Union['[Value]'],
                 text: Union['str'],
                 ):

        self.selectors = selectors
        self.text = text


# CSSStyleSheetHeader: CSS stylesheet metainformation.
class CSSStyleSheetHeader(ChromeTypeBase):
    def __init__(self,
                 styleSheetId: Union['StyleSheetId'],
                 frameId: Union['Page.FrameId'],
                 sourceURL: Union['str'],
                 origin: Union['StyleSheetOrigin'],
                 title: Union['str'],
                 disabled: Union['bool'],
                 isInline: Union['bool'],
                 startLine: Union['float'],
                 startColumn: Union['float'],
                 length: Union['float'],
                 sourceMapURL: Optional['str'] = None,
                 ownerNode: Optional['DOM.BackendNodeId'] = None,
                 hasSourceURL: Optional['bool'] = None,
                 ):

        self.styleSheetId = styleSheetId
        self.frameId = frameId
        self.sourceURL = sourceURL
        self.sourceMapURL = sourceMapURL
        self.origin = origin
        self.title = title
        self.ownerNode = ownerNode
        self.disabled = disabled
        self.hasSourceURL = hasSourceURL
        self.isInline = isInline
        self.startLine = startLine
        self.startColumn = startColumn
        self.length = length


# CSSRule: CSS rule representation.
class CSSRule(ChromeTypeBase):
    def __init__(self,
                 selectorList: Union['SelectorList'],
                 origin: Union['StyleSheetOrigin'],
                 style: Union['CSSStyle'],
                 styleSheetId: Optional['StyleSheetId'] = None,
                 media: Optional['[CSSMedia]'] = None,
                 ):

        self.styleSheetId = styleSheetId
        self.selectorList = selectorList
        self.origin = origin
        self.style = style
        self.media = media


# RuleUsage: CSS coverage information.
class RuleUsage(ChromeTypeBase):
    def __init__(self,
                 styleSheetId: Union['StyleSheetId'],
                 startOffset: Union['float'],
                 endOffset: Union['float'],
                 used: Union['bool'],
                 ):

        self.styleSheetId = styleSheetId
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.used = used


# SourceRange: Text range within a resource. All numbers are zero-based.
class SourceRange(ChromeTypeBase):
    def __init__(self,
                 startLine: Union['int'],
                 startColumn: Union['int'],
                 endLine: Union['int'],
                 endColumn: Union['int'],
                 ):

        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn


# ShorthandEntry: 
class ShorthandEntry(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 important: Optional['bool'] = None,
                 ):

        self.name = name
        self.value = value
        self.important = important


# CSSComputedStyleProperty: 
class CSSComputedStyleProperty(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 ):

        self.name = name
        self.value = value


# CSSStyle: CSS style representation.
class CSSStyle(ChromeTypeBase):
    def __init__(self,
                 cssProperties: Union['[CSSProperty]'],
                 shorthandEntries: Union['[ShorthandEntry]'],
                 styleSheetId: Optional['StyleSheetId'] = None,
                 cssText: Optional['str'] = None,
                 range: Optional['SourceRange'] = None,
                 ):

        self.styleSheetId = styleSheetId
        self.cssProperties = cssProperties
        self.shorthandEntries = shorthandEntries
        self.cssText = cssText
        self.range = range


# CSSProperty: CSS property declaration data.
class CSSProperty(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 important: Optional['bool'] = None,
                 implicit: Optional['bool'] = None,
                 text: Optional['str'] = None,
                 parsedOk: Optional['bool'] = None,
                 disabled: Optional['bool'] = None,
                 range: Optional['SourceRange'] = None,
                 ):

        self.name = name
        self.value = value
        self.important = important
        self.implicit = implicit
        self.text = text
        self.parsedOk = parsedOk
        self.disabled = disabled
        self.range = range


# CSSMedia: CSS media rule descriptor.
class CSSMedia(ChromeTypeBase):
    def __init__(self,
                 text: Union['str'],
                 source: Union['str'],
                 sourceURL: Optional['str'] = None,
                 range: Optional['SourceRange'] = None,
                 styleSheetId: Optional['StyleSheetId'] = None,
                 mediaList: Optional['[MediaQuery]'] = None,
                 ):

        self.text = text
        self.source = source
        self.sourceURL = sourceURL
        self.range = range
        self.styleSheetId = styleSheetId
        self.mediaList = mediaList


# MediaQuery: Media query descriptor.
class MediaQuery(ChromeTypeBase):
    def __init__(self,
                 expressions: Union['[MediaQueryExpression]'],
                 active: Union['bool'],
                 ):

        self.expressions = expressions
        self.active = active


# MediaQueryExpression: Media query expression descriptor.
class MediaQueryExpression(ChromeTypeBase):
    def __init__(self,
                 value: Union['float'],
                 unit: Union['str'],
                 feature: Union['str'],
                 valueRange: Optional['SourceRange'] = None,
                 computedLength: Optional['float'] = None,
                 ):

        self.value = value
        self.unit = unit
        self.feature = feature
        self.valueRange = valueRange
        self.computedLength = computedLength


# PlatformFontUsage: Information about amount of glyphs that were rendered with given font.
class PlatformFontUsage(ChromeTypeBase):
    def __init__(self,
                 familyName: Union['str'],
                 isCustomFont: Union['bool'],
                 glyphCount: Union['float'],
                 ):

        self.familyName = familyName
        self.isCustomFont = isCustomFont
        self.glyphCount = glyphCount


# CSSKeyframesRule: CSS keyframes rule representation.
class CSSKeyframesRule(ChromeTypeBase):
    def __init__(self,
                 animationName: Union['Value'],
                 keyframes: Union['[CSSKeyframeRule]'],
                 ):

        self.animationName = animationName
        self.keyframes = keyframes


# CSSKeyframeRule: CSS keyframe rule representation.
class CSSKeyframeRule(ChromeTypeBase):
    def __init__(self,
                 origin: Union['StyleSheetOrigin'],
                 keyText: Union['Value'],
                 style: Union['CSSStyle'],
                 styleSheetId: Optional['StyleSheetId'] = None,
                 ):

        self.styleSheetId = styleSheetId
        self.origin = origin
        self.keyText = keyText
        self.style = style


# StyleDeclarationEdit: A descriptor of operation to mutate style declaration text.
class StyleDeclarationEdit(ChromeTypeBase):
    def __init__(self,
                 styleSheetId: Union['StyleSheetId'],
                 range: Union['SourceRange'],
                 text: Union['str'],
                 ):

        self.styleSheetId = styleSheetId
        self.range = range
        self.text = text


# InlineTextBox: Details of post layout rendered text positions. The exact layout should not be regarded as stable and may change between versions.
class InlineTextBox(ChromeTypeBase):
    def __init__(self,
                 boundingBox: Union['DOM.Rect'],
                 startCharacterIndex: Union['int'],
                 numCharacters: Union['int'],
                 ):

        self.boundingBox = boundingBox
        self.startCharacterIndex = startCharacterIndex
        self.numCharacters = numCharacters


class CSS(PayloadMixin):
    """ This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles) have an associated <code>id</code> used in subsequent operations on the related object. Each object type has a specific <code>id</code> structure, and those are not interchangeable between objects of different kinds. CSS objects can be loaded using the <code>get*ForNode()</code> calls (which accept a DOM node id). A client can also keep track of stylesheets via the <code>styleSheetAdded</code>/<code>styleSheetRemoved</code> events and subsequently load the required stylesheet contents using the <code>getStyleSheet[Text]()</code> methods.
    """
    @classmethod
    def enable(cls):
        """Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables the CSS agent for the given page.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def getMatchedStylesForNode(cls,
                                nodeId: Union['DOM.NodeId'],
                                ):
        """Returns requested styles for a DOM node identified by <code>nodeId</code>.
        :param nodeId: 
        :type nodeId: DOM.NodeId
        """
        return (
            cls.build_send_payload("getMatchedStylesForNode", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "inlineStyle": {
                    "class": CSSStyle,
                    "optional": True
                },
                "attributesStyle": {
                    "class": CSSStyle,
                    "optional": True
                },
                "matchedCSSRules": {
                    "class": [RuleMatch],
                    "optional": True
                },
                "pseudoElements": {
                    "class": [PseudoElementMatches],
                    "optional": True
                },
                "inherited": {
                    "class": [InheritedStyleEntry],
                    "optional": True
                },
                "cssKeyframesRules": {
                    "class": [CSSKeyframesRule],
                    "optional": True
                },
            })
        )

    @classmethod
    def getInlineStylesForNode(cls,
                               nodeId: Union['DOM.NodeId'],
                               ):
        """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by <code>nodeId</code>.
        :param nodeId: 
        :type nodeId: DOM.NodeId
        """
        return (
            cls.build_send_payload("getInlineStylesForNode", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "inlineStyle": {
                    "class": CSSStyle,
                    "optional": True
                },
                "attributesStyle": {
                    "class": CSSStyle,
                    "optional": True
                },
            })
        )

    @classmethod
    def getComputedStyleForNode(cls,
                                nodeId: Union['DOM.NodeId'],
                                ):
        """Returns the computed style for a DOM node identified by <code>nodeId</code>.
        :param nodeId: 
        :type nodeId: DOM.NodeId
        """
        return (
            cls.build_send_payload("getComputedStyleForNode", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "computedStyle": {
                    "class": [CSSComputedStyleProperty],
                    "optional": False
                },
            })
        )

    @classmethod
    def getPlatformFontsForNode(cls,
                                nodeId: Union['DOM.NodeId'],
                                ):
        """Requests information about platform fonts which we used to render child TextNodes in the given node.
        :param nodeId: 
        :type nodeId: DOM.NodeId
        """
        return (
            cls.build_send_payload("getPlatformFontsForNode", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "fonts": {
                    "class": [PlatformFontUsage],
                    "optional": False
                },
            })
        )

    @classmethod
    def getStyleSheetText(cls,
                          styleSheetId: Union['StyleSheetId'],
                          ):
        """Returns the current textual content and the URL for a stylesheet.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        """
        return (
            cls.build_send_payload("getStyleSheetText", {
                "styleSheetId": styleSheetId,
            }),
            cls.convert_payload({
                "text": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def collectClassNames(cls,
                          styleSheetId: Union['StyleSheetId'],
                          ):
        """Returns all class names from specified stylesheet.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        """
        return (
            cls.build_send_payload("collectClassNames", {
                "styleSheetId": styleSheetId,
            }),
            cls.convert_payload({
                "classNames": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def setStyleSheetText(cls,
                          styleSheetId: Union['StyleSheetId'],
                          text: Union['str'],
                          ):
        """Sets the new stylesheet text.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        :param text: 
        :type text: str
        """
        return (
            cls.build_send_payload("setStyleSheetText", {
                "styleSheetId": styleSheetId,
                "text": text,
            }),
            cls.convert_payload({
                "sourceMapURL": {
                    "class": str,
                    "optional": True
                },
            })
        )

    @classmethod
    def setRuleSelector(cls,
                        styleSheetId: Union['StyleSheetId'],
                        range: Union['SourceRange'],
                        selector: Union['str'],
                        ):
        """Modifies the rule selector.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        :param range: 
        :type range: SourceRange
        :param selector: 
        :type selector: str
        """
        return (
            cls.build_send_payload("setRuleSelector", {
                "styleSheetId": styleSheetId,
                "range": range,
                "selector": selector,
            }),
            cls.convert_payload({
                "selectorList": {
                    "class": SelectorList,
                    "optional": False
                },
            })
        )

    @classmethod
    def setKeyframeKey(cls,
                       styleSheetId: Union['StyleSheetId'],
                       range: Union['SourceRange'],
                       keyText: Union['str'],
                       ):
        """Modifies the keyframe rule key text.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        :param range: 
        :type range: SourceRange
        :param keyText: 
        :type keyText: str
        """
        return (
            cls.build_send_payload("setKeyframeKey", {
                "styleSheetId": styleSheetId,
                "range": range,
                "keyText": keyText,
            }),
            cls.convert_payload({
                "keyText": {
                    "class": Value,
                    "optional": False
                },
            })
        )

    @classmethod
    def setStyleTexts(cls,
                      edits: Union['[StyleDeclarationEdit]'],
                      ):
        """Applies specified style edits one after another in the given order.
        :param edits: 
        :type edits: [StyleDeclarationEdit]
        """
        return (
            cls.build_send_payload("setStyleTexts", {
                "edits": edits,
            }),
            cls.convert_payload({
                "styles": {
                    "class": [CSSStyle],
                    "optional": False
                },
            })
        )

    @classmethod
    def setMediaText(cls,
                     styleSheetId: Union['StyleSheetId'],
                     range: Union['SourceRange'],
                     text: Union['str'],
                     ):
        """Modifies the rule selector.
        :param styleSheetId: 
        :type styleSheetId: StyleSheetId
        :param range: 
        :type range: SourceRange
        :param text: 
        :type text: str
        """
        return (
            cls.build_send_payload("setMediaText", {
                "styleSheetId": styleSheetId,
                "range": range,
                "text": text,
            }),
            cls.convert_payload({
                "media": {
                    "class": CSSMedia,
                    "optional": False
                },
            })
        )

    @classmethod
    def createStyleSheet(cls,
                         frameId: Union['Page.FrameId'],
                         ):
        """Creates a new special "via-inspector" stylesheet in the frame with given <code>frameId</code>.
        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: Page.FrameId
        """
        return (
            cls.build_send_payload("createStyleSheet", {
                "frameId": frameId,
            }),
            cls.convert_payload({
                "styleSheetId": {
                    "class": StyleSheetId,
                    "optional": False
                },
            })
        )

    @classmethod
    def addRule(cls,
                styleSheetId: Union['StyleSheetId'],
                ruleText: Union['str'],
                location: Union['SourceRange'],
                ):
        """Inserts a new rule with the given <code>ruleText</code> in a stylesheet with given <code>styleSheetId</code>, at the position specified by <code>location</code>.
        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :type styleSheetId: StyleSheetId
        :param ruleText: The text of a new rule.
        :type ruleText: str
        :param location: Text position of a new rule in the target style sheet.
        :type location: SourceRange
        """
        return (
            cls.build_send_payload("addRule", {
                "styleSheetId": styleSheetId,
                "ruleText": ruleText,
                "location": location,
            }),
            cls.convert_payload({
                "rule": {
                    "class": CSSRule,
                    "optional": False
                },
            })
        )

    @classmethod
    def forcePseudoState(cls,
                         nodeId: Union['DOM.NodeId'],
                         forcedPseudoClasses: Union['[]'],
                         ):
        """Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.
        :param nodeId: The element id for which to force the pseudo state.
        :type nodeId: DOM.NodeId
        :param forcedPseudoClasses: Element pseudo classes to force when computing the element's style.
        :type forcedPseudoClasses: []
        """
        return (
            cls.build_send_payload("forcePseudoState", {
                "nodeId": nodeId,
                "forcedPseudoClasses": forcedPseudoClasses,
            }),
            None
        )

    @classmethod
    def getMediaQueries(cls):
        """Returns all media queries parsed by the rendering engine.
        """
        return (
            cls.build_send_payload("getMediaQueries", {
            }),
            cls.convert_payload({
                "medias": {
                    "class": [CSSMedia],
                    "optional": False
                },
            })
        )

    @classmethod
    def setEffectivePropertyValueForNode(cls,
                                         nodeId: Union['DOM.NodeId'],
                                         propertyName: Union['str'],
                                         value: Union['str'],
                                         ):
        """Find a rule with the given active property for the given node and set the new value for this property
        :param nodeId: The element id for which to set property.
        :type nodeId: DOM.NodeId
        :param propertyName: 
        :type propertyName: str
        :param value: 
        :type value: str
        """
        return (
            cls.build_send_payload("setEffectivePropertyValueForNode", {
                "nodeId": nodeId,
                "propertyName": propertyName,
                "value": value,
            }),
            None
        )

    @classmethod
    def getBackgroundColors(cls,
                            nodeId: Union['DOM.NodeId'],
                            ):
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: DOM.NodeId
        """
        return (
            cls.build_send_payload("getBackgroundColors", {
                "nodeId": nodeId,
            }),
            cls.convert_payload({
                "backgroundColors": {
                    "class": [],
                    "optional": True
                },
            })
        )

    @classmethod
    def startRuleUsageTracking(cls):
        """Enables the selector recording.
        """
        return (
            cls.build_send_payload("startRuleUsageTracking", {
            }),
            None
        )

    @classmethod
    def takeCoverageDelta(cls):
        """Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation)
        """
        return (
            cls.build_send_payload("takeCoverageDelta", {
            }),
            cls.convert_payload({
                "coverage": {
                    "class": [RuleUsage],
                    "optional": False
                },
            })
        )

    @classmethod
    def stopRuleUsageTracking(cls):
        """The list of rules with an indication of whether these were used
        """
        return (
            cls.build_send_payload("stopRuleUsageTracking", {
            }),
            cls.convert_payload({
                "ruleUsage": {
                    "class": [RuleUsage],
                    "optional": False
                },
            })
        )



class MediaQueryResultChangedEvent(BaseEvent):

    js_name = 'Css.mediaQueryResultChanged'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class FontsUpdatedEvent(BaseEvent):

    js_name = 'Css.fontsUpdated'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class StyleSheetChangedEvent(BaseEvent):

    js_name = 'Css.styleSheetChanged'
    hashable = ['styleSheetId']
    is_hashable = True

    def __init__(self,
                 styleSheetId: Union['StyleSheetId', dict],
                 ):
        if isinstance(styleSheetId, dict):
            styleSheetId = StyleSheetId(**styleSheetId)
        self.styleSheetId = styleSheetId

    @classmethod
    def build_hash(cls, styleSheetId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class StyleSheetAddedEvent(BaseEvent):

    js_name = 'Css.styleSheetAdded'
    hashable = []
    is_hashable = False

    def __init__(self,
                 header: Union['CSSStyleSheetHeader', dict],
                 ):
        if isinstance(header, dict):
            header = CSSStyleSheetHeader(**header)
        self.header = header

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class StyleSheetRemovedEvent(BaseEvent):

    js_name = 'Css.styleSheetRemoved'
    hashable = ['styleSheetId']
    is_hashable = True

    def __init__(self,
                 styleSheetId: Union['StyleSheetId', dict],
                 ):
        if isinstance(styleSheetId, dict):
            styleSheetId = StyleSheetId(**styleSheetId)
        self.styleSheetId = styleSheetId

    @classmethod
    def build_hash(cls, styleSheetId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
