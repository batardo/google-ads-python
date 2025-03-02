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


from google.ads.googleads.v4.common.types import simulation
from google.ads.googleads.v4.enums.types import simulation_modification_method
from google.ads.googleads.v4.enums.types import simulation_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AdGroupSimulation",},
)


class AdGroupSimulation(proto.Message):
    r"""An ad group simulation. Supported combinations of advertising
    channel type, simulation type and simulation modification method is
    detailed below respectively.

    1. SEARCH - CPC_BID - DEFAULT
    2. SEARCH - CPC_BID - UNIFORM
    3. SEARCH - TARGET_CPA - UNIFORM
    4. SEARCH - TARGET_ROAS - UNIFORM
    5. DISPLAY - CPC_BID - DEFAULT
    6. DISPLAY - CPC_BID - UNIFORM
    7. DISPLAY - TARGET_CPA - UNIFORM
    8. VIDEO - CPV_BID - DEFAULT
    9. VIDEO - CPV_BID - UNIFORM

    Attributes:
        resource_name (str):
            Output only. The resource name of the ad group simulation.
            Ad group simulation resource names have the form:

            ``customers/{customer_id}/adGroupSimulations/{ad_group_id}~{type}~{modification_method}~{start_date}~{end_date}``
        ad_group_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. Ad group id of the simulation.
        type_ (google.ads.googleads.v4.enums.types.SimulationTypeEnum.SimulationType):
            Output only. The field that the simulation
            modifies.
        modification_method (google.ads.googleads.v4.enums.types.SimulationModificationMethodEnum.SimulationModificationMethod):
            Output only. How the simulation modifies the
            field.
        start_date (google.protobuf.wrappers_pb2.StringValue):
            Output only. First day on which the
            simulation is based, in YYYY-MM-DD format.
        end_date (google.protobuf.wrappers_pb2.StringValue):
            Output only. Last day on which the simulation
            is based, in YYYY-MM-DD format
        cpc_bid_point_list (google.ads.googleads.v4.common.types.CpcBidSimulationPointList):
            Output only. Simulation points if the simulation type is
            CPC_BID.
        cpv_bid_point_list (google.ads.googleads.v4.common.types.CpvBidSimulationPointList):
            Output only. Simulation points if the simulation type is
            CPV_BID.
        target_cpa_point_list (google.ads.googleads.v4.common.types.TargetCpaSimulationPointList):
            Output only. Simulation points if the simulation type is
            TARGET_CPA.
        target_roas_point_list (google.ads.googleads.v4.common.types.TargetRoasSimulationPointList):
            Output only. Simulation points if the simulation type is
            TARGET_ROAS.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    ad_group_id = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.Int64Value,
    )
    type_ = proto.Field(
        proto.ENUM,
        number=3,
        enum=simulation_type.SimulationTypeEnum.SimulationType,
    )
    modification_method = proto.Field(
        proto.ENUM,
        number=4,
        enum=simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod,
    )
    start_date = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    end_date = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    cpc_bid_point_list = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="point_list",
        message=simulation.CpcBidSimulationPointList,
    )
    cpv_bid_point_list = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="point_list",
        message=simulation.CpvBidSimulationPointList,
    )
    target_cpa_point_list = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="point_list",
        message=simulation.TargetCpaSimulationPointList,
    )
    target_roas_point_list = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="point_list",
        message=simulation.TargetRoasSimulationPointList,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
