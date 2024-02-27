import json

"""Support for AWTRIX service."""


class AwtrixTime:
    """Allows to send updated to applications."""

    def __init__(self,
                 hass,
                 entity_id
                 ) -> None:
        """Initialize the device."""

        self.hass = hass
        self.entity_id = entity_id

    async def push(self, app_id, data):
        """Update the application data."""

        state = self.hass.states.get(self.entity_id)
        if state is not None and state.state is not None:
            topic = state.state + "/custom/" + app_id

            data = data or {}
            msg = data.copy()

            payload = json.dumps(msg) if len(msg) else ""
            service_data = {"payload_template": payload,
                            "topic": topic}

            return await self.hass.services.async_call(
                "mqtt", "publish", service_data
            )

    async def settings(self, data):
        """Call API settings."""

        state = self.hass.states.get(self.entity_id)
        if state is not None and state.state is not None:
            topic = state.state + "/settings"

            data = data or {}
            msg = data.copy()

            payload = json.dumps(msg)
            service_data = {"payload_template": payload,
                            "topic": topic}

            return await self.hass.services.async_call(
                "mqtt", "publish", service_data
            )

    async def switch_app(self, name):
        """Call API switch app."""

        state = self.hass.states.get(self.entity_id)
        if state is not None and state.state is not None:
            topic = state.state + "/switch"
            payload = json.dumps({"name": name})
            service_data = {"payload_template": payload,
                            "topic": topic}

            return await self.hass.services.async_call(
                "mqtt", "publish", service_data
            )
