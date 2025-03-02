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


from google.ads.googleads.v4.enums.types import account_budget_proposal_type
from google.ads.googleads.v4.enums.types import account_budget_status
from google.ads.googleads.v4.enums.types import (
    spending_limit_type as gage_spending_limit_type,
)
from google.ads.googleads.v4.enums.types import time_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AccountBudget",},
)


class AccountBudget(proto.Message):
    r"""An account-level budget. It contains information about the budget
    itself, as well as the most recently approved changes to the budget
    and proposed changes that are pending approval. The proposed changes
    that are pending approval, if any, are found in 'pending_proposal'.
    Effective details about the budget are found in fields prefixed
    'approved_', 'adjusted_' and those without a prefix. Since some
    effective details may differ from what the user had originally
    requested (e.g. spending limit), these differences are juxtaposed
    via 'proposed_', 'approved_', and possibly 'adjusted_' fields.

    This resource is mutated using AccountBudgetProposal and cannot be
    mutated directly. A budget may have at most one pending proposal at
    any given time. It is read through pending_proposal.

    Once approved, a budget may be subject to adjustments, such as
    credit adjustments. Adjustments create differences between the
    'approved' and 'adjusted' fields, which would otherwise be
    identical.

    Attributes:
        resource_name (str):
            Output only. The resource name of the account-level budget.
            AccountBudget resource names have the form:

            ``customers/{customer_id}/accountBudgets/{account_budget_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the account-level
            budget.
        billing_setup (google.protobuf.wrappers_pb2.StringValue):
            Output only. The resource name of the billing setup
            associated with this account-level budget. BillingSetup
            resource names have the form:

            ``customers/{customer_id}/billingSetups/{billing_setup_id}``
        status (google.ads.googleads.v4.enums.types.AccountBudgetStatusEnum.AccountBudgetStatus):
            Output only. The status of this account-level
            budget.
        name (google.protobuf.wrappers_pb2.StringValue):
            Output only. The name of the account-level
            budget.
        proposed_start_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The proposed start time of the
            account-level budget in yyyy-MM-dd HH:mm:ss
            format.  If a start time type of NOW was
            proposed, this is the time of request.
        approved_start_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The approved start time of the
            account-level budget in yyyy-MM-dd HH:mm:ss
            format.
            For example, if a new budget is approved after
            the proposed start time, the approved start time
            is the time of approval.
        total_adjustments_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The total adjustments amount.
            An example of an adjustment is courtesy credits.
        amount_served_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The value of Ads that have been served, in
            micros.

            This includes overdelivery costs, in which case a credit
            might be automatically applied to the budget (see
            total_adjustments_micros).
        purchase_order_number (google.protobuf.wrappers_pb2.StringValue):
            Output only. A purchase order number is a
            value that helps users reference this budget in
            their monthly invoices.
        notes (google.protobuf.wrappers_pb2.StringValue):
            Output only. Notes associated with the
            budget.
        pending_proposal (google.ads.googleads.v4.resources.types.AccountBudget.PendingAccountBudgetProposal):
            Output only. The pending proposal to modify
            this budget, if applicable.
        proposed_end_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The proposed end time in yyyy-
            M-dd HH:mm:ss format.
        proposed_end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Output only. The proposed end time as a well-
            efined type, e.g. FOREVER.
        approved_end_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The approved end time in yyyy-
            M-dd HH:mm:ss format.
        approved_end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Output only. The approved end time as a well-
            efined type, e.g. FOREVER.
        proposed_spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The proposed spending limit in
            micros.  One million is equivalent to one unit.
        proposed_spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
            Output only. The proposed spending limit as a
            well-defined type, e.g. INFINITE.
        approved_spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The approved spending limit in
            micros.  One million is equivalent to one unit.
            This will only be populated if the proposed
            spending limit is finite, and will always be
            greater than or equal to the proposed spending
            limit.
        approved_spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
            Output only. The approved spending limit as a
            well-defined type, e.g. INFINITE.  This will
            only be populated if the approved spending limit
            is INFINITE.
        adjusted_spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The adjusted spending limit in
            micros.  One million is equivalent to one unit.
            If the approved spending limit is finite, the
            adjusted spending limit may vary depending on
            the types of adjustments applied to this budget,
            if applicable.

            The different kinds of adjustments are described
            here: https://support.google.com/google-
            ads/answer/1704323
            For example, a debit adjustment reduces how much
            the account is allowed to spend.
        adjusted_spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
            Output only. The adjusted spending limit as a
            well-defined type, e.g. INFINITE. This will only
            be populated if the adjusted spending limit is
            INFINITE, which is guaranteed to be true if the
            approved spending limit is INFINITE.
    """

    class PendingAccountBudgetProposal(proto.Message):
        r"""A pending proposal associated with the enclosing account-
        evel budget, if applicable.

        Attributes:
            account_budget_proposal (google.protobuf.wrappers_pb2.StringValue):
                Output only. The resource name of the proposal.
                AccountBudgetProposal resource names have the form:

                ``customers/{customer_id}/accountBudgetProposals/{account_budget_proposal_id}``
            proposal_type (google.ads.googleads.v4.enums.types.AccountBudgetProposalTypeEnum.AccountBudgetProposalType):
                Output only. The type of this proposal, e.g.
                END to end the budget associated with this
                proposal.
            name (google.protobuf.wrappers_pb2.StringValue):
                Output only. The name to assign to the
                account-level budget.
            start_date_time (google.protobuf.wrappers_pb2.StringValue):
                Output only. The start time in yyyy-MM-dd
                HH:mm:ss format.
            purchase_order_number (google.protobuf.wrappers_pb2.StringValue):
                Output only. A purchase order number is a
                value that helps users reference this budget in
                their monthly invoices.
            notes (google.protobuf.wrappers_pb2.StringValue):
                Output only. Notes associated with this
                budget.
            creation_date_time (google.protobuf.wrappers_pb2.StringValue):
                Output only. The time when this account-level
                budget proposal was created. Formatted as yyyy-
                MM-dd HH:mm:ss.
            end_date_time (google.protobuf.wrappers_pb2.StringValue):
                Output only. The end time in yyyy-MM-dd
                HH:mm:ss format.
            end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
                Output only. The end time as a well-defined
                type, e.g. FOREVER.
            spending_limit_micros (google.protobuf.wrappers_pb2.Int64Value):
                Output only. The spending limit in micros.
                One million is equivalent to one unit.
            spending_limit_type (google.ads.googleads.v4.enums.types.SpendingLimitTypeEnum.SpendingLimitType):
                Output only. The spending limit as a well-
                efined type, e.g. INFINITE.
        """

        account_budget_proposal = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )
        proposal_type = proto.Field(
            proto.ENUM,
            number=2,
            enum=account_budget_proposal_type.AccountBudgetProposalTypeEnum.AccountBudgetProposalType,
        )
        name = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.StringValue,
        )
        start_date_time = proto.Field(
            proto.MESSAGE, number=4, message=wrappers.StringValue,
        )
        purchase_order_number = proto.Field(
            proto.MESSAGE, number=9, message=wrappers.StringValue,
        )
        notes = proto.Field(
            proto.MESSAGE, number=10, message=wrappers.StringValue,
        )
        creation_date_time = proto.Field(
            proto.MESSAGE, number=11, message=wrappers.StringValue,
        )
        end_date_time = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="end_time",
            message=wrappers.StringValue,
        )
        end_time_type = proto.Field(
            proto.ENUM,
            number=6,
            oneof="end_time",
            enum=time_type.TimeTypeEnum.TimeType,
        )
        spending_limit_micros = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="spending_limit",
            message=wrappers.Int64Value,
        )
        spending_limit_type = proto.Field(
            proto.ENUM,
            number=8,
            oneof="spending_limit",
            enum=gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
        )

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.MESSAGE, number=2, message=wrappers.Int64Value,)
    billing_setup = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    status = proto.Field(
        proto.ENUM,
        number=4,
        enum=account_budget_status.AccountBudgetStatusEnum.AccountBudgetStatus,
    )
    name = proto.Field(proto.MESSAGE, number=5, message=wrappers.StringValue,)
    proposed_start_date_time = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    approved_start_date_time = proto.Field(
        proto.MESSAGE, number=7, message=wrappers.StringValue,
    )
    total_adjustments_micros = proto.Field(
        proto.MESSAGE, number=18, message=wrappers.Int64Value,
    )
    amount_served_micros = proto.Field(
        proto.MESSAGE, number=19, message=wrappers.Int64Value,
    )
    purchase_order_number = proto.Field(
        proto.MESSAGE, number=20, message=wrappers.StringValue,
    )
    notes = proto.Field(proto.MESSAGE, number=21, message=wrappers.StringValue,)
    pending_proposal = proto.Field(
        proto.MESSAGE, number=22, message=PendingAccountBudgetProposal,
    )
    proposed_end_date_time = proto.Field(
        proto.MESSAGE,
        number=8,
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
        number=10,
        oneof="approved_end_time",
        message=wrappers.StringValue,
    )
    approved_end_time_type = proto.Field(
        proto.ENUM,
        number=11,
        oneof="approved_end_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )
    proposed_spending_limit_micros = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="proposed_spending_limit",
        message=wrappers.Int64Value,
    )
    proposed_spending_limit_type = proto.Field(
        proto.ENUM,
        number=13,
        oneof="proposed_spending_limit",
        enum=gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
    )
    approved_spending_limit_micros = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="approved_spending_limit",
        message=wrappers.Int64Value,
    )
    approved_spending_limit_type = proto.Field(
        proto.ENUM,
        number=15,
        oneof="approved_spending_limit",
        enum=gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
    )
    adjusted_spending_limit_micros = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="adjusted_spending_limit",
        message=wrappers.Int64Value,
    )
    adjusted_spending_limit_type = proto.Field(
        proto.ENUM,
        number=17,
        oneof="adjusted_spending_limit",
        enum=gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
