# pyprun

This is a library that provides helper functions to perform data analysis on
Prosperous Universe objects.

The goal is to provide a library that makes it very easy to work with data
without thinking about calling the api or parsing csv files -- this will
do that for you.

**This project is extremely alpha.** At this point, only copy-paste code
from this repo. Soon, we can add tests and make proper pypi releases.


### Example usage

Getting prices
```
>>> from pyprun.prices.prices import CXPrices
>>> p = await CXPrices.create()
>>> p.get_by_ticker("RAT.IC1")
Type                ask        avg        bid  mm-buy  mm-sell
Material CX
RAT      IC1  98.599998  98.599998  88.099998    32.0    166.0
>>> p.get_by_ticker("RAT.IC1", "ask")
98.5999984741211
```