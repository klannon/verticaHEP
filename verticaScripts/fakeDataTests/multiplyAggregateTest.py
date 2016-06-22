#!/opt/vertica/oss/python/bin/python
#
# Notice which python is executing

import hp_vertica_client


def main():
    conn = hp_vertica_client.connect("")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS Moria")
    cursor.execute("CREATE TABLE Moria(Event int, dwarves float, goblins float)")
    cursor.execute("COPY Moria FROM '/home/newdbadmin/fakeDataTests/Moria.txt'")

    test_query = "select EXP(SUM(LN(dwarves))) FROM Moria"

    test_query2 = "SELECT Event, CASE	WHEN min = 0 THEN 0 WHEN neg % 2 = 1 THEN -1* EXP(prod) ELSE EXP(prod) END FROM ( SELECT Event, SUM(LN(ABS(dwarves))) as prod, SUM(CASE WHEN dwarves < 0 THEN 1 ELSE 0 END) as neg, MIN(ABS(dwarves)) as min FROM Moria GROUP BY Event) subQ "
    
    cursor.execute(test_query2)

    print "Test Query results: {0}".format(cursor.fetchall())
    

if __name__ == "__main__":
    main()
