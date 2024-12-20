from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("udf_bitbucket", udf_bitbucket)
    

    try:
        from prophecy.utils import ScalaUtil
        ScalaUtil.initializeUDFs(spark)
    except :
        pass

def udf_bitbucketGenerator():
    initial = 10

    @udf(returnType = IntegerType())
    def func(input):
        input = int(input) if input is not None else 2

        return int(input) * int(input) if input is not None else initial

    return func

udf_bitbucket = udf_bitbucketGenerator()
