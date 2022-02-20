#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from enum import Enum
from pydantic import BaseModel, ValidationError, validator, constr
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

    @validator('price')
    def valid_price_check(cls, val, values) -> float:
        logging.info(values)
        if val <= 0.0:
            raise ValueError('price cannot be <= 0.0')
        if val > 99.99:
            raise ValueError('price cannot be > 99.99')
        return val


def main():
    ipad_json = {'category': Category.ELECTRONICS,
                 'title': 'iPad Air 2',
                 'condition': Condition.USED,
                 'price': 100.00}

    try:
        Listing(**ipad_json)
    except ValidationError as ve:
        logging.error(ve.json())


if __name__ == '__main__':
    main()
