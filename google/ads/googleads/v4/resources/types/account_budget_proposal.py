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


from google.ads.googleads.v4.enums.types import account_budget_proposal_status
from google.ads.googleads.v4.enums.types import account_budget_proposal_type
from google.ads.googleads.v4.enums.types import spending_limit_type
from google.ads.googleads.v4.enums.types import time_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AccountBudgetProposal",},
)


class AccountBudgetProposal(proto.Message):
    r"""An account-level budget proposal.

    All fields prefixed with 'proposed' may not necessarily be applied
    directly. For example, proposed spending limits may be adjusted
    before their application. This is true if the 'proposed' field has
    an 'approved' counterpart, e.g. spending limits.

    Please note that the proposal type (proposal_type) changes which
    fields are required and which must remain empty.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the proposal.
            AccountBudgetProposal resource names have the form:

            ``customers/{customer_id}/accountBudgetProposals/{account_budget_proposal_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the proposal.
        billing_setup (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The resource name of the billing
            setup associated with this proposal.
        account_budget (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The resource name of the account-
            evel budget associated with this proposal.
        proposal_type (google.ads.googleads.v4.enums.types.AccountBudgetProposalTypeEnum.AccountBudgetProposalType):
            Immutable. The type of this proposal, e.g.
            END to end the budget associated with this
            proposal.
        status (google.ads.googleads.v4.enums.types.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus):
            Output only. The status of this proposal.
            When a new proposal is created, the status
            defaults to PENDING.
        proposed_name (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The name to assign to the account-
            evel budget.
        approved_start_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The approved start date time in
            yyyy-mm-dd hh:mm:ss format.
        proposed_purchase_order_number (google.protobuf.wrappers_pb2.StringValue):
            Immutable. A purchase order number is a value
            that enables the user to help them reference
            this budget in their monthly invoices.
        proposed_notes (google.protobuf.wrappers_pb2.StringValue):
            Immutable. Notes associated with this budget.
        creation_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The date time when this account-
            evel budget proposal was created, which is not
            the same as its approval date time, if
            applicable.
        approval_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The date time when this account-
            evel budget was approved, if applicable.
        proposed_start_date_time (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The proposed start date time in
            yyyy-mm-dd hh:mm:ss format.
        proposed_start_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Immutable. The proposed start date time as a
            well-defined type, e.g. NOW.
        proposed_end_date_time (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The proposed end date time in
            yyyy-mm-dd hh:mm:ss format.
        proposed_end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Immutable. The proposed end date time as a
            well-defined type, e.g. FOREVER.
        approved_end_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The approved end date time in
            yyyy-mm-dd hh:mm:ss format.
        approved_end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Output only. The approved end date time as a
            well-defined type, e.g. FOREVER.
        proposed_spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
            Immutable. The proposed spending limit in
            micros.  One million is equivalent to one unit.
        proposed_spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
            Immutable. The proposed spending limit as a
            well-defined type, e.g. INFINITE.
        approved_spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The approved spending limit in
            micros.  One million is equivalent to one unit.
        approved_spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
            Output only. The approved spending limit as a
            well-defined type, e.g. INFINITE.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.MESSAGE, number=14, message=wrappers.Int64Value,)
    billing_setup = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    account_budget = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    proposal_type = proto.Field(
        proto.ENUM,
        number=4,
        enum=account_budget_proposal_type.AccountBudgetProposalTypeEnum.AccountBudgetProposalType,
    )
    status = proto.Field(
        proto.ENUM,
        number=15,
        enum=account_budget_proposal_status.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus,
    )
    proposed_name = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    approved_start_date_time = proto.Field(
        proto.MESSAGE, number=20, message=wrappers.StringValue,
    )
    proposed_purchase_order_number = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.StringValue,
    )
    proposed_notes = proto.Field(
        proto.MESSAGE, number=13, message=wrappers.StringValue,
    )
    creation_date_time = proto.Field(
        proto.MESSAGE, number=16, message=wrappers.StringValue,
    )
    approval_date_time = proto.Field(
        proto.MESSAGE, number=17, message=wrappers.StringValue,
    )
    proposed_start_date_time = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="proposed_start_time",
        message=wrappers.StringValue,
    )
    proposed_start_time_type = proto.Field(
        proto.ENUM,
        number=7,
        oneof="proposed_start_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )
    proposed_end_date_time = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="proposed_end_time",
        message=wrappers.StringValue,
    )
    proposed_end_time_type = proto.Field(
        proto.ENUM,
        number=9,
        oneof="proposed_end_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )
    approved_end_date_time = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="approved_end_time",
        message=wrappers.StringValue,
    )
    approved_end_time_type = proto.Field(
        proto.ENUM,
        number=22,
        oneof="approved_end_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )
    proposed_spending_limit_micros = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="proposed_spending_limit",
        message=wrappers.Int64Value,
    )
    proposed_spending_limit_type = proto.Field(
        proto.ENUM,
        number=11,
        oneof="proposed_spending_limit",
        enum=spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
    )
    approved_spending_limit_micros = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="approved_spending_limit",
        message=wrappers.Int64Value,
    )
    approved_spending_limit_type = proto.Field(
        proto.ENUM,
        number=24,
        oneof="approved_spending_limit",
        enum=spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
