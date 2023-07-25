from homeassistant import config_entries
from .const import DOMAIN

SIDEPANEL_TITLE = "sidepanel_title"
SIDEPANEL_ICON = "sidepanel_icon"

@config_entries.HANDLERS.register("a_different_take")
class ADifferentTakeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 2
    async def async_step_user(self, info):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="", data={})

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return ADifferentTakeEditFLow(config_entry)

class ADifferentTakeEditFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = {
            vol.Optional(SIDEPANEL_TITLE, default=self.config_entry.options.get("sidepanel_title", "A Different Take")): str,
            vol.Optional(SIDEPANEL_ICON, default=self.config_entry.options.get("sidepanel_icon", "mdi:alpha-d-box")): str,
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(schema)
        )
