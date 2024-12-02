# Bridge Trainer

## Problem Description

The program for calculating the point value of a hand in bridge. A hand in bridge consists of 13 cards, and the points for each card are:

- Jack (J) = 1 point
- Queen (Q) = 2 points
- King (K) = 3 points
- Ace (A) = 4 points
- Other cards are worth 0 points.

A hand is illegal if:

- It contains more than 13 cards
- Any card appears more than 4 times
- It contains invalid cards

### Input

- An integer `n` (1 ≤ n ≤ 52) representing the number of cards.
- `n` strings, each representing a card.

### Output

- **The score** of the hand if it's legal.
- **OSZUST!** (Fraud in Polish) if the hand is illegal.

### Examples

**Input**:  
`13`  
`2`  
`3`  
`4`  
`5`  
`6`  
`7`  
`8`  
`9`  
`10`  
`J`  
`Q`  
`K`  
`K`

**Output**:  
`9`

**Input**:  
`13`  
`2`  
`3`  
`4`  
`5`  
`6`  
`7`  
`DOGE`  
`9`  
`10`  
`J`  
`Q`  
`K`  
`A`

**Output**:  
`OSZUST!`
