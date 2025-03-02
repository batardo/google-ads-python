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


from google.ads.googleads.v4.common.types import offline_user_data
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "UploadUserDataRequest",
        "UserDataOperation",
        "UploadUserDataResponse",
    },
)


class UploadUserDataRequest(proto.Message):
    r"""Request message for
    [UserDataService.UploadUserData][google.ads.googleads.v4.services.UserDataService.UploadUserData]

    Attributes:
        customer_id (str):
            Required. The ID of the customer for which to
            update the user data.
        operations (Sequence[google.ads.googleads.v4.services.types.UserDataOperation]):
            Required. The list of operations to be done.
        customer_match_user_list_metadata (google.ads.googleads.v4.common.types.CustomerMatchUserListMetadata):
            Metadata for data updates to a Customer Match
            user list.
    """

    customer_id = proto.Field(proto.STRING, number=1)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=3, message="UserDataOperation",
    )
    customer_match_user_list_metadata = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="metadata",
        message=offline_user_data.CustomerMatchUserListMetadata,
    )


class UserDataOperation(proto.Message):
    r"""Operation to be made for the UploadUserDataRequest.

    Attributes:
        create (google.ads.googleads.v4.common.types.UserData):
            The list of user data to be appended to the
            user list.
        remove (google.ads.googleads.v4.common.types.UserData):
            The list of user data to be removed from the
            user list.
    """

    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=offline_user_data.UserData,
    )
    remove = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=offline_user_data.UserData,
    )


class UploadUserDataResponse(proto.Message):
    r"""Response message for
    [UserDataService.UploadUserData][google.ads.googleads.v4.services.UserDataService.UploadUserData]

    Attributes:
        upload_date_time (google.protobuf.wrappers_pb2.StringValue):
            The date time at which the request was received by API,
            formatted as "yyyy-mm-dd hh:mm:ss+|-hh:mm", e.g. "2019-01-01
            12:32:45-08:00".
        received_operations_count (google.protobuf.wrappers_pb2.Int32Value):
            Number of upload data operations received by
            API.
    """

    upload_date_time = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    received_operations_count = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.Int32Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
