import os
import subprocess
import time

#didnt test
def compileAndExecuteJava(client,codeString):
    try:
        with open(client+'.java','w') as javafile:
            javafile.write(codeString)
            compileScript=f"javac {client}.java"
            executionScript=['java',client]
            javafile.close()
        # os for compile and subprocess for execution
        os.system(compileScript)
        strt=time.perf_counter()
        execute=subprocess.run(executionScript,capture_output=True,text=True)
        end=time.perf_counter()-strt
        # cleaner       
        os.remove(client+'.java')
        os.remove(client+".class")

        return [execute.stdout,end*1000] # OUTPUT and Execution time in ms
    except:
        print(execute)
        return "Server Error"
