import os
txt = "<RCC>\n    <qresource>\n"
cdir = os.path.dirname(__file__)
for subdir in ["icons", "ui", "translations"]:
    subpath = os.path.join(cdir, subdir)
    for f in sorted(os.listdir(subpath)):
        if f not in ["Arch.ts", "BIM.ts"]:
            txt += "        <file>" + subdir + "/" + f + "</file>\n"
txt += "    </qresource>\n</RCC>\n"
with open(os.path.join(cdir, "Arch.qrc"), "w") as resfile:
    resfile.write(txt)
    
