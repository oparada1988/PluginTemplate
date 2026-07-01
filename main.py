# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.PluginManager.ActionInputSupport import ActionInputSupport
from src.backend.DeckManagement.InputIdentifier import Input

# Import actions
from .actions.VolumeControl.VolumeControl import VolumeControl

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.volume_control_holder = ActionHolder(
            plugin_base = self,
            action_base = VolumeControl,
            action_id = "com_oparada_VolumeControllerPlus::VolumeControl",
            action_name = "Volume Controller Plus",
            action_support = {
                Input.Key: ActionInputSupport.UNSUPPORTED,
                Input.Dial: ActionInputSupport.SUPPORTED,
                Input.Touchscreen: ActionInputSupport.SUPPORTED
            }
        )
        self.add_action_holder(self.volume_control_holder)

        # Register plugin
        self.register(
            plugin_name = "Volume Controller Plus",
            github_repo = "https://github.com/oparada1988/Volume-Controller-Plus",
            plugin_version = "1.0.0",
            app_version = "1.0.0-alpha"
        )