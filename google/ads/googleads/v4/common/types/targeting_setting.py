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


from google.ads.googleads.v4.enums.types import (
    targeting_dimension as gage_targeting_dimension,
)
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.common",
    marshal="google.ads.googleads.v4",
    manifest={
        "TargetingSetting",
        "TargetRestriction",
        "TargetRestrictionOperation",
    },
)


class TargetingSetting(proto.Message):
    r"""Settings for the targeting-related features, at the campaign
    and ad group levels. For more details about the targeting
    setting, visit https://support.google.com/google-
    ads/answer/7365594

    Attributes:
        target_restrictions (Sequence[google.ads.googleads.v4.common.types.TargetRestriction]):
            The per-targeting-dimension setting to
            restrict the reach of your campaign or ad group.
        target_restriction_operations (Sequence[google.ads.googleads.v4.common.types.TargetRestrictionOperation]):
            The list of operations changing the target
            restrictions.
            Adding a target restriction with a targeting
            dimension that already exists causes the
            existing target restriction to be replaced with
            the new value.
    """

    target_restrictions = proto.RepeatedField(
        proto.MESSAGE, number=1, message="TargetRestriction",
    )
    target_restriction_operations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="TargetRestrictionOperation",
    )


class TargetRestriction(proto.Message):
    r"""The list of per-targeting-dimension targeting settings.

    Attributes:
        targeting_dimension (google.ads.googleads.v4.enums.types.TargetingDimensionEnum.TargetingDimension):
            The targeting dimension that these settings
            apply to.
        bid_only (google.protobuf.wrappers_pb2.BoolValue):
            Indicates whether to restrict your ads to show only for the
            criteria you have selected for this targeting_dimension, or
            to target all values for this targeting_dimension and show
            ads based on your targeting in other TargetingDimensions. A
            value of ``true`` means that these criteria will only apply
            bid modifiers, and not affect targeting. A value of
            ``false`` means that these criteria will restrict targeting
            as well as applying bid modifiers.
    """

    targeting_dimension = proto.Field(
        proto.ENUM,
        number=1,
        enum=gage_targeting_dimension.TargetingDimensionEnum.TargetingDimension,
    )
    bid_only = proto.Field(proto.MESSAGE, number=2, message=wrappers.BoolValue,)


class TargetRestrictionOperation(proto.Message):
    r"""Operation to be performed on a target restriction list in a
    mutate.

    Attributes:
        operator (google.ads.googleads.v4.common.types.TargetRestrictionOperation.Operator):
            Type of list operation to perform.
        value (google.ads.googleads.v4.common.types.TargetRestriction):
            The target restriction being added to or
            removed from the list.
    """

    class Operator(proto.Enum):
        r"""The operator."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
        REMOVE = 3

    operator = proto.Field(proto.ENUM, number=1, enum=Operator,)
    value = proto.Field(proto.MESSAGE, number=2, message="TargetRestriction",)


__all__ = tuple(sorted(__protobuf__.manifest))
