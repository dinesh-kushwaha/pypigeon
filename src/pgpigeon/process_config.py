
class PgChannel:
    def __init__(self, name, callbacks=[]) -> None:
        self.name: str = name if name else 'pg_pigeon_default_channel'
        self.callbacks: list[any] = callbacks if len(callbacks) else []

    def add_callback(self, callback):
        self.callbacks.append(callback)


class ProcessConfig:
    def __init__(self, name, channels=[]) -> None:
        self.name: str = name if name else 'pg_pigeon_default_channel'
        self.channels: list[PgChannel] = channels if len(channels) else []

    def add_callback(self, channel: PgChannel):
        self.channels.append(channel)
