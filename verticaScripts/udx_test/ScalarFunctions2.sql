\set libfile '\''`pwd`'/ScalarFunctions/MyUDx.so\'';
CREATE LIBRARY MyUDx AS :libfile;

CREATE FUNCTION mult2Floats AS LANGUAGE 'C++' NAME 'Mult2FloatsFactory' LIBRARY MyUDx;

CREATE TABLE T (c1 INTEGER, c2 float, c3 float, c4 INTEGER);
COPY T FROM STDIN DELIMITER ',';
1,2,3,4
2,2,5,6
3,2,9,3
1,4,5,3
5,2,8,4
\.

SELECT c2,c3, mult2Floats(c2,c3) from T;

DROP FUNCTION mult2Floats(x float, y float);
DROP TABLE T;
DROP LIBRARY MyUDx CASCADE;
