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

**Observation:**\
It is observed that, in general, gRPC performs better than REST. The fact that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries compensates for the above observation. From the results obtained, we can see that gRCP perform roughly 2.5 to 3 times better on an average over all tasks compared to REST. gRPC is designed for low latency and high throughput communication, which makes it ideal for applications where efficiency is critical (eg. real-time streaming applications). Use of protocol buffer in gRCP makes the payload lighter and also serializes the data.
