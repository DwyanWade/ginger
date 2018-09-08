"""
Created on 2018/6/9 16:31

"""
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

__Author__ = '阿强'

api = RedPrint('token')


@api.route('/get', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
