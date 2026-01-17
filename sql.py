'''
# https://www.youtube.com/watch?v=1RCMYG8RUSE&t=4665s
import csv 
with open("favorites.csv", "r") as file:
    #1 reader = csv.reader(file)
    reader = csv.DictReader(file)
    scratch = 0
    c = 0
    python = 0

    scratch, c, python = 0, 0, 0 #1


    #1
    for row in reader:
        #1 print(row[1])
        #1 favorite = row[1]
        favorite = row["language"] # for Dict
        print(favorite) #1
        print(row["language"]) #2
    #2
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c +=1
        elif favorite == "Python":
            python +=1

print(f"Scratch:{scratch}")
print(f"C:{c}")
print(f"Python:{python}")

#counters clever sample
with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite =  row["language"]
        if favorite in counts:
            counts[favorite]  += 1
        else:
            counts[favorite] = 1

for favorite in sorted(counts, key=counts.get, reverse=True): 
    print(f"{favorite}: {counts[favorite]}")

##
import csv
from collections import Counter

with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = Counter()
    for row in reader:
        favorite = row["problem"] #may "language change to "problem"
        counts[favorite] += 1

#1
for favorite in sorted(counts, key=counts.get, reverse=True): 
    print(f"{favorite}: {counts[favorite]}")

#2
for favorite, count in counts.most_common():
     print(f"{favorite}: {count}")

'''
'''
##!!!! input and count 
import csv
from collections import Counter

with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["problem"] #may "language change to "problem"
        counts[favorite] += 1

favorite = input("Favorite: ")
print(f"{favorite}: {counts[favorite]}")
'''

#sqlite3 //terminal command HEADER

#sqlite3 favorites.db //create a new DB
#.mode csv 
#.import favorites.csv favorites
#.schema //table format
#SELECT * FROM favorites;
#SELECT language FROM favorites;
#SELECT language FROM favorites LIMIT 10; //only 10 values
#SELECT COUNT(*) FROM favorites; // count number of rows
#SELECT DISTINCT(language) FROM favorites; //return unique values from colomn
#SELECT COUNT(DISTINCT(language)) FROM favorites; //return number of unique values from colomn
#SELECT COUNT(*) FROM favorites WHERE language = 'C';
#SELECT COUNT(*) FROM favorites WHERE language = 'C'AND problem = 'C';
#SELECT language, COUNT(*) FROM favorites GROUP BY language;
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) ASC; //from smollest to biggest
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC; // from biggest to smollest
#SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC; //time 51:50
#blueprint# INSERT INTO table (colomn, ...) VALUES (value, ...);
#INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');
#DELETE FROM favorites WHERE Timestamp IS NULL;
#blueprint#  UPDATE table SET colomn = value WHERE condition;
#DELETE FROM favorites; // delete all data
#UPDATE favorites SET problem = 'TEST' WHERE language = 'C';


#sqlite3 shows.db
#SELECT * FROM shows;
#CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, year NUMERIC, episodes INTEGER, PRIMARY KEY(Id));
#INSERT INTO shows (id, title, year, episodes) VALUES ('62614','Zeg ns Aaa ', '1981', '227');

#BLOB //Binary large object
# INTEGER
#NUMERIC
#REAL
#TEXT
#NOT NULL UNIQUE
#PRIMARY KEY is ID
#FOREIGN KEY

#SELECT * FROM ratings WHERE rating >= 6.0 LIMIT 10; 
#SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10; // select show id
#SELECT * FROM shows WHERE id = 62614; //select need row
#SELECT * FROM shows shows WHERE id IN(SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10); // at fist select show_id from ratings table, after select show rows from shows table with selected before shows_id
#SELECT * FROM shows JOIN ratings ON shows.id = ratings.show_id WHERE rating >= 6.0 LIMIT 10); //join two tables into temporary wide table
#SELECT title, rating FROM shows JOIN ratings ON shows.id = ratings.show_id WHERE rating >= 6.0 LIMIT 10); // new table title:rating
## one to many
#SELECT * FROM genres LIMIT 10;
#SELECT * FROM shows WHERE id = 63881;
#SELECT show_id FROM genres WHERE ganre = 'Comedy' Limit 10;
#SELECT title, rating FROM shows WHERE id IN (SELECT show_id FROM genres WHERE ganre = 'Comedy' Limit 10);
#SELECT genre FROM genres WHERE show_id = 63881;
#SELECT genre FROM geres WHERE show_id = (SELECT id FROM shows WHERE title = 'Catweasle');
#SELECT * FROM shows JOIN genres ON shows.id = genres.show_id WHERE id = 63881;
#SELECT * FROM shows WHERE title = 'The Office';
#SELECT * FROM shows WHERE title = 'The Office' AND year = '2005';
#SELECT person_id FROM stars WHERE show_id = (SELECT id FROM shows WHERE title = 'The office' AND year = '2005');
#SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE show_id = (SELECT id FROM shows WHERE title = 'The Office' AND year = "2005"));
#SELECT title FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carrel'));
#SELECT title FROM shows
#   JOIN stars ON shows.id = stars.show_id
#   JOIN people ON stars.person_id = people.id;
#   WHERE name = 'Steve Carell';

#SELECT title FROM shows,stars, people
#   WHERE shows.id = stars.show_id
#   AND people.id = stars person_id
#   AND name = 'Steve Carell';

#CREATE TABLE stars (
#   show_id INTEGER NOT NULL
#   person_id INTEGER NOT NULL     
#   FOREIGN KEY(show_id) REFERENCES shows(id)
#   FOREIGN KEY(person_id) REFERENCES people(id)
# );

#CREATE INDEX title_index ON shows (title);

#CREATE INDEX person_index ON stars (person_id);
#CREATE INDEX show_index ON stars (show_id);
#CREATE INDEX name_index ON people (name);

#Time 1:50
'''
from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")
row = db.execute("SELECT COUNT(*) AS n FROM faforites WHERE problem = ?", favorite)
row = [0]

print(row["n"])
'''

#BEGIN TRANSACTION
#COMMIT
#ROLLBACK

#SQL injection attack



