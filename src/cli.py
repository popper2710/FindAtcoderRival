import argparse

from src.manage import Manager
from src.rival_cond import RivalCond


def check_register(func):
    def wrapper(*args, **kwargs):
        manager = Manager()
        if not manager.is_register():
            print("Please login before. \n'far login'")
        else:
            return func(*args, **kwargs)


def login(args):
    manager = Manager()
    if args.username and args.password:
        manager.fetcher.login(args.username, args.password)
        if manager.fetcher.is_login:
            print("Username or password is incorrect")
    for _ in range(args.try_count):
        if manager.fetcher.is_login:
            break
        username = input("Please input your username and password in Atcoder\nusername:")
        password = input("password:")
        manager.fetcher.login(username, password)
        if manager.fetcher.is_login:
            print("Username or password is incorrect")


@check_register
def find(args):
    manager = Manager()
    manager.update_user_info(manager.register_user.username)
    manager.update_contests_info()


@check_register
def update(args):
    manager = Manager()
    manager.update_user_info()
    manager.update_rivals()


@check_register
def status(args):
    print(args)


def clear_session(args):
    manager = Manager()
    manager.fetcher.logout()


def cond(args):
    rival_cond = RivalCond()
    if not args.reset:
        if args.upper_rate:
            rival_cond.upper_rate_limit = args.upper_rate
        if args.lower_rate:
            rival_cond.upper_rate_limit = args.lower_rate
        if args.upper_rank:
            rival_cond.upper_rate_limit = args.upper_rank
        if args.lower_rank:
            rival_cond.upper_rate_limit = args.lower_rank
        if args.required_participatin:
            rival_cond.upper_rate_limit = args.required_participatin
        if args.recent_contest:
            rival_cond.upper_rate_limit = args.recent_contest
    Manager().set_rival_cond(rival_cond)


def main():
    parser = argparse.ArgumentParser(description="Find your rival in Atcoder")
    subparsers = parser.add_subparsers()
    parser_login = subparsers.add_parser("login", help="login to atcoder")
    parser_login.add_argument("-u", "--username", help="Atcoder username", default="")
    parser_login.add_argument("-p", "--password", help="Atcoder password", default="")
    parser_login.add_argument("-t", "--try_count", help="set try count (default: 3)", default=3)
    parser_login.set_defaults(handler=login)

    parser_update = subparsers.add_parser("find", help="find rivals")
    parser_update.set_defaults(handler=find)

    parser_update = subparsers.add_parser("update", help="update rivals")
    parser_update.set_defaults(handler=update)

    parser_status = subparsers.add_parser("status", help="prints comparison with rivals")
    parser_status.set_defaults(handler=status)

    parser_clear_session = subparsers.add_parser("clear_session", help="clear session data")
    parser_clear_session.set_defaults(handler=clear_session)

    parser_cond = subparsers.add_parser("cond", help="set condition of rival")
    parser_cond.add_argument("-ur", "--upper_rate", help="set upper rate limit")
    parser_cond.add_argument("-lr", "--lower_rate", help="set lower rate limit")
    parser_cond.add_argument("-uR", "--upper_rank", help="set upper ranking limit")
    parser_cond.add_argument("-lR", "--lower_rank", help="set upper ranking limit")
    parser_cond.add_argument("-rp", "--required_participation", help="set required participation count")
    parser_cond.add_argument("-rc", "--recent_contest", help="set recent contest count")
    parser_cond.add_argument("-d", "--reset", help="return to default value")
    parser_cond.set_defaults(handler=cond)

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
