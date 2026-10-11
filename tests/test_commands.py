import commands
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


def test_randka_pairs_two_random_chatters(monkeypatch):
    conn = DummyConnection()
    monkeypatch.setattr(commands.random, 'sample', lambda users, count: ['ania', 'ola'])

    process_command('!randka', conn, '#test', 'user', {'ania', 'ola', 'nightbot'}, {'nightbot'}, 'discord')

    assert conn.messages == [('#test', 'ania idzie na randke z ola BLACHARA')]


def test_randka_requires_two_non_ignored_chatters():
    conn = DummyConnection()

    process_command('!randka', conn, '#test', 'user', {'ania', 'nightbot'}, {'nightbot'}, 'discord')

    assert conn.messages == [('#test', 'Za mało osób na czacie żeby wybrać! ALERT')]


def test_randka_ignores_bots_case_insensitively(monkeypatch):
    conn = DummyConnection()
    monkeypatch.setattr(commands.random, 'sample', lambda users, count: users)

    process_command(
        '!randka',
        conn,
        '#test',
        'user',
        {'ania', 'ola', 'NightBot'},
        {'nightbot'},
        'discord',
    )

    assert conn.messages == [('#test', 'ania idzie na randke z ola BLACHARA')]


def test_kawa_pairs_two_random_non_bot_chatters(monkeypatch):
    conn = DummyConnection()

    def sample(users, count):
        assert set(users) == {'ania', 'ola'}
        assert count == 2
        return ['ania', 'ola']

    monkeypatch.setattr(commands.random, 'sample', sample)

    process_command(
        '!kawa',
        conn,
        '#test',
        'user',
        {'ania', 'ola', 'NightBot'},
        {'nightbot'},
        'discord',
    )

    assert conn.messages == [
        ('#test', 'ania chętnie wyskoczy na kawkę z ola peepoCoffee')
    ]
