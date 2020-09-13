#SQL

#Task1
  SELECT * 
  FROM city 
  WHERE ID = 1661;

#Task2
SELECT * 
FROM city
WHERE countrycode = "USA" AND population > 100000;

#Task3
SELECT *
FROM city
WHERE countrycode = 'JPN';

#Task4
SELECT name
FROM city
WHERE countrycode = 'JPN';

#Task5
SELECT city
FROM station
UNION 
SELECT state 
FROM station;

#Task6
SELECT DISTINCT city
FROM station
WHERE ID%2 = 0;

SELECT (count(city) -  DISTINCT count(city))
FROM station;

#Task7
SELECT CITY,LENGTH(CITY)
FROM STATION
WHERE LENGTH(CITY) IN (
  SELECT MAX(LENGTH(CITY))
  FROM STATION
  UNION
  SELECT MIN(LENGTH(CITY))
  FROM STATION
)
ORDER BY LENGTH(CITY) DESC,CITY ASC LIMIT 2;

#Task8
SELECT DISTINCT CITY FROM STATION 
WHERE CITY LIKE 'A%' 
OR CITY LIKE 'E%' 
OR CITY LIKE 'I%' 
OR CITY LIKE 'O%' 
OR CITY LIKE 'U%';

#Task9
SELECT DISTINCT CITY FROM STATION 
WHERE CITY LIKE '%A' 
OR CITY LIKE '%E' 
OR CITY LIKE '%I' 
OR CITY LIKE '%O' 
OR CITY LIKE '%U';

#Task10
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY LIKE '[AEIOU]%'
OR CITY LIKE '%[AEIOU]';

# Python
#Task1
if __name__ == '__main__':
    n = int(input())
    if n%2 != 0:
      print("Weird")
    elif n%2 == 0 and n>=2 and n <=5:
      print("Not Weird")
    elif n%2 == 0 and n>=6 and n <=20:
      print("Weird")
    elif n%2 == 0 and n > 20:
      print("Not Weird")

#Task2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("sum of 2 numbers: %s " %(a+b))
    print("diference of 2 numbers:",a-b)
    print("product of 2 numbers:",a*b)

#Task3
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
      print(i**2)

#Task4
def is_leap(year):
  if(year%4 == 0):
    if(year%100 == 0):
      return (year%400 == 0)
    return True
  return False

if __name__ == '__main__':
  y = int(input())
  while(y<1900 or y>10**5):
    y = int(input("enter again: "))
  print(is_leap(y))

#Task5
if __name__ == '__main__':
  n = int(input("number of participants: "))
  l = []
  for i in range(n):
    x = int(input())
    l.append(x)
  sort = sorted(l)
  print("runner up score: %s" %(sort[-2]))