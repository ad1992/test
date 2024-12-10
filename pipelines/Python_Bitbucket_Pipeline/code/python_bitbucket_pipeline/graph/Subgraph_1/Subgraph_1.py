from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> (DataFrame, DataFrame):
    Config.update(config)
    df_Reformat_2 = Reformat_2(spark, in0)
    df_CustomReformatBitbucket_2 = CustomReformatBitbucket_2(spark, df_Reformat_2)

    return df_Reformat_2, df_CustomReformatBitbucket_2
