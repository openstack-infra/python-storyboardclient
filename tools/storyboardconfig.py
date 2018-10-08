#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import configparser
import logging
import os
import os.path
import textwrap

from storyboardclient.v1 import client

LOG = logging.getLogger(__name__)
_DEFAULT_URL = 'https://storyboard.openstack.org/api/v1'


def write_empty_config_file(filename):
    LOG.info('creating {}'.format(filename))
    cfg_dir = os.path.dirname(filename)
    if cfg_dir and not os.path.exists(cfg_dir):
        os.makedirs(cfg_dir)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(textwrap.dedent('''\
        [DEFAULT]
        url = {}
        access_token =
        '''.format(_DEFAULT_URL)))


def get_config(filename):
    config = configparser.ConfigParser()
    LOG.info('loading config from {}'.format(filename))
    found_config = config.read(filename)

    if not found_config:
        LOG.error('could not load configuration')
        write_empty_config_file(filename)
        LOG.error('please update {} and try again'.format(filename))
        raise SystemExit('could not load configuration from {}'.format(
            filename))

    return config


def get_client(config):
    try:
        access_token = config.get('DEFAULT', 'access_token')
    except configparser.NoOptionError:
        access_token = ''

    if not access_token:
        raise SystemExit('Could not find access_token in configuration file')

    try:
        storyboard_url = config.get('DEFAULT', 'url')
    except configparser.NoOptionError:
        storyboard_url = _DEFAULT_URL

    try:
        verify_opt = config.get('DEFAULT', 'verify_cert')
    except configparser.NoOptionError:
        verify_opt = 'default'
    verify = verify_opt.lower() in set(['1', 'true', 'default'])

    LOG.info('Connecting to storyboard at {}'.format(storyboard_url))
    return client.Client(storyboard_url, access_token, verify=verify)


def find_story(sbc, title):
    LOG.info('searching for existing stories like {!r}'.format(title))
    existing = sbc.stories.get_all(title=title)
    if existing:
        story = existing[0]
        LOG.info('found existing story {}'.format(story.id))
        return story
    return None


def find_or_create_story(sbc, title, description):
    story = find_story(sbc, title)
    if not story:
        LOG.info('creating new story')
        story = sbc.stories.create(
            title=title,
            description=description,
        )
        LOG.info('created story {}'.format(story.id))
    return story
