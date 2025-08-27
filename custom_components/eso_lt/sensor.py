
from __future__ import annotations
from typing import TYPE_CHECKING
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

# from .entity import EsoLtObjectEntity
from .data import EsoLtConfigEntry
# from .coordinator import EsoLtDataUpdateCoordinator

# if TYPE_CHECKING:
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

# ENTITY_DESCRIPTIONS = (
#     SensorEntityDescription(
#         key="eso_lt",
#         name="HA eso.lt Integration Sensor",
#         icon="hass:power",
#     ),
# )


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: EsoLtConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""

#     # async_add_entities(
#     #     EsoLtMeter(
#     #         coordinator=entry.runtime_data.coordinator,
#     #         entity_description=entity_description,
#     #     )
#     #     for entity_description in ENTITY_DESCRIPTIONS
#     #)


# class EsoLtMeter(EsoLtObjectEntity):
#     """eso.lt meter"""    
#     def __init__(
#         self,
#         coordinator: EsoLtDataUpdateCoordinator#,
#         #entity_description: SensorEntityDescription,
#     ) -> None:
#         """Initialize the sensor class."""
#         #super().__init__(coordinator)
#         #self.entity_description = entity_description

#     # @property
#     # def native_value(self) -> str | None:
#     #     """Return the native value of the sensor."""
#     #     return self.coordinator.data.get("body")