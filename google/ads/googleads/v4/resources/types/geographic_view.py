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


from google.ads.googleads.v4.enums.types import geo_targeting_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"GeographicView",},
)


class GeographicView(proto.Message):
    r"""A geographic view.
    Geographic View includes all metrics aggregated at the country
    level, one row per country. It reports metrics at either actual
    physical location of the user or an area of interest. If other
    segment fields are used, you may get more than one row per
    country.

    Attributes:
        resource_name (str):
            Output only. The resource name of the geographic view.
            Geographic view resource names have the form:

            ``customers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}``
        location_type (google.ads.googleads.v4.enums.types.GeoTargetingTypeEnum.GeoTargetingType):
            Output only. Type of the geo targeting of the
            campaign.
        country_criterion_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. Criterion Id for the country.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    location_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=geo_targeting_type.GeoTargetingTypeEnum.GeoTargetingType,
    )
    country_criterion_id = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.Int64Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
