
# Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".
items = [1,2,3,4,5]
try: 
    item = items[4]
    print(item)
except Exception as e: 
    print("Item does not exist in the list", e)

    
# Add exception handling to return back 0 instead of allowing the error to be thrown.
def divide_by(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return 0

ans = divide_by(40, 0)
print(ans)


# Add exception handling to catch this error and return the following "The file could not be found".
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found")
