import logging

from homeassistant.components.lovelace.dashboard import LovelaceYAML
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
        "mode": "yaml",
        "icon": sidepanel_icon,
        "title": sidepanel_title,
        "filename": "custom_components/a_different_take/lovelace/ui-lovelace.yaml",
        "show_in_sidebar": True,
        "require_admin": False,
    }

    hass.data["lovelace"]["dashboards"][dashboard_url] = LovelaceYAML(hass, dashboard_url, dashboard_config)

    _register_panel(hass, dashboard_url, "yaml", dashboard_config, False)
