This is a file that provide a set of instructions in how to install necessary
packages to rum the this code in case the in case of failure of the venv or
its importation.

Please, execute the following comands with the termial oppen in the venv:

How to install Kivy:

setep 1: pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*

setep 2: pip install kivy_deps.gstreamer==0.1.*

setep 3: pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/


How to install Openxl:

single step: pip install openpyxl


How to install Networkx:

single step: pip install networkx