add sensors
===========

To add a sensor, you have to do two things:

* You have to code a `provider` inheriting `Provider` class
* There has to be a sensor `view` inheriting `Sensor` class

First, let start by adding Provider.


Move to `providers` file, look at other provider files and do it similary, remember to call a module using lower letters and `provider` suffix. Like `proximitysensorprovider`.

Provider class have to be in that naming convention too, but in `CamelCase`



Now, proceed to adding sensor view, do a class which inherits `Sensor` in `sensors` directory, import it in `main.py` file (remember to not redeclare it), then edit a `sensor.kv` file and add a sensor.
