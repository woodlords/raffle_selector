# Raffle Selector

## Overview
This code select raffle winners randomly based on entries related to the users asset count.


## Example
For example if we have the following list of discord users and their assets. WoodLords bot can generate this list. And we want to use the script to generate the list of winners (Whitelist Spots).

| UserName | DropName | AssetCount
|----------| ---------| ----------
| WoodLord | Early Bird | 4
| Cyboard | Early Bird | 5
| Freyja | Early Bird | 0
| Max | Early Bird | 1
| DM | Early Bird | 10


The winners will be selected based on the number of tokens they own, meaning DM will have 10 entires in the raffle, Freyja will have none. This will ensure that only asset owners are accounted for and the higher the count the better the chance of winning.


In this case and based on the number of total assets we have **20** total assets, meaning 20 entries.

If we are going to give away 10 whitelist spots we can do the following

* make sure the list of users is correct.
* change the `spots_available = 10` to the desired number.
* change the drop name to match the users drop `drop_name = 'early_bird'`
* run the script `python raffle.py`

The output should be like this

```
❯ python3 raffle.py
we are getting entries for drop early_bird
number of raffle entries 19 is higher than spots available  10
we are selecting random entries, multiple winning entries allowed
['DM', 'DM', 'DM', 'DM', 'DM', 'DM', 'DM', 'DM', 'WoodLords', 'Cyboard']
```
as you can see `DM` had multiple entires and higher chances of winning.


## No Multi Wins?
If you don't want to have the same user win more than once you can enable that function.

In this case comment out line 73 and uncomment line 74
```
    results = get_winners_no_multiples(users, drop_name, spots_available)
    #results = get_winners_multiples(users, drop_name, spots_available)

```

```
python3 raffle.py
we are getting entries for drop early_bird
number of raffle entries 19 is higher than spots available  10
['WoodLords', 'Max', 'Cyboard', 'DM']
```