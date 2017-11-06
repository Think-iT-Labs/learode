
MONGO_HOST = 'localhost'
MONGO_PORT = 27017


MONGO_USERNAME = ''
MONGO_PASSWORD = ''
X_DOMAINS = '*'
MONGO_DBNAME = 'Learode'
X_HEADERS = '*'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
ALLOWED_ROLES = ['*']
XML = False
DOMAIN = {
    'resource': {
        'schema': {
            'res_id': {
                'type': 'integer',
                'unique': True
            },
            'title': {
                'type': 'string'
            },
            'url': {
                'type': 'string'
            },
            'language': {
                'type': 'string'
            },
            'level': {
                'type': 'string'
            },
            'read_by': {
                'type': 'list'
            },
            'created_by': {
                'type': 'string'
            },
        },
        'additional_lookup': {
            'url': 'int',
            'field': 'res_id',

        }
    },
    'user': {
        'schema': {
            'user_id': {
                'type': 'int',
            },
            'github_username': {
                'type': 'string',

            },
            'github_access_token': {
                'type': 'string',

            },
            'last_reading_list': {
                'type': 'list',

            },
            'new_reading_list': {
                'type': 'list',

            }
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'github_username',

        }
    }
}
