from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from aakanshafork.config.ConfigStore import *
from aakanshafork.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Aakansha-fork")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Aakansha-fork")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Aakansha-fork", config = Config)(pipeline)

if __name__ == "__main__":
    main()
