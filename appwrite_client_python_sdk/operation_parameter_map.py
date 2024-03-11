operation_parameter_map = {
    '/account/mfa/authenticators/{type}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/account/status-PATCH': {
        'parameters': [
        ]
    },
    '/account/mfa/challenge-PUT': {
        'parameters': [
            {
                'name': 'challengeId'
            },
            {
                'name': 'otp'
            },
        ]
    },
    '/account/recovery-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/verification/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/sessions/anonymous-POST': {
        'parameters': [
        ]
    },
    '/account/sessions/email-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/tokens/email-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account/verification-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/verification-POST': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/account/jwt-POST': {
        'parameters': [
        ]
    },
    '/account/tokens/magic-url-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account/mfa/challenge-POST': {
        'parameters': [
            {
                'name': 'factor'
            },
        ]
    },
    '/account/mfa/recovery-codes-POST': {
        'parameters': [
        ]
    },
    '/account/sessions/oauth2/{provider}-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'success'
            },
            {
                'name': 'failure'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/account/tokens/oauth2/{provider}-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'success'
            },
            {
                'name': 'failure'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/account/recovery-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/account/tokens/phone-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/account/verification/phone-POST': {
        'parameters': [
        ]
    },
    '/account/targets/push-POST': {
        'parameters': [
            {
                'name': 'targetId'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'providerId'
            },
        ]
    },
    '/account/sessions/token-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa/authenticators/{type}-DELETE': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/account/identities/{identityId}-DELETE': {
        'parameters': [
            {
                'name': 'identityId'
            },
        ]
    },
    '/account/targets/{targetId}/push-DELETE': {
        'parameters': [
            {
                'name': 'targetId'
            },
        ]
    },
    '/account/sessions/{sessionId}-PATCH': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account-GET': {
        'parameters': [
        ]
    },
    '/account/mfa/recovery-codes-GET': {
        'parameters': [
        ]
    },
    '/account/prefs-GET': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/identities-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/logs-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/mfa/factors-GET': {
        'parameters': [
        ]
    },
    '/account/sessions-GET': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/mfa/recovery-codes-PATCH': {
        'parameters': [
        ]
    },
    '/account-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/account/sessions-DELETE': {
        'parameters': [
        ]
    },
    '/account/sessions/magic-url-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa-PATCH': {
        'parameters': [
            {
                'name': 'mfa'
            },
        ]
    },
    '/account/name-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/account/password-PATCH': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'oldPassword'
            },
        ]
    },
    '/account/phone-PATCH': {
        'parameters': [
            {
                'name': 'phone'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/sessions/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/prefs-PATCH': {
        'parameters': [
            {
                'name': 'prefs'
            },
        ]
    },
    '/account/targets/{targetId}/push-PUT': {
        'parameters': [
            {
                'name': 'identifier'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/account/email-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/mfa/authenticators/{type}-PUT': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/avatars/qr-GET': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'size'
            },
            {
                'name': 'margin'
            },
            {
                'name': 'download'
            },
        ]
    },
    '/avatars/browsers/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/flags/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/credit-cards/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/favicon-GET': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/avatars/image-GET': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
        ]
    },
    '/avatars/initials-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'background'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-POST': {
        'parameters': [
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-PATCH': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/functions/{functionId}/executions/{executionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'executionId'
            },
        ]
    },
    '/functions/{functionId}/executions-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/{functionId}/executions-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'async'
            },
            {
                'name': 'path'
            },
            {
                'name': 'method'
            },
            {
                'name': 'headers'
            },
        ]
    },
    '/graphql-POST': {
        'parameters': [
        ]
    },
    '/graphql/mutation-POST': {
        'parameters': [
        ]
    },
    '/locale/currencies-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/eu-GET': {
        'parameters': [
        ]
    },
    '/locale-GET': {
        'parameters': [
        ]
    },
    '/locale/codes-GET': {
        'parameters': [
        ]
    },
    '/locale/continents-GET': {
        'parameters': [
        ]
    },
    '/locale/countries-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/phones-GET': {
        'parameters': [
        ]
    },
    '/locale/languages-GET': {
        'parameters': [
        ]
    },
    '/messaging/topics/{topicId}/subscribers-POST': {
        'parameters': [
            {
                'name': 'subscriberId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers/{subscriberId}-DELETE': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'subscriberId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-POST': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/download-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/view-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/preview-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'gravity'
            },
            {
                'name': 'quality'
            },
            {
                'name': 'borderWidth'
            },
            {
                'name': 'borderColor'
            },
            {
                'name': 'borderRadius'
            },
            {
                'name': 'opacity'
            },
            {
                'name': 'rotation'
            },
            {
                'name': 'background'
            },
            {
                'name': 'output'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-PUT': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/teams/{teamId}/memberships-POST': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'url'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'roles'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/prefs-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}/memberships-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-PATCH': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}/status-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/prefs-PUT': {
        'parameters': [
            {
                'name': 'prefs'
            },
            {
                'name': 'teamId'
            },
        ]
    },
};