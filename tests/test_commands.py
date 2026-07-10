from commands import process_command


class DummyConnection:
    def __init__(self):
        self.messages = []

    def privmsg(self, channel, message):
        self.messages.append((channel, message))


def test_princespolo_does_not_match_princess():
    conn = DummyConnection()
    process_command('!princespolo', conn, '#test', 'user', [], set(), 'discord')

    assert conn.messages == []
