#!/usr/bin/env python
import re
from typing import Optional

import click
import twitter
import configparser

cfg = configparser.ConfigParser()
cfg.read('twitter.config')

api = twitter.Api(consumer_key=cfg['yourname.consumer']['key'],
                  consumer_secret=cfg['yourname.consumer']['secret'],
                  access_token_key=cfg['yourname.access']['key'],
                  access_token_secret=cfg['yourname.access']['secret'])

re_mt_url = re.compile(r'(\w+.social/@\w+)')
re_mt_name = re.compile(r'(@\w+@\w+.social)')


def mast_scan(text: Optional[str]) -> str:
    if text is None:
        return None
    name_res = re_mt_name.search(text)
    if name_res:
        return name_res.group(0)
    url_res = re_mt_url.search(text)
    if url_res:
        return url_res.group(0)


@click.group()
def exomus():
    pass


@exomus.command()
def scan():
    users = api.GetFriends()
    for user in users:
        desc_mast = mast_scan(user.description)
        if desc_mast:
            click.echo(f"{user.screen_name} ({user.name}): {desc_mast}")

        for unmasked_url in user._json.get('entities', {}).get('description', {}).get('urls', []):
            url_mast = mast_scan(unmasked_url['expanded_url'])
            if url_mast:
                click.echo(f"{user.screen_name} ({user.name}): {url_mast}")

        for unmasked_url in user._json.get('entities', {}).get('url', {}).get('urls', []):
            url_mast = mast_scan(unmasked_url['expanded_url'])
            if url_mast:
                click.echo(f"{user.screen_name} ({user.name}): {url_mast}")


if __name__ == '__main__':
    exomus()
