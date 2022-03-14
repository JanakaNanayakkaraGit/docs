#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import sys
from glob import glob


GLOB_PATTERN = 'source/*.md'
COMMIT_PATTERN = (
    r'([a-z0-9]{40}),\s[\w]+,\s([0-9]{1,2}\s[\w]{3}\s[0-9]{4}).*,\s(.*)'
)
GIT_CMD = ['git', 'log', '-2', '--oneline', '--pretty="%H, %cD, %s"']
UPDATE_HASH = '74dc12829b7ae2ce0c6c36364c5791b9f94d489d'
GIT_IGNORE_MSG = 'last updated'


def get_link(_hash, path):
    return f'https://github.com/kobotoolbox/docs/blob/{_hash}/{path}'


def get_git_data(path):
    stdout = (
        subprocess.run(GIT_CMD + [path], capture_output=True)
        .stdout.decode()
        .split('\n')[:-1]
    )
    if len(stdout) == 1:
        latest, _next = stdout[0], ''
    else:
        latest, _next = stdout

    _hash, date, msg = re.search(COMMIT_PATTERN, latest).groups()
    if not _hash.startswith(UPDATE_HASH) and not msg.startswith(GIT_IGNORE_MSG):
        return _hash, date
    return re.search(COMMIT_PATTERN, _next).groups()[:2]


def get_text(date, link):
    return f'**Last updated:** <a href="{link}" class="reference">{date}</a>\n'


def update_file(path):
    _hash, date = get_git_data(path)
    link = get_link(_hash, path)
    text = get_text(date, link)

    with open(path, 'r') as f:
        fs = f.readlines()

    # if `prettier` has been used, just remove the three lines
    if 'Last updated' in fs[2]:
        # if the link is up-to-date, carry on
        if link in fs[3]:
            return
        fs = [fs[0]] + fs[5:]

    if 'Last updated' in fs[1]:
        if fs[1] == text:
            return
        fs[1] = text
    else:
        fs.insert(1, text)

    with open(path, 'w') as f:
        sys.stdout.write(f'Updating: {path}\n')
        f.write(''.join(fs))


def main():
    parser = argparse.ArgumentParser(
        description='A CLI tool to update article "Last updated" dates.'
    )
    parser.add_argument('--file-path', '-f', type=str, help='Path to file')
    args = parser.parse_args()

    path = args.file_path
    if path:
        if not os.path.exists(path):
            os.sys.exit()
        update_file(path)
    else:
        for path in glob(GLOB_PATTERN):
            update_file(path)
    sys.stdout.write('Done 🎉\n')


if __name__ == '__main__':
    main()