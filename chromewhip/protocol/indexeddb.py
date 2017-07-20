# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime

# DatabaseWithObjectStores: Database with an array of object stores.
class DatabaseWithObjectStores(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 version: Union['int'],
                 objectStores: Union['[ObjectStore]'],
                 ):

        self.name = name
        self.version = version
        self.objectStores = objectStores


# ObjectStore: Object store.
class ObjectStore(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 keyPath: Union['KeyPath'],
                 autoIncrement: Union['bool'],
                 indexes: Union['[ObjectStoreIndex]'],
                 ):

        self.name = name
        self.keyPath = keyPath
        self.autoIncrement = autoIncrement
        self.indexes = indexes


# ObjectStoreIndex: Object store index.
class ObjectStoreIndex(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 keyPath: Union['KeyPath'],
                 unique: Union['bool'],
                 multiEntry: Union['bool'],
                 ):

        self.name = name
        self.keyPath = keyPath
        self.unique = unique
        self.multiEntry = multiEntry


# Key: Key.
class Key(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 number: Optional['float'] = None,
                 string: Optional['str'] = None,
                 date: Optional['float'] = None,
                 array: Optional['[Key]'] = None,
                 ):

        self.type = type
        self.number = number
        self.string = string
        self.date = date
        self.array = array


# KeyRange: Key range.
class KeyRange(ChromeTypeBase):
    def __init__(self,
                 lowerOpen: Union['bool'],
                 upperOpen: Union['bool'],
                 lower: Optional['Key'] = None,
                 upper: Optional['Key'] = None,
                 ):

        self.lower = lower
        self.upper = upper
        self.lowerOpen = lowerOpen
        self.upperOpen = upperOpen


# DataEntry: Data entry.
class DataEntry(ChromeTypeBase):
    def __init__(self,
                 key: Union['Runtime.RemoteObject'],
                 primaryKey: Union['Runtime.RemoteObject'],
                 value: Union['Runtime.RemoteObject'],
                 ):

        self.key = key
        self.primaryKey = primaryKey
        self.value = value


# KeyPath: Key path.
class KeyPath(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 string: Optional['str'] = None,
                 array: Optional['[]'] = None,
                 ):

        self.type = type
        self.string = string
        self.array = array


class IndexedDB(PayloadMixin):
    """ 
    """
    @classmethod
    def enable(cls):
        """Enables events from backend.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables events from backend.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def requestDatabaseNames(cls,
                             securityOrigin: Union['str'],
                             ):
        """Requests database names for given security origin.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        return (
            cls.build_send_payload("requestDatabaseNames", {
                "securityOrigin": securityOrigin,
            }),
            cls.convert_payload({
                "databaseNames": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def requestDatabase(cls,
                        securityOrigin: Union['str'],
                        databaseName: Union['str'],
                        ):
        """Requests database with given name in given frame.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        return (
            cls.build_send_payload("requestDatabase", {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
            }),
            cls.convert_payload({
                "databaseWithObjectStores": {
                    "class": DatabaseWithObjectStores,
                    "optional": False
                },
            })
        )

    @classmethod
    def requestData(cls,
                    securityOrigin: Union['str'],
                    databaseName: Union['str'],
                    objectStoreName: Union['str'],
                    indexName: Union['str'],
                    skipCount: Union['int'],
                    pageSize: Union['int'],
                    keyRange: Optional['KeyRange'] = None,
                    ):
        """Requests data from object store or index.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        :param indexName: Index name, empty string for object store data requests.
        :type indexName: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        :param keyRange: Key range.
        :type keyRange: KeyRange
        """
        return (
            cls.build_send_payload("requestData", {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
                "objectStoreName": objectStoreName,
                "indexName": indexName,
                "skipCount": skipCount,
                "pageSize": pageSize,
                "keyRange": keyRange,
            }),
            cls.convert_payload({
                "objectStoreDataEntries": {
                    "class": [DataEntry],
                    "optional": False
                },
                "hasMore": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def clearObjectStore(cls,
                         securityOrigin: Union['str'],
                         databaseName: Union['str'],
                         objectStoreName: Union['str'],
                         ):
        """Clears all entries from an object store.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        """
        return (
            cls.build_send_payload("clearObjectStore", {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
                "objectStoreName": objectStoreName,
            }),
            cls.convert_payload({
            })
        )

    @classmethod
    def deleteDatabase(cls,
                       securityOrigin: Union['str'],
                       databaseName: Union['str'],
                       ):
        """Deletes a database.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        return (
            cls.build_send_payload("deleteDatabase", {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
            }),
            cls.convert_payload({
            })
        )

