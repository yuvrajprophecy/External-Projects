from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def select_customer_orders(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("customer_id"), col("orders"), col("amounts"), col("account_length_days"))
