#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   19 Feb 2022
#

from pydantic import BaseModel
from typing import Optional
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class Listing(BaseModel):
    category: str
    title: str
    description: Optional[str] = None
    condition: str
    price: float


def main():
    ipad_json = {'category': 'Electronics',
                 'title': 'iPad Air 2',
                 'description': 'Sparingly used iPad Air 2 in Excellent working condition',
                 'condition': 'Excellent',
                 'price': 55.00}

    ipad = Listing(**ipad_json)

    logging.info(ipad)
    logging.info('{} ({}) - {}'.format(ipad.title, ipad.condition, ipad.price))

    table_json = {'category': 'Furniture',
                  'title': 'Oak Dressing Table',
                  'condition': 'Excellent',
                  'price': 75.00}

    table = Listing(**table_json)

    logging.info(table)


if __name__ == '__main__':
    main()
