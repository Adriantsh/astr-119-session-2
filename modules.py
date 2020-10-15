import test_module as tm

tm.helloworld()

x = 10.0

s = "The second function is 2.0 * %f + 1.0 = %f." % (x,tm.second_func(x))

print(s)