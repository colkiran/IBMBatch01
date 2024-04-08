
num = 10
div ="0"

try:
    res = num / div

except ZeroDivisionError as z:
    print("Exception Occured......")
    print(z)
except TypeError as t:
    print("Exception Occured......")
    print(t)
except Exception as e:
    print("Exception happened......")
    print(e)


else:
    print(f"res :{res}")

finally:
    print("Completed the job of division.......")