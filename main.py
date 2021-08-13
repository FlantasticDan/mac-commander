from flask import Flask
from deta import Deta

app = Flask(__name__)

deta = Deta()
db = deta('MACs')

