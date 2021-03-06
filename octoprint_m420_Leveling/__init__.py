# OctoPrint Multec Multirap m420 Leveling Plugin. Allows user to easily level 3D printer.
# Copyright (C) 2018  electr0sheep
# Forked and edit 2018 by Qixuga
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Email: electr0sheep@electr0sheep.com

from __future__ import absolute_import

from octoprint.settings import settings
import octoprint.plugin


class m420_levelingPlugin(octoprint.plugin.AssetPlugin,
                          octoprint.plugin.TemplatePlugin,
                          octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.StartupPlugin):

    def on_after_startup(self):
        s = settings()

        controlList = s.get(["controls"])

        for item in controlList:
            if (item['name'] == 'Bed Leveling') or (item['name'] == 'Bed Leveling m420'):
                controlList.remove(item)

        s.set(["controls"], controlList)

    def get_settings_defaults(self):
        offset = 30
        return dict(
                        bed_temp=50,
                        nozzle_temp=195,
                        play_tune=True,
                        wait_for_heat=True,

                        front_left_x=180,   # value: dimensions.width or volumeWidth - offset
                        front_left_y=370,   # value: dimensions.depth or volumeDepth - offset

                        front_right_x=0,
                        front_right_y=370,

                        back_left_x=0,
                        back_left_y=180,

                        back_right_x=0,
                        back_right_y=0,

                        center_x=105,       # volumeWidth / 2
                        center_y=200,       # volumeDepth / 2

                        lower_z=0,
                        upper_z=10,
                        feed_rate=3600,
                        heat_simultaneously=True,
                        autolevel=""
                   )

    def get_template_configs(self):
        return [dict(type="settings", custom_bindings=False)]

    def get_assets(self):
        return dict(js=["m420leveling.js"])

    def get_update_information(self):
        return dict(
            m420_Leveling=dict(
                displayName="Bed Leveling m420",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="Qixuga",
                repo="OctoPrint-m420_leveling",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/Qixuga/OctoPrint-m420_leveling/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Bed Leveling m420"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = m420_levelingPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
