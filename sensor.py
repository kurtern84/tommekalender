"""Sensor platform for Tommekalender."""
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import logging

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(hours=24)

WASTE_TYPES = ["Matavfall", "Restavfall", "Papir", "Glass/Metallemballasje"]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Tommekalender sensors."""
    address = config.get("address")
    if address is None:
        _LOGGER.error("No address provided for Tommekalender sensor")
        return

    sensors = [TommekalenderSensor(address, waste_type) for waste_type in WASTE_TYPES]
    add_entities(sensors, True)

class TommekalenderSensor(Entity):
    """Representation of a Tommekalender sensor."""

    def __init__(self, address, waste_type):
        """Initialize the sensor."""
        self._state = None
        self._address = address
        self._waste_type = waste_type
        self._icon = "mdi:recycle"
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Tommekalender {self._waste_type}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return self._icon

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get(f"https://www.hiks.no/privat/tommekalender/?adresse={self._address}")
            soup = BeautifulSoup(response.content, "html.parser")

            card = next(
                (card for card in soup.select(".card") if self._waste_type in card.select_one(".fraction-name span").text),
                None,
            )
            if card:
                first_date_element = card.select(".day-date")[0]
                self._state = first_date_element.text.strip() if first_date_element else "No date found"

        except Exception as e:
            _LOGGER.error(f"Error fetching Tommekalender data: {e}")
            self._state = "Error"
