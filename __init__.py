"""The tommekalender component."""
import logging

from homeassistant.helpers.typing import HomeAssistantType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "tommekalender"

async def async_setup(hass: HomeAssistantType, config: dict):
    """Set up the Tommekalender component."""
    _LOGGER.info("Setting up Tommekalender")
    return True
