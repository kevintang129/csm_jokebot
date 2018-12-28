# CSM Tech Committee Take-home - Jokebot

The little exercise below is something that you should be able to complete in 2-3 hours. (If you're familiar with all the libraries and attempt it in one sitting you might even finish it faster - within an hour or so.) It’s designed in parts with some guidance. Unlike class projects in 61A or 61B that you may have seen, there are less specific instructions. We’re interested in seeing how you can interpret design instructions, translate it into code, and find the right information when you need to. We also hope that you might learn a thing or two when doing this exercise.

We highly recommend that you use Python 3 for this exercise. All the libraries mentioned are Python 3 libraries. If you would prefer to use another language, please let us know in advance.

## Jokebot

We will be building a Jokebot program that tells us jokes. Specifically, we’re delivering jokes which have a prompt and a punchline.

> Why don't they play poker in the jungle? (prompt)
###
> There’s too many cheetahs! (punchline)  

The end result should be a Python program that we can run that keeps telling us these jokes until we tell it to quit, or it runs out of jokes.

## Part 1: Delivery

In this section we build the program that tells jokes. It should follow this procedure:

1. Deliver prompt
2. Wait 2s
3. Deliver punchline
4. Wait for user input
    - if “next”, goto 1.
    - if “quit”, exit program
    - else, print error message and wait for new input
5. Exit when no more jokes to tell

### Guidelines

1. Write a function that delivers jokes. It should take prompt and punchline parameters, then print the prompt, wait 2s and then print the punchline
> Hint: Look into the `time` library and `time.sleep`
2. Write a function that reads user input. It should return True if input is “next”, and return False if input is “quit”. If the input is neither of these, it should print an appropriate error message, e.g. “I don’t understand”, and then wait for user input again.
> Hint: Look into the `input` function. (Be careful! We're using Python 3. `input` has *very* different behaviour in Python 2)
3. Write a function that reads jokes from a comma-separated value (CSV) file. The CSV file has rows in the form: `prompt,punchline`. Then, return a list of these jokes. For your convenience, we've provided a sample `jokes.csv` file.
> Hint: Look into the `csv` library.
4. String the functions together into the Jokebot as described in the procedure. It should run with exactly one command line argument (the CSV file to read), e.g. `python jokebot.py jokes.csv`. If no CSV filename is given, it should quit with an appropriate message, e.g. “No joke file given”  
> Hint: Look into the `sys` standard library to extract command line arguments
###
> Hint: Python scripts have a specific check to execute only when run directly. See https://stackoverflow.com/questions/419163/what-does-if-name-main-do

## Part 2: Material

We’ve built version 1 of our Jokebot. However, most people don’t have jokes just lying around on their computer. To remedy that, we’re going to try and download jokes from Reddit’s /r/dadjokes when no jokes CSV is provided. (When one is provided, we’ll just use the CSV as a joke source.) We will use the post title as prompts, and the post bodies as punchlines. (Most jokes on /r/dadjokes are written like this)

### Guidelines
1. Write a function that gets a list of Reddit posts from /r/dadjokes. It should automatically download the JSON from here: `https://www.reddit.com/r/dadjokes.json` You do not need to handle pagination.
> Hint: Visit old.reddit.com/r/dadjokes and compare what you see to the JSON dump for help on how to proceed.
###
> Hint: Look into the `requests` library. You may also find the `json` library helpful.
###
> Hint: You may get HTTP 429 Errors (Too Many Requests). Python’s default User-agent causes this. Look here for a solution: https://www.reddit.com/r/redditdev/comments/3qbll8/429_too_many_requests/
2. Filter the posts. We want suitable jokes so we’ve picked these criteria:
    - Safe for Work only (filter out posts where `over_18` is True)
    - Start with a question (filter out posts whose post titles don't start with "Why", "What" or "How")
3. Extract the post titles and post bodies into a list of jokes that can be used with functions from Part 1. Then update the code you wrote in Part 1. It should now do the following:
    - If the jokebot is called with no arguments, it should use Reddit as a data source
    - If the jokebot is called with a CSV filename, it should use the CSV file as a data source 

## Part 3: Polish

Our Jokebot is now pretty solid. It’s in a good place and it works. Let’s clean it up and submit it.

1. Consider edge cases. Are there any things that we might have missed in our instructions, that could happen, that might break the Jokebot? Address these edge cases (if any).
2. Refactor your code. We don’t need detailed comments, but we’d like to see that you have structured your code appropriately, and have named variables/functions appropriately.
> Note: You don’t need to follow any of the code structure recommendations that we provided earlier. (For example, you may decide that you don’t want two separate functions to read from a CSV and from Reddit, and decide to combine the two. Or, you may decide to add another function that allows choosing between these two sources.) We only need the core functionality (telling jokes from either a CSV or Reddit) to work when we run the program.
3. If you have not been using git, create a repository and commit your jokebot program to it. Push the repository to a public Github repo that we can access, and submit it at https://goo.gl/forms/3z9hTVxwoUuoHCh42

## Finished!
We hope you've enjoyed this little exercise. We will be reaching out later in the break towards the beginning of the semester with next steps.
