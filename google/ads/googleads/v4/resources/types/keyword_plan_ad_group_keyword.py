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


from google.ads.googleads.v4.enums.types import keyword_match_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"KeywordPlanAdGroupKeyword",},
)


class KeywordPlanAdGroupKeyword(proto.Message):
    r"""A Keyword Plan ad group keyword.
    Max number of keyword plan keywords per plan: 10000.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the Keyword Plan ad group
            keyword. KeywordPlanAdGroupKeyword resource names have the
            form:

            ``customers/{customer_id}/keywordPlanAdGroupKeywords/{kp_ad_group_keyword_id}``
        keyword_plan_ad_group (google.protobuf.wrappers_pb2.StringValue):
            The Keyword Plan ad group to which this
            keyword belongs.
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the Keyword Plan
            keyword.
        text (google.protobuf.wrappers_pb2.StringValue):
            The keyword text.
        match_type (google.ads.googleads.v4.enums.types.KeywordMatchTypeEnum.KeywordMatchType):
            The keyword match type.
        cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            A keyword level max cpc bid in micros (e.g.
            $1 = 1mm). The currency is the same as the
            account currency code. This will override any
            CPC bid set at the keyword plan ad group level.
            Not applicable for negative keywords. (negative
            = true) This field is Optional.
        negative (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. If true, the keyword is negative.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    keyword_plan_ad_group = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    id = proto.Field(proto.MESSAGE, number=3, message=wrappers.Int64Value,)
    text = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)
    match_type = proto.Field(
        proto.ENUM,
        number=5,
        enum=keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType,
    )
    cpc_bid_micros = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.Int64Value,
    )
    negative = proto.Field(proto.MESSAGE, number=7, message=wrappers.BoolValue,)


__all__ = tuple(sorted(__protobuf__.manifest))
