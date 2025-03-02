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
    manifest={"AdGroupAdLabel",},
)


class AdGroupAdLabel(proto.Message):
    r"""A relationship between an ad group ad and a label.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad group ad label. Ad
            group ad label resource names have the form:
            ``customers/{customer_id}/adGroupAdLabels/{ad_group_id}~{ad_id}~{label_id}``
        ad_group_ad (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The ad group ad to which the label
            is attached.
        label (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The label assigned to the ad group
            ad.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    ad_group_ad = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    label = proto.Field(proto.MESSAGE, number=3, message=wrappers.StringValue,)


__all__ = tuple(sorted(__protobuf__.manifest))
