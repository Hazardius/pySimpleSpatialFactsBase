pySimpleSpatialFactsBase
========================
System that can store expert (certain) spacial facts.


The system should allow for easy input of spacial facts.<br />
We can assume that this knowledge is in certain format.


The system should answer simple spacial questions using RCC5.<br />
Questions are formed in natural language.

Requirements:
-------------
* [__psi-toolkit__](http://psi-toolkit.amu.edu.pl/)
* [__NetworkX__](http://networkx.github.ioh/)

---

Input data format.
------------------
  Certain knowledge given to the system must be formatted in a certain way.  
  For each RCC5 fact it must be transformated into a triple:

    (Subject, Relation, Object)

  where Subject and Object are Strings,  
  and Relation is taken from set {"EQ", "DR", "PO", "PP", "PPI"}

  That triple should be then formatted into line of text separated by "@|@" signs,
  f.e  

    Subject@|@EQ@|@Object

Output.
-------
  For now system works for polish questions *"Czy X [rel] Y?"* formed in natural language.  
  Relation finding and parsing is terrible for now. It's in main part just checking if phrase is in set.  
  To improve it in easy way - just edit [relation_phrases.py](../master/relation_phrases.py).

Usage:
------
  1. To feed system with certain facts.  
    You can add facts from hand after running program with command:

        python __init__.py -f

    But of course better way is to write all facts down in a file (for example - check [test_data.txt](../master/test_data.txt)).  
    And use command:

        cat test_data.txt | python __init__.py -f

    **Remember!**  
    Even executing main file another time - you write to the same database.  
    If You want to start a new one - use **--purge** argument as given below:  

        cat test_data.txt | python __init__.py -f --purge

  2. To ask a question.  
    You can ask from hand after running program with command:

        python __init__.py -a

    But of course better way is to write all questions down in a file (for example - check [test_questions.txt](../master/test_questions.txt)).  
    And use command:

        cat test_questions.txt | python __init__.py -a
