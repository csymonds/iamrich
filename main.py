import json

import quart
import quart_cors
from quart import request


app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.get("/iamrich.jpg")
async def plugin_logo():
    filename = 'iamrich.jpg'
    return await quart.send_file(filename, mimetype='image/jpg')

@app.get("/iamrich")
async def get_rich():
    return quart.Response("![I am rich](http://www.cjsymonds.com/iar/iamrich.jpg)", mimetype="text/json")

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()