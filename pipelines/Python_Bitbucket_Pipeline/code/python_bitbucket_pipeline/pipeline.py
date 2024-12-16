from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from python_bitbucket_pipeline.config.ConfigStore import *
from python_bitbucket_pipeline.udfs.UDFs import *
from prophecy.utils import *
from python_bitbucket_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset_bitbucket_csv = dataset_bitbucket_csv(spark)
    df_Reformat_1 = Reformat_1(spark, df_dataset_bitbucket_csv)
    df_Subgraph_1_out0, df_Subgraph_1_out1 = Subgraph_1(spark, Config.Subgraph_1, df_Reformat_1)
    df_CustomReformatBitbucket_1 = CustomReformatBitbucket_1(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Python_Bitbucket_Pipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Python_Bitbucket_Pipeline", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
