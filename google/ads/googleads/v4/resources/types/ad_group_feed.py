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


from google.ads.googleads.v4.common.types import (
    matching_function as gagc_matching_function,
)
from google.ads.googleads.v4.enums.types import feed_link_status
from google.ads.googleads.v4.enums.types import placeholder_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AdGroupFeed",},
)


class AdGroupFeed(proto.Message):
    r"""An ad group feed.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad group feed. Ad group
            feed resource names have the form:

            \`customers/{customer_id}/adGroupFeeds/{ad_group_id}~{feed_id}
        feed (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The feed being linked to the ad
            group.
        ad_group (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The ad group being linked to the
            feed.
        placeholder_types (Sequence[google.ads.googleads.v4.enums.types.PlaceholderTypeEnum.PlaceholderType]):
            Indicates which placeholder types the feed
            may populate under the connected ad group.
            Required.
        matching_function (google.ads.googleads.v4.common.types.MatchingFunction):
            Matching function associated with the
            AdGroupFeed. The matching function is used to
            filter the set of feed items selected. Required.
        status (google.ads.googleads.v4.enums.types.FeedLinkStatusEnum.FeedLinkStatus):
            Output only. Status of the ad group feed.
            This field is read-only.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    feed = proto.Field(proto.MESSAGE, number=2, message=wrappers.StringValue,)
    ad_group = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    placeholder_types = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=placeholder_type.PlaceholderTypeEnum.PlaceholderType,
    )
    matching_function = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gagc_matching_function.MatchingFunction,
    )
    status = proto.Field(
        proto.ENUM,
        number=6,
        enum=feed_link_status.FeedLinkStatusEnum.FeedLinkStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
