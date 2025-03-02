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


from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"ThirdPartyAppAnalyticsLink",},
)


class ThirdPartyAppAnalyticsLink(proto.Message):
    r"""A data sharing connection, allowing the import of third party
    app analytics into a Google Ads Customer.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the third party app
            analytics link. Third party app analytics link resource
            names have the form:

            ``customers/{customer_id}/thirdPartyAppAnalyticsLinks/{account_link_id}``
        shareable_link_id (google.protobuf.wrappers_pb2.StringValue):
            Output only. The shareable link ID that
            should be provided to the third party when
            setting up app analytics. This is able to be
            regenerated using regenerate method in the
            ThirdPartyAppAnalyticsLinkService.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    shareable_link_id = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
