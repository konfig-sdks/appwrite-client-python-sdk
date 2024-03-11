# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_client_python_sdk.paths.messaging_topics_topic_id_subscribers.post import AddNewSubscriber
from appwrite_client_python_sdk.paths.messaging_topics_topic_id_subscribers_subscriber_id.delete import DeleteSubscriberById
from appwrite_client_python_sdk.apis.tags.messaging_api_raw import MessagingApiRaw


class MessagingApi(
    AddNewSubscriber,
    DeleteSubscriberById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MessagingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MessagingApiRaw(api_client)