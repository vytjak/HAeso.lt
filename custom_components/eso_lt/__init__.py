"""
Lithuanian energy grid operator eso.lt integration for Home Assistant.
"""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_loaded_integration

from .const import DOMAIN, LOGGER
# from .api_client import EsoLtApiClient
# from .coordinator import EsoLtDataUpdateCoordinator
from .data import EsoLtConfigEntry#, EsoLtData

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    # from .data import EsoLtConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SENSOR    
]

# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: EsoLtConfigEntry,
) -> bool:    
    """Set up this integration using UI."""

    #!!!
    # coordinator = EsoLtDataUpdateCoordinator(
    #     hass=hass,
    #     logger=LOGGER,
    #     name=DOMAIN,
    #     update_interval=timedelta(hours=1),
    # )
    # entry.runtime_data = EsoLtData(
    #     client=EsoLtApiClient(
    #         username=entry.data[CONF_USERNAME],
    #         password=entry.data[CONF_PASSWORD],
    #         session=async_get_clientsession(hass),
    #     ),
    #     integration=async_get_loaded_integration(hass, entry.domain),
    #     coordinator=coordinator,
    # )

    # # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    # await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    # entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: EsoLtConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: EsoLtConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)