# Assortment-Optimization_Prefix Span 

An implementation of Prefix Span Algorithm for assortment optimization problem

## Motivation

There are theories about Prefix Span Algorithm on the internet and Github but no one has acctually implement this by python, besides, most of the examples of this algorithm use small sample with signle letter to represent products, which is not what the data looks like in reality, so I write this code to deal with situation that contains either single letter or strings.

## Data
For the transaction data, only need to keep the record of user name, upc and transction time

## Result 
By using this algorithm, we can get the frequent pattern cross transactions for each consumer,you can set the support according your requriments.

The result is like this 
``` 
pattern:[['c7f48de7f35e1902c1f03d1cdda26d8a']], support:405
pattern:[['c7f48de7f35e1902c1f03d1cdda26d8a', '985ece5369e28d3e825db88479340d83']], support:130 
```
