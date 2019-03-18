## Multi Block Generator
This script can convert structure.nbt file into multi_block_detection.mcfunction file.  

### About
This program will read any .nbt file inside folder `input/` and convert it into .mcfunction file inside folder `output/`, the program also take child directory into account as well so if you generate it from `input/path/to/structure/file.nbt` it'll generate that file to `output/path/to/structure/file.mcfunction`  
![You're trying to view an image but something went wrong](https://i.imgur.com/tOicp2C.png)  
![You're trying to view an image but something went wrong](https://i.imgur.com/8sYDyrF.png)

### Output File
The mcfunction file that generate from this program required 1 scoreboard objective `bb.success dummy` but you can use replace function in your text editor to change this.  
To determined if your multi block test pass or not you have to check if the entity that's running this command have tag given from this function or not.
![You're trying to view an image but something went wrong](https://i.imgur.com/7ksQeYm.png)  
In this case if this entity have tag `nature_aura.structure.init.enchanting_alter` that mean it pass multi block test (yay!)

## Requirements
1) [Python 3](https://www.python.org/downloads/)
2) [NBTlib](https://pypi.org/project/nbtlib/)
3) Command Prompt, Terminal or any kind of command line interface
4) Structure files

## Installation
1) Install Python 3 like how you usually install a program.
2) Install NBTlib, this one is a bit difference you have to open Terminal and type `pip install NBTlib`, make sure that you do this after you install Python.
3) Use the same Terminal that you use to install NBTlib and change directory to where the program is. Using `cd path/to/directory` command.
4) Prepare your structure files inside `input/` folder.
5) Run the program, `python multi_block_converter.py`.