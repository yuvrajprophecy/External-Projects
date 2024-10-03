from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_customers_orders = customers_orders(spark)
    df_customer_order_details = customer_order_details(spark, df_customers, df_customers_orders)
    df_ordered_by_amounts = ordered_by_amounts(spark, df_customer_order_details)
    df_limited_sort_results = limited_sort_results(spark, df_ordered_by_amounts)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_orders")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/customers_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
