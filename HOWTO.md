# How to Use the Sandsea Simulation Engine  
This is a step-by-step instructional guide to creating your own simulation and using the engine.
### Regarding updates  
Keep in mind that this document might update at a slightly different rate/time than the engine, but the team will keep this as relevant as possible! Don't
expect any of the core features to change, but when they do, check the `UPDATES` folder and look at the most recent update to check if any semantics or nitty-gritty bits
have changed, or maybe if a feature was added/tweaked.
### Regarding .SSD (*S*and*S*ea*D*ata) files  
Edit the code all you want; worst-case-scenario you can redownload the engine and reload your auto-backups. .SSD files are encrypted pieces of data that allow Sandsea to
run properly. The version number, backup location, and similar data are all stored under .SSDs. While I think it's ok for you to edit other files for compatibility on your
device, it's not recommended that you edit these files because it might break the engine. (quite possibly the backups too - say goodbye to your simulations.)
### Sandsong Syntax  
#### $ new <object, force, rule>
Used to create a new item, be that an object, force, rule, or other simulation parameter.
- `$ new object`
  - `$ new object cuboid <start coords> <end coords> <material> <connect, default true>` - Creates a new cuboid object in the simulation of the specified material (under the `material` parameter). The cuboid is rendered as the start and end coords being coordinates opposite each other on the cuboid, the start coordinate being closest to (0,0,0) and the end coordinate being the farthest. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
  - `$ new object sphere <center> <radius> <material>, <connect, default true>` - Creates a new sphere object in the simulation of the specified material (under the `material` parameter). The sphere is rendered as the radius extending from the center coordinates, as one would expect. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
