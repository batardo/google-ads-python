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
    package="google.ads.googleads.v4.enums",
    marshal="google.ads.googleads.v4",
    manifest={"FeedMappingCriterionTypeEnum",},
)


class FeedMappingCriterionTypeEnum(proto.Message):
    r"""Container for enum describing possible criterion types for a
    feed mapping.
    """

    class FeedMappingCriterionType(proto.Enum):
        r"""Possible placeholder types for a feed mapping."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_EXTENSION_TARGETING = 4
        DSA_PAGE_FEED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
