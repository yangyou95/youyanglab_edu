from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
import six

class UserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = six.text_type(user.id)
        ts = six.text_type(timestamp)
        is_active = six.text_type(user.active)
        return f"{user_id}{ts}{is_active}"

user_tokenizer = UserTokenGenerator()