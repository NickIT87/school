q_base = {
    'q1': {
        'text': 'Укажи дріб що неможливо подати у вигляді десяткового.',
        '1': {
            'text': '3/10',
            'state': False
        },
        '2': {
            'text': '45/50',
            'state': False
        },
        '3': {
            'text': '23/24',
            'state': True
        },
        '4': {
            'text': '15/16',
            'state': False
        }
    },

    'q2': {
        'text': 'Вирази дріб 0.04 у вигляді відсотка.',
        '1': {
            'text': '4%',
            'state': True
        },
        '2': {
            'text': '40%',
            'state': False
        },
        '3': {
            'text': '400%',
            'state': False
        },
        '4': {
            'text': '4000%',
            'state': False
        }
    },

    'q3': {
        'text': 'Знайди 12,5 % від 8.',
        '1': {
            'text': '1',
            'state': True
        },
        '2': {
            'text': '2',
            'state': False
        },
        '3': {
            'text': '0.4',
            'state': False
        }
    },

    'q4': {
        'text': 'Визнач, що більше: 33 % від 25 чи 25 % від 33',
        '1': {
            'text': '33% від 25',
            'state': False
        },
        '2': {
            'text': '25% від 33',
            'state': False
        },
        '3': {
            'text': 'значення виразів рівні',
            'state': True
        }
    },

    'q5': {
        'text': 'Обчисли 1% від 125',
        '1': {
            'text': '1.25',
            'state': True
        },
        '2': {
            'text': '12.5',
            'state': False
        },
        '3': {
            'text': '0.125',
            'state': False
        }
    },

    'q6': {
        'text': 'Обчисли 2% від 80',
        '1': {
            'text': '4',
            'state': False
        },
        '2': {
            'text': '8',
            'state': False
        },
        '3': {
            'text': '16',
            'state': False
        },
        '4': {
            'text': '1.6',
            'state': True
        }
    },

    'q7': {
        'text': 'Обчисли 141% від 2',
        '1': {
            'text': '28.2',
            'state': False
        },
        '2': {
            'text': '0.282',
            'state': False
        },
        '3': {
            'text': '2.82',
            'state': True
        }
    },

    'q8': {
        'text': 'Запиши нескінченний періодичний десятковий дріб 7,444...=',
        '1': {
            'text': '7.(4)',
            'state': True
        },
        '2': {
            'text': '7.(44)',
            'state': False
        }
    },

    'q9': {
        'text': 'Запиши нескінченний періодичний десятковий дріб 96,4222...=',
        '1': {
            'text': '96.(42)',
            'state': False
        },
        '2': {
            'text': '96.4(22)',
            'state': False
        },
        '3': {
            'text': '96.4(2)',
            'state': True
        }
    },

    'q10': {
        'text': 'Запиши нескінченний періодичний десятковий дріб 2,121212...=',
        '1': {
            'text': '2.(12)',
            'state': True
        },
        '2': {
            'text': '2.1(2)',
            'state': False
        },
        '3': {
            'text': '2.(121)',
            'state': False
        }
    },

    'q11': {
        'text': 'На виборах мера проголосувало 80 тис. осіб, що становить 40 % населення міста. Скільки жителів у місті?',
        '1': {
            'text': '32000',
            'state': False
        },
        '2': {
            'text': '200000',
            'state': True
        }
    },

    'q12': {
        'text': 'Сплав містить 15 % цинку. Скільки кілограмів цинку міститься в 150 кг сплаву?',
        '1': {
            'text': '1000 г.',
            'state': True
        },
        '2': {
            'text': '22.5 кг.',
            'state': False
        },
        '3': {
            'text': '225 кг.',
            'state': False
        },
    }
}

import json

txt = json.dumps(q_base, indent = 4)
print(txt)

# with open('q_base.json') as json_file:
#     data = json.load(json_file)

# print(type(data))
# print(data['q1']['text'])