# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from appwrite_client_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT = "account"
    TEAMS = "teams"
    LOCALE = "locale"
    STORAGE = "storage"
    AVATARS = "avatars"
    DATABASES = "databases"
    FUNCTIONS = "functions"
    GRAPHQL = "graphql"
    MESSAGING = "messaging"
    HEALTH = "health"
    PROJECTS = "projects"
    PROJECT = "project"
    USERS = "users"
    PROXY = "proxy"
    CONSOLE = "console"
    MIGRATIONS = "migrations"
