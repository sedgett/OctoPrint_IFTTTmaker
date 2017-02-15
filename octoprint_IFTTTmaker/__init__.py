# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import requests
from octoprint.events import Events

import os


class IFTTTMakerPlugin(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.SettingsPlugin,
                        octoprint.plugin.EventHandlerPlugin):

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        if (hasattr, self._settings, 'makerkey'):
#            self.makerkey = self._settings.get(["makerkey"])
            self._logger.info("Saving IFTTT Maker Key: %s" % self._settings.get(["makerkey"]))
        else:
#            self.makerkey=''
            self._logger.info("No Maker key set while trying to save!")
                    
    def on_after_startup(self):
        self._logger.info("IFTTT Maker Plugin Active")
#        self.makerkey = self._settings.get(["makerkey"])
#        self._logger.debug("IFTTT Maker Key: %s" % self.makerkey)

    def get_settings_defaults(self):
        return dict(makerkey='ENTER_YOUR_MAKER_KEY',
                    events=dict(
                        PrintStarted=False,
                        PrintFailed=False,
                        PrintCancelled=False,
                        PrintDone=False,
                        MovieDone=False,
                        ClientOpened=False)
                    )
                
            
    def get_template_configs(self):
        return [ dict(type="settings", name="IFTTTmaker", custom_bindings=False) ]

    def get_settings_restricted_paths(self):
        # only used in OctoPrint versions > 1.2.16
        return dict(admin=[["makerkey"]])

######

    def on_event(self, event, payload):
        events = self._settings.get(['events'], merged=True)
        makerkey = self._settings.get(['makerkey'])
#        self._logger.debug("on_event: makerkey: %s" % makerkey)
        if event in events and events[event]:
            v1 = v2 = v3 = ""
            if 'file' in payload:
                v1 = os.path.basename(payload["file"])
            if 'time' in payload:
                v2 = payload["time"]
            if 'remoteAddress' in payload:
                v3 = payload["remoteAddress"]
            self._send_ifttt("op-"+event, makerkey, v1, v2, v3)
        else:
            self._logger.info("Event skipped: %s" % event)
          
        
#         == Events.PRINT_DONE:
#            file = os.path.basename(payload["file"])
#            elapsed_time_in_seconds = payload["time"]
#            import datetime
#            import octoprint.util    
#            elapsed_time = octoprint.util.get_formatted_timedelta(datetime.timedelta(seconds=elapsed_time_in_seconds))
#            self._send_ifttt("op-PrintDone", file, elapsed_time)



    def _send_ifttt(self, trigger, makerkey, value1=None, value2=None, value3=None):
        import requests
        payload = "{ 'value1' : value1, 'value2' : value2, 'value3' : value3}"
        url = "https://maker.ifttt.com/trigger/" + trigger + "/with/key/" + makerkey
        res = requests.post(url, data=payload)
        self._logger.debug("URL: %s" % url)
        self._logger.info("Trigger: %s Response: %s" % (trigger,  res.text))
        
        
                                                                                            
######
                        
__plugin_name__ = "IFTTT Maker"
__plugin_implementation__ = IFTTTMakerPlugin()


