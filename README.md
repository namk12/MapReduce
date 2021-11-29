# MapReduce Tasks on Nee York City Taxi Data
Big Data MapReduce Coding

Task 1: Map-reduce job that joins the 'trips' and 'fare' data (taxi data).
The 'fares' and 'trips' data share 4 attributes:
      medallion, hack_license, vendor_id, pickup_datetime.
The join MUST BE a reduce-side inner join.
Output: A key-value pair per line. Use a “tab” to separate key and value, a comma between multiple keys (and values)
      key: medallion, hack_license, vendor_id, pickup_datetime 
      value: the remaining attributes of 'trips' data in their original order and the remaining attributes of 'fare' data in their original order.


Task 2: Map-reduce jobs for each of the following sub-tasks, using the output of Task 1 (joined data) as input:

a) Find the distribution of fare amounts (fare_amount) for each of the following ranges:
[0, 20], [20.01, 40], [40.01, 60], [60.01, 80], [80.01, infinite],
Output: A key-value pair per line, where the key is the range, and the value is the number of trips. For example,
          0,20 100
          20.01,40   300
          ...

b) Find the number of trips whose cost is less than or equal to $15 (total_amount). Output: The number of trips.

c) Find the distribution of the number of passengers, i.e., for each number of passengers A, the number of trips that had A passengers.
Output: A key-value pair per line, where the key is the number of passengers, and the value is the number of trips.

d) Find the total revenue (for all taxis) and the total amount of tips, per day (from pickup_datetime). Revenue should include the fare amount, tips, and surcharges.
Output: A key-value pair per line, where the key is the day YYYY-MM-DD, and the value contains the total revenue and the total tips for that day, in this order.
Use two decimal digits, e.g., 3.02245 should be represented as 3.02. For example,
            2016-01-01    100000.02,11000.00
            2016-01-02    202000.00,1000.00

e) For each taxi (medallion) find the total number of trips, and the average number of trips per day. For the average trips per day, use 2 decimal digits.
Your average should be over all days that the taxi drove, e.g., if the input data has entries for a given taxi on 6 different days, your average should be over 6 days.
Output: A key-value pair per line, where the key is the medallion, and the value contains the total number of trips and the average number of trips per day.

f) Find the number of different taxis (medallion) used by each driver (license). 
Output: A key-value pair per line, where the key is the driver, and the value is the number of different taxis used by that driver.
