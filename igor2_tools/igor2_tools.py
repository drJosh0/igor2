

'''
SEARCH
SORT
SAVE
'''


class Search:

    def __init__(self, args):
        if args[-2:] == '-s':
            self.stringsearch = args
        elif args[-2:] == '-r':
            self.reportsearch = args
        else:
            raise ValueError


class Sort:

    def __init__(self, company, report):
        self.company = company
        self.report = report