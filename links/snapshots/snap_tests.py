# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['APITestCase::test_all_links_resolver 1'] = {
    'data': {
        'links': [
            {
                'description': 'Link 1',
                'id': '1',
                'url': 'https://www.example.com/1'
            },
            {
                'description': 'Link 2',
                'id': '2',
                'url': 'https://www.example.com/2'
            },
            {
                'description': 'Link 3',
                'id': '3',
                'url': 'https://www.example.com/3'
            },
            {
                'description': 'Link 4',
                'id': '4',
                'url': 'https://www.example.com/4'
            }
        ]
    }
}

snapshots['APITestCase::test_links_first_resolver 1'] = {
    'data': {
        'links': [
            {
                'description': 'Link 1',
                'id': '1',
                'url': 'https://www.example.com/1'
            },
            {
                'description': 'Link 2',
                'id': '2',
                'url': 'https://www.example.com/2'
            }
        ]
    }
}

snapshots['APITestCase::test_links_skip_resolver 1'] = {
    'data': {
        'links': [
            {
                'description': 'Link 3',
                'id': '3',
                'url': 'https://www.example.com/3'
            },
            {
                'description': 'Link 4',
                'id': '4',
                'url': 'https://www.example.com/4'
            }
        ]
    }
}
