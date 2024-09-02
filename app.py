from flask import Flask, jsonify, request

import langCodecs.executePython
import langCodecs.executeC
import langCodecs.executeJava


app = Flask(__name__)

@app.route('/execute/C', methods=['POST'])
def ExecuteC():
    token = request.headers.get('clientId')
    code = request.get_json()['code']
    Result=langCodecs.executeC.compileAndExecuteC(token,code)
    return jsonify({'received': Result})

@app.route('/execute/python', methods=['POST'])
def ExecutePython():
    token = request.headers.get('clientId')
    code = request.get_json()['code']
    Result=langCodecs.executePython.compileAndExecutePython(token,code)
    return jsonify({'received': Result})

@app.route('/execute/java', methods=['POST'])
def ExecuteJava():
    token = request.headers.get('clientId')
    code = request.get_json()['code']
    Result=langCodecs.executeJava.compileAndExecuteJava(token,code)
    return jsonify({'received': Result})
if __name__ == '__main__':
    app.run(debug=True)
