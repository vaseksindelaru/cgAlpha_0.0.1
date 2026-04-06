"""
cgalpha_v3/infrastructure/binance_data.py - Binance Vision Data Fetcher (Migrated from Legacy)
Misión: Adquisición robusta de klines históricos desde Binance Vision.
"""

import os
import zipfile
import logging
import pandas as pd
from datetime import date
from typing import Optional, List, Any

log = logging.getLogger(__name__)

class BinanceVisionFetcher:
    """
    Fetcher especializado en datos OHLCV de Binance Vision.
    Migrado desde legacy_vault/infrastructure/data_processor/.
    """
    BASE_URL = "https://data.binance.vision/data/spot/daily/klines"
    
    def __init__(self, download_dir: str = "data/raw/binance"):
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)

    def fetch_daily_klines(self, symbol: str, interval: str, year: int, month: int, day: int) -> Optional[pd.DataFrame]:
        """Descarga y procesa un día de klines."""
        import requests
        
        symbol = symbol.upper()
        date_str = f"{year:04d}-{month:02d}-{day:02d}"
        url = f"{self.BASE_URL}/{symbol}/{interval}/{symbol}-{interval}-{date_str}.zip"
        
        local_zip = os.path.join(self.download_dir, f"{symbol}-{interval}-{date_str}.zip")
        
        if not os.path.exists(local_zip):
            log.info(f"Downloading {url}...")
            resp = requests.get(url)
            if resp.status_code != 200:
                log.error(f"Download failed: {resp.status_code}")
                return None
            with open(local_zip, "wb") as f:
                f.write(resp.content)

        # Parsear ZIP
        try:
            with zipfile.ZipFile(local_zip, 'r') as zf:
                csv_name = f"{symbol}-{interval}-{date_str}.csv"
                with zf.open(csv_name) as f:
                    cols = ["Open_Time", "Open", "High", "Low", "Close", "Volume", "Close_Time", 
                            "Quote_Asset_Volume", "Number_of_Trades", "Taker_Buy_Base", "Taker_Buy_Quote", "Ignore"]
                    df = pd.read_csv(f, header=None, names=cols)
                    df["Open_Time"] = pd.to_datetime(df["Open_Time"], unit="ms")
                    return df
        except Exception as e:
            log.error(f"Error parsing {local_zip}: {e}")
            return None
