# python-comment-uncomment

This is a simple program in python to comment and uncomment linnes in a file.<br/>
It takes the string to be commented as an input. The line to be commented should start with the string passed in argument.<br/>
-c for comment, -u for uncomment

```
localhost% cat sample
one
two
three
one
three
localhost% python check.py -c one
localhost% cat sample
#one
two
three
#one
three
localhost% python check.py -u one
localhost% cat sample
one
two
three
one
three
localhost% python check.py -u one
localhost% cat sample
one
two
three
one
three
localhost% python check.py -c one
localhost% cat sample
#one
two
three
#one
three
localhost% python check.py -c one
localhost% cat sample
#one
two
three
#one
three
localhost% python check.py -c two
localhost% cat sample
#one
#two
three
#one
three
localhost% python check.py -u one
localhost% cat sample
one
#two
three
one
three
localhost% python check.py -u two
localhost% cat sample
one
two
three
one
three
```
