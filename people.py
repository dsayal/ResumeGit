import re

def parse_name(text):
    """This function uses regular expressions to capture the first and last name of the person. 

    Args:
        text (str): represents a single line of the file

    Returns:
       tuple : contains the first amd last name as strings
    """
    reg_expression = (r'^(\w+)\s(\w+)', text)
    match = re.match(reg_expression, text)
    if match:
        return match.group(1), match.group(2)
    else:
        return None


def parse_address(text):
    """This function uses regular expressions in order to capture the street, city, and state of the person.

    Args:
        text (str): represents a single line of the file 

    Returns:
        Address: create and return an address object using the street, city, and state identified. 
    """
    reg_expression  = r"(\d+.*?)\s+([A-Za-z_]+)\s+([A-Z]{2})"
    match = re.search(reg_expression, text)
    if match:
        street, city, state = match.groups()
        return Address(street, city, state)  
    else:
        return None


def parse_email(text):
    """This function uses regular expressions in order to capture the email  of the person. 

    Args:
        text (str): represents a single line of the file 

    Returns:
        str: email identified
    """
    reg_expression = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(reg_expression, text)
    if match:
        return match.group()
    else:
        return None
    
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state


class Employee:
    def __init__(self, line):
        self.first_name, self.last_name = parse_name(line)
        self.address = parse_address(line)
        self.email = parse_email(line)

        
def main(path):
    """Parse the data from a text file and create a list of Employee objects.

    Args:
        path (str): path to the file that is being parsed

    Returns:
        list: A list containing Employee objects parsed from the file.
    """
    employee_list = []
    with open(path, 'r') as file:
        for line in file:
            employee = Employee(line.strip())  
            employee_list.append(employee)
    return employee_list

if __name__ == "__main__":
    employees = main("people.txt")
    print(employees)

    


    
        
        
        
    