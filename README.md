# markov-gen
![Markov Chain Text Generator](https://github.com/itsron717/markov-gen/blob/master/static/Screenshot%202019-12-15%20at%2011.28.26%20AM.png)

> Demo can be found [here](https://markov-gen.herokuapp.com/).

# About
Markov Chains allow the prediction of a future state based on the characteristics of a present state. Suitable for text, the principle of Markov chain can be turned into a sentences generator. 

The project contains two types of Markov Models:
- **N-gram**<br>
An n-gram is simply a sequence of units drawn from a longer sequence.
- **Word Markov Model**<br>
Uses each word as a sequence of units drawn from the text corpus.

_Note_ - The generator is in its early stages so it generates improper sentences without caring for the sentence structure. Modifications will be made in the next update.

# Installation
- Clone the repository

  ```
  $ git clone https://github.com/itsron717/markov-gen.git
  ```
  
- Move into the repository

  ```
  $ cd markov-gen
  ```

- Install the required packages

  ```
  $ pip install requirements.txt
  ```

- Run the server 

  ```
  $ python app.py
  ```

Feel free to contribute! Let me know if there are any issues with the installation or running of the prject using the GitHub issues. All suggestion are welcome.

## License

The MIT License (MIT)

Copyright (c) 2019 [Rounak Vyas](https://www.linkedin.com/in/itsron143/)
