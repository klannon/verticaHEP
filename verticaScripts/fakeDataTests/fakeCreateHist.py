#!/opt/vertica/oss/python/bin/python
#
# Notice which python is executing

import hp_vertica_client


def main():
    conn = hp_vertica_client.connect("")
    cursor = conn.cursor()

    test_query = "select Gondor  from fakeData"
    
    cursor.execute(test_query)

    print "Test Query results: {0}".format(cursor.fetchall())
    

if __name__ == "__main__":
    main()
