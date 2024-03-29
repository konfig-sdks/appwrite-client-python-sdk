# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_client_python_sdk.paths.locale_currencies.get import GetCurrenciesRaw
from appwrite_client_python_sdk.paths.locale_countries_eu.get import GetEuCountriesRaw
from appwrite_client_python_sdk.paths.locale.get import GetUserLocaleRaw
from appwrite_client_python_sdk.paths.locale_codes.get import ListCodesRaw
from appwrite_client_python_sdk.paths.locale_continents.get import ListContinentsRaw
from appwrite_client_python_sdk.paths.locale_countries.get import ListCountriesRaw
from appwrite_client_python_sdk.paths.locale_countries_phones.get import ListCountriesPhonesRaw
from appwrite_client_python_sdk.paths.locale_languages.get import ListLanguagesRaw


class LocaleApiRaw(
    GetCurrenciesRaw,
    GetEuCountriesRaw,
    GetUserLocaleRaw,
    ListCodesRaw,
    ListContinentsRaw,
    ListCountriesRaw,
    ListCountriesPhonesRaw,
    ListLanguagesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
