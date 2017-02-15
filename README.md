# OctoPrint_IFTTTmaker

Connect Octoprint to the IFTTT maker channel.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/sedgett/OctoPrint_IFTTTmaker/archive/master.zip

## Configuration

1. Setup the IFTTT maker channel at https://ifttt.com/maker/
2. Get you Maker key from https://ifttt.com/services/maker/settings (it's the bit at the end, after /use/)
3. Login to your Octopi, goto settings, then click on IFTTTmaker
4. Enter your key in the settings screen for the plugin in Octopi
5. Select the events to send to IFTTT via settings.
6. Create recipies on IFTTT for your new events.
	- Use op-EventName as the trigger
	- value1 is filename (where applicable)
	- value2 is elapsed time (where applicable)
	- value3 is remote IP (where applicable)
