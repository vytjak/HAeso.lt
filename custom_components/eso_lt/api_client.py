from __future__ import annotations

from datetime import datetime
import socket
import aiohttp
import logging
import uuid
from typing import Any
from asyncio import timeout

API_CLIENT_OBJECTS = '/objects-api/v1/objects/json?date={0}'
API_MONTHLY_CONSUMPTION_BY_OBJ = '/consumptions-api/v1/interval-scale/month/consumption-byobject/json?objectId={0}?date={1}'

class EsoLtApiClientError(Exception):
    """ """

class EsoLtApiClientAuthenticationError(EsoLtApiClientError):
    """ """

class EsoLtApiClientCommunicationError(EsoLtApiClientError):
    """ """

class EsoLtApiClient:
    """Eso.lt API Client."""

    def __init__(
        self,
        base_url: str,
        api_key: str
    ) -> None:    
        self._base_url = base_url
        self._api_key = api_key
        self._session = aiohttp.ClientSession()    

    async def test_connection(
        self
    ) -> Any:
        """Check that we can connect and the API key is valid"""    
        try:
            logMan = logging.getLogger(__name__)            
            cs = self._session
            auth_value = f'api-key" {self._api_key}'
            headers = {'api-key': self._api_key, 'X-B3-TraceId': uuid.uuid4().hex}
            request_dt = datetime(2000, 1, 1, 0, 0, 0)  #TODO: maybe switch to today()?
            request_dt_text = request_dt.astimezone().isoformat()
            request_url = self._base_url + API_CLIENT_OBJECTS.format(request_dt_text)            
            logMan.info(f'Testing API connection to: {request_url}')
            logMan.info(f'Authorization: {auth_value}')
            logMan.info(f'Headers: {repr(headers)}')
            async with timeout(10):
                response = await cs.get(request_url, headers=headers)
            if (response.status == 401):
                raise(EsoLtApiClientAuthenticationError)
            #!!!elif (response.status)
            response.raise_for_status()
            return True
                                    
        except Exception as exception:  # pylint: disable=broad-except
             msg = f"Something really wrong happened! - {exception}"
             raise EsoLtApiClientError(
                 msg,
             ) from exception    
        
    
    
#     async def async_get_data(self) -> Any:
#         #Get data from the API.
#         return await self._api_wrapper(
#             method="get",
#             url="https://jsonplaceholder.typicode.com/posts/1",
#         )
    
#     async def async_set_title(self, value: str) -> Any:
#         #Get data from the API.
#         return await self._api_wrapper(
#             method="patch",
#             url="https://jsonplaceholder.typicode.com/posts/1",
#             data={"title": value},
#             headers={"Content-type": "application/json; charset=UTF-8"},
#         )
    
#     async def _api_wrapper(
#         self,
#         method: str,
#         url: str,
#         data: dict | None = None,
#         headers: dict | None = None,
#     ) -> Any:
#         #Get information from the API.
#         try:
#             async with timeout(10):
#                 response = await self._session.request(
#                     method=method,
#                     url=url,
#                     headers=headers,
#                     json=data,
#                 )

#                 # Verify that the response is valid.
#                 if (response.status in (401, 403)):
#                     msg = "Invalid credentials"
#                     raise EsoLtApiClientAuthenticationError(
#                         msg,
#                     )
#                 response.raise_for_status()

#                 return await response.json()

#         except TimeoutError as exception:
#             msg = f"Timeout error fetching information - {exception}"
#             raise EsoLtApiClientCommunicationError(
#                 msg,
#             ) from exception
#         except (aiohttp.ClientError, socket.gaierror) as exception:
#             msg = f"Error fetching information - {exception}"
#             raise EsoLtApiClientCommunicationError(
#                 msg,
#             ) from exception
#         except Exception as exception:  # pylint: disable=broad-except
#             msg = f"Something really wrong happened! - {exception}"
#             raise EsoLtApiClientError(
#                 msg,
#             ) from exception    