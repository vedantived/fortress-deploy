from flask import Flask

#"AKIA_FAKE_SECRET_123456" this aws pattern so gitleak not detect this now we change this for testing purpose
AWS_ACCESS_KEY_ID="AKIA_FAKE_SECRET_123456"

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Fortress Flask App"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
