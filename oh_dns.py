#!/bin/python3
import whois

print(
    """
░█████╗░██╗░░██╗██████╗░███╗░░██╗░██████╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝
██║░░██║███████║██║░░██║██╔██╗██║╚█████╗░
██║░░██║██╔══██║██║░░██║██║╚████║░╚═══██╗
╚█████╔╝██║░░██║██████╔╝██║░╚███║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚═════╝░

Menu -------
1 ) whois lookup
"""
)


def who_is(x):
    print(f"{x} is ")
    target = whois.whois(x)
    print(target)


while True:
    user_input = input("What tool will you use: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            x = input("Enter IP or website.com: ")
            who_is(x)
        else:
            exit()
