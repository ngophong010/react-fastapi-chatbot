import json
from redis.exceptions import ResponseError


class Cache:
    def __init__(self, json_client):
        self.json_client = json_client

    async def get_chat_history(self, token: str):
        data = await self.json_client.get(str(token))
        return json.loads(data) if data else None

    async def add_message_to_cache(self, token: str, source: str, message_data: dict):
        if source == "human":
            message_data['msg'] = "Human: " + (message_data['msg'])
        elif source == "bot":
            message_data['msg'] = "Bot: " + (message_data['msg'])

        data = await self.get_chat_history(token)
        if data:
            data['messages'].append(message_data)
            await self.json_client.set(str(token), json.dumps(data))
