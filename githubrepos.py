#!/usr/bin/env python3

'''
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:


Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/pymivn/repos

Câu lệnh của chương trình có dạng::

    python3 githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse

'''


import requests
import sys
import json
import logging
sys.tracebacklimit = 0
logger = logging.getLogger(__name__)


def solve(input_user):
    url = 'https://api.github.com/users/{}/repos'
    user_repo = url.format(input_user)
    resp = requests.get(user_repo)
    data = resp.json()

    if not data:
        raise ValueError('No data found!')

    result = []
    for i in data:
        result.append(i['name'])

    return result


def main():
    if len(sys.argv[1:]) < 1:
        raise ValueError('No argument provided!')
    elif len(sys.argv[1:]) > 1:
        raise ValueError('Only 1 argument available!')
    print(solve(sys.argv[1]))


if __name__ == "__main__":
    main()
