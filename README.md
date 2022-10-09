# OpenTriviaQA

A creative commons dataset of trivia, multiple choice questions and answers.

url: [https://github.com/uberspot/OpenTriviaQA](https://github.com/uberspot/OpenTriviaQA)

I searched around some years ago and couldn't find any publicly available dataset of trivia questions so some were 
gathered and split a bit crudely in categories for public usage.

The general format of the files is:

    #Q A question until the newline
    ^ The text of the correct answer
    A multiple choice answer 1
    B multiple choice answer 2
    C multiple choice answer 3
    D ....
    E ...
    .....

A better format could be used in retrospect but a) this one is easy for humans to edit and change questions b) it can be
parsed fairly easy to json or something different later on.

## Contributing

Just fork the project on github, add your changes and send a pull request

Possible contributions can be adding more questions/answers, doing finer categorization, writing a quick parser to
change the files to a better format that is also human friendly.

## Changes to text2csv.py

To make the csv files generated more useful for our purposes, we made some changes to the text2csv.py file.

We put the final output into one csv that can be read by pandas and added a category column to keep track of which category each one question came from.

## Making Data Avaliable

We copied the trivia.csv file to a public GitHub repository called opendata and pushed a commit. Now that the csv file is on Github, we can use the raw data link

## License

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of
this license, visit [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/) .
