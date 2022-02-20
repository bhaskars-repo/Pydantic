#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from enum import Enum
from pydantic import BaseModel, root_validator, constr
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

    class Config:
        allow_mutation = False
        use_enum_values = True

    @root_validator
    def valid_price_check(cls, values) -> dict:
        val = values.get('price')
        if val <= 0.0:
            raise ValueError('price cannot be <= 0.0')
        if val > 99.99:
            raise ValueError('price cannot be > 99.99')
        return values


def main():
    toy_json = {'category': Category.TOYS,
                'title': 'Chutes and Ladders',
                'condition': Condition.USED,
                'price': 4.99,
                'extra': 'Extra information'}

    toy = Listing(**toy_json)

    logging.info(toy.dict())

    try:
        toy.description = 'Changing the description'
    except TypeError as te:
        logging.error('***ERROR*** {}'.format(te))


if __name__ == '__main__':
    main()
