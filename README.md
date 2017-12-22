# DAUtilites
Utility snippets for data analytics


## RecodeLongFiles
A code snippet that is useful for processing of data from the client when the files are big and the encoding and other issues are incompatible with SQL Server's upload tool. 

## GraphAnalysis-Example
This code allows to identify users within a credit organisation who need to be investigated based on the performance indicators of credit products that they work with. The code requires credit data with user ids, non-performance indicators, credit balance, credited amount, non-serviced indicator, and less4months indicators linked to the client of the loan.
The code can be re-used for any dataset where there is a list of user id's associated with some action (edges of graph), and a list of 'goodness' of action needs to be weighted to show the 'quality' of connection between users.
