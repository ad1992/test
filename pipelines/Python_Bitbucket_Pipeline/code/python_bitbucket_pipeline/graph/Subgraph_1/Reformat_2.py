from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from python_bitbucket_pipeline.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        udf_bitbucket(lit(1)).alias("c_udf_parent"), 
        concat(lit(Config.c_string_sg_1), lit("hello")).alias("c_config")
    )
