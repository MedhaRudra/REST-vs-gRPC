# Experimental Comparison of REST and gRPC APIs 

## Overview
Thi sproject demonstrates the programmatic and performance differences between REST and gRPC API's. We develop a REST and a gRPC API then compare the performance for latency / bandwidth.

## Experiment
We use the client to accept a command-line argument indicating the endpoint to be tested and the number of iterations to test. For example,
in REST:
```
python rest-client.py localhost add 1000
```
and in gRPC:
```
python grpc-client.py localhost add 1000
```
would run the `add` endpoint 1000 times against the server on the `localhost` and then report the time taken divided by the number of queries (1000). This gives a time-per-query, which is expressed in milliseconds. The python `perf_counter` routine from the [`time` module] makes it easy to conduct such timing tests. We measure multiple queries because each query is fairly short and we want to average over many such queries.

All experiments have ben conducted on VM instance of Google Cloud Platform (`e2-standard-2` instance)

## Results
| Method 			| Local  |Same Zone | Different Region |
| ------------------|--------|----------| -----------------|
| REST add  		| 3.28	 | 4.07   	| 289.11
| gRPC add  		| 0.55   | 0.61		| 149.59
| REST rawImage		| 7.60   | 7.93		| 1199.88
| gRPC rawImage  	| 8.79   | 9.22		| 209.12
| REST dotproduct 	| 4.46   | 5.54		| 292.72
| gRPC dotproduct  	| 0.75   | 0.84 	| 146.24
| REST jsonImage  	| 68.80  | 75.61 	| 1376.48
| gRPC jsonImage  	| 28.79  | 30.46	| 244.78
| PING				| 0.044	 | 0.356	| 148.18

(NOTE: all time delays mentioned above are in ms)

## Observation:
It is observed that, in general, gRPC performs better than REST. The fact that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries compensates for the above observation. From the results obtained, we can see that gRCP perform roughly 2.5 to 3 times better on an average over all tasks compared to REST. gRPC is designed for low latency and high throughput communication, which makes it ideal for applications where efficiency is critical (eg. real-time streaming applications). Use of protocol buffer in gRCP makes the payload lighter and also serializes the data.
