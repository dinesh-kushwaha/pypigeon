from .constants import PIGEON_JSON,PG_PIGEON_SAMPLE_LISTENER_CODE

def init():
    with open('pigeon.json', 'w') as f:
            f.write(PIGEON_JSON)

    with open('pigeon.py', 'w') as f:
            f.write(PG_PIGEON_SAMPLE_LISTENER_CODE)