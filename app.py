from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # HPA 작동 확인을 위해 환경 변수에서 Pod 이름을 가져옵니다.
    pod_name = os.environ.get('HOSTNAME', 'Unknown-Pod')
    return render_template('index.html', pod_name=pod_name, version="v1.8")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
