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
import datetime

#might not need pprint later but its good for visualization
from pprint import pprint

# Useful as a global variable instead of parameter to everything
# use:  'global guild_ledger' at start of functions
guild_ledger = None
today = datetime.datetime.now().strftime("%m/%d/%Y")
guild_funds_file = 'guild_funds.json'

def set_guild_ledger(tmp):
    '''
        Sets the ledger for the tracking script.  Useful for
        test/debugging or for running with a specific script from
        an alternate program
    '''
    global guild_ledger
    guild_ledger = tmp
    return

def get_guild_ledger():
    '''  returns the full ledger dictionary '''
    return guild_ledger

def get_total_funds():
    ''' Returns the total guild funds amount '''
    return guild_ledger["total_funds"]

### -------------------------------- ###
###   Transactions for guild ledger  ###
### -------------------------------- ###
def new_entry(amount, reason, date=today):
    ''' Takes the amount and reason as data and
        appends it to the appropriate location
        in the json object

        Can be positive or negative values
        If date exists, add to list
        otherwise:  create new list with this entry at date
    '''
    date_data = { "amount": amount, "reason": reason}
    
    if date in guild_ledger:
        guild_ledger[date].append(date_data)
    else:
        guild_ledger[date] = [date_data]
    
    # calculate into guild fund total
    guild_ledger["total_funds"] += amount
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