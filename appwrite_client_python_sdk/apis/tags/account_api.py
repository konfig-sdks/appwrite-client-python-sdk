# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_client_python_sdk.paths.account_mfa_authenticators_type.post import AddAuthenticator
from appwrite_client_python_sdk.paths.account_status.patch import BlockUserStatus
from appwrite_client_python_sdk.paths.account_mfa_challenge.put import CompleteMfaChallenge
from appwrite_client_python_sdk.paths.account_recovery.put import CompletePasswordRecovery
from appwrite_client_python_sdk.paths.account_verification_phone.put import ConfirmPhoneVerification
from appwrite_client_python_sdk.paths.account_sessions_anonymous.post import CreateAnonymousSession
from appwrite_client_python_sdk.paths.account_sessions_email.post import CreateEmailPasswordSession
from appwrite_client_python_sdk.paths.account_tokens_email.post import CreateEmailToken
from appwrite_client_python_sdk.paths.account_verification.put import CreateEmailVerification
from appwrite_client_python_sdk.paths.account_verification.post import CreateEmailVerification0
from appwrite_client_python_sdk.paths.account_jwt.post import CreateJwt
from appwrite_client_python_sdk.paths.account_tokens_magic_url.post import CreateMagicUrlToken
from appwrite_client_python_sdk.paths.account_mfa_challenge.post import CreateMfaChallenge
from appwrite_client_python_sdk.paths.account_mfa_recovery_codes.post import CreateMfaRecoveryCodes
from appwrite_client_python_sdk.paths.account_sessions_oauth2_provider.get import CreateOAuth2Session
from appwrite_client_python_sdk.paths.account_tokens_oauth2_provider.get import CreateOAuth2Token
from appwrite_client_python_sdk.paths.account_recovery.post import CreatePasswordRecovery
from appwrite_client_python_sdk.paths.account_tokens_phone.post import CreatePhoneToken
from appwrite_client_python_sdk.paths.account_verification_phone.post import CreatePhoneVerification
from appwrite_client_python_sdk.paths.account_targets_push.post import CreatePushTarget
from appwrite_client_python_sdk.paths.account_sessions_token.post import CreateSessionFromToken
from appwrite_client_python_sdk.paths.account_mfa_authenticators_type.delete import DeleteAuthenticator
from appwrite_client_python_sdk.paths.account_identities_identity_id.delete import DeleteIdentityById
from appwrite_client_python_sdk.paths.account_targets_target_id_push.delete import DeletePushTarget
from appwrite_client_python_sdk.paths.account_sessions_session_id.patch import ExtendSessionLength
from appwrite_client_python_sdk.paths.account.get import GetCurrentUser
from appwrite_client_python_sdk.paths.account_mfa_recovery_codes.get import GetMfaRecoveryCodes
from appwrite_client_python_sdk.paths.account_prefs.get import GetPrefs
from appwrite_client_python_sdk.paths.account_sessions_session_id.get import GetSession
from appwrite_client_python_sdk.paths.account_identities.get import ListIdentities
from appwrite_client_python_sdk.paths.account_logs.get import ListLogs
from appwrite_client_python_sdk.paths.account_mfa_factors.get import ListMfaFactors
from appwrite_client_python_sdk.paths.account_sessions.get import ListSessions
from appwrite_client_python_sdk.paths.account_sessions_session_id.delete import LogoutSessionById
from appwrite_client_python_sdk.paths.account_mfa_recovery_codes.patch import RegenerateMfaRecoveryCodes
from appwrite_client_python_sdk.paths.account.post import RegisterUser
from appwrite_client_python_sdk.paths.account_sessions.delete import RemoveSessions
from appwrite_client_python_sdk.paths.account_sessions_magic_url.put import UpdateMagicUrlSession
from appwrite_client_python_sdk.paths.account_mfa.patch import UpdateMfaStatus
from appwrite_client_python_sdk.paths.account_name.patch import UpdateNameOperation
from appwrite_client_python_sdk.paths.account_password.patch import UpdatePassword
from appwrite_client_python_sdk.paths.account_phone.patch import UpdatePhone
from appwrite_client_python_sdk.paths.account_sessions_phone.put import UpdatePhoneSession
from appwrite_client_python_sdk.paths.account_prefs.patch import UpdatePreferences
from appwrite_client_python_sdk.paths.account_targets_target_id_push.put import UpdatePushTarget
from appwrite_client_python_sdk.paths.account_email.patch import UpdateUserEmail
from appwrite_client_python_sdk.paths.account_mfa_authenticators_type.put import VerifyAuthenticator
from appwrite_client_python_sdk.apis.tags.account_api_raw import AccountApiRaw


class AccountApi(
    AddAuthenticator,
    BlockUserStatus,
    CompleteMfaChallenge,
    CompletePasswordRecovery,
    ConfirmPhoneVerification,
    CreateAnonymousSession,
    CreateEmailPasswordSession,
    CreateEmailToken,
    CreateEmailVerification,
    CreateEmailVerification0,
    CreateJwt,
    CreateMagicUrlToken,
    CreateMfaChallenge,
    CreateMfaRecoveryCodes,
    CreateOAuth2Session,
    CreateOAuth2Token,
    CreatePasswordRecovery,
    CreatePhoneToken,
    CreatePhoneVerification,
    CreatePushTarget,
    CreateSessionFromToken,
    DeleteAuthenticator,
    DeleteIdentityById,
    DeletePushTarget,
    ExtendSessionLength,
    GetCurrentUser,
    GetMfaRecoveryCodes,
    GetPrefs,
    GetSession,
    ListIdentities,
    ListLogs,
    ListMfaFactors,
    ListSessions,
    LogoutSessionById,
    RegenerateMfaRecoveryCodes,
    RegisterUser,
    RemoveSessions,
    UpdateMagicUrlSession,
    UpdateMfaStatus,
    UpdateNameOperation,
    UpdatePassword,
    UpdatePhone,
    UpdatePhoneSession,
    UpdatePreferences,
    UpdatePushTarget,
    UpdateUserEmail,
    VerifyAuthenticator,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccountApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccountApiRaw(api_client)
