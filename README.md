# Bed Leveling m420

Special Edition for Multec Multirap M420 (Dual-Head, 2Move 3D-Printerhead)and other [Multec](https://www.multec.de) printers.

My Printer: 
* Read with M115
* MACHINE_TYPE:Multirap M420_2Move_230 FIRMWARE:2.1.0

Original Module forked from: https://github.com/electr0sheep/OctoPrint-Cr10_leveling/

Thank electr0sheep for your work!

### Adds bed leveling buttons to the controls tab.

This plugin adds buttons to apply heat to the bed and nozzle, and move the printing head to each of the four corners of the bed, as well as the center of the bed.

The coordinates and temperatures can all be customized in the plugin’s settings.

### Adds special Multec Printer controls to the controls tab.

* Home (G28) - like octoprint used above but better in this context again the Home-Option with G-Code G28 is available
* G0 X0 Y0 - goto Origin in X/Y (no Z-axis movement)
* AutoLevel (G29) - The m420 got an optional autolevel-sensor and so you could start the procedure manualy.
* Init 2Move (G222) - The m420 also got an optional 2move-extruder which need to be initialized with this G222 gcode manualy

Also i modified the default-values of the print-bed navigation and integrate it from a m420 (210x400). you can easily edit the suggestions in plugin settings, may be for other multec printers

### Future functions
In the future i plan to integrate the following functions
* read the printbed-settings and calculate the suggestions from it (width - offset, depth - offset)
* option settings for hardware-variant of you printer (autobedleveling, 2move, 4move extruder) and deactivating unnecessary buttons
* automatic 5-point movement with wating some (configureable) time on each point to ajust the printbed
* (if possible) use the autolevel sensor on each point to ajust the value (current i don't know how i can do that and if the firmware supports it)

## Warning

After turning on your printer, you must first home it (G28) before you can safely issuing gcode that causes movement.
This is true for this plugin, OctoPrint's default movement controls.

Failing to do so can cause the printer to move out-of-bounds.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/Qixuga/OctoPrint-m420_leveling/archive/master.zip

## Configuration

Options can be configured from OctoPrint's settings menu under "Plugins"
Available options are:
 - Bed Temp
 - Nozzle Temp
 - Simultaneously heat Bed and Nozzle
 - Feed Rate (Speed of movement)
 - Lower Z coordinate
 - Upper Z coordinate
 - Autolevel Commands
 - Front Left Position
 - Front Right Position
 - Back Left Position
 - Back Right Position
 - Center Position
