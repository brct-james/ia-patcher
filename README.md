# ia-patcher
 Idleon Armory Patcher
## Description
 Patches modded index.html file into Legends of Idleon (Steam).
## How to Use
 By default the index.html, patch.css, and patch.js files in the patchfiles directory will be patched into the game (note: you will need to editor your index.html to import patch.css and patch.js if you actually want to use them - the unmodified index.html is included). To patch other files edit the patchfiles list in ia-patcher.py (cli options coming) to include an ordered pair in the format [path to new file on disk, path to destination in archive]. This will destructively write over the existing game files by the same name (if they exist) so you may need to re-verify your game files if you mess up.