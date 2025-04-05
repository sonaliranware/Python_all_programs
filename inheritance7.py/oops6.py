class demo:
    def __init__(self):
        print("this is default constructor calling....")
    def __del__(self):
        print("this is default distructor calling....")
d=demo()
del d            