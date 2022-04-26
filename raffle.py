# Author: Hyder @ Wood Lords

import random

def generate_user_entries_per_drop_asset_count(users, drop_name):
    """ Get all users entries (weight)"""
    print(f'we are getting entries for drop {drop_name}')
    results = []
    start_range = 0
    for user in users:
        user_data = {}
        if user[drop_name] > 0:
            user_entries = [w for w in range(start_range, start_range+user[drop_name])]
            user_data['userid'] = user['userid']
            user_data['entries'] = user_entries
            results.append(user_data)
            #results[user['userid']] = user_entries
            start_range += user[drop_name]
    return results

#====================

def select_entries_no_multiples(users_raffle_entries_per_drop, spots_available):
    highest_entry_number = users_raffle_entries_per_drop[-1]['entries'][-1]
    if spots_available > highest_entry_number:
        print(f'number of raffle entries {highest_entry_number} is lowers than spots available {spots_available}')
    else:
        print(f'number of raffle entries {highest_entry_number} is higher than spots available  {spots_available}')
    winners = []
    if highest_entry_number > spots_available:
        while len(winners) < spots_available:
            winning_number = random.randint(0, highest_entry_number)
            if winning_number not in winners:
                winners.append(winning_number)
        return winners
    else:
        print('All are winners, less entries than spots available')
        return [winner for winner in range(0, highest_entry_number)]

def winning_users_no_multiples(users_raffle_entries_per_drop, winning_numbers):
    win_users = []
    for winning_number in winning_numbers:
        for user in users_raffle_entries_per_drop:
            if winning_number in user['entries']:
                if user['userid'] not in win_users:
                    win_users.append(user['userid'])
    return win_users


def get_winners_no_multiples(users,drop_name,spots_available):
    results = generate_user_entries_per_drop_asset_count(users, drop_name)
    winning_entries = select_entries_no_multiples(results, spots_available)
    winners = winning_users_no_multiples(results, winning_entries)
    return winners


#====================

def select_random_entries_with_multiples(users_raffle_entries_per_drop, spots_available):
    print('we are selecting random entries, multiple winning entries allowed')
    highest_entry_number = users_raffle_entries_per_drop[-1]['entries'][-1]
    if spots_available > highest_entry_number:
        print(f'number of raffle entries {highest_entry_number} is lowers than spots available {spots_available}')
    else:
        print(f'number of raffle entries {highest_entry_number} is higher than spots available  {spots_available}')
    winners = []
    while len(winners) < spots_available:
        winning_number = random.randint(0,highest_entry_number)
        winners.append(winning_number)
    return winners

def winning_users(users_data, winning_numbers):
    win_users = []
    for winning_number in winning_numbers:
        for user in users_data:
            if winning_number in user['entries']:
                win_users.append(user['userid'])
    return win_users

def get_winners_multiples(users,drop_name,spots_available):
    results = generate_user_entries_per_drop_asset_count(users, drop_name)
    winning_entries = select_random_entries_with_multiples(results, spots_available)
    winners = winning_users(results, winning_entries)
    return winners



def main():
    # data can be changed!
    users  = [
        {'userid': 'WoodLords', 'season_one': 0, 'early_bird': 4},
        {'userid': 'Cyboard', 'season_one': 12, 'early_bird': 5},
        {'userid': 'Freyja', 'season_one': 26, 'early_bird': 0},
        {'userid': 'Max', 'season_one': 0, 'early_bird': 1},
        {'userid': 'DM', 'season_one': 0, 'early_bird': 10}
    ]
    spots_available = 10
    drop_name = 'early_bird'

    results = get_winners_no_multiples(users, drop_name, spots_available)
    #results = get_winners_multiples(users, drop_name, spots_available)
    print(results)

main()