import uuid
from enum import Enum

token_table_name = 'tokens'


class TokenContext(str, Enum):
    TokenID = 'token_id'
    Enabled = 'enabled'
    RedeemCode = 'redeem_code'
    DiscordID = 'discord_id'
    Groups = 'groups'
    ExtraReps = 'extra_reps'

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class Token:
    def __init__(self, redeem_code: str, discord_id: int, groups: [str], extra_reps: [str] = None):
        self.token_id = create_id()
        self.enabled = True
        self.redeem_code = redeem_code
        self.discord_id = discord_id
        self.groups = groups
        self.extra_reps = extra_reps

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        state = self.__dict__.copy()
        if not state['extra_reps']:
            del state['extra_reps']
        return state


def create_id() -> str:
    return str(uuid.uuid4())
