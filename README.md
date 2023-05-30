# Django RestAPI BaseLine

> 1. model 생성
> 2. serializer 생성
> 3. views 생성
> 4. urls 생성


```
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  height INT,
  weight INT,
  class_name VARCHAR(10)
);
```

```
INSERT INTO students (id, name, height, weight, class)
VALUES
  (1, 'John', 175, 70, 'A'),
  (2, 'Emma', 165, 60, 'B'),
  (3, 'Michael', 180, 75, 'A'),
  (4, 'Sophia', 160, 55, 'B'),
  (5, 'William', 185, 80, 'C'),
  (6, 'Olivia', 155, 50, 'A'),
  (7, 'James', 170, 65, 'B'),
  (8, 'Ava', 175, 70, 'C'),
  (9, 'Robert', 165, 60, 'A'),
  (10, 'Mia', 180, 75, 'C'),
  (11, 'David', 160, 55, 'B'),
  (12, 'Charlotte', 185, 80, 'A'),
  (13, 'Joseph', 155, 50, 'C'),
  (14, 'Abigail', 170, 65, 'A'),
  (15, 'Matthew', 175, 70, 'B'),
  (16, 'Emily', 165, 60, 'C'),
  (17, 'Daniel', 180, 75, 'B'),
  (18, 'Harper', 160, 55, 'A'),
  (19, 'Jackson', 185, 80, 'C'),
  (20, 'Sofia', 155, 50, 'B'),
  (21, 'Andrew', 170, 65, 'A'),
  (22, 'Avery', 175, 70, 'C'),
  (23, 'Joshua', 165, 60, 'B'),
  (24, 'Ella', 180, 75, 'A'),
  (25, 'Christopher', 160, 55, 'C'),
  (26, 'Amelia', 185, 80, 'A'),
  (27, 'Ryan', 155, 50, 'B'),
  (28, 'Grace', 170, 65, 'C'),
  (29, 'Ethan', 175, 70, 'A'),
  (30, 'Chloe', 165, 60, 'B');
```