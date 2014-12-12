1. app.yaml에 application 이름 등록
2. apps/settings.py에 SECRET_KEY, ADMIN, SQLALCHEMY_DATABASE_URI 수정
3. models.py에 class 수정
4. cmd에서 폴더 위치로 이동 후 python manger.py db init / python manager.py db migrate / python manager.py db upgrade
* such no revision 뜨면 drop alembic_version 