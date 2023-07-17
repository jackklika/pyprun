import io
from typing import Final

import httpx
import pandas as pd


class FnarApi:
    _PRICES_ENDPOINT: Final[str] = "/csv/prices/condensed"
    _DEFAULT_EXCHANGE: Final[str] = "IC1"

    def __init__(self):
        self.base_url: str = "https://rest.fnar.net"

    async def _fetch_csv_data(self, endpoint: str) -> pd.DataFrame:
        """
        Fetch data from an endpoint and return a pandas DataFrame
        """
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            resp = await client.get(endpoint)
        return pd.read_csv(io.StringIO(resp.content.decode()))

    async def get_prices(self) -> pd.DataFrame:
        """
        Full price information as raw dataframe
        """
        return await self._fetch_csv_data(self._PRICES_ENDPOINT)
