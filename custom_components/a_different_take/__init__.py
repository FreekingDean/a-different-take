from .const import DOMAIN

from .load_dashboard import load_dashboard


async def async_setup(hass, config):
    hass.states.async_set(DOMAIN+".world", "Dean")

    # Return boolean to indicate that initialization was successful.
    return True

async def async_setup_entry(hass, config_entry):
    load_dashboard(hass, config_entry)

    return True
