"""
This is a boilerplate pipeline 'download_mei'
generated using Kedro 0.18.6
"""

import pandas as pd
import requests


def download_inadimplencia_mei():

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.27393/dados?formato=json"
    resp = requests.get(url)

    df_bcb = (
        pd.DataFrame(resp.json())
        .assign(
            data=lambda x: pd.to_datetime(x['data'], dayfirst=True),
            valor=lambda x: x['valor'].astype('float64'),
        )
    )

    return df_bcb