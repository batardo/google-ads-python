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

from collections import OrderedDict
from distutils import util
import os
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.ads.googleads.v4.resources.types import keyword_plan
from google.ads.googleads.v4.services.types import keyword_plan_service
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore

from .transports.base import KeywordPlanServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import KeywordPlanServiceGrpcTransport


class KeywordPlanServiceClientMeta(type):
    """Metaclass for the KeywordPlanService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[KeywordPlanServiceTransport]]
    _transport_registry["grpc"] = KeywordPlanServiceGrpcTransport

    def get_transport_class(
        cls, label: str = None,
    ) -> Type[KeywordPlanServiceTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class KeywordPlanServiceClient(metaclass=KeywordPlanServiceClientMeta):
    """Service to manage keyword plans."""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Convert api endpoint to mTLS endpoint.
        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "googleads.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            KeywordPlanServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(
            info
        )
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            KeywordPlanServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename
        )
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> KeywordPlanServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            KeywordPlanServiceTransport: The transport used by the client instance.
        """
        return self._transport

    @staticmethod
    def keyword_plan_path(customer: str, keyword_plan: str,) -> str:
        """Return a fully-qualified keyword_plan string."""
        return "customers/{customer}/keywordPlans/{keyword_plan}".format(
            customer=customer, keyword_plan=keyword_plan,
        )

    @staticmethod
    def parse_keyword_plan_path(path: str) -> Dict[str, str]:
        """Parse a keyword_plan path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/keywordPlans/(?P<keyword_plan>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Return a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Return a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Return a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Return a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Return a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path
        )
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = None,
        transport: Union[str, KeywordPlanServiceTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the keyword plan service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.KeywordPlanServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(
                os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
            )
        )

        ssl_credentials = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                import grpc  # type: ignore

                cert, key = client_options.client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
                is_mtls = True
            else:
                creds = SslCredentials()
                is_mtls = creds.is_mtls
                ssl_credentials = creds.ssl_credentials if is_mtls else None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                api_endpoint = (
                    self.DEFAULT_MTLS_ENDPOINT
                    if is_mtls
                    else self.DEFAULT_ENDPOINT
                )
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, KeywordPlanServiceTransport):
            # transport is a KeywordPlanServiceTransport instance.
            if credentials:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            self._transport = transport
        elif isinstance(transport, str):
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials, host=self.DEFAULT_ENDPOINT
            )
        else:
            self._transport = KeywordPlanServiceGrpcTransport(
                credentials=credentials,
                host=api_endpoint,
                ssl_channel_credentials=ssl_credentials,
                client_info=client_info,
            )

    def get_keyword_plan(
        self,
        request: keyword_plan_service.GetKeywordPlanRequest = None,
        *,
        resource_name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> keyword_plan.KeywordPlan:
        r"""Returns the requested plan in full detail.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.GetKeywordPlanRequest`):
                The request object. Request message for
                [KeywordPlanService.GetKeywordPlan][google.ads.googleads.v4.services.KeywordPlanService.GetKeywordPlan].
            resource_name (:class:`str`):
                Required. The resource name of the
                plan to fetch.

                This corresponds to the ``resource_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.resources.types.KeywordPlan:
                A Keyword Planner plan.
                Max number of saved keyword plans:
                10000.
                It's possible to remove plans if limit
                is reached.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([resource_name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a keyword_plan_service.GetKeywordPlanRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, keyword_plan_service.GetKeywordPlanRequest):
            request = keyword_plan_service.GetKeywordPlanRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if resource_name is not None:
                request.resource_name = resource_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_keyword_plan]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource_name", request.resource_name),)
            ),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

        # Done; return the response.
        return response

    def mutate_keyword_plans(
        self,
        request: keyword_plan_service.MutateKeywordPlansRequest = None,
        *,
        customer_id: str = None,
        operations: Sequence[keyword_plan_service.KeywordPlanOperation] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> keyword_plan_service.MutateKeywordPlansResponse:
        r"""Creates, updates, or removes keyword plans. Operation
        statuses are returned.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.MutateKeywordPlansRequest`):
                The request object. Request message for
                [KeywordPlanService.MutateKeywordPlans][google.ads.googleads.v4.services.KeywordPlanService.MutateKeywordPlans].
            customer_id (:class:`str`):
                Required. The ID of the customer
                whose keyword plans are being modified.

                This corresponds to the ``customer_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            operations (:class:`Sequence[google.ads.googleads.v4.services.types.KeywordPlanOperation]`):
                Required. The list of operations to
                perform on individual keyword plans.

                This corresponds to the ``operations`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.services.types.MutateKeywordPlansResponse:
                Response message for a keyword plan
                mutate.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([customer_id, operations]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a keyword_plan_service.MutateKeywordPlansRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, keyword_plan_service.MutateKeywordPlansRequest
        ):
            request = keyword_plan_service.MutateKeywordPlansRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if customer_id is not None:
                request.customer_id = customer_id
            if operations is not None:
                request.operations = operations

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.mutate_keyword_plans
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("customer_id", request.customer_id),)
            ),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

        # Done; return the response.
        return response

    def generate_forecast_curve(
        self,
        request: keyword_plan_service.GenerateForecastCurveRequest = None,
        *,
        keyword_plan: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> keyword_plan_service.GenerateForecastCurveResponse:
        r"""Returns the requested Keyword Plan forecast curve.
        Only the bidding strategy is considered for generating
        forecast curve. The bidding strategy value specified in
        the plan is ignored.
        To generate a forecast at a value specified in the plan,
        use KeywordPlanService.GenerateForecastMetrics.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.GenerateForecastCurveRequest`):
                The request object. Request message for
                [KeywordPlanService.GenerateForecastCurve][google.ads.googleads.v4.services.KeywordPlanService.GenerateForecastCurve].
            keyword_plan (:class:`str`):
                Required. The resource name of the
                keyword plan to be forecasted.

                This corresponds to the ``keyword_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.services.types.GenerateForecastCurveResponse:
                Response message for
                [KeywordPlanService.GenerateForecastCurve][google.ads.googleads.v4.services.KeywordPlanService.GenerateForecastCurve].

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([keyword_plan]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a keyword_plan_service.GenerateForecastCurveRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, keyword_plan_service.GenerateForecastCurveRequest
        ):
            request = keyword_plan_service.GenerateForecastCurveRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if keyword_plan is not None:
                request.keyword_plan = keyword_plan

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_forecast_curve
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("keyword_plan", request.keyword_plan),)
            ),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

        # Done; return the response.
        return response

    def generate_forecast_metrics(
        self,
        request: keyword_plan_service.GenerateForecastMetricsRequest = None,
        *,
        keyword_plan: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> keyword_plan_service.GenerateForecastMetricsResponse:
        r"""Returns the requested Keyword Plan forecasts.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.GenerateForecastMetricsRequest`):
                The request object. Request message for
                [KeywordPlanService.GenerateForecastMetrics][google.ads.googleads.v4.services.KeywordPlanService.GenerateForecastMetrics].
            keyword_plan (:class:`str`):
                Required. The resource name of the
                keyword plan to be forecasted.

                This corresponds to the ``keyword_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.services.types.GenerateForecastMetricsResponse:
                Response message for
                [KeywordPlanService.GenerateForecastMetrics][google.ads.googleads.v4.services.KeywordPlanService.GenerateForecastMetrics].

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([keyword_plan]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a keyword_plan_service.GenerateForecastMetricsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, keyword_plan_service.GenerateForecastMetricsRequest
        ):
            request = keyword_plan_service.GenerateForecastMetricsRequest(
                request
            )

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if keyword_plan is not None:
                request.keyword_plan = keyword_plan

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_forecast_metrics
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("keyword_plan", request.keyword_plan),)
            ),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

        # Done; return the response.
        return response

    def generate_historical_metrics(
        self,
        request: keyword_plan_service.GenerateHistoricalMetricsRequest = None,
        *,
        keyword_plan: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> keyword_plan_service.GenerateHistoricalMetricsResponse:
        r"""Returns the requested Keyword Plan historical
        metrics.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.GenerateHistoricalMetricsRequest`):
                The request object. Request message for
                [KeywordPlanService.GenerateHistoricalMetrics][google.ads.googleads.v4.services.KeywordPlanService.GenerateHistoricalMetrics].
            keyword_plan (:class:`str`):
                Required. The resource name of the
                keyword plan of which historical metrics
                are requested.

                This corresponds to the ``keyword_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.services.types.GenerateHistoricalMetricsResponse:
                Response message for
                [KeywordPlanService.GenerateHistoricalMetrics][google.ads.googleads.v4.services.KeywordPlanService.GenerateHistoricalMetrics].

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([keyword_plan]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a keyword_plan_service.GenerateHistoricalMetricsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, keyword_plan_service.GenerateHistoricalMetricsRequest
        ):
            request = keyword_plan_service.GenerateHistoricalMetricsRequest(
                request
            )

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if keyword_plan is not None:
                request.keyword_plan = keyword_plan

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_historical_metrics
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("keyword_plan", request.keyword_plan),)
            ),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

        # Done; return the response.
        return response


__all__ = ("KeywordPlanServiceClient",)
