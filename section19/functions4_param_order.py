"""
PARAMETER ORDERING

1. Parameters
2. *args
3. Default parameters
4. **kwargs

"""
def display_info(a,b,*args,instructor="Colt", **kwargs):
    return [a,b,args,instructor,kwargs]

print(display_info(1,2,3,last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args - (3) (tuple)
# default param: instructor - "Colt" (cause nothing was passed in)
# kwargs - {last_name: "Steele", job="Instructor} (Dict)