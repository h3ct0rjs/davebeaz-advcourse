#!/usr/bin/env python 
import csv 

def greeting(name):
    '''
    Issues a greeting, this is call the docstring 
    and it help you to show info in the interactive interpreter.
    '''
    print('Hallo {}!'.format(name))

def portfolio_cost(filename):
    rows = []
    const_val = 231
    total = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:  
            total +=row[2]*const_val
    return total

def portfolio_cost_power(filename='data2.csv', * , debug='silence'):
    # defensive positions in function definitions
    if debug not in {'warn','silence','raise'}:
        raise ValueError("Erros for debug should be 'warn','silence','raise'")

    total = 0.0 

    with open(filename,'r') as f: 
        rows = csv.reader(f)
        header = next(rows)
        for rownumber, row in enumerate(rows,start = 1 ):
            try: 
                row[2]  = float(row[2])
                row[0]  = str(row[0])
            #except Exception as err: #Really a bad idea and dangerous. 
            except ValueError as err:
                if debug == 'warn': 
                    print('Error in Row# {},\nFailed Row: {}'.format(rownumber,row))
                    print('Reason for the error : {}'.format(err))
                elif debug == 'raise':
                    raise 
                else : 
                    pass

                continue
            total+=row[2]*len(row[0])
    return total


def main():


    '''
    Main Function
    '''
    #data_path = 'data2.csv'
    #total_shares = portfolio_cost(data_path)
    #print(total_shares)
    total_shares = portfolio_cost_power(debug=True)
    print(total_shares)



if __name__ == '__main__':
    main()
