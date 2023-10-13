name1 = 'Eva, can I see bees in a cave'
name = name1.replace(' ','')
name = name.replace(',','')
name = name.replace("’",'')
name=name.lower()
print(name)
len_name = len(name)
print(len_name)
if len_name % 2 == 1:
    mid = int(len_name/2)
    first =name[:mid][::-1]
    last = name[mid+1:]
    if last == first:
        print(f"{name1} -->  is palindrome")
    else:
        print(f"{name1} -->  is not palindrome")
else:
    mid = int(len_name/2)
    first =name[:mid][::-1]
    last = name[mid:]
    if last == first:
        print(f"{name1} -->  is palindrome")
    else:
        print(f"{name1} -->  is not palindrome")