# udacity-spark-streaming-project
Udacity Project 2 - Spark Streaming and Kafka

Questions

Question - 1 How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Changing various config properties on Spark session as wells as the Kafka properites through .option() on readStream, I noticed below two parameters are affected               inputRowsPerSecond and processedRowsPerSecond 
which clearly indicates the throughput and latency for each micro batch of Spark Streaming

Question 2 - What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

spark.sql.shuffle.partitions - 3 (Default was 200 which was not necessary for this Streaming applicaiton data)
spark.executor.cores - 3 ( As it was ran on local workspace)
spark.streaming.kafka.maxRatePerPartition - 80
