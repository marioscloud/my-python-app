from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # We use a blue color for Version 1.0
    return """
    <div style="background-color: #007bff; color: white; padding: 50px; text-align: center; font-family: sans-serif;">
        <h1>Hello! This is my own app running on Argo CD.</h1>
        <p style="font-size: 24px;">This is the version 1.0 of this python app.</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
