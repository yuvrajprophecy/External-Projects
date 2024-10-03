from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sdgfdsfsdf.config.ConfigStore import *
from sdgfdsfsdf.functions import *
from prophecy.utils import *
from sdgfdsfsdf.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("sdgfdsfsdf")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/sdgfdsfsdf")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/sdgfdsfsdf", config = Config)(pipeline)

if __name__ == "__main__":
    main()
