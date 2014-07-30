__author__ = 'ONISYN'

def round_down_and_out(isk, remainder):
    amt_to_round_to = 1000000
    #divmod(isk, amt_to_round_to)

    remainder = isk % amt_to_round_to
    isk = isk - remainder

    print isk
    print remainder

    return(isk, remainder)
