# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are a group of objects. Lists are mutable (meaning they can be changed) and Tuples are immutable. Lists are denoted by square brackets and tuples by parentheses. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python list and sets are both groups of objects. Lists are unstructured and can have repeating values. Sets are structured objects that can not have repeating values. 
example of a list:  [1, 5, 8, 8, 2, 5]
example of a set: [1, 2, 5, 8]

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python lambda function makes writting code a bit easier and, when used, a bit cleaner by allowing the creation of a function that is to be used once without the need to creat a function. 
NHLmetro=['Capitals','Rangers','Penguins','Islanders','Flyers','Panthers','Devils','BlueJackets']
sorted(NHLmetro, key=lambda x:len(x))

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to create a list of numbers with one line of code, rather than typing a list out or using a loop. 
The following examples will print '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
List: 
  Top10=[i for i in range(1,11)] 
Map:
  map_Top10= map(lambda i: i, range(1,10))
Filter:
  filter_Top10 = filter(lambda s: s, Top10)
Set Comprehension:
  set_Top10 = [q for q in range(1,11)]
Dictionary Comprehension:
  dic_Top10 = {x: x**2 for x in Top10} '''returns dicitonary of the square of each element within Top10


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 daysd

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





