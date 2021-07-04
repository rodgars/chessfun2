import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from match.cache import get_cache_store

class MatchFinderConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "match-finder-group"
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        self.score = int(self.scope['url_route']['kwargs']['score'])

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        cache = get_cache_store()
        key = cache.find_or_create_match(self.user_name, self.score)
        if key is not None:
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'group_message',
                    'message': {
                        'match_key': key,
                        'match': cache.get_cache(key)
                    }
                }
            )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def group_message(self, event):
        message = event['message']

        players = [
            message.get("match").get("player1"),
            message.get("match").get("player2")
        ]

        if self.user_name in players:
            self.send(text_data=json.dumps({
                'message': message
            }))

class MatchConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']

        self.send(data=json.dumps({
            'messsage': message
        }))
