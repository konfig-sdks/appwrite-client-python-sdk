# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from appwrite_client_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNT = "/account"
    ACCOUNT_EMAIL = "/account/email"
    ACCOUNT_IDENTITIES = "/account/identities"
    ACCOUNT_IDENTITIES_IDENTITY_ID = "/account/identities/{identityId}"
    ACCOUNT_JWT = "/account/jwt"
    ACCOUNT_LOGS = "/account/logs"
    ACCOUNT_MFA = "/account/mfa"
    ACCOUNT_MFA_AUTHENTICATORS_TYPE = "/account/mfa/authenticators/{type}"
    ACCOUNT_MFA_CHALLENGE = "/account/mfa/challenge"
    ACCOUNT_MFA_FACTORS = "/account/mfa/factors"
    ACCOUNT_MFA_RECOVERYCODES = "/account/mfa/recovery-codes"
    ACCOUNT_NAME = "/account/name"
    ACCOUNT_PASSWORD = "/account/password"
    ACCOUNT_PHONE = "/account/phone"
    ACCOUNT_PREFS = "/account/prefs"
    ACCOUNT_RECOVERY = "/account/recovery"
    ACCOUNT_SESSIONS = "/account/sessions"
    ACCOUNT_SESSIONS_ANONYMOUS = "/account/sessions/anonymous"
    ACCOUNT_SESSIONS_EMAIL = "/account/sessions/email"
    ACCOUNT_SESSIONS_MAGICURL = "/account/sessions/magic-url"
    ACCOUNT_SESSIONS_OAUTH2_PROVIDER = "/account/sessions/oauth2/{provider}"
    ACCOUNT_SESSIONS_PHONE = "/account/sessions/phone"
    ACCOUNT_SESSIONS_TOKEN = "/account/sessions/token"
    ACCOUNT_SESSIONS_SESSION_ID = "/account/sessions/{sessionId}"
    ACCOUNT_STATUS = "/account/status"
    ACCOUNT_TARGETS_PUSH = "/account/targets/push"
    ACCOUNT_TARGETS_TARGET_ID_PUSH = "/account/targets/{targetId}/push"
    ACCOUNT_TOKENS_EMAIL = "/account/tokens/email"
    ACCOUNT_TOKENS_MAGICURL = "/account/tokens/magic-url"
    ACCOUNT_TOKENS_OAUTH2_PROVIDER = "/account/tokens/oauth2/{provider}"
    ACCOUNT_TOKENS_PHONE = "/account/tokens/phone"
    ACCOUNT_VERIFICATION = "/account/verification"
    ACCOUNT_VERIFICATION_PHONE = "/account/verification/phone"
    AVATARS_BROWSERS_CODE = "/avatars/browsers/{code}"
    AVATARS_CREDITCARDS_CODE = "/avatars/credit-cards/{code}"
    AVATARS_FAVICON = "/avatars/favicon"
    AVATARS_FLAGS_CODE = "/avatars/flags/{code}"
    AVATARS_IMAGE = "/avatars/image"
    AVATARS_INITIALS = "/avatars/initials"
    AVATARS_QR = "/avatars/qr"
    DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS = "/databases/{databaseId}/collections/{collectionId}/documents"
    DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS_DOCUMENT_ID = "/databases/{databaseId}/collections/{collectionId}/documents/{documentId}"
    FUNCTIONS_FUNCTION_ID_EXECUTIONS = "/functions/{functionId}/executions"
    FUNCTIONS_FUNCTION_ID_EXECUTIONS_EXECUTION_ID = "/functions/{functionId}/executions/{executionId}"
    GRAPHQL = "/graphql"
    GRAPHQL_MUTATION = "/graphql/mutation"
    LOCALE = "/locale"
    LOCALE_CODES = "/locale/codes"
    LOCALE_CONTINENTS = "/locale/continents"
    LOCALE_COUNTRIES = "/locale/countries"
    LOCALE_COUNTRIES_EU = "/locale/countries/eu"
    LOCALE_COUNTRIES_PHONES = "/locale/countries/phones"
    LOCALE_CURRENCIES = "/locale/currencies"
    LOCALE_LANGUAGES = "/locale/languages"
    MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS = "/messaging/topics/{topicId}/subscribers"
    MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS_SUBSCRIBER_ID = "/messaging/topics/{topicId}/subscribers/{subscriberId}"
    STORAGE_BUCKETS_BUCKET_ID_FILES = "/storage/buckets/{bucketId}/files"
    STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID = "/storage/buckets/{bucketId}/files/{fileId}"
    STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_DOWNLOAD = "/storage/buckets/{bucketId}/files/{fileId}/download"
    STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_PREVIEW = "/storage/buckets/{bucketId}/files/{fileId}/preview"
    STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_VIEW = "/storage/buckets/{bucketId}/files/{fileId}/view"
    TEAMS = "/teams"
    TEAMS_TEAM_ID = "/teams/{teamId}"
    TEAMS_TEAM_ID_MEMBERSHIPS = "/teams/{teamId}/memberships"
    TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID = "/teams/{teamId}/memberships/{membershipId}"
    TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID_STATUS = "/teams/{teamId}/memberships/{membershipId}/status"
    TEAMS_TEAM_ID_PREFS = "/teams/{teamId}/prefs"
