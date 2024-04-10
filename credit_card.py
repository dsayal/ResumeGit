"""Perform credit card calculations."""
from argparse import ArgumentParser
import sys
def get_min_payment(balance, fees=0):
    """
    This function computes the minimum credit card payment. 
    The paramteres include balance, fees, and m. Balance is of str data type and is the total amount of balance in an account that is left to pay. 
    Fees is of str data type and are the fees associated with the credit card account. 
    m is represented as a float and serves as the percent of the balance that needs to be paid. 
    This function returns the minimum payment. 
    
    """
    m = 0.02
    min_payment = (balance * m) + fees
    if min_payment < 25: 
        min_payment = 25
    return min_payment 
def interest_charged(balance, apr):
     """
     This function computes and returns the amount of interest accured in the next payment according to a specific formula. 
     The parameters include balance(str) and apr(int).
     Balance is the balance on the credit card that has not been paid off yet. Apr is an int between 0-100 which is the annual APR. 
     This function returns the interest value.  

     """
     a = apr / 100
     y = 365
     d = 30
     b = balance
     i = (a/y) * b * d 
     return i 
def remaining_payments(balance, apr, targetamount=None, credit_line=5000, fees=0):
     """
     This function computes the number of payments required to pay off the credit card balance. 
     The parameters consist of balance(str), apr(int), targetamount(str), credit_line(int), fees(int). 
     Balance is the amount on the credit card that has not been paid off yet. Apr is an int between 0-100 which is the annual apr. 
     The targetamount is the amount the user wants to pay per payment. Credit_line is the maximum balance that an account holder can keep in their account. It defaults to 5000. 
     Fees is the amount of fees that will be charged in addition to the minimum payment. 
     This function returns the number of payments required to pay off the credit card balance (tup). 

     """
     payment_counter = 0 
     payment = 0 
     paymentabove_25 = 0
     paymentabove_50 = 0
     paymentabove_75 = 0
     while balance > 0:
          if targetamount == None:
               payment = get_min_payment(balance, fees)
          else: 
               payment = targetamount
          payment -= interest_charged(balance,apr)
          if payment <0:
               sys.exit("Your card balance cannot be paid off")
          balance -= payment

          if balance >=(credit_line*0.75):
               paymentabove_75+=1
          if balance >= (credit_line*0.50):
               paymentabove_50+=1
          if balance >= (credit_line*0.25):
               paymentabove_25+=1
          payment_counter += 1
     return payment_counter, paymentabove_25, paymentabove_50, paymentabove_75
              
def main(balance, apr, targetamount= None, credit_line=5000, fees=0):
     """
     This function computes the recoomended minimum payment using the get_min_payment function. It displays the recommended minimum payment to the user. 
     The parameters consist of balance(str), apr(int), targetamount(str), credit_line(int), fees(int). 
     Balance is the amount on the credit card that has not been paid off yet. Apr is an int between 0-100 which is the annual apr. 
     The targetamount is the amount the user wants to pay per payment. Credit_line is the maximum balance that an account holder can keep in their account. It defaults to 5000. 
     Fees is the amount of fees that will be charged in addition to the minimum payment. 

     """
     x = ""
     min_payment = get_min_payment(balance, fees)
     total_payment = remaining_payments(balance, apr, targetamount, credit_line, fees)
     pays_minimum = False
     if targetamount == None:
           pays_minimum = True
     elif targetamount < min_payment:
          x += ("Your target payment is less than the minimum payment for this credit card")
          quit()    
     x += f"Your recommended starting minimum payment is ${min_payment}"
     if pays_minimum == True:
          x += f"\nIf you pay the minimum payments each month, you will pay off the credit card in {total_payment[0]} payments"
     else:
          x += f"If you make payments of ${targetamount}, you will pay off the credit card in {total_payment[0]} payments."
     
     x += f"\nYou will spend a total of {total_payment[1]} months over 25% of the credit line, You will spend a total of {total_payment[2]} months over 50% of the credit line, You will spend a total of {total_payment[3]} months over 75% of the credit line"
     return(x)
                      
def parse_args(args_list):
     """Takes a list of strings from the command prompt and passes them through as
     arguments
     Args:
     args_list (list) : the list of strings from the command prompt
     Returns:
     args (ArgumentParser)
     """  
     parser = ArgumentParser()
     parser.add_argument('balance_amount', type = float, help = 'The total amount of balance left on the credit account')
     parser.add_argument('apr', type = int, help = 'The annual APR, should be an int between 1 and 100')
     parser.add_argument('credit_line', type = int, help = 'The maximum amount of balance allowed on the credit line.')
     parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
     parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')
    # parse and validate arguments
     args = parser.parse_args(args_list)
     if args.balance_amount < 0:
        raise ValueError("balance amount must be positive")
     if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
     if args.credit_line < 1:
        raise ValueError("credit line must be positive")
     if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
     if args.fees < 0:
          raise ValueError("fees must be positive")
     
     return args
     


if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    print(main(arguments.balance_amount, arguments.apr, credit_line = arguments.credit_line, targetamount = arguments.payment, fees = arguments.fees))