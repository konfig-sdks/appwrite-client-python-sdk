import typing_extensions

from appwrite_client_python_sdk.paths import PathValues
from appwrite_client_python_sdk.apis.paths.account import Account
from appwrite_client_python_sdk.apis.paths.account_email import AccountEmail
from appwrite_client_python_sdk.apis.paths.account_identities import AccountIdentities
from appwrite_client_python_sdk.apis.paths.account_identities_identity_id import AccountIdentitiesIdentityId
from appwrite_client_python_sdk.apis.paths.account_jwt import AccountJwt
from appwrite_client_python_sdk.apis.paths.account_logs import AccountLogs
from appwrite_client_python_sdk.apis.paths.account_mfa import AccountMfa
from appwrite_client_python_sdk.apis.paths.account_mfa_authenticators_type import AccountMfaAuthenticatorsType
from appwrite_client_python_sdk.apis.paths.account_mfa_challenge import AccountMfaChallenge
from appwrite_client_python_sdk.apis.paths.account_mfa_factors import AccountMfaFactors
from appwrite_client_python_sdk.apis.paths.account_mfa_recovery_codes import AccountMfaRecoveryCodes
from appwrite_client_python_sdk.apis.paths.account_name import AccountName
from appwrite_client_python_sdk.apis.paths.account_password import AccountPassword
from appwrite_client_python_sdk.apis.paths.account_phone import AccountPhone
from appwrite_client_python_sdk.apis.paths.account_prefs import AccountPrefs
from appwrite_client_python_sdk.apis.paths.account_recovery import AccountRecovery
from appwrite_client_python_sdk.apis.paths.account_sessions import AccountSessions
from appwrite_client_python_sdk.apis.paths.account_sessions_anonymous import AccountSessionsAnonymous
from appwrite_client_python_sdk.apis.paths.account_sessions_email import AccountSessionsEmail
from appwrite_client_python_sdk.apis.paths.account_sessions_magic_url import AccountSessionsMagicUrl
from appwrite_client_python_sdk.apis.paths.account_sessions_oauth2_provider import AccountSessionsOauth2Provider
from appwrite_client_python_sdk.apis.paths.account_sessions_phone import AccountSessionsPhone
from appwrite_client_python_sdk.apis.paths.account_sessions_token import AccountSessionsToken
from appwrite_client_python_sdk.apis.paths.account_sessions_session_id import AccountSessionsSessionId
from appwrite_client_python_sdk.apis.paths.account_status import AccountStatus
from appwrite_client_python_sdk.apis.paths.account_targets_push import AccountTargetsPush
from appwrite_client_python_sdk.apis.paths.account_targets_target_id_push import AccountTargetsTargetIdPush
from appwrite_client_python_sdk.apis.paths.account_tokens_email import AccountTokensEmail
from appwrite_client_python_sdk.apis.paths.account_tokens_magic_url import AccountTokensMagicUrl
from appwrite_client_python_sdk.apis.paths.account_tokens_oauth2_provider import AccountTokensOauth2Provider
from appwrite_client_python_sdk.apis.paths.account_tokens_phone import AccountTokensPhone
from appwrite_client_python_sdk.apis.paths.account_verification import AccountVerification
from appwrite_client_python_sdk.apis.paths.account_verification_phone import AccountVerificationPhone
from appwrite_client_python_sdk.apis.paths.avatars_browsers_code import AvatarsBrowsersCode
from appwrite_client_python_sdk.apis.paths.avatars_credit_cards_code import AvatarsCreditCardsCode
from appwrite_client_python_sdk.apis.paths.avatars_favicon import AvatarsFavicon
from appwrite_client_python_sdk.apis.paths.avatars_flags_code import AvatarsFlagsCode
from appwrite_client_python_sdk.apis.paths.avatars_image import AvatarsImage
from appwrite_client_python_sdk.apis.paths.avatars_initials import AvatarsInitials
from appwrite_client_python_sdk.apis.paths.avatars_qr import AvatarsQr
from appwrite_client_python_sdk.apis.paths.databases_database_id_collections_collection_id_documents import DatabasesDatabaseIdCollectionsCollectionIdDocuments
from appwrite_client_python_sdk.apis.paths.databases_database_id_collections_collection_id_documents_document_id import DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId
from appwrite_client_python_sdk.apis.paths.functions_function_id_executions import FunctionsFunctionIdExecutions
from appwrite_client_python_sdk.apis.paths.functions_function_id_executions_execution_id import FunctionsFunctionIdExecutionsExecutionId
from appwrite_client_python_sdk.apis.paths.graphql import Graphql
from appwrite_client_python_sdk.apis.paths.graphql_mutation import GraphqlMutation
from appwrite_client_python_sdk.apis.paths.locale import Locale
from appwrite_client_python_sdk.apis.paths.locale_codes import LocaleCodes
from appwrite_client_python_sdk.apis.paths.locale_continents import LocaleContinents
from appwrite_client_python_sdk.apis.paths.locale_countries import LocaleCountries
from appwrite_client_python_sdk.apis.paths.locale_countries_eu import LocaleCountriesEu
from appwrite_client_python_sdk.apis.paths.locale_countries_phones import LocaleCountriesPhones
from appwrite_client_python_sdk.apis.paths.locale_currencies import LocaleCurrencies
from appwrite_client_python_sdk.apis.paths.locale_languages import LocaleLanguages
from appwrite_client_python_sdk.apis.paths.messaging_topics_topic_id_subscribers import MessagingTopicsTopicIdSubscribers
from appwrite_client_python_sdk.apis.paths.messaging_topics_topic_id_subscribers_subscriber_id import MessagingTopicsTopicIdSubscribersSubscriberId
from appwrite_client_python_sdk.apis.paths.storage_buckets_bucket_id_files import StorageBucketsBucketIdFiles
from appwrite_client_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id import StorageBucketsBucketIdFilesFileId
from appwrite_client_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_download import StorageBucketsBucketIdFilesFileIdDownload
from appwrite_client_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_preview import StorageBucketsBucketIdFilesFileIdPreview
from appwrite_client_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_view import StorageBucketsBucketIdFilesFileIdView
from appwrite_client_python_sdk.apis.paths.teams import Teams
from appwrite_client_python_sdk.apis.paths.teams_team_id import TeamsTeamId
from appwrite_client_python_sdk.apis.paths.teams_team_id_memberships import TeamsTeamIdMemberships
from appwrite_client_python_sdk.apis.paths.teams_team_id_memberships_membership_id import TeamsTeamIdMembershipsMembershipId
from appwrite_client_python_sdk.apis.paths.teams_team_id_memberships_membership_id_status import TeamsTeamIdMembershipsMembershipIdStatus
from appwrite_client_python_sdk.apis.paths.teams_team_id_prefs import TeamsTeamIdPrefs

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_EMAIL: AccountEmail,
        PathValues.ACCOUNT_IDENTITIES: AccountIdentities,
        PathValues.ACCOUNT_IDENTITIES_IDENTITY_ID: AccountIdentitiesIdentityId,
        PathValues.ACCOUNT_JWT: AccountJwt,
        PathValues.ACCOUNT_LOGS: AccountLogs,
        PathValues.ACCOUNT_MFA: AccountMfa,
        PathValues.ACCOUNT_MFA_AUTHENTICATORS_TYPE: AccountMfaAuthenticatorsType,
        PathValues.ACCOUNT_MFA_CHALLENGE: AccountMfaChallenge,
        PathValues.ACCOUNT_MFA_FACTORS: AccountMfaFactors,
        PathValues.ACCOUNT_MFA_RECOVERYCODES: AccountMfaRecoveryCodes,
        PathValues.ACCOUNT_NAME: AccountName,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_PHONE: AccountPhone,
        PathValues.ACCOUNT_PREFS: AccountPrefs,
        PathValues.ACCOUNT_RECOVERY: AccountRecovery,
        PathValues.ACCOUNT_SESSIONS: AccountSessions,
        PathValues.ACCOUNT_SESSIONS_ANONYMOUS: AccountSessionsAnonymous,
        PathValues.ACCOUNT_SESSIONS_EMAIL: AccountSessionsEmail,
        PathValues.ACCOUNT_SESSIONS_MAGICURL: AccountSessionsMagicUrl,
        PathValues.ACCOUNT_SESSIONS_OAUTH2_PROVIDER: AccountSessionsOauth2Provider,
        PathValues.ACCOUNT_SESSIONS_PHONE: AccountSessionsPhone,
        PathValues.ACCOUNT_SESSIONS_TOKEN: AccountSessionsToken,
        PathValues.ACCOUNT_SESSIONS_SESSION_ID: AccountSessionsSessionId,
        PathValues.ACCOUNT_STATUS: AccountStatus,
        PathValues.ACCOUNT_TARGETS_PUSH: AccountTargetsPush,
        PathValues.ACCOUNT_TARGETS_TARGET_ID_PUSH: AccountTargetsTargetIdPush,
        PathValues.ACCOUNT_TOKENS_EMAIL: AccountTokensEmail,
        PathValues.ACCOUNT_TOKENS_MAGICURL: AccountTokensMagicUrl,
        PathValues.ACCOUNT_TOKENS_OAUTH2_PROVIDER: AccountTokensOauth2Provider,
        PathValues.ACCOUNT_TOKENS_PHONE: AccountTokensPhone,
        PathValues.ACCOUNT_VERIFICATION: AccountVerification,
        PathValues.ACCOUNT_VERIFICATION_PHONE: AccountVerificationPhone,
        PathValues.AVATARS_BROWSERS_CODE: AvatarsBrowsersCode,
        PathValues.AVATARS_CREDITCARDS_CODE: AvatarsCreditCardsCode,
        PathValues.AVATARS_FAVICON: AvatarsFavicon,
        PathValues.AVATARS_FLAGS_CODE: AvatarsFlagsCode,
        PathValues.AVATARS_IMAGE: AvatarsImage,
        PathValues.AVATARS_INITIALS: AvatarsInitials,
        PathValues.AVATARS_QR: AvatarsQr,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS: DatabasesDatabaseIdCollectionsCollectionIdDocuments,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS_DOCUMENT_ID: DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS: FunctionsFunctionIdExecutions,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS_EXECUTION_ID: FunctionsFunctionIdExecutionsExecutionId,
        PathValues.GRAPHQL: Graphql,
        PathValues.GRAPHQL_MUTATION: GraphqlMutation,
        PathValues.LOCALE: Locale,
        PathValues.LOCALE_CODES: LocaleCodes,
        PathValues.LOCALE_CONTINENTS: LocaleContinents,
        PathValues.LOCALE_COUNTRIES: LocaleCountries,
        PathValues.LOCALE_COUNTRIES_EU: LocaleCountriesEu,
        PathValues.LOCALE_COUNTRIES_PHONES: LocaleCountriesPhones,
        PathValues.LOCALE_CURRENCIES: LocaleCurrencies,
        PathValues.LOCALE_LANGUAGES: LocaleLanguages,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS: MessagingTopicsTopicIdSubscribers,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS_SUBSCRIBER_ID: MessagingTopicsTopicIdSubscribersSubscriberId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES: StorageBucketsBucketIdFiles,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID: StorageBucketsBucketIdFilesFileId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_DOWNLOAD: StorageBucketsBucketIdFilesFileIdDownload,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_PREVIEW: StorageBucketsBucketIdFilesFileIdPreview,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_VIEW: StorageBucketsBucketIdFilesFileIdView,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS: TeamsTeamIdMemberships,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID: TeamsTeamIdMembershipsMembershipId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID_STATUS: TeamsTeamIdMembershipsMembershipIdStatus,
        PathValues.TEAMS_TEAM_ID_PREFS: TeamsTeamIdPrefs,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_EMAIL: AccountEmail,
        PathValues.ACCOUNT_IDENTITIES: AccountIdentities,
        PathValues.ACCOUNT_IDENTITIES_IDENTITY_ID: AccountIdentitiesIdentityId,
        PathValues.ACCOUNT_JWT: AccountJwt,
        PathValues.ACCOUNT_LOGS: AccountLogs,
        PathValues.ACCOUNT_MFA: AccountMfa,
        PathValues.ACCOUNT_MFA_AUTHENTICATORS_TYPE: AccountMfaAuthenticatorsType,
        PathValues.ACCOUNT_MFA_CHALLENGE: AccountMfaChallenge,
        PathValues.ACCOUNT_MFA_FACTORS: AccountMfaFactors,
        PathValues.ACCOUNT_MFA_RECOVERYCODES: AccountMfaRecoveryCodes,
        PathValues.ACCOUNT_NAME: AccountName,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_PHONE: AccountPhone,
        PathValues.ACCOUNT_PREFS: AccountPrefs,
        PathValues.ACCOUNT_RECOVERY: AccountRecovery,
        PathValues.ACCOUNT_SESSIONS: AccountSessions,
        PathValues.ACCOUNT_SESSIONS_ANONYMOUS: AccountSessionsAnonymous,
        PathValues.ACCOUNT_SESSIONS_EMAIL: AccountSessionsEmail,
        PathValues.ACCOUNT_SESSIONS_MAGICURL: AccountSessionsMagicUrl,
        PathValues.ACCOUNT_SESSIONS_OAUTH2_PROVIDER: AccountSessionsOauth2Provider,
        PathValues.ACCOUNT_SESSIONS_PHONE: AccountSessionsPhone,
        PathValues.ACCOUNT_SESSIONS_TOKEN: AccountSessionsToken,
        PathValues.ACCOUNT_SESSIONS_SESSION_ID: AccountSessionsSessionId,
        PathValues.ACCOUNT_STATUS: AccountStatus,
        PathValues.ACCOUNT_TARGETS_PUSH: AccountTargetsPush,
        PathValues.ACCOUNT_TARGETS_TARGET_ID_PUSH: AccountTargetsTargetIdPush,
        PathValues.ACCOUNT_TOKENS_EMAIL: AccountTokensEmail,
        PathValues.ACCOUNT_TOKENS_MAGICURL: AccountTokensMagicUrl,
        PathValues.ACCOUNT_TOKENS_OAUTH2_PROVIDER: AccountTokensOauth2Provider,
        PathValues.ACCOUNT_TOKENS_PHONE: AccountTokensPhone,
        PathValues.ACCOUNT_VERIFICATION: AccountVerification,
        PathValues.ACCOUNT_VERIFICATION_PHONE: AccountVerificationPhone,
        PathValues.AVATARS_BROWSERS_CODE: AvatarsBrowsersCode,
        PathValues.AVATARS_CREDITCARDS_CODE: AvatarsCreditCardsCode,
        PathValues.AVATARS_FAVICON: AvatarsFavicon,
        PathValues.AVATARS_FLAGS_CODE: AvatarsFlagsCode,
        PathValues.AVATARS_IMAGE: AvatarsImage,
        PathValues.AVATARS_INITIALS: AvatarsInitials,
        PathValues.AVATARS_QR: AvatarsQr,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS: DatabasesDatabaseIdCollectionsCollectionIdDocuments,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS_DOCUMENT_ID: DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS: FunctionsFunctionIdExecutions,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS_EXECUTION_ID: FunctionsFunctionIdExecutionsExecutionId,
        PathValues.GRAPHQL: Graphql,
        PathValues.GRAPHQL_MUTATION: GraphqlMutation,
        PathValues.LOCALE: Locale,
        PathValues.LOCALE_CODES: LocaleCodes,
        PathValues.LOCALE_CONTINENTS: LocaleContinents,
        PathValues.LOCALE_COUNTRIES: LocaleCountries,
        PathValues.LOCALE_COUNTRIES_EU: LocaleCountriesEu,
        PathValues.LOCALE_COUNTRIES_PHONES: LocaleCountriesPhones,
        PathValues.LOCALE_CURRENCIES: LocaleCurrencies,
        PathValues.LOCALE_LANGUAGES: LocaleLanguages,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS: MessagingTopicsTopicIdSubscribers,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS_SUBSCRIBER_ID: MessagingTopicsTopicIdSubscribersSubscriberId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES: StorageBucketsBucketIdFiles,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID: StorageBucketsBucketIdFilesFileId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_DOWNLOAD: StorageBucketsBucketIdFilesFileIdDownload,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_PREVIEW: StorageBucketsBucketIdFilesFileIdPreview,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_VIEW: StorageBucketsBucketIdFilesFileIdView,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS: TeamsTeamIdMemberships,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID: TeamsTeamIdMembershipsMembershipId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID_STATUS: TeamsTeamIdMembershipsMembershipIdStatus,
        PathValues.TEAMS_TEAM_ID_PREFS: TeamsTeamIdPrefs,
    }
)
