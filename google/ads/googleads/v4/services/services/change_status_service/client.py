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

from google.ads.googleads.v4.resources.types import change_status
from google.ads.googleads.v4.services.types import change_status_service
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore

from .transports.base import ChangeStatusServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import ChangeStatusServiceGrpcTransport


class ChangeStatusServiceClientMeta(type):
    """Metaclass for the ChangeStatusService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[ChangeStatusServiceTransport]]
    _transport_registry["grpc"] = ChangeStatusServiceGrpcTransport

    def get_transport_class(
        cls, label: str = None,
    ) -> Type[ChangeStatusServiceTransport]:
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


class ChangeStatusServiceClient(metaclass=ChangeStatusServiceClientMeta):
    """Service to fetch change statuses."""

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
            ChangeStatusServiceClient: The constructed client.
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
            ChangeStatusServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename
        )
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ChangeStatusServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            ChangeStatusServiceTransport: The transport used by the client instance.
        """
        return self._transport

    @staticmethod
    def ad_group_path(customer: str, ad_group: str,) -> str:
        """Return a fully-qualified ad_group string."""
        return "customers/{customer}/adGroups/{ad_group}".format(
            customer=customer, ad_group=ad_group,
        )

    @staticmethod
    def parse_ad_group_path(path: str) -> Dict[str, str]:
        """Parse a ad_group path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/adGroups/(?P<ad_group>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ad_group_ad_path(customer: str, ad_group_ad: str,) -> str:
        """Return a fully-qualified ad_group_ad string."""
        return "customers/{customer}/adGroupAds/{ad_group_ad}".format(
            customer=customer, ad_group_ad=ad_group_ad,
        )

    @staticmethod
    def parse_ad_group_ad_path(path: str) -> Dict[str, str]:
        """Parse a ad_group_ad path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/adGroupAds/(?P<ad_group_ad>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ad_group_bid_modifier_path(
        customer: str, ad_group_bid_modifier: str,
    ) -> str:
        """Return a fully-qualified ad_group_bid_modifier string."""
        return "customers/{customer}/adGroupBidModifiers/{ad_group_bid_modifier}".format(
            customer=customer, ad_group_bid_modifier=ad_group_bid_modifier,
        )

    @staticmethod
    def parse_ad_group_bid_modifier_path(path: str) -> Dict[str, str]:
        """Parse a ad_group_bid_modifier path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/adGroupBidModifiers/(?P<ad_group_bid_modifier>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ad_group_criterion_path(customer: str, ad_group_criterion: str,) -> str:
        """Return a fully-qualified ad_group_criterion string."""
        return "customers/{customer}/adGroupCriteria/{ad_group_criterion}".format(
            customer=customer, ad_group_criterion=ad_group_criterion,
        )

    @staticmethod
    def parse_ad_group_criterion_path(path: str) -> Dict[str, str]:
        """Parse a ad_group_criterion path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/adGroupCriteria/(?P<ad_group_criterion>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ad_group_feed_path(customer: str, ad_group_feed: str,) -> str:
        """Return a fully-qualified ad_group_feed string."""
        return "customers/{customer}/adGroupFeeds/{ad_group_feed}".format(
            customer=customer, ad_group_feed=ad_group_feed,
        )

    @staticmethod
    def parse_ad_group_feed_path(path: str) -> Dict[str, str]:
        """Parse a ad_group_feed path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/adGroupFeeds/(?P<ad_group_feed>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def campaign_path(customer: str, campaign: str,) -> str:
        """Return a fully-qualified campaign string."""
        return "customers/{customer}/campaigns/{campaign}".format(
            customer=customer, campaign=campaign,
        )

    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]:
        """Parse a campaign path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/campaigns/(?P<campaign>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def campaign_criterion_path(customer: str, campaign_criterion: str,) -> str:
        """Return a fully-qualified campaign_criterion string."""
        return "customers/{customer}/campaignCriteria/{campaign_criterion}".format(
            customer=customer, campaign_criterion=campaign_criterion,
        )

    @staticmethod
    def parse_campaign_criterion_path(path: str) -> Dict[str, str]:
        """Parse a campaign_criterion path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/campaignCriteria/(?P<campaign_criterion>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def campaign_feed_path(customer: str, campaign_feed: str,) -> str:
        """Return a fully-qualified campaign_feed string."""
        return "customers/{customer}/campaignFeeds/{campaign_feed}".format(
            customer=customer, campaign_feed=campaign_feed,
        )

    @staticmethod
    def parse_campaign_feed_path(path: str) -> Dict[str, str]:
        """Parse a campaign_feed path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/campaignFeeds/(?P<campaign_feed>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def change_status_path(customer: str, change_status: str,) -> str:
        """Return a fully-qualified change_status string."""
        return "customers/{customer}/changeStatus/{change_status}".format(
            customer=customer, change_status=change_status,
        )

    @staticmethod
    def parse_change_status_path(path: str) -> Dict[str, str]:
        """Parse a change_status path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/changeStatus/(?P<change_status>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def feed_path(customer: str, feed: str,) -> str:
        """Return a fully-qualified feed string."""
        return "customers/{customer}/feeds/{feed}".format(
            customer=customer, feed=feed,
        )

    @staticmethod
    def parse_feed_path(path: str) -> Dict[str, str]:
        """Parse a feed path into its component segments."""
        m = re.match(r"^customers/(?P<customer>.+?)/feeds/(?P<feed>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def feed_item_path(customer: str, feed_item: str,) -> str:
        """Return a fully-qualified feed_item string."""
        return "customers/{customer}/feedItems/{feed_item}".format(
            customer=customer, feed_item=feed_item,
        )

    @staticmethod
    def parse_feed_item_path(path: str) -> Dict[str, str]:
        """Parse a feed_item path into its component segments."""
        m = re.match(
            r"^customers/(?P<customer>.+?)/feedItems/(?P<feed_item>.+?)$", path
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
        transport: Union[str, ChangeStatusServiceTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the change status service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ChangeStatusServiceTransport]): The
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
        if isinstance(transport, ChangeStatusServiceTransport):
            # transport is a ChangeStatusServiceTransport instance.
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
            self._transport = ChangeStatusServiceGrpcTransport(
                credentials=credentials,
                host=api_endpoint,
                ssl_channel_credentials=ssl_credentials,
                client_info=client_info,
            )

    def get_change_status(
        self,
        request: change_status_service.GetChangeStatusRequest = None,
        *,
        resource_name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> change_status.ChangeStatus:
        r"""Returns the requested change status in full detail.

        Args:
            request (:class:`google.ads.googleads.v4.services.types.GetChangeStatusRequest`):
                The request object. Request message for
                '[ChangeStatusService.GetChangeStatus][google.ads.googleads.v4.services.ChangeStatusService.GetChangeStatus]'.
            resource_name (:class:`str`):
                Required. The resource name of the
                change status to fetch.

                This corresponds to the ``resource_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ads.googleads.v4.resources.types.ChangeStatus:
                Describes the status of returned
                resource. ChangeStatus could have up to
                3 minutes delay to reflect a new change.

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
        # in a change_status_service.GetChangeStatusRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, change_status_service.GetChangeStatusRequest
        ):
            request = change_status_service.GetChangeStatusRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if resource_name is not None:
                request.resource_name = resource_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_change_status
        ]

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


__all__ = ("ChangeStatusServiceClient",)
