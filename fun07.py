# **kwargs

def myfun(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}")

myfun(name="ravi",subject="python")