Hangman Game

This is a Hangman game created using object-oriented Python programming language (classes).

This game runs and can be interacted in a console.

By studying this code, you can learn how to apply classes and objects in your code, use "random" module to randomize values, and get a bit familiar of list comprehension.

This hangman game has 3 categories of words: fruit, vegetable, and animal. However, you can easily add more categories by following the examples in assign_words_for_category() function.

You can also configure how each difficulties as you want. The current list of difficulties includes easy, normal, and hard.

To create a class instance, you can start by taking a look at line 100th.  
In this case, it is my_hangman = Hangman("fruit", "hard")
    instance_name = class_name(argument(s))
The "my_hangman" is an instance, Hangman is a class, and "fruit" and "hard" are arguments.
The next 2 lines are function callings.
To start the game, we have to call these two functions namely welcome_message() to print out a welcome message, and start_the_game() to start the game.

Normally, when we want to call a function, we only need to type function_name(). However, in this case, the functions are in the class, so we have to "instance_name.function_name()" to call a function in a class.

Finally, you can learn more by looking at this code.

Also don't forget to "import random".


This is my second contribution in my entire life so far. If you don't mind, I want to showcase this in my portfolio.
