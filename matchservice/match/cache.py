import uuid, base64
from django.core.cache import cache

def get_cache_store():
    return Cache()

class Cache:

    def _gen_key(self, user_name: str, score: int):
        return f"{int(score / 100) * 100}_{user_name}"

    def _gen_key_range(self, key: str, range: int):
        kscore = int(key.split("_")[0]) + range
        return f"{key.split('_')[1]}_{kscore}"

    def _match_key_in_store(self, key: str):
        scan = key.split("_")[0]
        keys = cache.keys(f"{scan}_*")
        return keys[0] if keys else None

    def _get_match_key(self, key: str):
        keys = [
            key,
            self._gen_key_range(key, -100),
            self._gen_key_range(key, 100)
        ]

        match_key = None

        for k in keys:
            match_key = self._match_key_in_store(k)
            if match_key is not None:
                break

        return match_key

    def get_cache(self, key):
        return cache.get(key)

    def set_cache(self, key, value):
        return cache.set(key, value, timeout=10000)

    def find_or_create_match(self, user_name: str, score: int):
        key = self._gen_key(user_name, score)
        match_key = self._get_match_key(key)
        if match_key is not None:
            match_val = self.get_cache(match_key)
            match_val["player2"] = user_name
            self.set_cache(match_key, match_val)
        else:
            match = {
                "player1": user_name,
                "player2": None,
                "match_id": base64.urlsafe_b64encode(uuid.uuid1().bytes).rstrip(b'=').decode('ascii'),
            }
            self.set_cache(key, match)

        return match_key





