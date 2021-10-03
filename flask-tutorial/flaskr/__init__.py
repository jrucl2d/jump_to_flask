import os

from flask import Flask

# application factory 함수
def create_app(test_config=None):
    # 플라스크 인스턴스를 생성함
    # instance_relative_config는 instance 폴더에 대해서 config 파일이 상대적임
    # instance_path='/어쩌고/어쩌고폴더' 이렇게 설정 가능
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev', # 실제 배포환경에서는 다른 랜덤 문자열로 변경 필요
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # instance 폴더의 config.py가 존재하면 이걸 가져옴. 배포 환경의 실제 SECRET_KEY 따위.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # test config를 로드함
        app.config.from_mapping(test_config)

    # os.makedirs로 app.instance_path가 존재함을 ensure
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    # simple hello page
    @app.route("/hello")
    def hello():
        return 'Hello, World'

    return app