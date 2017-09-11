import urllib2
import httplib
from math import sqrt
scope = {'url':urllib2}
# urllib2.urlopen('http://www.baidu.com')
exec 'print url.urlopen(\'http://www.baidu.com\')' in scope
print len(scope)
print scope.keys()

print eval('4*12')