# Name:
# SBUID: 

# Remove the ellipses (...) when writing your solutions.

def checkValidInterval(sorted_lst, query):
    """ This function check if the query value can
    exist in the sorted list
    
    Args:
        sorted_lst (list)
        query (int or float)
    
    Returns:
        bool: is the query possibly in the sorted list?
    """
    # Your code here!!
    return False
    
def backwardLinearSearch(lst, query, max_index, min_index):
    """ This function is backward linear search applyed on lst
    in order to find the index of the query value
    the search is backward perform in the range [min_index, max_index]
    
    Args:
        lst (list)
        query (int or float)
        max_index (int)
        min_index (int)
    
    Returns:
        int: index of the query value
        return None if the value is not in list
    """
    # Your code here!!
    return 1

def findStepSize(lst):
    """ Compute the jump step size sqrt(N)
    where N is the length of the list lst
    
    Args:
        lst (list)
    
    Returns:
        int: the ideal jump size for jump sortss
    """
    # Your code here!!
    return 1

def jumpSearch(lst, query):
    """ Implementation of the jump search function
    
    Args:
        lst (list)
        query (int or float)
    
    Returns:
        int: index of the query value in the list
        return None if the value is not in list
    """
    # Your code here!!
    return 1

# ---------------------------- MAIN FCT ---------------------------------
def main():

    lst = [0,2,3,4,10,20,30,50,100,200,300,400,1000,1001]
    query = 300
    print(jumpSearch(lst, query))

    
if __name__ == "__main__": # do not mind this line, it is something we commonly use in python. You can google
    main() # Here we run the main
