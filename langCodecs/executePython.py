import os
import subprocess


#didnt test
def compileAndExecutePython(client,codeString):
    try:
        with open(client+'.py','w') as pythonFile:
            pythonFile.write(codeString)
            runScript=f"python3 {client}.py"
            #executionScript=f"./"+client
            pythonFile.close()
        # os for compile and subprocess for execution
        execute=subprocess.run(runScript,capture_output=True,text=True)
        # cleaner 
        os.remove(client+'.c')
        os.remove(client)

        return execute.stdout
    except:
        return "Server Error"
