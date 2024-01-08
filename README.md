# ImgToFGC
Convert image to Fall Guys Creative Level!

# Examples
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/b37c4ddf-8d96-4174-bb7e-6a512e7cf5da" width="400" height="225"/>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/6f4ba9e7-51b3-4f4d-8bf0-b6434ea79287" width="314" height="225"/>
<br>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/5e065e81-686a-48ce-8fbb-12f5cc6b182f" width="400" height="225"/>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/5fde924e-ef3f-42bb-9659-bf45161691f5"/>


# Requirements
- requirements.txt 
- Python 3
- FallGuysTools for load json map (not necessary if you know how to load map)

# Features 
- Convert image to Fall Guys Creative 
- Change Theme
- Delete white/black pixels
- Edit colors usage via json in BepInEx/plugins/FallGuysTools

# Usage
- With FallGuysTools
1. Set config in GUI
2. Click "Generate Level"
3. After generation go to Load creative tab and click "Replace existing maps with level"
4. Open any map

- Without FallGuysTools
1. The config is stored in "\AppData\LocalLow\Mediatonic\FallGuys_client\output.txt", and looks like this:
```
path_to_file = path without ""
width = 75
height = 75
shouldDeleteBlackPixels = False/True
shouldDeleteWhitePixels = False/True
isDigital = False/True
```
2. Run ImgToFGC
3. After generation the map file will be saved in "AppData\LocalLow\Mediatonic\FallGuys_client\" with name "myfile.json"
4. Now, you need to load this json file in to the game, good luck! (if you dont know how to do it, use FallGuysTools)

# Credits
- [@repinek](https://github.com/repinek) creator of this program
- [@FloyzI](https://github.com/floyzi) for creating mod and betatest


