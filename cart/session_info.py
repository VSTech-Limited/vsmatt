from django.conf import settings


class SessionInfo:
    def __init__(self, request):
        self.session = request.session
        meta = self.session.get(settings.META_SESSION_ID)
        if not meta:
            meta = self.session[settings.META_SESSION_ID] = {}
        self.meta = meta

    def add(self, data: dict):
        self.meta.update(data)
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, key: str):
        if key in self.meta:
            del self.meta[key]
            self.save()

    def get(self, key: str):
        if key in self.meta:
            return self.meta[key]

    def pop(self, key):
        data = self.get(key)
        if data:
            self.remove(key)
            return data

    def clear(self):
        del self.session[settings.META_SESSION_ID]
        self.save()
