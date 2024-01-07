# ImgToFGC
Convert image to Fall Guys Creative Level!
# Requirements
- requirements.txt 
- Python 3
- FallGuysTools for load json map (not necessary if you know how to load map)
# Usage
- With FallGuysTools
1. Set config in gui
2. Click Generate Level
3. After generation go to Load creative tab and click "Replace existing maps with level"
4. Open any map
- Without FallGuysTools
1. The config is stored in "\AppData\LocalLow\Mediatonic\FallGuys_client\output.txt", and looks like this:
``
path_to_file = path without ""
width = 75
height = 75
shouldDeleteBlackPixels = False/True
shouldDeleteWhitePixels = False/True
isDigital = False/True
``

