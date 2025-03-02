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


from google.ads.googleads.v4.common.types import criteria
from google.ads.googleads.v4.enums.types import (
    bid_modifier_source as gage_bid_modifier_source,
)
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AdGroupBidModifier",},
)


class AdGroupBidModifier(proto.Message):
    r"""Represents an ad group bid modifier.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad group bid modifier.
            Ad group bid modifier resource names have the form:

            ``customers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}``
        ad_group (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The ad group to which this
            criterion belongs.
        criterion_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the criterion to bid
            modify.
            This field is ignored for mutates.
        bid_modifier (google.protobuf.wrappers_pb2.DoubleValue):
            The modifier for the bid when the criterion
            matches. The modifier must be in the range: 0.1
            - 10.0. The range is 1.0 - 6.0 for
            PreferredContent. Use 0 to opt out of a Device
            type.
        base_ad_group (google.protobuf.wrappers_pb2.StringValue):
            Output only. The base ad group from which this draft/trial
            adgroup bid modifier was created. If ad_group is a base ad
            group then this field will be equal to ad_group. If the ad
            group was created in the draft or trial and has no
            corresponding base ad group, then this field will be null.
            This field is readonly.
        bid_modifier_source (google.ads.googleads.v4.enums.types.BidModifierSourceEnum.BidModifierSource):
            Output only. Bid modifier source.
        hotel_date_selection_type (google.ads.googleads.v4.common.types.HotelDateSelectionTypeInfo):
            Immutable. Criterion for hotel date selection
            (default dates vs. user selected).
        hotel_advance_booking_window (google.ads.googleads.v4.common.types.HotelAdvanceBookingWindowInfo):
            Immutable. Criterion for number of days prior
            to the stay the booking is being made.
        hotel_length_of_stay (google.ads.googleads.v4.common.types.HotelLengthOfStayInfo):
            Immutable. Criterion for length of hotel stay
            in nights.
        hotel_check_in_day (google.ads.googleads.v4.common.types.HotelCheckInDayInfo):
            Immutable. Criterion for day of the week the
            booking is for.
        device (google.ads.googleads.v4.common.types.DeviceInfo):
            Immutable. A device criterion.
        preferred_content (google.ads.googleads.v4.common.types.PreferredContentInfo):
            Immutable. A preferred content criterion.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    ad_group = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    criterion_id = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.Int64Value,
    )
    bid_modifier = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.DoubleValue,
    )
    base_ad_group = proto.Field(
        proto.MESSAGE, number=9, message=wrappers.StringValue,
    )
    bid_modifier_source = proto.Field(
        proto.ENUM,
        number=10,
        enum=gage_bid_modifier_source.BidModifierSourceEnum.BidModifierSource,
    )
    hotel_date_selection_type = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="criterion",
        message=criteria.HotelDateSelectionTypeInfo,
    )
    hotel_advance_booking_window = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="criterion",
        message=criteria.HotelAdvanceBookingWindowInfo,
    )
    hotel_length_of_stay = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="criterion",
        message=criteria.HotelLengthOfStayInfo,
    )
    hotel_check_in_day = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="criterion",
        message=criteria.HotelCheckInDayInfo,
    )
    device = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="criterion",
        message=criteria.DeviceInfo,
    )
    preferred_content = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="criterion",
        message=criteria.PreferredContentInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
