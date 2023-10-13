def chap_name():
    try: # dakhel try code asli ra vered kon 
       # w =int(input("insert: ")) jehat chek vorodi  ValueError
        #print("gorbah")
        #print(a) ValueError
        #print(3/0) ZeroDivisionError
        #9r = "kkl:" NameError
        #int("kj")
    #exceptions  dar in qesmat anva error ha miarim    
    except SyntaxError:
        print("can't assign to literal")    
    except ZeroDivisionError:
        print("division by zero")
    except ValueError:
        print("value error dadash")
    except:
        print("rafti to baqali dadash")
    else: # ekhtyari 
        print("no exception")
    finally: # ekhtyari 
        print("finally hay anjam shod kaka")
    
chap_name()
# try:
#     lunch()
# except SyntaxError:
#     print('Fix your syntax')
# except TypeError:
#     print('Oh no! A TypeError has occured')
# except ValueError:
#     print('A ValueError occured!')
# except ZeroDivisionError:
#     print('Did by zero?')
# else:
#     print('No exception')
# finally:
#     print('Ok then')