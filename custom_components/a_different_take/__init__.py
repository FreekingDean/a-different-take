DOMAIN = "a_different_take"


async def async_setup(hass, config):
    hass.states.async_set("a_different_take.world", "Dean")

    # Return boolean to indicate that initialization was successful.
    return True
