from devispora.ovo_tokens.model.token import Token
from devispora.ovo_tokens.model.token_request_info import TokenRequestInfo


def token_request_from_event(event_body: {}) -> TokenRequestInfo:
    print(event_body)
    print(f'is dict: {isinstance(event_body, dict)}')
    print(event_body['group_name'])
    new_info = TokenRequestInfo(
        requester_id=event_body['requester_id'],
        group_name=event_body['group_name']
    )
    if 'approved_ids' in event_body:
        new_info.approved_ids = event_body['approved_ids']
    return new_info


def create_token_from_token_info(redeem_code: str, token_info: TokenRequestInfo) -> Token:
    created_token = Token(
        redeem_code=redeem_code,
        discord_id=token_info.requester_id,
        groups=[token_info.group_name]
    )
    if hasattr(token_info, 'approved_ids'):
        created_token.extra_reps = token_info.approved_ids
    return created_token
