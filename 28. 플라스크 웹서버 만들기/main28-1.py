# flask로 간단한 웹서버 만들고 구동하는 코드

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

def main():
    app.run(debug=True, port=80)
    
if __name__=='__main__':
    main()
# 코드를 직접 실행하면 __name__의 이름이 __main__이고, 코드가 모듈로 동작하면 모듈 이름이 된다.
# 따라서 코드를 직접 실행 시 위 조건은 참이다.