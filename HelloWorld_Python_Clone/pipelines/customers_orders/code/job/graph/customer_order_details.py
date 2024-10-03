from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def customer_order_details(spark: SparkSession, customers: DataFrame, customers_orders: DataFrame, ) -> DataFrame:
    return customers\
        .alias("customers")\
        .join(
          customers_orders.alias("customers_orders"),
          (col("customers.customer_id") == col("customers_orders.customer_id")),
          "inner"
        )\
        .select(col("customers.customer_id").alias("CUSTOMER_ID"), col("customers.first_name").alias("FIRST_NAME"), col("customers.last_name").alias("LAST_NAME"), col("customers.phone").alias("PHONE"), col("customers.email").alias("EMAIL"), col("customers.country_code").alias("COUNTRY_CODE"), col("customers.account_open_date").alias("ACCOUNT_OPEN_DATE"), col("customers.account_flags").alias("ACCOUNT_FLAGS"), col("customers_orders.orders").alias("ORDERS"), col("customers_orders.amounts").alias("AMOUNTS"), col("customers_orders.account_length_days").alias("ACCOUNT_LENGTH_DAYS"))
