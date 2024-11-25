def add_before_UI_after_UI (func):

 def wrapper():
     print("before running the testcase")
     print("start the browser")
     func()  #test(UI)
     print("ending running tc")
     print("quit browser!")

 return wrapper()  # before_after


@add_before_UI_after_UI
def test_ui():
    print("i'll test ui")