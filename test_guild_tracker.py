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

def get_funds_2():
    return { "total_funds": 1, "09/01/1991":[ {"amount": 1, "reason": "birthday"}, {"amount": 2, "reason": "presents"}] }

def test_guild_fund_access():
    guild_ledger = create_guild_ledger_for_tests(get_funds_1())
    assert get_total_funds() == 1
    assert guild_ledger["09/01/1991"] is not None
    assert guild_ledger["09/01/1991"][0]["amount"] == 1

def test_new_date_transactions():
    guild_ledger = create_guild_ledger_for_tests(get_funds_1())
    assert get_total_funds() == 1
    assert len(guild_ledger) == 2

    new_entry(42, "new stuff", "00/00/0000")

    # Added new entry, total funds increase, new entry is accounted for
    assert get_total_funds() == 43
    assert len(guild_ledger) == 3
    assert guild_ledger["00/00/0000"][0] == {"amount":42, "reason":"new stuff"}

def test_same_date_transactions():
    guild_ledger = create_guild_ledger_for_tests(get_funds_1())
    new_date = "00/00/0000"
    new_entry(42, "new stuff 1", new_date)
    new_entry(-37, "new stuff 2", new_date)

    assert get_total_funds() == 6  # 1 + 43 - 37

    assert len(guild_ledger) == 3
    assert len(guild_ledger[new_date]) == 2

def test_remove_entry():
    guild_ledger = create_guild_ledger_for_tests(get_funds_2())
    date = "09/01/1991"
    assert guild_ledger[date] is not None
    assert len(guild_ledger[date]) == 2

    value = remove_entry(date, 0)

    assert value
    assert len(guild_ledger[date]) == 1
    assert get_total_funds() == 1  # shoudln't change without refund parameter
    
def test_remove_all_entries():
    guild_ledger = create_guild_ledger_for_tests(get_funds_2())
    date = "09/01/1991"
    assert guild_ledger[date] is not None
    assert len(guild_ledger[date]) == 2

    value = remove_entry(date, 0)
    value = remove_entry(date, 0)

    assert value
    assert date not in guild_ledger
    assert get_total_funds() == 1  # shoudln't change without refund parameter

    value = remove_entry(date, 0)
    assert not value  # no more date to remove

def test_remove_with_refund():
    guild_ledger = create_guild_ledger_for_tests(get_funds_2())
    date = "09/01/1991"
    assert guild_ledger[date] is not None
    assert get_total_funds() == 1

    value = remove_entry(date, 0, True)

    assert value
    assert get_total_funds() == 0 # was 1 but entry amount was 1 so refund removes from total


    value = remove_entry(date, 0, True)

    assert value
    assert get_total_funds() == -2 # was 0 but entry amount was 2 so refund removes from total

def test_remove_all_with_just_date():
    guild_ledger = create_guild_ledger_for_tests(get_funds_2())
    date = "09/01/1991"
    value = remove_all_entries("no_date")
    assert not value
    value = remove_all_entries(date)
    assert value
    assert not date_exists(date)
    value = remove_entry(date,0)
    assert not value


