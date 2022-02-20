#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from enum import Enum
from pydantic import BaseModel
from typing import Optional
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class Category(Enum):
    ELECTRONICS = 'Electronics'
    FURNITURE = 'Furniture'
    TOYS = 'Toys'


class Condition(Enum):
    NEW = 'New'
    USED = 'Used'


class Listing(BaseModel):
    category: Category
    title: str
    description: Optional[str] = None
    condition: Condition
    price: float


def main():
    ipad_json = {'category': Category.ELECTRONICS,
                 'title': 'iPad Air 2',
                 'description': 'Sparingly used iPad Air 2 in Excellent working condition',
                 'condition': Condition.USED,
                 'price': 55.00}

    ipad = Listing(**ipad_json)

    logging.info(ipad)
    logging.info('{} ({}) - {}'.format(ipad.title, ipad.condition.value, ipad.price))

    table_json = {'category': Category.FURNITURE,
                  'title': 'Oak Dressing Table',
                  'condition': Condition.USED,
                  'price': 75.00}

    table = Listing(**table_json)

    logging.info(table)


if __name__ == '__main__':
    main()
