import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
try:
    fn = input("fn: ")
    ln = input("ln: ")
    eid = input("EID: ")
    gender = input("gender: ")
    age = int(input("age: "))
    sal = int(input("salary: "))
    sql = "INSERT INTO EMPLOYEE (`FIRST_NAME`, `LAST_NAME`, `EID`, `GENDER`, `AGE`, `SALARY`) VALUES ('{}', '{}', '{}', '{}', {}, {})".format(fn, ln, eid, gender, age, sal)
    c.execute(sql)
    conn.commit()
    print("Created Successfully.")
except:
    print("Error.")
    conn.rollback()
finally:
    conn.close()
