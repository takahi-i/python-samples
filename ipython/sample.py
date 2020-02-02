# https://recruit-tech.co.jp/blog/2018/10/16/jupyter_notebook_tips/#b3 より
def foo():
    a = list([i*2**2+1 for i in range(10)])
    b = list([i if i % 2 == 0 else 0 for i in range(2, 53, 5)])
    c = a + b
    for i in range(len(c)-1):
        idx = int(i/2)
        c[i] += i + a[-idx] + b[idx]
        c[-i] += i + a[idx] + b[-idx]
    raise Exception
    d = len([i*2**2+1 for i in range(-80, 130, 10)])
    return c * d
