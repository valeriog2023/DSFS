from collections import defaultdict
import pprint

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

assert average_salary_by_tenure == {
    0.7: 48000.0,
    1.9: 48000.0,
    2.5: 60000.0,
    4.2: 63000.0,
    6: 76000.0,
    6.5: 69000.0,
    7.5: 76000.0,
    8.1: 88000.0,
    8.7: 83000.0,
    10: 83000.0
}

# all tenures are differnt so we want to group them in buckets
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
    
salary_by_tenure_bucket=defaultdict(list)
for salary,tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_tenure_bucket = { tenure: sum(salaries)/len(salaries) for tenure,salaries in salary_by_tenure_bucket.items() }

pprint.pprint("------- salary_by_tenure")
pprint.pprint(salary_by_tenure)
pprint.pprint("------- average_salary_by_tenure")
pprint.pprint(average_salary_by_tenure)
pprint.pprint("------- salary_by_tenure_bucket")
pprint.pprint(salary_by_tenure_bucket)
pprint.pprint("------- average_salary_by_tenure_bucket")
pprint.pprint(average_salary_by_tenure_bucket)