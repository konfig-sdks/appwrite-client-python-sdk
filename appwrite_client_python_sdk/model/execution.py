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


class Execution(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Execution
    """


    class MetaOapg:
        required = {
            "responseBody",
            "requestMethod",
            "$createdAt",
            "trigger",
            "$permissions",
            "$updatedAt",
            "duration",
            "responseStatusCode",
            "functionId",
            "requestHeaders",
            "responseHeaders",
            "logs",
            "errors",
            "requestPath",
            "$id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
        
            @staticmethod
            def permissions() -> typing.Type['Executionpermissions']:
                return Executionpermissions
            functionId = schemas.StrSchema
            trigger = schemas.StrSchema
            status = schemas.StrSchema
            requestMethod = schemas.StrSchema
            requestPath = schemas.StrSchema
            
            
            class requestHeaders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Headers']:
                        return Headers
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Headers'], typing.List['Headers']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requestHeaders':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Headers':
                    return super().__getitem__(i)
            responseStatusCode = schemas.Int32Schema
            responseBody = schemas.StrSchema
            
            
            class responseHeaders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Headers']:
                        return Headers
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Headers'], typing.List['Headers']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'responseHeaders':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Headers':
                    return super().__getitem__(i)
            logs = schemas.StrSchema
            errors = schemas.StrSchema
            duration = schemas.Float64Schema
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "$permissions": permissions,
                "functionId": functionId,
                "trigger": trigger,
                "status": status,
                "requestMethod": requestMethod,
                "requestPath": requestPath,
                "requestHeaders": requestHeaders,
                "responseStatusCode": responseStatusCode,
                "responseBody": responseBody,
                "responseHeaders": responseHeaders,
                "logs": logs,
                "errors": errors,
                "duration": duration,
            }
    
    responseBody: MetaOapg.properties.responseBody
    requestMethod: MetaOapg.properties.requestMethod
    trigger: MetaOapg.properties.trigger
    duration: MetaOapg.properties.duration
    responseStatusCode: MetaOapg.properties.responseStatusCode
    functionId: MetaOapg.properties.functionId
    requestHeaders: MetaOapg.properties.requestHeaders
    responseHeaders: MetaOapg.properties.responseHeaders
    logs: MetaOapg.properties.logs
    errors: MetaOapg.properties.errors
    requestPath: MetaOapg.properties.requestPath
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$permissions"]) -> 'Executionpermissions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionId"]) -> MetaOapg.properties.functionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestMethod"]) -> MetaOapg.properties.requestMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestPath"]) -> MetaOapg.properties.requestPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestHeaders"]) -> MetaOapg.properties.requestHeaders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseStatusCode"]) -> MetaOapg.properties.responseStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseBody"]) -> MetaOapg.properties.responseBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseHeaders"]) -> MetaOapg.properties.responseHeaders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "$permissions", "functionId", "trigger", "status", "requestMethod", "requestPath", "requestHeaders", "responseStatusCode", "responseBody", "responseHeaders", "logs", "errors", "duration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$permissions"]) -> 'Executionpermissions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionId"]) -> MetaOapg.properties.functionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestMethod"]) -> MetaOapg.properties.requestMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestPath"]) -> MetaOapg.properties.requestPath: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestHeaders"]) -> MetaOapg.properties.requestHeaders: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseStatusCode"]) -> MetaOapg.properties.responseStatusCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseBody"]) -> MetaOapg.properties.responseBody: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseHeaders"]) -> MetaOapg.properties.responseHeaders: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "$permissions", "functionId", "trigger", "status", "requestMethod", "requestPath", "requestHeaders", "responseStatusCode", "responseBody", "responseHeaders", "logs", "errors", "duration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        responseBody: typing.Union[MetaOapg.properties.responseBody, str, ],
        requestMethod: typing.Union[MetaOapg.properties.requestMethod, str, ],
        trigger: typing.Union[MetaOapg.properties.trigger, str, ],
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, ],
        responseStatusCode: typing.Union[MetaOapg.properties.responseStatusCode, decimal.Decimal, int, ],
        functionId: typing.Union[MetaOapg.properties.functionId, str, ],
        requestHeaders: typing.Union[MetaOapg.properties.requestHeaders, list, tuple, ],
        responseHeaders: typing.Union[MetaOapg.properties.responseHeaders, list, tuple, ],
        logs: typing.Union[MetaOapg.properties.logs, str, ],
        errors: typing.Union[MetaOapg.properties.errors, str, ],
        requestPath: typing.Union[MetaOapg.properties.requestPath, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Execution':
        return super().__new__(
            cls,
            *args,
            responseBody=responseBody,
            requestMethod=requestMethod,
            trigger=trigger,
            duration=duration,
            responseStatusCode=responseStatusCode,
            functionId=functionId,
            requestHeaders=requestHeaders,
            responseHeaders=responseHeaders,
            logs=logs,
            errors=errors,
            requestPath=requestPath,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_client_python_sdk.model.executionpermissions import Executionpermissions
from appwrite_client_python_sdk.model.headers import Headers
