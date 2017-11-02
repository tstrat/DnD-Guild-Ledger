'''
Test file for guild_gold_tracker.py
'''
import guild_gold_tracker as ggt
import pytest

def create_guild_ledger_for_tests(funds):
    ggt.guild_ledger = funds

def get_funds_1():
    return { "total_funds": 1, "09/01/1991":[ {"amount": 1, "reason": "birthday"}] }

def test_guild_fund_access():
    create_guild_ledger_for_tests(get_funds_1())
    assert ggt.get_guild_funds() == 1
    assert ggt.guild_ledger["09/01/1991"] is not None
    assert ggt.guild_ledger["09/01/1991"][0]["amount"] == 1

def test_new_date_transactions():
    create_guild_ledger_for_tests(get_funds_1())
    assert ggt.get_guild_funds() == 1
    ggt.new_transaction(42, "new stuff", "00/00/0000")
    assert ggt.get_guild_funds() == 43
    assert ggt.guild_ledger["00/00/0000"][0] == {"amount":42, "reason":"new stuff"}