# Copyright 2021 Jacob Bodell

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os

def stringify(list):
   o = ""
   for x in list: o = o + x
   return o

# Auto-compile working directory
wdir = stringify(sys.argv[0].split("engine/")[0].split("init.py"))
# Get the directory of this script, then remove the SANDSEA
# extension directory from it to get the directory of the
# Sandsea folder.

def getSSD(ssdName):
   return open(wdir + str(ssdName) + ".ssd", "r").read()

def getSSLC(directory):
   allFiles = [f for f in os.listdir(directory) if os.isfile(os.join(directory, f))]
   configFiles = [cf for f in allFiles if str(f).split(".")[1] == "sslc"]
   for x in configFiles:
      if str(f).split(".")[2] == "ante":
         exec(open(f, "r").read())
   for x in configFiles:
      if str(f).split(".")[2] == "post":
         exec(open(f, "r").read())

print(f"\nSANDSEA Console v{getSSD('currentVersion')}\nType 'help' for a list of commands, and type 'q' to quit.")
while True:
   user = input(wdir + "SANDSEA>")
   cmd = user.split(" ")
   ctype = list(user)[0]
   if user == "q":
      print("Exiting ...")
      exit()
   if ctype == "@":
      if stringify(list(cmd[1:-1])) != "null":
         getSSLC(stringify(list(cmd[1:-1])))
