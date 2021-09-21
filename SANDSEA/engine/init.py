import sys

# Auto-compile working directory
wdir = sys.argv[0].split("/SANDSEA/engine/init.py")[0]
# Get the directory of this script, then remove the SANDSEA
# extension directory from it to get the directory of the
# Sandsea folder.

def getSSD(ssdName):
   return open(wdir + str(ssdName) + ".ssd", "r").read()

print(f"SANDSEA Console v{getSSD("currentVersion")}\nType {'"help"'} for a list of commands, and type {'"q"'} to quit.")
while True:
   user = input(wdir + "SANDSEA>")
   cmd = user.split(" ")
   cType = list(user)[0]
   if user == "q":
      print("Exiting ...")
      exit()
   
