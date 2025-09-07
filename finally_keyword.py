def func():
    try:
        l=[1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        # return "a"
    
    except:
        print("Some error occured")
        # return "b"
    
    finally:
        print("I am always exceuted")
    # print("I am always exceuted")  
    
func()
