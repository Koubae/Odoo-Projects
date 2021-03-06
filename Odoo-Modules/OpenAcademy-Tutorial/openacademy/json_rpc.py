import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'openacademy'
USER = 'admin'
PASS = 'admin'


def json_rpc(url, method, params):

    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1_000_000_000),
    }

    req = urllib.request.Request(url=url, data=json.dumps(data).encode(),
                                headers={"Content-Type": "application/json", })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))

    if reply.get("error"):
        raise Exception(reply['error'])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# Log in the Given DB
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

args = {
    'color': 8,
    'memo': "This is another node", 
    'create_uid': uid,
}
note_id = call(url, "object", "execute", DB, uid, PASS, 'node.node', 'create', args)