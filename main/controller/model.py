from api import api
from flask_restx import fields
from model.user import UserTypeEnum

user_model  = api.model('user', {
    'name' : fields.String,
    'email' : fields.String,
    'pswd' : fields.String,
    'user_type' : fields.String(description="User type", enum=[x.name for x in UserTypeEnum])
})