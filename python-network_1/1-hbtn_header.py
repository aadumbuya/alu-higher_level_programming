#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays
the value of X-Request-Id varialble found in the header
of the response
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    if argv[1]:
        with request.urlopen(argv[1]) as response:
            print(response.getheader('X-Request-Id'))
