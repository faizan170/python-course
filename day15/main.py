from flask import Flask
import tensorflow as tf
import cv2


app = Flask(__name__)

@app.route("/")
def main():
    return "App is working"

if __name__ == "__main__":
    app.run(host="0.0.0.0")