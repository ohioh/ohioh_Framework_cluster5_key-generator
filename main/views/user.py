from flask_restful import Resource
from flask import request, jsonify
from flask_http_response import result, error

from main import db
from ..models.user import User
from ..schemas.user import UserSchema


class UserView(Resource):
    
    def get(self):
        page = request.args.get('page', 1)
        page_size = request.args.get('page_size', 10)
        users = User.query.filter_by()

        paginated_data = users.order_by(User.id.desc()).paginate(page, page_size, error_out=False)
        response = UserSchema(many=True).dump(paginated_data.items)
        payload = {
            'current_page': paginated_data.page,
            'page_size': paginated_data.per_page,
            'total_count': paginated_data.total,
            'results': response
        }
        return result.return_response(payload)

    def post(self):
        request_data = request.get_json()
        user = User(**request_data)
        db.session.add(user)
        db.session.commit()
        db.session.flush()
        response = UserSchema().dump(user)
        return result.return_response(response, 201) 