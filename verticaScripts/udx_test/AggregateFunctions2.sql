/*****************************
 * Vertica Analytic Database
 *
 * Example SQL for User Defined Aggregate Functions
 *
 * Copyright (c) 2005 - 2015 Hewlett Packard Enterprise Development LP 
 */


-- Step 1: Create LIBRARY 
\set libfile '\''`pwd`'/AggregateFunctions/AggregateFunctions.so\'';
CREATE LIBRARY AggregateFunctions AS :libfile;

-- Step 2: Create Functions
/*
CREATE AGGREGATE FUNCTION agg_average AS LANGUAGE 'C++'
NAME 'AverageFactory' LIBRARY AggregateFunctions;
*/
/*
CREATE AGGREGATE FUNCTION agg_concatenate AS LANGUAGE 'C++'
NAME 'ConcatenateFactory' LIBRARY AggregateFunctions; 

CREATE AGGREGATE FUNCTION agg_count AS LANGUAGE 'C++'
NAME 'CountOccurencesFactory' LIBRARY AggregateFunctions;
*/

CREATE AGGREGATE FUNCTION agg_multiply AS LANGUAGE 'C++'
NAME 'MultiplyFactory' LIBRARY AggregateFunctions;
/*
CREATE AGGREGATE FUNCTION agg_sum AS LANGUAGE 'C++'
NAME 'SumFactory' LIBRARY AggregateFunctions;
*/
-- Step 3: Use Functions

-- Example table used by Average and Concatenate.

CREATE TABLE T (x INTEGER, y NUMERIC(5,2), z VARCHAR(10));
COPY T FROM STDIN DELIMITER ',';
1,1.5,'A'
1,3.5,'A'
2,2.0,'B'
2,3.0,'A'
2,2.6,'B'
2,1.4,'A'
3,0.5,'C'
3,3.5,'C'
3,1.5,'B'
3,7.5,'B'
\.


CREATE TABLE T2 (ewoks float, gungans float);
COPY T2 FROM STDIN DELIMITER ',';
1,42
2,42
2,42
3,42
3,0
4,42
4,-1
5,42
5,-1
5,-1
\.

/***** Example 1: Average *****/
/*
-- Invoke UDF
SELECT x, z, agg_average(y) as average
FROM T
GROUP BY x, z
ORDER BY x, z;
*/
/*
--Add
Select ewoks, agg_sum(gungans)
FROM T2
GROUP BY ewoks;
*/
--Multiply

SELECT ewoks, agg_multiply(gungans)
FROM T2
GROUP BY ewoks;

/***** Example 2: Concatenate *****/

-- Invoke UDF
/*
SELECT ts.x, agg_concatenate(ts.z) as concat
FROM (
  SELECT x, z
  FROM T
  ORDER BY x, z) as ts
GROUP BY x;
*/
/******* Example 3: Count Occurences of a num *******/
/*
SELECT agg_count(y using parameters n=1.5) as num_occurences
FROM T;

SELECT x, agg_count(y using parameters n=1.5) as num_occurences
FROM T group by x;
*/
-- Step 4: Cleanup
DROP TABLE T;
DROP TABLE T2;
DROP LIBRARY AggregateFunctions CASCADE;
