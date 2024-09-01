import os
import subprocess

def compileAndExecuteC(client,codeString):
    try:
        with open(client+'.c','w') as C:
            C.write(codeString)
            compileScript=f"gcc {client}.c -o {client}"
            executionScript=f"./"+client
            C.close()
        # os for compile and subprocess for execution
        os.system(compileScript)
        execute=subprocess.run(executionScript,capture_output=True,text=True)
        # cleaner 
        os.remove(client+'.c')
        os.remove(client)

        return execute.stdout
    except:
        return "Server Error"
