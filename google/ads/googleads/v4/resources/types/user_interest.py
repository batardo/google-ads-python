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


from google.ads.googleads.v4.common.types import criterion_category_availability
from google.ads.googleads.v4.enums.types import user_interest_taxonomy_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"UserInterest",},
)


class UserInterest(proto.Message):
    r"""A user interest: a particular interest-based vertical to be
    targeted.

    Attributes:
        resource_name (str):
            Output only. The resource name of the user interest. User
            interest resource names have the form:

            ``customers/{customer_id}/userInterests/{user_interest_id}``
        taxonomy_type (google.ads.googleads.v4.enums.types.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType):
            Output only. Taxonomy type of the user
            interest.
        user_interest_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the user interest.
        name (google.protobuf.wrappers_pb2.StringValue):
            Output only. The name of the user interest.
        user_interest_parent (google.protobuf.wrappers_pb2.StringValue):
            Output only. The parent of the user interest.
        launched_to_all (google.protobuf.wrappers_pb2.BoolValue):
            Output only. True if the user interest is
            launched to all channels and locales.
        availabilities (Sequence[google.ads.googleads.v4.common.types.CriterionCategoryAvailability]):
            Output only. Availability information of the
            user interest.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    taxonomy_type = proto.Field(
        proto.ENUM,
        number=2,
        enum=user_interest_taxonomy_type.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType,
    )
    user_interest_id = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.Int64Value,
    )
    name = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)
    user_interest_parent = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    launched_to_all = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.BoolValue,
    )
    availabilities = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=criterion_category_availability.CriterionCategoryAvailability,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
