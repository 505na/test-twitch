import random
import logging
import os
import sys

logger = logging.getLogger("TwitchBot")


def handle_test(connection, channel, username, chatters, ignored_users):
    """!test - Bot test command"""
    connection.privmsg(channel, "✅ Bot działa!")


def handle_buu(connection, channel, username, chatters, ignored_users):
    """!buu - Scare a random chatter"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma kogo wystraszyć! sadCat")
        return
    connection.privmsg(channel, f"{username} straszy {target}! aaaa")


def handle_fmk(connection, channel, username, chatters, ignored_users):
    """!fmk - Fuck Marry Kill game"""
    valid_users = [u for u in chatters if u not in ignored_users and u != username]
    if len(valid_users) < 3:
        connection.privmsg(channel, "Potrzeba minimum 3 osób! ALERT")
        return
    users = random.sample(valid_users, 3)
    connection.privmsg(
        channel,
        f"fuck - {users[0]} Segz, "
        f"marry - {users[1]} peepoLove, "
        f"kill - {users[2]} Deadge"
    )


def handle_hug(connection, channel, username, chatters, ignored_users):
    """!hug - Give a hug"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma nikogo do przytulenia! sadCat")
        return
    connection.privmsg(channel, f"{username} serdecznie przytula {target} hugg")


def handle_kiss(connection, channel, username, chatters, ignored_users):
    """!kiss - Give a kiss"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma komu dać buziaka! sadCat")
        return
    connection.privmsg(
        channel,
        f"{username} daje buzaka w czółko dla {target} catKISS"
    )


def handle_bite(connection, channel, username, chatters, ignored_users):
    """!bite - Bite a random chatter"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma kogo ugryźć! sadCat")
        return
    connection.privmsg(
        channel,
        f"{username} gryzie {target}! CatBite "
    )


def handle_myszka(connection, channel, username, chatters, ignored_users):
    """!myszka - Random chatter becomes mouse of the day"""
    target = get_random_chatter(chatters, ignored_users)
    if not target:
        connection.privmsg(channel, "Za mało osób żeby wybrać! ALERT ")
        return
    connection.privmsg(channel, f"Dzisiejszą myszką zostaje {target} ohCute")


def handle_makowiec(connection, channel, username, chatters, ignored_users):
    """!makowiec - Random chatter eats a makowiec"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nikt nie je makowaca !")
        return
    connection.privmsg(channel, f"{target} wpierdala makowca monkaO")


def handle_ship(connection, channel, username, chatters, ignored_users):
    """!ship - Ship two random chatters"""
    valid_users = [u for u in chatters if u not in ignored_users]
    if len(valid_users) < 2:
        connection.privmsg(channel, "Za mało osób na czacie! ALERT")
        return
    user1, user2 = random.sample(valid_users, 2)
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"Ship {user1} z {user2} ma {percent}% Sure")


def handle_60(connection, channel, username, chatters, ignored_users):
    """!60 - Random chatter becomes sixtieth of the day"""
    target = get_random_chatter(chatters, ignored_users)
    if not target:
        connection.privmsg(channel, "Za mało osób żeby wybrać! ALERT ")
        return
    connection.privmsg(channel, f"Sześćdziesioną dzisiejszego dnia zostaje {target} monkaO")


def handle_dekiel(connection, channel, username, chatters, ignored_users):
    """!dekiel - Random chatter becomes dekiel of the day"""
    target = get_random_chatter(chatters, ignored_users)
    if not target:
        connection.privmsg(channel, "Za mało osób żeby wybrać! ALERT ")
        return
    connection.privmsg(channel, f"Deklem dzisiejszego dnia zostaje {target} xdx")


def handle_aura(connection, channel, username, chatters, ignored_users):
    """!aura - Get today's aura"""
    aura = random.randint(-2, 1000)
    connection.privmsg(channel, f"{username} ma dzisiaj {aura} Aury baseg")


def handle_iq(connection, channel, username, chatters, ignored_users):
    """!iq - Get today's IQ"""
    iq = random.randint(-2, 200)
    connection.privmsg(channel, f"{username} masz {iq} iq Nerdge")


def handle_cmd(connection, channel, username, chatters, ignored_users):
    """!cmd - List all commands"""
    connection.privmsg(
        channel,
        "!test | !buu | !fmk | !hug | !kiss | !bite | !myszka | !makowiec | !ship | !60 | !dekiel | !aura | !iq | !gay | !cute | !adopt | !redflag | !greenflag | !jealous | !romantic | !princess | !prince | !princepałki | !princessa | !princepolo | !branie | !randka | !kawa | !cmd | !dc | !classic | !urlop | !reload | !update"
    )


def handle_dc(connection, channel, username, chatters, ignored_users, discord_link):
    """!dc - Discord link"""
    connection.privmsg(channel, f"Zapraszam na Discorda! {discord_link}")


def get_random_chatter(chatters, ignored_users, exclude_user=None):
    """Get a random chatter, optionally excluding a user"""
    valid_users = [
        u for u in chatters
        if u not in ignored_users
        and u != exclude_user
    ]
    if not valid_users:
        return None
    return random.choice(valid_users)


def handle_gay(connection, channel, username, chatters, ignored_users):
    """!gay - Dzisiejszym gejem jest user"""
    target = get_random_chatter(chatters, ignored_users)
    if not target:
        connection.privmsg(channel, "Za mało osób żeby wybrać! ALERT")
        return
    connection.privmsg(channel, f"Dzisiejszym gejem zostaje {target} Gayge")


def handle_cute(connection, channel, username, chatters, ignored_users):
    """!cute - user jest w % słodki"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% słodki/a SoCute ")


def handle_adopt(connection, channel, username, chatters, ignored_users):
    """!adopt - user adoptuje user"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma kogo adoptować! ALERT")
        return
    connection.privmsg(channel, f"{username} adoptuje {target} :d ")


def handle_redflag(connection, channel, username, chatters, ignored_users):
    """!redflag - user jest w % redflagiem"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% redflagiem redFLG ")


def handle_greenflag(connection, channel, username, chatters, ignored_users):
    """!greenflag - user jest w % greenflagiem"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% greenflagiem greenFLG ")


def handle_jealous(connection, channel, username, chatters, ignored_users):
    """!jealous - user jest w % zazdrosny o user"""
    target = get_random_chatter(chatters, ignored_users, username)
    if not target:
        connection.privmsg(channel, "Nie ma o kogo być zazdrosnym! ALERT")
        return
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% zazdrosny/a o {target} catLook ")


def handle_romantic(connection, channel, username, chatters, ignored_users):
    """!romantic - user jest w % romantyczny"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% romantyczny/a  Romantic ")


def handle_Princess(connection, channel, username, chatters, ignored_users):
    """!Princess - user jest w % księżniczką"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% księżniczką princess ")


def handle_Prince(connection, channel, username, chatters, ignored_users):
    """!Prince - user jest w % księciem"""
    percent = random.randint(0, 100)
    connection.privmsg(channel, f"{username} jest {percent}% księciem prince ")

def handle_branie(connection, channel, username, chatters, ignored_users):
    """!branie - randomuser ma branie na randomuser"""
    valid_users = [u for u in chatters if u not in ignored_users]
    if len(valid_users) < 2:
        connection.privmsg(channel, "Za mało osób na czacie żeby wybrać! ALERT")
        return
    user1, user2 = random.sample(valid_users, 2)
    connection.privmsg(channel, f"{user1} ma branie na {user2}! onniewie ")


def handle_randka(connection, channel, username, chatters, ignored_users):
    """!randka - Two random chatters go on a date"""
    ignored_users_lower = {u.lower() for u in ignored_users}
    valid_users = [u for u in chatters if u.lower() not in ignored_users_lower]
    if len(valid_users) < 2:
        connection.privmsg(channel, "Za mało osób na czacie żeby wybrać! ALERT")
        return
    user1, user2 = random.sample(valid_users, 2)
    connection.privmsg(channel, f"{user1} idzie na randke z {user2} BLACHARA")


def handle_kawa(connection, channel, username, chatters, ignored_users):
    """!kawa - Two random chatters go for coffee"""
    ignored_users_lower = {u.lower() for u in ignored_users}
    valid_users = [u for u in chatters if u.lower() not in ignored_users_lower]
    if len(valid_users) < 2:
        connection.privmsg(channel, "Za mało osób na czacie żeby wybrać! ALERT")
        return
    user1, user2 = random.sample(valid_users, 2)
    connection.privmsg(
        channel,
        f"{user1} chętnie wyskoczy na kawkę z {user2} peepoCoffee",
    )


def handle_classic(connection, channel, username, chatters, ignored_users):
    """!classic - user samo się klikło Kek """
    connection.privmsg(channel, f"{username} samo się klikło Kek ")

def handle_urlop(connection, channel, username, chatters, ignored_users):
    """!urlop - ide na urlop """
    connection.privmsg(channel, f" ide na urlop :b  ")


def handle_princepałki(connection, channel, username, chatters, ignored_users):
    """!princepałki - Special prince response"""
    connection.privmsg(channel, f"{username} IDZ I SE KUP! Clap")


def handle_princessa(connection, channel, username, chatters, ignored_users):
    """!princessa - Special princess response"""
    connection.privmsg(channel, f"{username} NIE MAM, KUP SE! Clap")


def handle_princepolo(connection, channel, username, chatters, ignored_users):
    """!princepolo - Special prince response"""
    connection.privmsg(channel, f"{username} NIE MAM, IDZ I SE KUP! Clap")


def handle_reload(connection, channel, username, streamer, tags):
    """!reload - Reload the bot (streamer and mods only)"""
    # Check if user is streamer or moderator
    is_streamer = username == streamer
    is_mod = tags.get('mod') == '1'
    is_broadcaster = tags.get('badges', '').find('broadcaster') != -1
    
    if not (is_streamer or is_mod or is_broadcaster):
        connection.privmsg(channel, f"Nie masz uprawnień! Tylko streamer i moderacja mogą przeładować bota.")
        return
    
    logger.info(f"[RELOAD] Bot przeładowywany przez {username}")
    connection.privmsg(channel, f"Przeładowuję bota... DankMods")
    
    # Restart the bot
    os.execl(sys.executable, sys.executable, sys.argv[0])


def handle_update(connection, channel, username, streamer, tags):
    """!update - Pull latest changes and restart the bot (streamer and mods only)"""
    is_streamer = username == streamer
    is_mod = tags.get('mod') == '1'
    is_broadcaster = tags.get('badges', '').find('broadcaster') != -1

    if not (is_streamer or is_mod or is_broadcaster):
        connection.privmsg(channel, "Nie masz uprawnień! Tylko streamer i moderacja mogą aktualizować bota.")
        return

    logger.info(f"[UPDATE] Aktualizacja przez {username}")
    connection.privmsg(channel, "Aktualizuję bota... DankMods")

    repo_path = os.path.dirname(os.path.abspath(__file__))
    try:
        import subprocess
        result = subprocess.run(
            ["git", "pull", "--ff-only"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            connection.privmsg(channel, f"Błąd aktualizacji: {result.stderr.strip() or result.stdout.strip() or 'brak informacji'}")
            return
        connection.privmsg(channel, "Aktualizacja zakończona. Restartuję bota...")
    except FileNotFoundError:
        connection.privmsg(channel, "Nie znaleziono git. Upewnij się, że git jest zainstalowany.")
        return

    os.execl(sys.executable, sys.executable, sys.argv[0])

# Command registry - maps command names to handler functions
COMMANDS = {
    "!test": handle_test,
    "!buu": handle_buu,
    "!fmk": handle_fmk,
    "!hug": handle_hug,
    "!kiss": handle_kiss,
    "!bite": handle_bite,
    "!myszka": handle_myszka,
    "!makowiec": handle_makowiec,
    "!ship": handle_ship,
    "!60": handle_60,
    "!dekiel": handle_dekiel,
    "!aura": handle_aura,
    "!iq": handle_iq,
    "!gay": handle_gay,
    "!cute": handle_cute,
    "!adopt": handle_adopt,
    "!redflag": handle_redflag,
    "!greenflag": handle_greenflag,
    "!jealous": handle_jealous,
    "!romantic": handle_romantic,
    "!princess": handle_Princess,
    "!prince": handle_Prince,
    "!princepałki": handle_princepałki,
    "!princessa": handle_princessa,
    "!princepolo": handle_princepolo,
    "!branie": handle_branie,
    "!randka": handle_randka,
    "!kawa": handle_kawa,
    "!classic": handle_classic,
    "!urlop": handle_urlop,
    "!reload": handle_reload,
    "!update": handle_update,
    "!cmd": handle_cmd,
    "!dc": handle_dc,
}


def process_command(msg, connection, channel, username, chatters, ignored_users, discord_link, streamer=None, tags=None):
    """Process a command message"""
    if tags is None:
        tags = {}

    if not msg:
        return False

    command = msg.split()[0]

    for registered_command, handler in COMMANDS.items():
        if command == registered_command:
            try:
                # Special case for !dc which needs discord_link
                if registered_command == "!dc":
                    handler(connection, channel, username, chatters, ignored_users, discord_link)
                # Special case for !reload and !update which need streamer and tags
                elif registered_command in {"!reload", "!update"}:
                    handler(connection, channel, username, streamer, tags)
                else:
                    handler(connection, channel, username, chatters, ignored_users)
            except Exception as e:
                logger.exception(f"Błąd w komendzie {registered_command}: {e}")
            return True
    return False
