# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.errors",
    marshal="google.ads.googleads.v4",
    manifest={"OfflineUserDataJobErrorEnum",},
)


class OfflineUserDataJobErrorEnum(proto.Message):
    r"""Container for enum describing possible offline user data job
    errors.
    """

    class OfflineUserDataJobError(proto.Enum):
        r"""Enum describing possible request errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_USER_LIST_ID = 3
        INVALID_USER_LIST_TYPE = 4
        NOT_WHITELISTED_FOR_USER_ID = 5
        INCOMPATIBLE_UPLOAD_KEY_TYPE = 6
        MISSING_USER_IDENTIFIER = 7
        INVALID_MOBILE_ID_FORMAT = 8
        TOO_MANY_USER_IDENTIFIERS = 9
        NOT_WHITELISTED_FOR_STORE_SALES_DIRECT = 10
        NOT_WHITELISTED_FOR_UNIFIED_STORE_SALES = 28
        INVALID_PARTNER_ID = 11
        INVALID_ENCODING = 12
        INVALID_COUNTRY_CODE = 13
        INCOMPATIBLE_USER_IDENTIFIER = 14
        FUTURE_TRANSACTION_TIME = 15
        INVALID_CONVERSION_ACTION = 16
        MOBILE_ID_NOT_SUPPORTED = 17
        INVALID_OPERATION_ORDER = 18
        CONFLICTING_OPERATION = 19
        EXTERNAL_UPDATE_ID_ALREADY_EXISTS = 21
        JOB_ALREADY_STARTED = 22
        REMOVE_NOT_SUPPORTED = 23
        REMOVE_ALL_NOT_SUPPORTED = 24
        INVALID_SHA256_FORMAT = 25
        CUSTOM_KEY_DISABLED = 26
        CUSTOM_KEY_NOT_PREDEFINED = 27
        CUSTOM_KEY_NOT_SET = 29
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS = 30


__all__ = tuple(sorted(__protobuf__.manifest))
