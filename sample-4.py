#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from enum import Enum
from pydantic import BaseModel, ValidationError, constr
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
    title: constr(max_length=25)
    description: Optional[str]
    condition: Condition
    price: float


def main():
    ipad_json = {'title': 'iPad Air 2 (Generation Two)',
                 'description': 'Sparingly used iPad Air 2 in Excellent working condition',
                 'condition': Condition.USED,
                 'price': 100.00}

    try:
        Listing(**ipad_json)
    except ValidationError as ve:
        logging.error(ve.json())


if __name__ == '__main__':
    main()
