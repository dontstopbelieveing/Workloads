To set up the test use setup.py - It can help set up x databases with y tables each 
To run the test use workload.py 
If your workload is 200 connections at a time, each connection doing about 10 inserts per second - spin up 200 threads and increase the for loop for inserts to 10.
To simulate the load run workload.py once per second
To clean up after tests and drop objects use teardown.py
