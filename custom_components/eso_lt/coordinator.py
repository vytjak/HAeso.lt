
from __future__ import annotations

from typing import TYPE_CHECKING, Any
import voluptuous as vol

from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api_client import (
    EsoLtApiClientAuthenticationError,
    EsoLtApiClientError,
)

# if TYPE_CHECKING:
from .data import EsoLtConfigEntry

OBJECT_INFO_SCHEMA = vol.Schema(
    {
        vol.Required("object_id"): str,
        vol.Required("object_name"): str,
        vol.Required("object_address"): str,
        vol.Required("meters_qty"): int,
        vol.Required("retrieve_consumption", default=True): bool,
        vol.Required("retrieve_generation", default=False): bool,
    }
)

# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class EsoLtDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: EsoLtConfigEntry
    
#     async def _async_update_data(self) -> Any:
#         """Update data via library."""
#         try:
#             return await self.config_entry.runtime_data.client.async_get_data()
#         except EsoLtApiClientAuthenticationError as exception:
#             raise ConfigEntryAuthFailed(exception) from exception
#         except EsoLtApiClientError as exception:
#              raise UpdateFailed(exception) from exception
    