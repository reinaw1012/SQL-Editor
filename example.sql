CREATE TABLE Parents AS

  SELECT "abraham" AS parent, "barack" AS child UNION

  SELECT "abraham"          , "clinton"         UNION

  SELECT "delano"           , "herbert"         UNION

  SELECT "fillmore"         , "abraham"         UNION

  SELECT "fillmore"         , "delano"          UNION

  SELECT "fillmore"         , "grover"          UNION

  SELECT "eisenhower"       , "fillmore";



CREATE TABLE children AS

  SELECT "abraham" AS parent, "barack" AS child UNION

  SELECT "abraham"          , "clinton"         UNION

  SELECT "delano"           , "herbert"         UNION

  SELECT "fillmore"         , "abraham"         UNION

  SELECT "fillmore"         , "delano"          UNION

  SELECT "fillmore"         , "grover"          UNION

  SELECT "eisenhower"       , "fillmore";

  

  CREATE TABLE people AS

  SELECT "abraham" AS parent, "barack" AS child UNION

  SELECT "abraham"          , "clinton"         UNION

  SELECT "delano"           , "herbert"         UNION

  SELECT "fillmore"         , "abraham"         UNION

  SELECT "fillmore"         , "delano"          UNION

  SELECT "fillmore"         , "grover"          UNION

  SELECT "eisenhower"       , "fillmore";



SELECT * FROM children;

SELECT * FROM people;

SELECT * from parents;