import json
import csv
from csv import DictReader

b_list = []

with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        b_list.append(row)

for book_current in range(len(b_list)):
    del b_list[book_current]['Publisher']

current_l_user = ['name', 'gender', 'address', 'age']
user_l = []
final_l_user = []

with open('users.json', 'r') as file:
    users = json.load(file)
    for row in users:
        user_l.append(row)

for i in range(len(user_l)):
    new_l = {k: v for k, v in user_l[i].items() if k in current_l_user}
    final_l_user.append(new_l)

final_l_user = [
    {'name': object['name'], 'gender': object['gender'], 'address': object['address'], 'age': object['age']}
    for object in final_l_user]

start = 0
difference = len(b_list) // len(final_l_user)
if len(b_list) % len(final_l_user) != 0:
    difference = difference + 1

for i in range(len(final_l_user)):
    final_l_user[i]['books'] = []
    for k in b_list[start: start + difference]:
        final_l_user[i]['books'].append(k)
    start = start + 1

with open('result.json', 'w') as f:
    f.write(json.dumps(final_l_user, indent=4))
