
MONGO_HOST = 'localhost'
MONGO_PORT = 27017


MONGO_USERNAME = ''
MONGO_PASSWORD = ''
X_DOMAINS = '*'
MONGO_DBNAME = 'Learode'
X_HEADERS = 'Access-Control-Allow-Origin: *'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


DOMAIN = {
    'resource': {
        'schema': {
            'res_id': {
                'type': 'int',

            },
            'title': {
                'type': 'string',

            },
            'url': {
                'type': 'string',

            },
            'language': {
                'type': 'string',

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
            'oauth_data': {
                'type': 'string',

            },
            'last_reading_list': {
                'type': 'array',

            },
            'new_reading_list': {
                'type': 'array',

            }
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'github_username',

        }
    }
}
