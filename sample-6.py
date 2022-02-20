#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from enum import Enum
from pydantic import BaseModel, ValidationError, root_validator, constr
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

    @root_validator
    def valid_price_check(cls, values) -> dict:
        val = values.get('price')
        if val <= 0.0:
            raise ValueError('price cannot be <= 0.0')
        if val > 99.99:
            raise ValueError('price cannot be > 99.99')
        return values


def main():
    table_json = {'category': Category.FURNITURE,
                  'title': 'Coffee Table',
                  'condition': Condition.NEW,
                  'price': 35.99}

    table = Listing(**table_json)
    table.description = 'Beautiful glass top coffee table'

    logging.info(table.dict())


if __name__ == '__main__':
    main()
