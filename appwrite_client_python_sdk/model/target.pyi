# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from appwrite_client_python_sdk import schemas  # noqa: F401


class Target(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Target
    """


    class MetaOapg:
        required = {
            "identifier",
            "name",
            "$createdAt",
            "userId",
            "providerType",
            "$id",
            "$updatedAt",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            name = schemas.StrSchema
            userId = schemas.StrSchema
            providerType = schemas.StrSchema
            identifier = schemas.StrSchema
            
            
            class providerId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'providerId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "name": name,
                "userId": userId,
                "providerType": providerType,
                "identifier": identifier,
                "providerId": providerId,
            }
    
    identifier: MetaOapg.properties.identifier
    name: MetaOapg.properties.name
    userId: MetaOapg.properties.userId
    providerType: MetaOapg.properties.providerType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerType"]) -> MetaOapg.properties.providerType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerId"]) -> MetaOapg.properties.providerId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "name", "userId", "providerType", "identifier", "providerId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerType"]) -> MetaOapg.properties.providerType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerId"]) -> typing.Union[MetaOapg.properties.providerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "name", "userId", "providerType", "identifier", "providerId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        identifier: typing.Union[MetaOapg.properties.identifier, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        providerType: typing.Union[MetaOapg.properties.providerType, str, ],
        providerId: typing.Union[MetaOapg.properties.providerId, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Target':
        return super().__new__(
            cls,
            *args,
            identifier=identifier,
            name=name,
            userId=userId,
            providerType=providerType,
            providerId=providerId,
            _configuration=_configuration,
            **kwargs,
        )
