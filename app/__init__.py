import logging
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.ERROR)