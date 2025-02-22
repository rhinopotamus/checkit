import importlib.resources
import subprocess, os, tempfile, shutil
from ..utils import working_directory

def sage(outcome,output_path,amount=1000,preview=True,images=False):
    """
    Wraps generator and builds to a seeds.json file at output_path
    """
    if preview:
        preview_s = "preview"
    else:
        preview_s = "build"
    if not os.path.isfile(outcome.generator_path()):
        raise FileNotFoundError(outcome.generator_path())
    with importlib.resources.path("checkit.wrapper", "wrapper.sage") as wrapper_path:
        with tempfile.TemporaryDirectory() as tmpdir:
            shutil.copyfile(wrapper_path,os.path.join(tmpdir,"wrapper.sage"))
            with working_directory(outcome.bank.abspath()):
                cmds = [
                    "sage",
                    os.path.join(tmpdir,"wrapper.sage"), #arg index 0
                    outcome.generator_path(), #1
                    output_path, #2
                    preview_s, #3
                    str(amount), #4
                ]
                if images:
                    cmds += ["images"] #5
                subprocess.run(cmds,check=True)
