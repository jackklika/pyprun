from __future__ import annotations

from typing import Union

import pandas as pd
from pydantic import BaseModel, Field

from pyprun.prun_api.fnar.client import FnarApi


class CxPricesRawRow(BaseModel):
    Ticker: str
    MMBuy: Union[int, str]
    MMSell: Union[int, str]
    AI1_Average: float = Field(..., alias="AI1-Average")
    AI1_AskAmt: Union[int, str] = Field(..., alias="AI1-AskAmt")
    AI1_AskPrice: Union[float, str] = Field(..., alias="AI1-AskPrice")
    AI1_AskAvail: int = Field(..., alias="AI1-AskAvail")
    AI1_BidAmt: Union[int, str] = Field(..., alias="AI1-BidAmt")
    AI1_BidPrice: Union[int, str] = Field(..., alias="AI1-BidPrice")
    AI1_BidAvail: int = Field(..., alias="AI1-BidAvail")
    CI1_Average: float = Field(..., alias="CI1-Average")
    CI1_AskAmt: Union[int, str] = Field(..., alias="CI1-AskAmt")
    CI1_AskPrice: Union[float, str] = Field(..., alias="CI1-AskPrice")
    CI1_AskAvail: int = Field(..., alias="CI1-AskAvail")
    CI1_BidAmt: Union[int, str] = Field(..., alias="CI1-BidAmt")
    CI1_BidPrice: Union[float, str] = Field(..., alias="CI1-BidPrice")
    CI1_BidAvail: int = Field(..., alias="CI1-BidAvail")
    CI2_Average: float = Field(..., alias="CI2-Average")
    CI2_AskAmt: Union[int, str] = Field(..., alias="CI2-AskAmt")
    CI2_AskPrice: Union[int, str] = Field(..., alias="CI2-AskPrice")
    CI2_AskAvail: int = Field(..., alias="CI2-AskAvail")
    CI2_BidAmt: Union[int, str] = Field(..., alias="CI2-BidAmt")
    CI2_BidPrice: Union[int, str] = Field(..., alias="CI2-BidPrice")
    CI2_BidAvail: int = Field(..., alias="CI2-BidAvail")
    NC1_Average: float = Field(..., alias="NC1-Average")
    NC1_AskAmt: Union[int, str] = Field(..., alias="NC1-AskAmt")
    NC1_AskPrice: Union[int, str] = Field(..., alias="NC1-AskPrice")
    NC1_AskAvail: int = Field(..., alias="NC1-AskAvail")
    NC1_BidAmt: Union[int, str] = Field(..., alias="NC1-BidAmt")
    NC1_BidPrice: Union[int, str] = Field(..., alias="NC1-BidPrice")
    NC1_BidAvail: int = Field(..., alias="NC1-BidAvail")
    NC2_Average: float = Field(..., alias="NC2-Average")
    NC2_AskAmt: Union[int, str] = Field(..., alias="NC2-AskAmt")
    NC2_AskPrice: Union[int, str] = Field(..., alias="NC2-AskPrice")
    NC2_AskAvail: int = Field(..., alias="NC2-AskAvail")
    NC2_BidAmt: Union[int, str] = Field(..., alias="NC2-BidAmt")
    NC2_BidPrice: Union[int, str] = Field(..., alias="NC2-BidPrice")
    NC2_BidAvail: int = Field(..., alias="NC2-BidAvail")
    IC1_Average: float = Field(..., alias="IC1-Average")
    IC1_AskAmt: Union[int, str] = Field(..., alias="IC1-AskAmt")
    IC1_AskPrice: Union[int, str] = Field(..., alias="IC1-AskPrice")
    IC1_AskAvail: int = Field(..., alias="IC1-AskAvail")
    IC1_BidAmt: Union[int, str] = Field(..., alias="IC1-BidAmt")
    IC1_BidPrice: Union[int, str] = Field(..., alias="IC1-BidPrice")
    IC1_BidAvail: int = Field(..., alias="IC1-BidAvail")


class CXPrices:
    def __init__(self):
        self.client = FnarApi()

    @staticmethod
    def _translate_dataframe(df: pd.DataFrame):
        """
        transform data to hierarchical format, splitting into tickers
        """
        df_long = df.melt(id_vars="Ticker", var_name="Var", value_name="Value")
        df_long[["Exchange", "PriceType"]] = df_long["Var"].str.split("-", expand=True)
        df_long = df_long.drop("Var", axis=1)
        return df_long.pivot(
            index="Ticker", columns=["Exchange", "PriceType"], values="Value"
        )

    def get_all_prices(self):
        pass
