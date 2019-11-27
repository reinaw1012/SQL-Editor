CREATE TABLE parents AS

  SELECT "abraham" AS parent, "barack" AS child UNION

  SELECT "abraham"          , "clinton"         UNION

  SELECT "delano"           , "herbert"         UNION

  SELECT "fillmore"         , "abraham"         UNION

  SELECT "fillmore"         , "delano"          UNION

  SELECT "fillmore"         , "grover"          UNION

  SELECT "eisenhower"       , "fillmore";


select * from parents;