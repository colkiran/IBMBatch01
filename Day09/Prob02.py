
try:

    FL = open("C:\Training\PycharmProjects\IBMBatch01\Day09\Employe.csv", "r")
    st = FL.read()
    print(st)
    FL.close()

except FileNotFoundError as f:
    print("Exception Occured.....")
    print(f)
except Exception as e:
    print(e)

finally:
    print("file operation completed successfully")
