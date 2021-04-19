import tempfile
import shutil
import argparse
import ctypes, sys

from asarPy.asar import pack_asar, extract_asar

# parser arguments
parser = argparse.ArgumentParser()
parser.add_argument('-sp', '--steam-path', default="C:/Program Files (x86)/Steam/steamapps/common/Legends of Idleon/resources/app.asar")
parser.add_argument('-fs', '--file-set', nargs=2, action='append')
args = parser.parse_args()

def run():
    print(args)
    if args.file_set == None:
        print("No file-sets given, using default")
        patchfiles = [["patchfiles/index.html", "/distBuild/static/game/index.html"],["patchfiles/patch.css", "/distBuild/static/game/patch.css"],["patchfiles/patch.js", "/distBuild/static/game/patch.js"]]
    else:
        print(args.file_set)
        patchfiles = args.file_set
    
    steamasarpath = args.steam_path
    # extract files to temp, patch there, repackage
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        archivepath = tmpdirname + "/asar"
        extract_asar(steamasarpath, archivepath)
        print('extracted asar from', steamasarpath)

        # list of ordered pairs in the format [path to new file on disk, path to destination in archive]
        for i in patchfiles:
            try:
                newfile = i[0]
                destpath = archivepath + i[1]
                shutil.copy(newfile, destpath)
                print('copied', newfile, 'to replace', i[1])
            except:
                print('error while coping', newfile, 'to replace', i[1], "in temp archive", archivepath)
                input("Press enter to acknowledge")
        print('finished patching, packing new asar')
        pack_asar(archivepath, "C:/Users/green/Documents/GitHub/ia-patcher/newapp.asar")
        #steamasarpath
        input('finished patch, press any key to close')

# handle UAC elevation
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    run()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
