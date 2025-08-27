from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant import data_entry_flow
from .const import DOMAIN, DEFAULT_API_URL
from .api_client import EsoLtApiClient

API_SETUP_SCHEMA = {
    # Specify items in the order they are to be displayed in the UI
    vol.Required("api_url", default=DEFAULT_API_URL): str,
    vol.Required("api_key"): str
        # Items can be grouped by collapsible sections                        
    }

class EsoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 0
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(
        self, 
        user_input = None
    ) -> config_entries.ConfigFlowResult:
              
        await self.async_set_unique_id(DOMAIN)

        errors: dict[str, str] = {}

        if (user_input is not None):
            return self.async_create_entry(
                title=DOMAIN, data=user_input
            )                
     
        return self.async_show_form(
            step_id="user", 
            data_schema=vol.Schema(API_SETUP_SCHEMA),
            errors=errors
            )
    
    async def async_step_reconfigure(
        self, 
        user_input: dict[str, Any] | None = None
        ) -> config_entries.ConfigFlowResult:
                  
        await self.async_set_unique_id(DOMAIN)

        errors: dict[str, str] = {}

        existing_entry = self._get_reconfigure_entry()
        if (user_input is not None):
            #this is called when setup form was already submitted
            api_url = user_input['api_url']
            api_key = user_input['api_key']
            data = {'api_url': api_url, 'api_key': api_key}
            client = EsoLtApiClient(api_url, api_key)
            await client.test_connection()
            return self.async_update_reload_and_abort(
                self._get_reconfigure_entry(),
                data_updates=data
            )
        else:
            #this is called when we're opening setup form with aleady existing config
            api_setup_schema = {
                vol.Required("api_url", default=existing_entry.data['api_url']): str,
                vol.Required("api_key", default=existing_entry.data['api_key']): str                
                }
            return self.async_show_form(
                step_id="reconfigure",            
                data_schema=vol.Schema(api_setup_schema)
            )
        
