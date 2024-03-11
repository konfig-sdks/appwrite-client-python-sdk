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


class TeamsCreateNewTeamRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "teamId",
            "name",
        }
        
        class properties:
            teamId = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def roles() -> typing.Type['TeamsCreateNewTeamRequestRoles']:
                return TeamsCreateNewTeamRequestRoles
            __annotations__ = {
                "teamId": teamId,
                "name": name,
                "roles": roles,
            }
    
    teamId: MetaOapg.properties.teamId
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> 'TeamsCreateNewTeamRequestRoles': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["teamId", "name", "roles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union['TeamsCreateNewTeamRequestRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["teamId", "name", "roles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        teamId: typing.Union[MetaOapg.properties.teamId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        roles: typing.Union['TeamsCreateNewTeamRequestRoles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TeamsCreateNewTeamRequest':
        return super().__new__(
            cls,
            *args,
            teamId=teamId,
            name=name,
            roles=roles,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_client_python_sdk.model.teams_create_new_team_request_roles import TeamsCreateNewTeamRequestRoles
