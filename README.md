# WOM (끝말잇기 ai)
This repo is 끝말잇기 ai.

## Requirements
- Python

## Introduction
This repo contain fully working code. you can train this ai with custom dataset. and code for evaluate it. and also you can use this ai inference.

### How does it work?
If you train this model, This model will continue to iterate over and over again these steps. 
1. Will play game by its ownself until the end.
2. When the game is over. evaluating words used in this game. and save its result.

### How to inference.
A trained model has a couple of data that winning rate, frequency,...etc representative that word. inference step is a combine this data and make choice according to its score.

## How to use
1. Prepare dataset. (this repo contain sample dataset. you can pass this step)

Make your dataset. and add them **data/words.txt**.
training data must fallow these template.
```
가돌리늄
가듁
가래톳
가렌
가렛좃
```

2. Training WOM model
```
python index.py
```
Variable **episodes** is the number of times to repeat. You can adjust this.
If train finished, trained_model.pickle file will be created.

3. inference
```

```
