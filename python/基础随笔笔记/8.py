while True:
    year = int(raw_input('please input a year:'))
    if year%100 ==0 and year%400 == 0:
        print 's is leap year '%(year)
    elif year%100>0 and year%4==0:
         print '%s is leap year'%(year)
else:
    print 'not'
