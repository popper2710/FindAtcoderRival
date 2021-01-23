import argparse

from src.manage import Manager


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
        password = input("password")
        manager.fetcher.login(username, password)
        if manager.fetcher.is_login:
            print("Username or password is incorrect")


def update(args):
    print(args)


def status(args):
    print(args)


def clear_session(args):
    print(args)


def main():
    parser = argparse.ArgumentParser(description="Find your rival in Atcoder")
    subparsers = parser.add_subparsers()
    parser_login = subparsers.add_parser("login", help="login to atcoder")
    parser_login.add_argument("-u", "--username", help="Atcoder username", default="")
    parser_login.add_argument("-p", "--password", help="Atcoder password", default="")
    parser_login.add_argument("-t", "--try_count", help="set try count (default: 3)", default=3)
    parser_login.set_defaults(handler=login)

    parser_update = subparsers.add_parser("update", help="find and update rivals")
    parser_update.set_defaults(handler=update)

    parser_status = subparsers.add_parser("status", help="prints comparison with rivals")
    parser_status.set_defaults(handler=status)

    parser_clear_session = subparsers.add_parser("clear_session", help="clear session data")
    parser_clear_session.set_defaults(handler=clear_session)

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
