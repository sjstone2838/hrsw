#!/usr/bin/python
"""Write [n] employee records to performance_reviews.json."""
from sys import argv
import json
from datetime import datetime, date
from random import choice, normalvariate

import pydash

start_time = datetime.now()

# positions are ordered by promotion path
POSITIONS = [
    "analyst",
    "associate",
    "manager"
]
# Maximum performance value is 1
# Maximum retention value is 1
UNIVERSITIES = [
    {
        "name": "Stanford University",
        "outcomes": {
            "analyst": {
                "retention": 0.2,
                "performance": 0.9
            },
            "associate": {
                "retention": 0.5,
                "performance": 0.9
            },
            "manager": {
                "retention": 0.5,
                "performance": 0.9
            }
        }
    },
    {
        "name": "Yale University",
        "outcomes": {
            "analyst": {
                "retention": 0.9,
                "performance": 0.9
            },
            "associate": {
                "retention": 0.5,
                "performance": 0.2
            },
            "manager": {
                "retention": 0.5,
                "performance": 0.2
            }
        }
    },
    {
        "name": "Berkeley University",
        "outcomes": {
            "analyst": {
                "retention": 0.9,
                "performance": 0.5
            },
            "associate": {
                "retention": 0.9,
                "performance": 0.5
            },
            "manager": {
                "retention": 0.9,
                "performance": 0.5
            }
        }
    }
]

MAJORS = [
    {
        "name": "Mathematics",
        "outcomes": {
            "analyst": {
                "retention": 0.9,
                "performance": 0.9
            },
            "associate": {
                "retention": 0.9,
                "performance": 0.5
            },
            "manager": {
                "retention": 0.9,
                "performance": 0.5
            }
        }
    },
    {
        "name": "Biology",
        "outcomes": {
            "analyst": {
                "retention": 0.9,
                "performance": 0.9
            },
            "associate": {
                "retention": 0.9,
                "performance": 0.9
            },
            "manager": {
                "retention": 0.2,
                "performance": 0.2
            }
        }
    },
    {
        "name": "English",
        "outcomes": {
            "analyst": {
                "retention": 0.2,
                "performance": 0.2
            },
            "associate": {
                "retention": 0.9,
                "performance": 0.9
            },
            "manager": {
                "retention": 0.9,
                "performance": 0.9
            }
        }
    }
]

GPA = {
    "mean": 3.5,
    "sdev": 0.2,
    "maximum": 4.0,
}

WEIGHTINGS = {
    "performance": {
        "analyst": {
            "university": 0.4,
            "major": 0.4,
            "GPA": 0.2
        },
        "associate": {
            "university": 0.4,
            "major": 0.4,
            "GPA": 0.2
        },
        "manager": {
            "university": 0.4,
            "major": 0.4,
            "GPA": 0.2
        }
    },
    "retention": {
        "analyst": {
            "university": 0.5,
            "major": 0.5,
        },
        "associate": {
            "university": 0.5,
            "major": 0.5,
        },
        "manager": {
            "university": 0.5,
            "major": 0.5,
        }
    }
}

PROMOTION_THRESHOLD = 0.5
PROMOTION_ACCEPTANCE_THRESHOLD = 0.5


class DataGenerator:
    """Data generator class."""

    def __init__(self):
        """Initiate."""
        self.counter = 0

    def generate_person(self, person_id):
        """Generate a person."""
        attributes = {
            "id": person_id,
            "university": choice(UNIVERSITIES)['name'],
            "major": choice(MAJORS)['name'],
            "GPA": round(min(normalvariate(
                GPA['mean'],
                GPA['sdev']
            ), GPA['maximum']), 2)
        }

        outcomes = self.generate_outcomes({}, attributes, 0)

        return {
            "attributes": attributes,
            "outcomes": outcomes,
        }

    def generate_rating(self, attributes, pos_index, rating_type):
        """Generate a value between 0 and 1 for performance and retention."""
        position_name = POSITIONS[pos_index]
        weightings = WEIGHTINGS[rating_type][position_name]
        university_outcomes = pydash.find(UNIVERSITIES, ['name', attributes['university']])['outcomes']
        major_outcomes = pydash.find(MAJORS, ['name', attributes['major']])['outcomes']

        if rating_type == 'performance':
            return round((
                weightings['university'] * university_outcomes[position_name]['performance'] +
                weightings['major'] * major_outcomes[position_name]['performance'] +
                weightings['GPA'] * attributes['GPA'] / GPA['maximum']
            ), 2)
        elif rating_type == 'retention':
            return round((
                weightings['university'] * university_outcomes[position_name]['retention'] +
                weightings['major'] * major_outcomes[position_name]['retention']
            ), 2)
        else:
            raise Exception(rating_type + "is not a rating_type option.")

    def generate_outcomes(self, outcome, attributes, pos_index):
        """Generate outcomes."""
        position_name = POSITIONS[pos_index]
        performance = self.generate_rating(attributes, pos_index, 'performance')
        offered_promotion = performance > PROMOTION_THRESHOLD

        outcome[position_name] = {
            "performance": performance,
            "offered_promotion": offered_promotion,
        }
        if offered_promotion:
            outcome[position_name]['accepted_promotion'] = (
                self.generate_rating(attributes, pos_index, 'retention') > PROMOTION_ACCEPTANCE_THRESHOLD
            )
        pos_index += 1
        if ("accepted_promotion" in outcome[position_name] and
                outcome[position_name]["accepted_promotion"] and
                pos_index != len(POSITIONS)):

            self.generate_outcomes(
                outcome, attributes, pos_index)

        return outcome


DataGenerator = DataGenerator()
data = []
for i in range(0, int(argv[1])):
    data.append(DataGenerator.generate_person(i))


def json_serial(obj):
    """
    JSON serializer for objects not serializable by default json code.

    http://stackoverflow.com/questions/11875770/how-to-overcome-datetime
    -datetime-not-json-serializable-in-python
    """
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")

with open('performance_reviews.json', 'w') as outfile:
    json.dump(data, outfile, default=json_serial)

end_time = datetime.now()
run_time = end_time - start_time
print 'Took {0} seconds to generate {1} records.'.format(
    round(run_time.seconds + run_time.microseconds / 100000., 2),
    argv[1]
)
