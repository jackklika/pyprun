from typing import Final

from pyprun.prun_api.fnar.client import FnarApi

import pandas as pd


class CXPrices:
    _REMOVE_THIS_DEFAULT_CX: Final[str] = "IC1"

    def __init__(self, default_cx: str = _REMOVE_THIS_DEFAULT_CX):
        self.default_cx: str = default_cx
        self.api = FnarApi()
        self.data: pd.DataFrame = None

    @classmethod
    async def create(cls):
        cxprices = CXPrices()
        cxprices.data = cls._translate_dataframe(await cxprices.api.get_prices())
        return cxprices

    @staticmethod
    def _translate_dataframe(df: pd.DataFrame):
        """
        transform data to simple format like this:
        ```
                CX     Type         Value Material
        0      AI1      ask  15000.000000      AAR
        1      IC1      avg  11000.000000      RAT
        ```
        """
        splits = df["Id"].str.split("-", expand=True, n=2)
        df["Material"] = splits[0]
        df["CX"] = splits[1]
        df["Type"] = splits[2]
        df = df.drop("Id", axis=1)
        df = df.drop("Ticker", axis=1)

        # Could set other index...
        df.set_index(["Material", "CX"], inplace=True)
        df.sort_index(inplace=True)

        return df

    async def get_prices_df(self):
        """
        Get raw dataframe for all exchanges and datapoints in nested
        hierarchical format
        """
        return self._translate_dataframe(await self.api.get_prices())

    async def get_by_ticker(self, ticker: str) -> pd.DataFrame:
        """
        Get a price matrix for a ticker like "RAT.IC1"

        Returns a single-series dataframe like this:
        ```
        Material  CX        ask   avg        bid  mm-buy  mm-sell
        RAT      IC1  98.599998  88.0  88.099998    32.0    166.0
        ```
        """
        # todo: validate input
        split_ticker: list[str] = ticker.split(".")
        mat, cx = split_ticker[0], split_ticker[1]
        df = self.data.loc[(mat, cx)]

        # pivot so we can select by price
        df_pivot = df.pivot_table(
            index=["Material", "CX"], columns="Type", values="Value"
        )
        return df_pivot
