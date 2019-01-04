# GitHub Year in Review Stats Generator

A script to generate statistics about your contributions on GitHub in the year 2018.

## Requirements

* Python 3
* [pipenv](https://github.com/pypa/pipenv)

## Setup

1. Go to https://github.com/settings/tokens/new and generate a new token, and copy it. Ensure it has the following permissions:
    * read:discussion
    * read:org
    * read:user
    * repo
    * user:email
2. Clone the repo, and put the token in `token.txt` in the root of the repo
3. Install dependencies
    ```bash
    $ pipenv install
    ```
4. Run the script. It can take some time, depending on how many repos you have access to.
    ```bash
    $ pipenv run python github_stats.py
    ```

## Demo

My results for 2018:

```
$ pipenv run python github_stats.py

Fetching data from 01/04/18 to 01/04/19

Total Issues Created: 64
Total Issues Assigned To: 429
Total Repos Touched: 37
Total Commits Created: 1020
Total Lines Added: 837487
Total Lines Removed: 101839
```

## Acknowledgements

Thanks to [PyGithub](https://pygithub.readthedocs.io/) for the API, and to last year's fancier (but alas no longer functional) [Year In Review](http://year-in-review.herokuapp.com/) project for the idea.
