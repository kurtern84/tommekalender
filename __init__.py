"""The tommekalender component."""
import logging
from homeassistant.core import HomeAssistant  # Oppdatert import

_LOGGER = logging.getLogger(__name__)

DOMAIN = "tommekalender"

async def async_setup(hass: HomeAssistant, config: dict):  # Endret HomeAssistantType til HomeAssistant
    """Set up the Tommekalender component."""
    _LOGGER.info("Setting up Tommekalender")
    return True
