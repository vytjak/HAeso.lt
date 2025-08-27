from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

#if TYPE_CHECKING:
from homeassistant.config_entries import ConfigEntry
from homeassistant.loader import Integration

#     from .api_client import EsoLtApiClient
#     from .coordinator import EsoLtDataUpdateCoordinator


class EsoLtConfigEntry(ConfigEntry):
    """Eso.Lt Config """


# @dataclass
# class EsoLtData:    
#     client: EsoLtApiClient
#     coordinator: EsoLtDataUpdateCoordinator
#     integration: Integration