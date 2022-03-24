
import secrets

from devispora.ovo_tokens.model.helper.token_helper import create_token_from_token_info, token_request_from_event
from devispora.ovo_tokens.service.dynamodb_service import process_token_creation


def generate_redeem_code(event_body: {}):
    redeem_code = secrets.token_urlsafe(15)
    token_info = token_request_from_event(event_body)
    new_token = create_token_from_token_info(redeem_code, token_info)
    response = process_token_creation(new_token)
    print(f'dynamodb response next')
    print(response)
    # check token response if ok or not
    # create shittonne of tests
    return redeem_code
