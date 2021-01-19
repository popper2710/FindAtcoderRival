import argparse

from src.manage import Manager

LOGIN_COUNT = 3


def login(args):
    manager = Manager()
    for _ in range(LOGIN_COUNT):
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
