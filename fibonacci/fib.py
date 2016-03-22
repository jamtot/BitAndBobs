import time

def rec_fib(num):
    if num<=1:
        return num
    else:
        return rec_fib(num-1)+rec_fib(num-2)

def iter_fib(num):
    a=0
    b=1
    count=1
    #print b
    while count<num:    
        b,a=a,a+b
        count+=1
    return a

start=time.time()
for x in xrange(30):
    rec_fib(x)
end=time.time()
print "Time elapsed for recursive fibonacci sequence - %r secs"%(
            end-start)#0.44219398498535156 secs


start2=time.time()
iter_fib(30)
end2=time.time()
print "Time elapsed for iterative fibonacci sequence - %r secs"%(
            end-start2)#-4.696846008300781e-05 secs
