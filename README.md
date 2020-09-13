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




EXECUTION STEPS 
To start Zookeeper. --- 
Run ./start_zookeeper.sh

To Start Kafka Broker ---
Run ./start_kafka.sh


To start producing police call records in Topic through Kafka Producer call  ----
python kafka_server.py 

To list topic through Kafka CLI. ----
kafka-topics --list --zookeeper localhost:2181

Details about project topic  ----
kafka-topics --describe --topic com.city.sf.police.department.calls.v1 --zookeeper localhost:2181


To check Producer is producing correct records,run Consumer through CLI. ----
kafka-console-consumer --topic "com.city.sf.police.department.calls.v1" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning

To Run consumer Server. ----- python consumer_server.py

To run data_stream.py ----
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 data_stream.py
