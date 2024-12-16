from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from python_bitbucket_pipeline.udfs.UDFs import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> (DataFrame, DataFrame):
    Config.update(subgraph_config)
    df_Reformat_2 = Reformat_2(spark, in0)
    subgraph_config.update(Config)

    return df_Reformat_2
