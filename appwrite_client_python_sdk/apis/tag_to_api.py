import typing_extensions

from appwrite_client_python_sdk.apis.tags import TagValues
from appwrite_client_python_sdk.apis.tags.account_api import AccountApi
from appwrite_client_python_sdk.apis.tags.teams_api import TeamsApi
from appwrite_client_python_sdk.apis.tags.locale_api import LocaleApi
from appwrite_client_python_sdk.apis.tags.storage_api import StorageApi
from appwrite_client_python_sdk.apis.tags.avatars_api import AvatarsApi
from appwrite_client_python_sdk.apis.tags.databases_api import DatabasesApi
from appwrite_client_python_sdk.apis.tags.functions_api import FunctionsApi
from appwrite_client_python_sdk.apis.tags.graphql_api import GraphqlApi
from appwrite_client_python_sdk.apis.tags.messaging_api import MessagingApi
from appwrite_client_python_sdk.apis.tags.health_api import HealthApi
from appwrite_client_python_sdk.apis.tags.projects_api import ProjectsApi
from appwrite_client_python_sdk.apis.tags.project_api import ProjectApi
from appwrite_client_python_sdk.apis.tags.users_api import UsersApi
from appwrite_client_python_sdk.apis.tags.proxy_api import ProxyApi
from appwrite_client_python_sdk.apis.tags.console_api import ConsoleApi
from appwrite_client_python_sdk.apis.tags.migrations_api import MigrationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.LOCALE: LocaleApi,
        TagValues.STORAGE: StorageApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.DATABASES: DatabasesApi,
        TagValues.FUNCTIONS: FunctionsApi,
        TagValues.GRAPHQL: GraphqlApi,
        TagValues.MESSAGING: MessagingApi,
        TagValues.HEALTH: HealthApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.USERS: UsersApi,
        TagValues.PROXY: ProxyApi,
        TagValues.CONSOLE: ConsoleApi,
        TagValues.MIGRATIONS: MigrationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.LOCALE: LocaleApi,
        TagValues.STORAGE: StorageApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.DATABASES: DatabasesApi,
        TagValues.FUNCTIONS: FunctionsApi,
        TagValues.GRAPHQL: GraphqlApi,
        TagValues.MESSAGING: MessagingApi,
        TagValues.HEALTH: HealthApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.USERS: UsersApi,
        TagValues.PROXY: ProxyApi,
        TagValues.CONSOLE: ConsoleApi,
        TagValues.MIGRATIONS: MigrationsApi,
    }
)
