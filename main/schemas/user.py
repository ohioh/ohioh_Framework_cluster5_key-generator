from main import db, ma
from ..models.user import User


class UserSchema(ma.ModelSchema):

    class Meta:
        model = User
        sqla_session = db.session