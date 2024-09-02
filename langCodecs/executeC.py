import os
import subprocess
import time

def compileAndExecuteC(client,codeString):
    try:
        with open(client+'.c','w') as C:
            C.write(codeString)
            compileScript=f"gcc {client}.c -o {client}"
            executionScript=f"./"+client
            C.close()
        # os for compile and subprocess for execution
        os.system(compileScript)
        strt=time.perf_counter()
        execute=subprocess.run(executionScript,capture_output=True,text=True)
        end=time.perf_counter()-strt
        # cleaner 
        os.remove(client+'.c')
        os.remove(client)

        return [execute.stdout,end*1000]
    except:
        return "Server Error"
