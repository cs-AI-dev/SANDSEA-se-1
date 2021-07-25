import os
os.system("pip install tqdm")
import tqdm

print("Loading SANDSEA ...")


print("Done!\n")

print(" |  SANDSEA Simulation Engine v." + str(open("E:/sandsea/SANDSEA-se-1/SANDSEA/currentVersion.ssd").read()).strip() + " Console    | ")
print(" | Command console open. If you need info on commands \n | and how to use them, you can check the HOWTO.md \n | file at the root!")
print("_|_______________________________________________________\n")

commandTypes = {
    "$": "3-space simulation modification command",
    "?": "query request",
    "s": "setting modification"
}

while True:
    user = input("-")

    if user.split(" ")[0] in commandTypes.keys():
        print("Processing " + commandTypes[user.split(" ")[0]] + " ...")
    else:
        print('ERROR [ 1 ] "' + user.split(" ")[0] + '" is not a valid command type.')
