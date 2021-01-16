import argparse


def main():
    # [("command", "help text", "argument count")...]
    sub_commands = [("login", "login to atcoder",),
                    ("update", "find and update rivals"),
                    ("status", "prints comparison with rivals"),
                    ("clear-session", "clear session data"),
                    ]

    parser = argparse.ArgumentParser()
    for command in sub_commands:
        parser.add_argument(command[0], help=command[1])
