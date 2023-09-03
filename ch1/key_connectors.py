import pprint
from collections import Counter, defaultdict

users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendships_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships =  { user['id']: [] for user in users } 

for i,j in friendships_pairs:
    if j not in friendships[i]: friendships[i].append(j)
    if i not in friendships[j]: friendships[j].append(i)    

print("------ friendships ")
pprint.pprint(friendships)


def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

num_friends_by_id =  [ (user['id'], number_of_friends(user)) for user in users ]
print("------ num_friends_by_id ")
pprint.pprint(num_friends_by_id)
num_friends_by_id.sort(key=lambda x: x[1],reverse=True)
pprint.pprint(num_friends_by_id)
assert num_friends_by_id[0][1] == 3     # several people have 3 friends
assert num_friends_by_id[-1] == (9, 1)  # user 9 has only 1 friend


total_connections = sum(number_of_friends(user) for user in users)        # 24
assert total_connections == 24


num_users = len(users)                            # length of the users list
avg_connections = total_connections / num_users   # 24 / 10 == 2.4
assert num_users == 10
assert avg_connections == 2.4


def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    user_id = user['id']
    return Counter([foaf_id
            for friend_id in friendships[user_id]
            for foaf_id in friendships[friend_id]
            if foaf_id != user_id and              #remove the user id
               foaf_id not in friendships[user_id] #remove the direct friends
            ])
print("------ fireds of a firend for user 3 ")
pprint.pprint(foaf_ids_bad(users[3]))


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    results = [ user_id for (user_id, user_interest) in interests if user_interest == target_interest ]
    return results

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interests for that user_id.
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )
            

#most common word in interests
most_common_words_in_interests = Counter( word for (_,interest) in interests for word in interest.lower().split() )
print("---------------")
pprint.pprint(most_common_words_in_interests)

            
