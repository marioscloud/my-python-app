from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # We use lightgreen for Version 2.0
    return """
    <div style="background-color: lightgreen; color: black; padding: 50px; text-align: center; font-family: sans-serif;">
        <h1>Hello! This is my own app running on Argo CD.</h1>
        <p style="font-size: 24px;">This is the version 2.0 of this python app.</p>
        <p style="font-size: 18px;">BlueGreen Deployment Strategy - Argo Rollouts</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
