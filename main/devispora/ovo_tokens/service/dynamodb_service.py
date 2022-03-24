import boto3
from devispora.ovo_tokens.model.token import token_table_name, Token, TokenContext

dynamodb = boto3.resource('dynamodb')


class DynamoDBService:
    pass


def process_token_creation(token: Token):
    item = create_item(token)
    store_token(item)


def store_token(item):
    table = dynamodb.Table(token_table_name)
    response = table.put_item(
        Item=item
    )
    return response


def create_item(token: Token):
    token_context = {
        TokenContext.TokenID: token.token_id,
        TokenContext.Enabled: token.enabled,
        TokenContext.RedeemCode: token.redeem_code,
        TokenContext.DiscordID: token.discord_id,
        TokenContext.Groups: token.groups,
        TokenContext.ExtraReps: token.extra_reps
    }
    if token_context[TokenContext.ExtraReps] is None:
        del token_context[TokenContext.ExtraReps]

    return token_context
