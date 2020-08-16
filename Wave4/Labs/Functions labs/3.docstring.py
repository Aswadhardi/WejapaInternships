def readable_timedelta(days):
    # insert your docstring here
    '''
        readable_timedelta function takes one integer argument(days). It  returns a string that says number of week(s) and number of day(s).  Calling the function and printing the result like this:
        print(readable_timedelta(16))
        should output the following:
        4 week(s) and 0 day(s).
    '''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
