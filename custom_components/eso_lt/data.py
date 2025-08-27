from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    ###from .api import IntegrationBlueprintApiClient
    from .coordinator import EsoLtDataUpdateCoordinator


type EsoLtConfigEntry = ConfigEntry[EsoLtData]


@dataclass
class EsoLtData:    
    ###client: IntegrationBlueprintApiClient
    coordinator: EsoLtDataUpdateCoordinator
    integration: Integration