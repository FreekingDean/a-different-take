from .const import DOMAIN


async def async_setup(hass, config):
    hass.states.async_set(DOMAIN+".world", "Dean")

    # Return boolean to indicate that initialization was successful.
    return True
