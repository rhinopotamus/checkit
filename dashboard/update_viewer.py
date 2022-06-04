import os, subprocess, glob, shutil, tempfile
from checkit.utils import working_directory

with working_directory("../viewer"):
    print("building viewer...")
    subprocess.run("npm run build".split(" "))

print('zipping up viewer')
with tempfile.TemporaryDirectory() as temporary_directory:
    copied_directory = shutil.copytree(
        os.path.join('..','viewer','dist'),
        temporary_directory,
        dirs_exist_ok=True,
    )
    os.remove(os.path.join(temporary_directory,"bank.json"))
    shutil.make_archive(
        os.path.join('src','checkit','static','viewer'),
        'zip',
        temporary_directory,
    )
