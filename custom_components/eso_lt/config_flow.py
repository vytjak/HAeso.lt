from __future__ import annotations

from typing import Any
import json
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry, ConfigSubentryFlow, SubentryFlowResult
from homeassistant import data_entry_flow
from .const import DOMAIN, DEFAULT_API_URL

from .data import EsoLtConfigEntry
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

            #subentries per object
            await self.async_step_user_objectsetup(
                #self, 
                user_input
            )

            return self.async_update_reload_and_abort(
                self._get_reconfigure_entry(),
                data_updates=data
            )
        else:
            #this is called when we're opening the setup form with aleady existing config
            api_setup_schema = {
                vol.Required("api_url", default=existing_entry.data['api_url']): str,
                vol.Required("api_key", default=existing_entry.data['api_key']): str                
                }
            return self.async_show_form(
                step_id="reconfigure",            
                data_schema=vol.Schema(api_setup_schema)
            )        

    async def async_step_user_objectsetup(
        self, 
        user_input: dict[str, Any] | None = None
        ) -> config_entries.ConfigFlowResult:
        #clientObjects = 
        """ setup objects associated with the account """
        
        testFile = open('test/test_objects.json')
        clientObjects = json.load(testFile)         
        configSubEntryData = dict()
        for clientObject in clientObjects:
            configSubEntryData['objectId'] = clientObject['objectId']
            configSubEntryData['objectName'] = clientObject['objectName']
            #self.async_create_entry(title=clientObject['objectName'], description=clientObject['objectAddress'], subentries=configSubEntryData)


        return self.async_update_reload_and_abort(
            self._get_reconfigure_entry()
                )
    
    @classmethod
    #@callback
    def async_get_supported_subentry_types(
        cls, config_entry: ConfigEntry
    ) -> dict[str, type[ConfigSubentryFlow]]:
        """Return subentries supported by this integration."""
        return {"EsoLtObject": EsoLtAccountSubentryFlowHandler}

class EsoLtAccountSubentryFlowHandler(ConfigSubentryFlow):
    """Handle subentry flow for adding and modifying a energy grid objects (buildings/locations).

    Subentry configuration consists of one entry per object associated to the account.
    """

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> SubentryFlowResult:
        """User flow to add a new location."""
        ...
        
