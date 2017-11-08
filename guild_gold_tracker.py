''' 
Program:  To keep logs of gold spending for our DnD campaign
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

### -------------------------------- ###
###   Setters and Getters for Ledger ###
### -------------------------------- ###
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

def remove_entry(date, index, refund=False) :
    '''  Remove an entry from the ledger
        If the value should be refunded, set
        total gold appropriately.  If no more entries
        in the date, remove it from the ledger

        returns entry that was removed or False if nothing removed
    '''
    if not entry_exists(date, index):   # entry does not exist
        return False

    entry = guild_ledger[date][index] # get the index from the ledger
    
    #   Remove entry. If last entry in date, remove date
    del guild_ledger[date][index]
    if len(guild_ledger[date]) == 0:
        del guild_ledger[date]
    
    # If refund is selected, take the amount and remove it from the total gold counter
    # If it was an addition subtract it, subtraction add missing value back to total
    if refund:
        guild_ledger["total_funds"] -= entry["amount"] # used in refund

    return entry  # return entry in case you need to un-do deletion

def remove_all_entries(date, refund=False):
    '''  Removes all entries by date 
         Returns a list of all entries removed, Empty list if nothing was removed
    '''
    if not date_exists(date):
        return False

    # Keep removing until no longer possible
    removed_entries = []
    removed = True
    while removed:
        removed = remove_entry(date, 0, refund) # removes first entry if it exists
        if removed:
            removed_entries.append(removed)

    return removed_entries  # return list of all removed entries in case of deletion un-do

def date_exists(date):
    ''' Return whether this is a valid date within the ledger '''
    return date in guild_ledger

def entry_exists(date, index):
    ''' Return whether a specific index can be found at that date '''
    return date_exists(date) and index < len(guild_ledger[date])


### -------------------------------- ###
###   Entry to Text Display          ###
### -------------------------------- ###
def display_total_funds():
    return "\tTotal Guild Funds: " + str(get_total_funds())

def display_single_entry(date, index):
    '''
        Display for single entry in ledger
        ----------------------------------
           Amount  |   $$$$$$
           Reason  |   "Reason for entry"
        ----------------------------------
    '''
    if not entry_exists(date, index):
        return "|\tInvalid: Entry could not be found\t|"
    entry = guild_ledger[date][index]
    tab = 10
    amount = "Amount |".ljust(tab) + str(entry["amount"])
    reason = "Reason |".ljust(tab) + entry["reason"]
    divider = ""
    for i in reason:
        divider += "-"

    return divider + "\n" + amount + "\n" + reason + "\n"

def display_entries_for_date(date):
    '''
        Displays all single entries within the date requested
    '''
    if not date_exists(date):
        return ""
    return_str = "\"" + date + "\"\n"
    for i in range(len(guild_ledger[date])):
        return_str += display_single_entry(date, i)

    return return_str

def display_full_ledger():
    '''
        Displays the full ledger in a nice easy-readable way
    '''
    return_str = ""
    for date in guild_ledger:
        if date != "total_funds":
            return_str += display_entries_for_date(date)
    return return_str + "\n" + display_total_funds()

### -------------------------------- ###
###   Main Settup and Building       ###
### -------------------------------- ###
def get_data(file_name):
    content = None
    try:
        with open(file_name, 'r') as content_file:
            content = json.load(content_file)
    except:
        print("No file found for \"" + file_name + "\"")
    return content

def main():
    global guild_ledger

    guild_ledger = get_data(input('Enter a file name (or press enter for default): ') or guild_funds_file)
    if guild_ledger is None:
        print("Shutting down...")
        return

    print(display_full_ledger())
    
    with open("test_write.txt", "w") as overwrite:
        json.dump(guild_ledger, overwrite)


if __name__ == '__main__':
    main()
