from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from python_bitbucket_pipeline.udfs.UDFs import *

def CustomReformatBitbucket_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0
