"""
This is a boilerplate pipeline 'download_mei'
generated using Kedro 0.18.6
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import download_inadimplencia_mei


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=download_inadimplencia_mei,
            inputs=None,
            outputs='inadimplencia_mei',
            name='download_inadimplencia_mei',
        )
    ])
