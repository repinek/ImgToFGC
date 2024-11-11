> [!IMPORTANT]
> This repository is deprecated, use the [Loamfy fork](https://github.com/Loamfy/img2FGC_v2)


# ImgToFGC
Convert image to Fall Guys Creative Level! <br>
NOTE: Although I don’t believe that you can get banned for this, but be careful!

## Examples
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/b37c4ddf-8d96-4174-bb7e-6a512e7cf5da" width="400" height="225"/>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/6f4ba9e7-51b3-4f4d-8bf0-b6434ea79287" width="314" height="225"/>
<br>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/5e065e81-686a-48ce-8fbb-12f5cc6b182f" width="400" height="225"/>
<img src="https://github.com/repinek/ImgToFGC/assets/137826826/5fde924e-ef3f-42bb-9659-bf45161691f5"/>

## Question and answers 
Can I get banned using this?
> There has not been a single case of a player being banned for using mods/scripts, including creative ones. But in any case, the developer does not take responsibility, use it at your own risk!

I want to change the colors, but when I go to colors.json I see strange numbers
> These numbers are the color index.
If you want to find out the color index, there are two ways to do this:
- default method
1. Place floor
2. the floor is placed with index color 0, and each subsequent color is +1 to the index. That it, if you change the color 2 times then you get index 2
- via Unity Explorer
1. place floor
2. find it in Object Explorer. Its name is Placeable_Floor_Soft_Original(Clone) (or Placeable_Floor_Soft_Retro(Clone) if you are using the Digital theme)
3. Select it in the inspector, find the LevelEditorColourSwapParameter component
4. Select it, find the set_ColourSwapIndex method
5. Write an index from 0 to 19 (0 and below is the default color, the color above the index will be the last possible)

## Requirements
- For source code:
1. requirements.txt (pip install -r requirements.txt)
2. Python 3
- Exe version
1. FallGuysTools for load json map (not necessary if you know how to load map)

## Features 
- Convert image to Fall Guys Creative 
- Digital/Original Theme
- Delete white/black pixels
- Edit colors usage via json in BepInEx/plugins/FallGuysTools

## Usage
- With [FallGuysTools](https://discord.gg/MpGcpZT4pY)
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
3. After generation the map file will be saved in "AppData\LocalLow\Mediatonic\FallGuys_client\" with name "Img2FGC.json"
4. Now, you need to load this json file in to the game, good luck! (if you dont know how to do it, use FallGuysTools)

## Credits
- [@repinek](https://github.com/repinek) creator of this program
- [@FloyzI](https://github.com/floyzi) for creating mod and betatest


