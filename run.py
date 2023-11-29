from app import create_app, db
from flask_pydantic_spec import FlaskPydanticSpec

run = create_app()
spec = FlaskPydanticSpec('flask', title='CRUD API')
spec.register(run)


if __name__ == '__main__':
    with run.app_context():
        db.create_all()
    run.run(debug=True)