from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

nyctaxi = glueContext.create_dynamic_frame.from_catalog(database="glue-demo", table_name="s3_nyctaxi")
print('Count: ', nyctaxi.count())
nyctaxi.printSchema()
