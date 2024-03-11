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


class Currency(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Currency
    """


    class MetaOapg:
        required = {
            "namePlural",
            "symbol",
            "code",
            "symbolNative",
            "name",
            "rounding",
            "decimalDigits",
        }
        
        class properties:
            symbol = schemas.StrSchema
            name = schemas.StrSchema
            symbolNative = schemas.StrSchema
            decimalDigits = schemas.Int32Schema
            rounding = schemas.Float64Schema
            code = schemas.StrSchema
            namePlural = schemas.StrSchema
            __annotations__ = {
                "symbol": symbol,
                "name": name,
                "symbolNative": symbolNative,
                "decimalDigits": decimalDigits,
                "rounding": rounding,
                "code": code,
                "namePlural": namePlural,
            }
    
    namePlural: MetaOapg.properties.namePlural
    symbol: MetaOapg.properties.symbol
    code: MetaOapg.properties.code
    symbolNative: MetaOapg.properties.symbolNative
    name: MetaOapg.properties.name
    rounding: MetaOapg.properties.rounding
    decimalDigits: MetaOapg.properties.decimalDigits
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolNative"]) -> MetaOapg.properties.symbolNative: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimalDigits"]) -> MetaOapg.properties.decimalDigits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rounding"]) -> MetaOapg.properties.rounding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["namePlural"]) -> MetaOapg.properties.namePlural: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "symbolNative", "decimalDigits", "rounding", "code", "namePlural", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolNative"]) -> MetaOapg.properties.symbolNative: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimalDigits"]) -> MetaOapg.properties.decimalDigits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rounding"]) -> MetaOapg.properties.rounding: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["namePlural"]) -> MetaOapg.properties.namePlural: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "symbolNative", "decimalDigits", "rounding", "code", "namePlural", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        namePlural: typing.Union[MetaOapg.properties.namePlural, str, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        symbolNative: typing.Union[MetaOapg.properties.symbolNative, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        rounding: typing.Union[MetaOapg.properties.rounding, decimal.Decimal, int, float, ],
        decimalDigits: typing.Union[MetaOapg.properties.decimalDigits, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Currency':
        return super().__new__(
            cls,
            *args,
            namePlural=namePlural,
            symbol=symbol,
            code=code,
            symbolNative=symbolNative,
            name=name,
            rounding=rounding,
            decimalDigits=decimalDigits,
            _configuration=_configuration,
            **kwargs,
        )