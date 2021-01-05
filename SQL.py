# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:10:22 2020

@author: shima
"""
# SQL stands for Structured Query Language, interacting with data stored in relational databases
# Relational database can be considered as a collection of tables, like a spreadsheet

# Each column, or field, of a table contains a single attribute

# In SQL, you can select data from a table using a SELECT statement

#SELECT title # the column name
#FROM films; # the data file name

# SELECT and FROM are called keywords,  In SQL, keywords are not case-sensitive

# Include a semicolon at the end of your query, This tells SQL where the end of your query is!
# FROM films; 

# To select multiple columns from a table, simply separate the column names with commas
# SELECT name, birthdate
# FROM people;

# To select all columns from a table use * as as shortcut
# SELECT *
# FROM people;

# To return a certain number of results (rows), use the LIMIT
# SELECT *
# FROM people
# LIMIT 10;

# Get the title of every film from the films table
# SELECT title FROM films

# To select all the unique values from a column, use DISTINCT
# SELECT DISTINCT language
# FROM films;

# Count the number of employees
# SELECT COUNT(*)
# FROM people;

# count the number of non-missing values in a particular column
# Count the number of (non-missing) birth dates in the people table

# SELECT COUNT(birthdate)
# FROM people;

# Count the number of unique birth dates in the people table
# SELECT COUNT(DISTINCT birthdate)
# FROM people;

# different comparison operators with python syntax
# = equal
# <> not equal

#  filter the title 'Metropolis':
# SELECT title
# FROM films
# WHERE title = 'Metropolis';  # WHERE clause always comes after the FROM statement!

# Films released after the year 2000: 
# SELECT title
#FROM films
#WHERE release_year > 2000;

# Get all details for all films released in 2016:
# SELECT * FROM films WHERE release_year = 2016

# Get all details for all French language films
# SELECT * FROM films WHERE language='French'

# Get the title and release year for all Spanish language films released before 2000
# SELECT title, release_year FROM films WHERE language='Spanish' AND release_year < 2000

# Get the title and release year for films released in the 90s
# SELECT title, release_year
# FROM films
# WHERE release_year >= 1990 AND release_year < 2000;

# Get the title and release year of all films released in 1990 or 2000 that were longer than two hours. Remember, duration is in minutes!
# SELECT title, release_year FROM films WHERE (release_year=1990 OR release_year=2000) AND 
# duration > 120

# Get the names of people who are still alive, i.e. whose death date is missing
# SELECT name FROM people WHERE deathdate IS NULL

#  query matches companies like 'Data', 'DataC' 'DataCamp', 'DataMind', and so on
# SELECT name
# FROM companies
# WHERE name LIKE 'Data%';

# Get the names of all people whose names begin with 'B'. The pattern you need is 'B%'
# SELECT name FROM people WHERE name LIKE 'B%'

# use the NOT LIKE operator to find records that don't match the pattern you specify
# Aggregate functions

# Use the SUM function to get the total duration of all films
# SELECT SUM(duration) FROM films

# Use the SUM function to get the total amount grossed by all films
# SELECT SUM(gross) FROM films

# Use the SUM function to get the total amount grossed by all films made in the year 2000 or late
# SELECT SUM(gross) FROM films WHERE release_year >= 2000

# Aliasing
# SQL assumes that if you divide an integer by an integer, you want to get an integer back
# The result of SELECT 45 / 10 * 100.0; is 400.0, while this one returns the correct answer 450.0,  45 * 100.0 / 10;

# Now, Get the percentage of people who are no longer alive. Alias the result as percentage_dead. Remember to use 100.0 and not 100
# SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead FROM people

#  In SQL, the ORDER BY keyword is used to sort results, By default ORDER BY will sort in ascending order
#  To sort the results in descending order, you can use the DESC keyword

# Sorting single columns
# Get the names of people from the people table, sorted alphabetically
# SELECT name FROM people ORDER BY name

# Get the title of films released in 2000 or 2012, in the order they were released
# ELECT title FROM films WHERE release_year IN (2000,2012) ORDER BY release_year

# Get the IMDB score and film ID for every film from the reviews table, sorted from highest to lowest score
# SELECT imdb_score, film_id FROM reviews ORDER BY imdb_score DESC

# Get the birth date and name of people in the people table, in order of when they were born and alphabetically by name
# SELECT birthdate, name FROM people ORDER BY birthdate, name

# GROUP BY
# Note also that ORDER BY always goes after GROUP BY

# Get the release year and count of films released in each year
# SELECT release_year, COUNT(*) FROM films GROUP BY (release_year)

# Get the release year and lowest gross earnings per release year
# SELECT release_year, MIN(gross) FROM films GROUP BY (release_year)

# In SQL, aggregate functions can't be used in WHERE clauses
# Get the release year, budget and gross earnings for each film in the films table
# SELECT release_year, budget, gross FROM films

# Get the country, average budget, and average gross take of countries that have made more than 10 films. Order the result by country name, and limit the number of results displayed to 5. You should alias the averages as avg_budget and avg_gross respectively
# -- select country, average budget, average gross
# SELECT country, AVG(budget) as avg_budget, AVG(gross) as avg_gross

# -- from the films table
# FROM films

# -- group by country 
# ROUP BY country

# -- where the country has more than 10 titles
# HAVING COUNT(title) > 10

# -- order by country
# ORDER BY country

# -- limit to only show 5 results
# LIMIT 5

#  to query multiple tables,  to get the ID of the movie from the films table and then use it to get IMDB information from the reviews table
# SELECT title, imdb_score
# FROM films
# JOIN reviews
# ON films.id = reviews.film_id
# WHERE title = 'To Kill a Mockingbird';


