import time

from flask import Flask, render_template, request
from deta import Deta

from util import normalize_mac_address

app = Flask(__name__)

deta = Deta()
status = deta.Base('Status')
command = deta.Base('Command')

@app.get('/mac/<mac_address>')
def mac_summary(mac_address):
    state = status.get(normalize_mac_address(mac_address, False))
    if state:
        return render_template('mac.html', mac=normalize_mac_address(mac_address), **state)
    return render_template('mac.html', mac=normalize_mac_address(mac_address), local='Unknown', public='Unknown', timestamp='Never')

@app.post('/ping')
def incoming_ping():
    payload = request.json
    summary = {
        'key': normalize_mac_address(payload['mac'], display=False),
        'local': payload['local'],
        'public': payload['public'],
        'timestamp': time.time()
    }
    status.put(summary)
    return 'OK'