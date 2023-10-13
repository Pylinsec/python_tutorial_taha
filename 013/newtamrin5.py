# with open("taha2.txt","r") as golabi:
# #     print(golabi.readlines())
#     for line in golabi.readlines():
#         
#         if "hamid hamidi\n"==line:
#             print("baba hast bikhial")
#             break
#         else:
#             print("baba nist ya eshkal dar code")
            
#  halat  dovom vaqti hame dar tak line bashad
with open("taha2.txt","r") as golabi:
    list=golabi.readline().split(',')
    print(list)
    for line in list:
        if line=="hamid hamidi":
             print("baba hast bikhial",list.index("hamid hamidi"))
             break
        else:
            print("baba nist ya eshkal dar code")