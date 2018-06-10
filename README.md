# SMARTHOME PLUGIN FOR GEDIT #

This is a plugin for GEdit 3 that enables the SmartHome mode. That means that
the *HOME* key will move the cursor to the first non-space character in the line,
and not to the first column. This is very useful when using Gedit as a code editor.

The main advantage of this plugin over others, is that this has been written in
Vala, which compiles to native code and, thus, it is very lightweight.


# INSTALLING THE PLUGIN #

## Local installation ##

Local installation is the preferable way for installing this plugin. It makes
the plugin accesible only to the user that installed it, but has the advantage
of not needing root priviledges, and also avoids the problems with library
paths (which, in 64bit systems, are problematic). To install it in this way,
just type:

        mkdir install
        cd install
        cmake .. -DATHOME=on -DCMAKE_INSTALL_PREFIX=$HOME/.local
        make
        make install


## System-wide installation ##

To install this plugin system-wide, allowing to be used by all users in the
system, just type:

        mkdir install
        cd install
        cmake .. -DCMAKE_INSTALL_PREFIX=/usr
        make
        sudo make install

This mode needs root priviledges, and in some systems can be installed in the
wrong folder, forcing the user to manually move the files to the right place.


## Enabling the plugin ##

After installation, close all GEdit windows, open it again and go to
Preferences -> Plugins to enable the Autovala plugin.


# Contacting the author #

Sergio Costas Rodriguez (raster software vigo)  
rastersoft@gmail.com  
http://www.rastersoft.com  
https://gitlab.com/rastersoft/smarthome
