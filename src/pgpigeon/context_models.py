import enum


class PgExecutionStrategy(enum.Enum):
    IN_SEPARATE_PROCESS = 1
    IN_SEPARATE_THREAD = 2


class PigeonChannelContext:
    def __init__(self, name, callbacks=[]) -> None:
        self.name: str = name if name else 'pg_pigeon_default_channel'
        self.callbacks: list[any] = callbacks if len(callbacks) else []

    def add_callback(self, callback):
        self.callbacks.append(callback)


class PigeonContext:
    def __init__(self, name, channels=[]) -> None:
        self.name: str = name if name else 'pg_pigeon_default_pigeon_context'
        self.channels: list[PigeonChannelContext] = channels if len(channels) else []
        self.execution_strategy: PgExecutionStrategy = PgExecutionStrategy.IN_SEPARATE_PROCESS
        self.is_main_on_hold: bool = False

    def add_callback(self, channel: PigeonChannelContext):
        self.channels.append(channel)
