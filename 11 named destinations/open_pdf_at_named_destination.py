import os
import subprocess

subprocess.Popen([r"C:PATHTOACROBAT.EXE", "/A", "nameddest=NAMEDDESTINATION", r"PATHTOPDF"],shell=True)