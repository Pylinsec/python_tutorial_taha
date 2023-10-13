
def lunch():
    'foo' = 1
    print("lunch from function")
try:
    lunch()
except SyntaxError:
    print("can't assign to literal")
else:
     pass # ek
finally:
    pass
    
    