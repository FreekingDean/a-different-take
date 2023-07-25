import logging

from homeassistant.components.lovelace.dashboard import LovelaceStorage
from homeassistant.components.lovelace import _register_panel

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

def load_dashboard(hass, config_entry):
    sidepanel_title = "A Different Take"
    sidepanel_icon = "mdi:alpha-d-box"

    if("sidepanel_title" in config_entry.options):
        sidepanel_title = config_entry.options["sidepanel_title"]

    if("sidepanel_icon" in config_entry.options):
        sidepanel_icon = config_entry.options["sidepanel_icon"]

    dashboard_url = "a-different-take"
    dashboard_config = {
        "mode": "storage",
        "icon": sidepanel_icon,
        "title": sidepanel_title,
        "url": dashboard_url,
        "show_in_sidebar": True,
        "require_admin": False,
        "theme": "tablet",
        "views": [
            {
                "type": "custom:grid-layout",
                "theme": "tablet",
                "path": 0,
                "layout": {
                    "margin": 0,
                },
            },
        ],
    }

    hass.data["lovelace"]["dashboards"][dashboard_url] = LovelaceStorage(hass, dashboard_url, dashboard_config)

    _register_panel(hass, dashboard_url, "storage", dashboard_config, False)
