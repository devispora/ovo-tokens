

class TokenRequestInfo:

    def __init__(self, requester_id: int, group_name: str, approved_ids: [int] = None):
        self.requester_id = requester_id
        self.group_name = group_name
        self.approved_ids = approved_ids
