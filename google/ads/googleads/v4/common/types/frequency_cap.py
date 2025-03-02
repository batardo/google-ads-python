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


from google.ads.googleads.v4.enums.types import frequency_cap_event_type
from google.ads.googleads.v4.enums.types import frequency_cap_level
from google.ads.googleads.v4.enums.types import frequency_cap_time_unit
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.common",
    marshal="google.ads.googleads.v4",
    manifest={"FrequencyCapEntry", "FrequencyCapKey",},
)


class FrequencyCapEntry(proto.Message):
    r"""A rule specifying the maximum number of times an ad (or some
    set of ads) can be shown to a user over a particular time
    period.

    Attributes:
        key (google.ads.googleads.v4.common.types.FrequencyCapKey):
            The key of a particular frequency cap. There
            can be no more than one frequency cap with the
            same key.
        cap (google.protobuf.wrappers_pb2.Int32Value):
            Maximum number of events allowed during the
            time range by this cap.
    """

    key = proto.Field(proto.MESSAGE, number=1, message="FrequencyCapKey",)
    cap = proto.Field(proto.MESSAGE, number=2, message=wrappers.Int32Value,)


class FrequencyCapKey(proto.Message):
    r"""A group of fields used as keys for a frequency cap.
    There can be no more than one frequency cap with the same key.

    Attributes:
        level (google.ads.googleads.v4.enums.types.FrequencyCapLevelEnum.FrequencyCapLevel):
            The level on which the cap is to be applied
            (e.g. ad group ad, ad group). The cap is applied
            to all the entities of this level.
        event_type (google.ads.googleads.v4.enums.types.FrequencyCapEventTypeEnum.FrequencyCapEventType):
            The type of event that the cap applies to
            (e.g. impression).
        time_unit (google.ads.googleads.v4.enums.types.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit):
            Unit of time the cap is defined at (e.g. day,
            week).
        time_length (google.protobuf.wrappers_pb2.Int32Value):
            Number of time units the cap lasts.
    """

    level = proto.Field(
        proto.ENUM,
        number=1,
        enum=frequency_cap_level.FrequencyCapLevelEnum.FrequencyCapLevel,
    )
    event_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=frequency_cap_event_type.FrequencyCapEventTypeEnum.FrequencyCapEventType,
    )
    time_unit = proto.Field(
        proto.ENUM,
        number=2,
        enum=frequency_cap_time_unit.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit,
    )
    time_length = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.Int32Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
