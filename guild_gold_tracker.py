''' 
Program:  To keep logs of gold spending for our DnD campaign

Basic goals:
	Read from file, get total current gold
	Add to/sub from it with specific data
		Write in to file tracking for history
	Use prompts to access it
	Gain values like "How much is party funds how much personal"

Stretch goal:
    modify entries
    add compendium of items and values to view and purchase
        includes viewing for personal gold expenses
    when rewards are added, display breakdown of loss, guild, and personal amounts

Important notes:
    keywords in json:
        "total_funds" - the total of all the guild funds
        "dd/mm/yy" - format for date of entry
            "amount" - amount spent/gained
            "reason"  - reason for expense/income

'''
import json
#might not need pprint later but its good for visualization
from pprint import pprint
import datetime

# Useful as a global variable instead of parameter to everything
# use:  'global guild_ledger' at start of functions
guild_ledger = None
today = datetime.datetime.now().strftime("%m/%d/%Y")
guild_funds_file = 'guild_funds.json'

def get_guild_funds():
    ''' Returns the total guild funds amount '''
    return guild_ledger["total_funds"]

### -------------------------------- ###
###   Transactions for guild ledger  ###
### -------------------------------- ###
def new_transaction(amount, reason, date=today):
    ''' Takes the amount and reason as data and
        appends it to the appropriate location
        in the json object
        Can be adding or subtracting
    '''
    date_data = { "amount": amount, "reason": reason}
    if date in guild_ledger:
        guild_ledger[date].append(date_data)
    else:
        guild_ledger[date] = [date_data]
    guild_ledger["total_funds"] += amount
    return

def new_expense(amount, reason, date):
    ''' Name abstraction for simplicity '''
    new_transaction(amount, reason, date)
    return

def new_earnings(amount, reason, date):
    ''' Name abstraction for simplicity '''
    new_transaction(amount, reason, date)
    return

def get_data(file_name):
    content = None
    try:
        with open(file_name, 'r') as content_file:
            content = json.load(content_file)
    except:
        print("No file found for \"" + file_name + "\"")
    return content

def main():
    #print('working')
    global guild_ledger

    guild_ledger = get_data(input('Enter a file name (or press enter for default): ') or guild_funds_file)
    if guild_ledger is None:
        print("Shutting down...")
        return
    else:
        print("The guild has: %dgp" % get_guild_funds())

    pprint(guild_ledger)
    with open("test_write.txt", "w") as overwrite:
        json.dump(guild_ledger, overwrite)

    #comment out when in production


if __name__ == '__main__':
    main()




#print("Works when imported")