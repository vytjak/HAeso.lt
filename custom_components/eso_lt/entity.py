from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import EsoLtDataUpdateCoordinator


class EsoLtObjectEntity(CoordinatorEntity[EsoLtDataUpdateCoordinator]):    
    """Represents an ESO object (apartment/building/etc.), which might have one or more energy meters installed """
    def __init__(self, coordinator: EsoLtDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={
                (
                    coordinator.config_entry.domain,
                    coordinator.config_entry.entry_id,
                ),
            },
         )