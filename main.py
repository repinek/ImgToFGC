from PIL import Image
import webcolors
import json
import uuid
import time
import os
from colorama import Fore, Style
import getpass

user_name = getpass.getuser()

file_path_output = "C:\\Users\\" + user_name + "\\AppData\\LocalLow\\Mediatonic\\FallGuys_client\\output.txt"
FGC_json = "C:\\Users\\" + user_name + "\\AppData\\LocalLow\\Mediatonic\\FallGuys_client\\Img2FGC.json"

# reading output.txt by mod
try:
    with open(file_path_output, "r", encoding="utf-8") as f1:
        lines = f1.readlines()
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Unable to find file " + Style.RESET_ALL + ", try again\n")
    os.system("pause")
    exit()

for line in lines:
    try:
        line = line.strip()
        key, value = line.split(' = ')
        if key == 'path_to_file':
            image_input = value
        elif key == 'width':
            width_input = value
        elif key == 'height':
            height_input = value
        elif key == 'shouldDeleteBlackPixels':
            shouldDeleteBlackPixels = value.lower()
        elif key == 'shouldDeleteWhitePixels':
            shouldDeleteWhitePixels = value.lower()
        elif key == 'isDigital':
            isDigital = value.lower() # I know there are better ways to do this, but I'm lazy
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Unable to find file" + Style.RESET_ALL + ", try again\n")
        os.system("pause")
        exit()
    except Exception as e:
        print(f"Looks like file " + Fore.LIGHTRED_EX + " is corrupted" + Style.RESET_ALL + ", try again, if you can't fix this error by yourself tell " + Fore.LIGHTYELLOW_EX + "repinek about this, " + Style.RESET_ALL + "{e}, {e.__traceback__.tb_lineno}\n")
        os.system("pause")
        exit()

if shouldDeleteWhitePixels == "false":
    white_yes_or_no = "no"
elif shouldDeleteWhitePixels == "true":
    white_yes_or_no = "yes"
else:
    print("Something went wrong, report about this to " + Fore.LIGHTYELLOW_EX + " repinek" + Style.RESET_ALL + ", 49\n")
    os.system("pause")
    exit()
if shouldDeleteBlackPixels == "false":
    black_yes_or_no = "no"
elif shouldDeleteBlackPixels == "true":
    black_yes_or_no = "yes"
else:
    print("Something went wrong, report about this to " + Fore.LIGHTYELLOW_EX + " repinek" + Style.RESET_ALL + ", 57\n")
    os.system("pause")
    exit()

if isDigital == "false":
    theme = "original"
elif isDigital == "true":
    theme = "digital"
else:
    print("Something went wrong, report about this to " + Fore.LIGHTYELLOW_EX + " repinek" + Style.RESET_ALL + ", 66\n")
    os.system("pause")
    exit()

print(Fore.LIGHTCYAN_EX + "NOTE: Although I don’t believe that you can get " + Fore.LIGHTRED_EX + "banned " + Fore.LIGHTCYAN_EX + "for this, but " + Fore.LIGHTGREEN_EX + "be careful!"+ Fore.LIGHTRED_EX + " Don't use this script if you want to import NSFW or if you are stupid\n\n" +
      Style.RESET_ALL + "You cannot save maps larger than " + Fore.LIGHTRED_EX + "2MB" + Fore.LIGHTGREEN_EX + " (around 700 pixels)\n" +
      Fore.LIGHTGREEN_EX + "1000 pixels" + Style.RESET_ALL + " are generated in ~" + Fore.LIGHTGREEN_EX + " one second\n\n" +
      Style.RESET_ALL + "Script created by " + Fore.LIGHTYELLOW_EX + "repinek" + Style.RESET_ALL + " (" + Fore.LIGHTYELLOW_EX + "@repinek " + Style.RESET_ALL + "in " + Fore.LIGHTCYAN_EX + "tg/ds" + Style.RESET_ALL + ", " + Fore.LIGHTYELLOW_EX + "@repinek840" + Style.RESET_ALL + " in X), and thanks " + Fore.LIGHTGREEN_EX + "FloyzI " + Style.RESET_ALL + "for help\n") # добавить про кал с долгой герекой
try:
    print(Fore.LIGHTGREEN_EX + "config:\n" + Style.RESET_ALL +
      f"path: {image_input}\n"
      f"width: {width_input}\n"
      f"height: {height_input}\n"
      f"delete white: {white_yes_or_no}, black: {black_yes_or_no}\n"
      f"theme: {theme}")
except Exception as e:
    print(f"send this to repinek. {e.__traceback__.tb_lineno}, {e}\n")
    os.system("pause")
    exit()

try:
    image = Image.open(image_input)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
except OSError:
    print("didnt found image with path", image_input + "\n")
    os.system("pause")
    exit()
except Exception as e:
    print(f"send this to repinek. {e.__traceback__.tb_lineno}, {e}\n")
    os.system("pause")
    exit()

# checking
width, height = image.size
try:
    width_input_int = int(width_input)
except TypeError:
    print("Width should be as number\n")
    os.system("pause")
    exit()
except Exception as e:
    print(f"Report about this to repinek. {e.__traceback__.tb_lineno}, {e}\n")
    os.system("pause")
    exit()
try:
    height_input_int = int(height_input)
except TypeError:
    print("Height should be as number\n")
    os.system("pause")
    exit()
except Exception as e:
    print(f"Report about this to repinek. {e.__traceback__.tb_lineno}, {e}\n")
    os.system("pause")
    exit()

if width_input_int > width:
    print("Width can't be more than image width\n")
    os.system("pause")
    exit()
elif height_input_int > height:
    print("Height can't be more than image height\n")
    os.system("pause")
    exit()
try:
    image = image.resize((width_input_int, height_input_int))
except Exception as e:
    print(f"Report about this to repinek. {e.__traceback__.tb_lineno}, {e}\n")
    os.system("pause")
    exit()

# white_yes_or_no = input("delete all white pixels? ('yes' or 'no'): ")
# black_yes_or_no = input("delete all black pixels? ('yes' or 'no'): ")
# ↑ old code

print("After" + Fore.LIGHTGREEN_EX + " 5 seconds " + Style.RESET_ALL + "map should start generating, you will see some debug info (BETA)\n"
"If you get some errors report about them to repinek, thanks")
time.sleep(5)

a = "no alpha"
width, height = image.size # again (sigma)
rgb_colors = []
# default colors
real_colors = {
    "original": {
        "aqua": 4,
        "gray": 18,
        "silver": 17,
        "navy": 12,
        "black": 19,
        "green": 13,
        "teal": 10,
        "olive": 9,
        "blue": 12,
        "lime": 13,
        "white": 16,
        "purple": 14,
        "fuchsia": 1,
        "maroon": 11,
        "yellow": 2,
        "red": 11,
        "cyan": -1,
        "orange": 8
    },
    "digital": {
        "aqua": 3,
        "gray": 4,
        "silver": 8,
        "navy": -1,
        "black": 4,
        "green": 3,
        "teal": 5,
        "olive": 9,
        "blue": -1,
        "lime": 3,
        "white": 15,
        "purple": 12,
        "fuchsia": 2,
        "maroon": 14,
        "yellow": 6,
        "red": 14,
        "cyan": 3,
        "orange": 13
    }
}
colors_json = "\BepInEx\plugins\FallGuysTools\сolors.json"
cwd = os.getcwd()
full_path_tolko_u_menya = cwd + colors_json
# colors check
try:
    with open(full_path_tolko_u_menya, 'r', encoding='utf-8') as file_kek:
        data = json.load(file_kek) # im a furry btw
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + f"Unable to find colors.json " + Style.RESET_ALL + f", a new colors.json will be generated by this path {full_path_tolko_u_menya} with " + Fore.LIGHTGREEN_EX + f"recommended colors" + Style.RESET_ALL)
    with open(full_path_tolko_u_menya, 'w') as f2:
        json.dump(real_colors, f2)
        data = real_colors
except Exception as e:
    print(f"Report about this to repinek. {e.__traceback__.tb_lineno}, {e}")
    os.system("pause")
    exit()

# colors
colors_original = {
    "aqua": data["original"]["aqua"],
    "gray": data["original"]["gray"], # -1
    "silver": data["original"]["silver"], # -1
    "navy": data["original"]["navy"],
    "black": data["original"]["black"],
    "green": data["original"]["green"],
    "teal": data["original"]["teal"],
    "olive": data["original"]["olive"],
    "blue": data["original"]["blue"],
    "lime": data["original"]["lime"],
    "white": data["original"]["white"],
    "purple": data["original"]["purple"],
    "fuchsia": data["original"]["fuchsia"],
    "maroon": data["original"]["maroon"],
    "yellow": data["original"]["yellow"],
    "red": data["original"]["red"],
    "cyan": data["original"]["cyan"],
    "orange": data["original"]["orange"],
    "teal": data["original"]["teal"]
}
colors_digital = {
    "aqua": data["digital"]["aqua"],
    "gray": data["digital"]["gray"], # -1
    "silver": data["digital"]["silver"], # -1
    "navy": data["digital"]["navy"],
    "black": data["digital"]["black"],
    "green": data["digital"]["green"],
    "teal": data["digital"]["teal"],
    "olive": data["digital"]["olive"],
    "blue": data["digital"]["blue"],
    "lime": data["digital"]["lime"],
    "white": data["digital"]["white"],
    "purple": data["digital"]["purple"],
    "fuchsia": data["digital"]["fuchsia"],
    "maroon": data["digital"]["maroon"],
    "yellow": data["digital"]["yellow"],
    "red": data["digital"]["red"],
    "cyan": data["digital"]["cyan"],
    "orange": data["digital"]["orange"],
    "teal": data["digital"]["teal"]
}
# id number for object
id_number = -1

# object example
data = {
    "Name": "Placeable_Floor_Soft_Vanilla(Clone)",
    "ID": -10005,
    "VariantGuid": "9422ba3d-b426-486f-864f-385cb21d1212",
    "GUIDs": "0e2247bc-1388-4226-917d-d9a26e6813b0",
    "Position": [
        -3.81721544,
        65.0,
        -152.007324
    ],
    "CurrentRotation": [
        0.0,
        0.0,
        0.0
    ],
    "Local Scale": [
        1.0,
        1.0,
        1.0
    ],
    "Group Type": "None",
    "ColourSwapIndex": -1,
    "Shader Scale": [
        1.0,
        1.0,
        1.0
    ],
    "Floor Pivot Pos": 0.0,
    "Floor Depth": 0.0,
    "Floor Increment Amount": 1.0
}
# fix for digital
if theme == "digital":
    data["Name"] = "Placeable_Floor_Soft_Retro(Clone)"
kek = {"Version": "V1",
                    "Test Mode Completed": True,
                    "Level Theme ID": "THEME_VANILLA",
                    "Level Published": False,
                    "Level Music": "MUS_InGame_Fall_N_Roll",
                    "What does the bean say": "gbgGpO5UXftvdC+TK/5zR6pknqciPVunpoMnuNzkBRyjKjqy81CYwVwdQ/HJ+RU2g5B2UaQZq6MEiA2BvXh7wg==",
                    "SkyboxId": "Vanilla_Skybox",
                    "Game Mode ID": "GAMEMODE_GAUNTLET",
                    "Max Capacity": 40,
                    "No of Winners": -1,
                    "No of Eliminations": -1.0,
                    "Slime Height": -1.0,
                    "Slime Speed": -1.0,
                    "Camera": {"Position": [135.094772, 90.8210449, -216.08284],
                    "Pitch and Yaw": [14.6352329, -83.75641],
                    "Distance": 100.0},
                    "Button Thumbnail": "",
                    "Floors": {}}
if theme == 'digital':
    kek["Level Theme ID"] = 'THEME_RETRO'
    kek["SkyboxId"] = 'Retro_Skybox'

# its shitcode, but i dont care (im so lazy to found other solution)
with open(FGC_json, 'w') as f:
    f.write(json.dumps(kek))
with open(FGC_json, 'rb+') as fh:
    fh.seek(-3, 2)
    fh.truncate()
with open(FGC_json, 'a') as f:
    f.write("[")

# for global
variant_guid = "kek"
guids_sss = "obed"

#func for add pixels to json (experimental)
def addpixeltojson():
    global id_number
    global data
    global FGC_json
    global variant_guid
    global guids_sss
    id_number = id_number - 1
    data["ID"] = id_number
    data["Position"][0] = x * 4.075
    data["Position"][2] = y * 4.075
    data["ColourSwapIndex"] = closest_value
    random_key = uuid.uuid4()
    formatted_key = str(random_key).replace('-', '')
    variant_guid = f"{formatted_key[:8]}-{formatted_key[8:12]}-{formatted_key[12:16]}-{formatted_key[16:20]}-{formatted_key[20:]}"
    random_key2 = uuid.uuid4()
    formatted_key2 = str(random_key2).replace('-', '')
    guids_sss = f"{formatted_key2[:8]}-{formatted_key2[8:12]}-{formatted_key2[12:16]}-{formatted_key2[16:20]}-{formatted_key2[20:]}"
    data["GUIDs"] = guids_sss
    data["VariantGuid"] = variant_guid
    with open(FGC_json, "a") as f:
        f.write(json.dumps(data, ensure_ascii=False))
        f.write(",")
# every pixel
for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y)) # get pixel rgb
        r, g, b = pixel[:3] # fix alpha
        try:
            a = pixel[3]
        except IndexError:
             a = 1 # im stupid why 0 LOL
        #parsed random closest color from internet xd
        def closest_colour(requested_colour):
            min_colours = {}
            for key, name in webcolors.CSS2_HEX_TO_NAMES.items():
                r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                rd = (r_c - requested_colour[0]) ** 2
                gd = (g_c - requested_colour[1]) ** 2
                bd = (b_c - requested_colour[2]) ** 2
                min_colours[(rd + gd + bd)] = name
            return min_colours[min(min_colours.keys())]
        def get_colour_name(requested_colour):
            try:
                closest_name = actual_name = webcolors.rgb_to_name(requested_colour, spec=u'css2')
            except ValueError:
                closest_name = closest_colour(requested_colour)
                actual_name = None
            return actual_name, closest_name

        requested_colour = (r, g, b)
        actual_name, closest_name = get_colour_name(requested_colour)
        if theme == "digital":
            closest_value = colors_digital[closest_name]
        else:
            closest_value = colors_original[closest_name]
        if white_yes_or_no == "yes" and closest_name == "white":
            print("skip")
            continue
        elif black_yes_or_no == "yes" and closest_name == "black":
            print("skip")
            continue
        else:
            try:
                if a > 0: #alpha above 0
                    addpixeltojson()
                # elif a == "no alpha":
                    # addpixeltojson()
                #dont needed anymore
                else:
                    print("Alpha is 0, unable to set pixel")
                    continue
            except Exception as e:
                print(f"Report about this to repinek. {e.__traceback__.tb_lineno}, {e}")
            posx = x * 4.075
            posy = y * 4.075
            print(f"RGB: {pixel}, alpha: {a}, color name: {closest_name}, color index: {closest_value}, object ID: {id_number}, POS X: {posx}, POS Y: {posy}, VatirantGuid: {variant_guid}, GUIDs: {guids_sss}")
            # my old bad code below, fixed by a = 0, 359 line
            '''
            except TypeError:
                id_number = id_number - 1
                data["ID"] = id_number
                data["Position"][0] = x * 4.075
                data["Position"][2] = y * 4.075
                data["ColourSwapIndex"] = closest_value
                random_key = uuid.uuid4()
                formatted_key = str(random_key).replace('-', '')
                variant_guid = f"{formatted_key[:8]}-{formatted_key[8:12]}-{formatted_key[12:16]}-{formatted_key[16:20]}-{formatted_key[20:]}"
                random_key2 = uuid.uuid4()
                formatted_key2 = str(random_key2).replace('-', '')
                guids_sss = f"{formatted_key2[:8]}-{formatted_key2[8:12]}-{formatted_key2[12:16]}-{formatted_key2[16:20]}-{formatted_key2[20:]}"
                data["GUIDs"] = guids_sss
                data["VariantGuid"] = variant_guid

                with open(FGC_json, "a") as f:
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.write(",")
                '''

# its shitcode x2, but i dont care (im so lazy to found other solution)
with open(FGC_json, 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open(FGC_json, 'a') as f:
    f.write("],")
with open(FGC_json, 'a') as f:
    f.write('"FirstBuildSessionId": "38f4bbc0-3978-4194-b3e7-463f1a25e2ee",')
    f.write(' "LevelCreationTimestamp": 1703262048686,')
    f.write(' "LevelSavedAtTimestamp": 1703262185389,')
    f.write(' "LevelLastModifiedAtTimestamp": 1703262181223,')
    f.write(' "LevelPublishedAtTimestamp": 1703262185389,')
    f.write(' "LevelNameIsCustom": true,')
    f.write(' "LevelDescriptionIsCustom": false,')
    f.write(' "Min Capacity": 1}')

print("Generation completed! Press \"Replace existing maps with level\" in FallGuysTools to load your level\n") #yea, use FGTools guys
os.remove(file_path_output)
time.sleep(3)
