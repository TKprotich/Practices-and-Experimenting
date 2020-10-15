import os
path = "C:/"
for root, dirs, names in os.walk(path):
    for name in names:
        if "Current Session" in name:
            print(os.path.join(root, name))
