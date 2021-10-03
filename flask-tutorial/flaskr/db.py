import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

"""
g
하나의 request에 걸쳐서 데이터를 저장하기 좋은 장소.
request 진행 중에 여러 함수에서 접근 가능.

이곳에서는 g 안에 db connection을 저장해서 같은 요청에서는 같은 db connection을 사용

current_app
현재의 request를 처리하는 어플리케이션에 대한 프록시.
import 없이 어플리케이션에 접근하기 좋다.
"""

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_COLNAMES
        )
        g.db.row_factory = sqlite3.Row # dict 타입으로 결과를 리턴받을 수 있음

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

"""
flask cli로 생성됨. flask init-db 실행하면 '데이터베이스 init...' 문자열이 출력되고
instance 폴더와 sqlite 파일이 생성됨.
"""

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('데이터베이스 init...')

def init_app(app):
    app.teardown_appcontext(close_db) # 응답 후 cleaning up 할 때 메소드 실행
    app.cli.add_command(init_db_command)