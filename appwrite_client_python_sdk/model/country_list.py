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


class CountryList(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Countries List
    """


    class MetaOapg:
        required = {
            "total",
            "countries",
        }
        
        class properties:
            total = schemas.Int32Schema
            
            
            class countries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Country']:
                        return Country
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Country'], typing.List['Country']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Country':
                    return super().__getitem__(i)
            __annotations__ = {
                "total": total,
                "countries": countries,
            }
    
    total: MetaOapg.properties.total
    countries: MetaOapg.properties.countries
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countries"]) -> MetaOapg.properties.countries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "countries", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countries"]) -> MetaOapg.properties.countries: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "countries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        countries: typing.Union[MetaOapg.properties.countries, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CountryList':
        return super().__new__(
            cls,
            *args,
            total=total,
            countries=countries,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_client_python_sdk.model.country import Country
