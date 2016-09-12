# -*- coding: utf-8 -*-

import os
import itertools

WORDS_PER_MINUTE = 700
#  refer to https://help.medium.com/hc/en-us/articles/214991667-Read-time

IMAGE_READ_TIME = 12  # seconds
# count 12 seconds for the first image, 11 for the second, and minus an
# additional second for each subsequent image. Any images after the tenth
# image are counted at three seconds.


def get_md_data(path):
    with open(path, 'r') as f:
        tmp = f.readlines()[10:]

    text = []
    images = []

    for line in tmp:
        if line == '\n' or line == '***\n':
            continue
        elif line.startswith('!['):
            images.append(line)
        else:
            text.append(line)

    return (text, images)


def minutes_to_read(text, images):
    chain = itertools.chain(*text)
    total_words = sum([len(line) for line in chain])
    print('total words: %d' % total_words)
    text_minute = total_words / WORDS_PER_MINUTE

    image_seconds = len(images) * IMAGE_READ_TIME
    image_minute = image_seconds / 60

    return text_minute + image_minute


def absolute_paths():
    for dirpath, _, filenames in os.walk('./sources/'):
        for f in filenames:
            if not f.startswith('.'):
                yield os.path.abspath(os.path.join(dirpath, f))


def update_members():
    out = open('./members/all.md', 'w')
    translators = set()
    for file in absolute_paths():
        f = open(file, 'r')
        for line in f:
            if line.startswith('translator'):
                translators.add(line.split(':')[1])
    for item in translators:
        out.write(item)
    out.close()


def main():
    files = os.listdir('./sources')

    for file in files:
        if file.endswith('.md'):
            path = './sources/' + file
            text, images = get_md_data(path)
            minutes = minutes_to_read(text, images)
            print(round(minutes, 0))


if __name__ == '__main__':
    update_members()
