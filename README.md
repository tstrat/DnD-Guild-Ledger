## Ledger Project
##### A Tool for gold/item tracking of party funds and items in the world of Dungeons and Dragons

Program:  To keep logs of gold spending for our DnD campaign

Basic goals:
* Read from file, get total current gold
* Add to/sub from it with specific data
  * Write in to file tracking for history
* Use prompts to access it
* Gain values like "How much is party funds how much personal"

Stretch goal:
* modify entries
* add compendium of items and values to view and purchase
  * includes viewing for personal gold expenses
* when rewards are added, display breakdown of loss, guild, and personal amounts

Important notes:

    keywords in json:
        "total_funds" - the total of all the guild funds
        "dd/mm/yy" - format for date of entry
            "amount" - amount spent/gained
            "reason"  - reason for expense/income

For my own use:  
  py.test  -- runs python test scripts that begin with "test_.py"  
  coverage -- usage:  
    coverage run -m py.test test_file_to_run.py  
    coverage html      # generates html files  

