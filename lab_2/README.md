# Tasks for Lab 2

## Task 1.
Log file analyzer. Write a function that takes the path to an HTTP server log file as input and reads each line. Count the number of occurrences of unique HTTP response codes (e.g., 200, 404, 500). Store the results in a dictionary where the keys are response codes and the values are their counts. Handle possible exceptions such as missing file or read errors. Return the resulting dictionary.

## Task 2.
File hash generator. Write a function that takes multiple file paths as input and calculates the SHA-256 hash of each file. Store the results in a dictionary where the keys are file paths and the values are the hashes in hexadecimal format. Handle exceptions such as missing files or read errors. Use the hashlib library to compute the hashes. Return the dictionary with hashes.

## Task 3.
IP address filter. Write a function that reads IP addresses from a log file and checks whether each address is present in a predefined list of allowed IPs. Count how many times allowed IPs occur and save the result to an output file in the format <IP address> - <count>. Handle exceptions such as missing input file or write errors for the output file.
