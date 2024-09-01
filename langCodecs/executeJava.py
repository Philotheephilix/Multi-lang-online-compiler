import os
import subprocess


#didnt test
def compileAndExecuteJava(client,codeString):
    try:
        with open(client+'.java','w') as javafile:
            javafile.write(codeString)
            compileScript=f"javac {client}.java"
            #executionScript=f"./"+client
            javafile.close()
        # os for compile and subprocess for execution
        os.system(compileScript)
        execute=subprocess.run(executionScript,capture_output=True,text=True)
        # cleaner 
        os.remove(client+'.c')
        os.remove(client)

        return execute.stdout
    except:
        return "Server Error"
