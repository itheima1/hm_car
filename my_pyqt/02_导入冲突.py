
# from hello import say
# from hi import say

# import hello
# import hi

from hello import say as hello_say
from hi import say as hi_say


if __name__ == '__main__':
    # # hello的say
    # hello.say()
    #
    # # hi的say
    # hi.say()

    hello_say()
    hi_say()