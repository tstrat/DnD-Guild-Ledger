'''
Test file for guild_gold_tracker.py
'''
from guild_gold_tracker import *
import pytest

def create_guild_ledger_for_tests(new_ledger):
    set_guild_ledger(new_ledger)
    return get_guild_ledger()

def get_funds_1():
    return { "total_funds": 1, "09/01/1991":[ {"amount": 1, "reason": "birthday"}] }

def test_guild_fund_access():
    guild_ledger = create_guild_ledger_for_tests(get_funds_1())
    assert get_total_funds() == 1
    assert guild_ledger["09/01/1991"] is not None
    assert guild_ledger["09/01/1991"][0]["amount"] == 1
'''
def test_new_date_transactions():
    create_guild_ledger_for_tests(get_funds_1())
    assert get_guild_funds() == 1
    new_transaction(42, "new stuff", "00/00/0000")
    assert get_guild_funds() == 43
    assert guild_ledger["00/00/0000"][0] == {"amount":42, "reason":"new stuff"}
'''