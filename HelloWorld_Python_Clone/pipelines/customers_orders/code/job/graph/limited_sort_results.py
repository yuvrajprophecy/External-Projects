from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def limited_sort_results(spark: SparkSession, ordered_by_amounts: DataFrame) -> DataFrame:
    return ordered_by_amounts.limit(50)
