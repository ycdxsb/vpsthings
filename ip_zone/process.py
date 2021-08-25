import os
import json

ROOT_DIR = os.path.abspath('.')
RESULT_DIR = os.path.join(ROOT_DIR,'results')

results = []
for i in range(0,256):
    for j in range(0,256):
        filename = "%d.%d.json"%(i,j)
        p = os.path.join(RESULT_DIR,"%d"%i,filename)
        #print(p)
        with open(p,'r') as f:
            data = f.read()
        if data=="":
            continue
        result = json.loads(data)
        for _ in result:
            results.append(",".join(_))
        print(len(results))
with open("results.txt",'w') as f:
    f.write("\n".join(results))
