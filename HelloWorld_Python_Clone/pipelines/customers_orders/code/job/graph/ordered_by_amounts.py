from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def ordered_by_amounts(spark: SparkSession, customer_order_details: DataFrame) -> DataFrame:
    return customer_order_details.orderBy(col("AMOUNTS").desc())
