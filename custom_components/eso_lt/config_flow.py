from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant import data_entry_flow
from .const import DOMAIN


class EsoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 0
    MINOR_VERSION = 1
    async def async_step_user(self, info):
        # Specify items in the order they are to be displayed in the UI
        data_schema = {
            vol.Required("username"): str,
            vol.Required("password"): str,
            # Items can be grouped by collapsible sections            
        }

        return self.async_show_form(
            step_id="init", data_schema=vol.Schema(data_schema))    