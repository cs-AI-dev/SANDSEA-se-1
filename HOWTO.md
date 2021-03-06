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
## Console Syntax  
In console syntax, capitalization does not matter except in parameters
- `@<directory>``
  - `@<directory> load <filename> <x, default 0> <y, default 0> <z, default 0> <overlap, default "connect" from "connect", "deleteExisting", "deleteNew", "deletePartialHollow", "deletePartialSolid>` - Loads a file into the simulation. The lower northeastern (least X, Y, and Z) corner of the loaded simulation is copied and placed in the coordinates described in the `x`, `y`, and `z` parameters accordingly. If you don't provide those parameters then they default to 0. If the copied simulation parts overlap with existing ones, then the simulation corrects the clipping in one of three ways, defined by the `overlap` parameter. `connect` will merge overlapped objects. `deleteExisting` will delete objects in the original simulation that the copied parts overlap with, whereas `deleteNew` will effectively only paste objects if they do not overlap with an existing object, deleting pasted objects if they do overlap. In addition, `deletePartialHollow` will paste all objects, deleting parts of pasted object that intersect with existing objects, while `deletePartialSolid` will delete parts of existing objects that intersect with pasted ones. The copy/paste function is also executed in the native directory given under `directory`; local `.sslc` configuration files will be executed before (config.sslc.ante) and/or after (config.sslc.post) the copy/paste is executed.
  - `@<directory> exec <filename>` - Executes the simulation found under the folder given in the `directory` parameter and in the filename given under the `filename` parameter. The current simulation is erased; if it wasn't saved it is automatically saved as an untitled simulation (UntitledSimulation.song unless the default untitled name was changed). The native directory given under `directory` will cause the system to execute configuration files before (config.sslc.ante) and/or after (config.sslc.post) the file is executed.
  - `@<directory> copy <copyFilename> <pasteFilename> <overwrite, default "add" from "overwrite", "writeNew", "add">` - Copies the file from `copyFilename` to `pasteFilename` directly. Trailing whitespace is stripped. The `overwrite` parameter determines how the copy works: `overwrite` will delete any existing file in place of the copied one, `writeNew` will create a new paste file with the same name as the existing one (numbers added), and `add` will open the existing file, write a new line, and then paste the copied file onto the existing one. Configurations found in the native directory under `directory` will be executed before (config.sslc.ante) and/or after (config.sslc.post) the copy/paste is executed.
  - `@<directory> backup <fileName> to <backupFileName>` - Backs up files from `filename` to `backupFilename`.

## Sandsong Syntax  
Note: When I talk about a coordinate parameter, you define that like this: `{ <x> <y> <z> ... }`. I put it that way because then you can change the simulation to 4+ or 2 dimensions, and writing it out like that allows you to prepare hypercubes using the regular cube command instead of a whole different hyperdimensional syntax.

### Simulation Control

- `$ define object`
  - `$ define object cuboid <name> with <start coordinates> <end coordinates> <material, default simulo> <connect, default true> ;` - Creates a new cuboid object in the simulation of the specified material (under the `material` parameter). The cuboid is rendered as the start and end coordinates being coordinates opposite each other on the cuboid, the start coordinate being closest to (0,0,0) and the end coordinate being the farthest, and as a function that collides with an object if any part of the object is within the range of each coordinate of the vertices. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
  - `$ define object sphere <name> with <center> <radius, default 0> <material, default simulo> <connect, default true> ;` - Creates a new sphere object in the simulation of the specified material (under the `material` parameter). The sphere is rendered as the radius extending from the center coordinates, as one would expect, and as a function that collides with an object if any part of the object is equal to or less than a number of units equal to the radius away from the center of the sphere. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
  - `$ define object ellipsoid <name> with <radii for each dimension, default 0> <material, default simulo> <connect, default true> ;` - Creates a new ellipsoid object in the simulation of the specified material (under the `material`). The ellipsoid is rendered as a spheroid, being extended in a direction based on which axis the coordinate is for - the X-axis is extended by the X-radius, the Y by the Y, etc., and as a function that collides with an object if any part of the object is inside the Z-coord-modified elliptical function. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
  - `$ define object cylinder <name> with <base coordinates> <radius, default 0> <height, default 0> <axis, default z> <material, default simulo> <connect, default true> ;` - Creates a new cylinder object in the simulation of the specified material (under the `material` parameter). The cylinder is rendered as the base extended by the radius and height (which MUST BE POSITIVE) and which collides with an object if the object is within a circular function and within a range along the selected axis under `axis` parameter. The `connect` parameter defines if the cuboid automatically merges with other objects that would be touching or inside of it during its generation, and is defaulted to `true`.
- `$ define simple`
  -  `$ define simple point <name> at <coords> ;` - Defines a point at the specified coordinates. If those coordinates would be referenced again, then they are referred to as the name of the point, defined under the `name` parameter.
  -  `$ define simple ray <name> at <startCoords> end <endCoords> ;` - Draws a ray with an endpoint at the coordinates defined under `startX`, `startY`, and `startZ` that is collinear with the endpoint defined under `endX`, `endY`, and `endZ`.
  -  `$ define simple line <name> at <startCoords> <endCoords> ;` - Draws a line that is collinear with points defined in the coordinate parameters.
- `$ define effect`
  - `$ define effect linearGravity add <axis> <strength> <name> ;` - Adds a linear gravity effect to the simulation.
  - `$ define effect linearGravity remove <name> ;` - Removes a linear gravity effects from the simulation.
  - `$ define effect wellGravity add <coords> <strength> <name> ;` - Adds a gravity well to the simulation at the point described.
  - `$ define effect wellGravity remove <name> ;` - Removes a gravity wells from the simulation.
  - `$ define effect universalGravity <axis> <strength> ;` - Sets the universal gravity.
  - `$ define effect universalGravity reset ;` - Resets the universal gravity to 0 m/s/s and to the X axis.
  - `$ define effect magnetism magneticDipole <positiveCoords> <negativeCoords> <strength> <name> ;` - Adds a magnetic field to the simulation with the requested strength, the positive and negative poles placed at the coordinates described. If `strength` is negative, then it switches the poles.
  - `$ define effect magnetism positiveMonopole <coords> <strength> <name> ;` - Adds a positive monopole with the given strength at the coordinates described.
  - `$ define effect magnetism negativeMonopole <coords> <strength> <name> ;` - Adds a negative monopole with the given strength at the coordinates described.
  - `$ define effect magnetism remove <name> ;` - Removes any magnetic effect from the simulation.
  - `$ define effect darkMatter <default coords from coordinates or universal> <strength> <name> ;` - Adds a dark matter effect to the simulation. Dark matter effects come in two types, defined by the `coords` parameter - *Coordinate* DM effects and *Universal* DM effects. Coordinate effects gradually push all objects away from the set coordinates with an equal force. Universal effects push all objects away from the simulation's own center of gravity. Beware, both of these effect types ***will*** reduce simulation speed.
  - `$ define effect darkMatter remove <name> ;` - Removes a dark matter effect from the simulation.

### Logic & Standard Programming

###

#### Variables
Variables are defined in Sandsong as follows.
- `variable <name> = <value> ;` - Defines a variable with name as described under `name` as an integer, float number, string, or an instance of object. Can't define lists, sets, dictionaries or functions. The `=` is necessary.
- `list <name> = { <elements> } ;` - Defines a list with all values inside the `elements` parameter. The elements should be separated with commas, so a list named list1 containing integers 1, 2, and string "Hello" would be described as `list list1 = { 1,2,"Hello" } ;`.
- `set <name> = { <elements> } ;` - Defines a set as the sytem would define a list. Sets are identical to lists, except that the elements are impermeable.
- `delete <name> ;` - Deletes a variable from the simulation backend.

#### Logic
Logic and Boolean values are assembled like this.
- `not { <condition> }` - Returns **True** if `condition` is **False** and vice versa.
- `{ <condition1> } and { <condition2> }` - Returns **True** if and only if both `condition1` and `condition2` return **True**, otherwise returns **False**.
- `{ <condition1> } or { <condition2> }` - Returns **True** if either `condition1` or `condition2` return **True**.
- `xor { <conditions> }` - Returns **True** if and only if exactly one of the conditions described under `conditions` returns **True**. Conditions should be separated by commas, so a `xor` statement with conditions `c1`, `c2`, and `c3` (the statement accepts any number of arguments) will be written as `xor { c1,c2,c3 }`.
- `event occurred { <event> }` - Returns **True** if and only if an event
If, while, until, and
