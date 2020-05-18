# advantage-of-disadvantage
This repository is a response to the fivethrityeight.com aricle entitled [Can You Find The Best Dungeons &amp; Dragons Strategy?](https://fivethirtyeight.com/features/can-you-find-the-best-dungeons-dragons-strategy/)

## The Challenge
On May 15, 2020. FiveThrityEight.com published an aricle entitled, 'Can You Find The Best Dungeons & Dragons Strategy?'. In it they postulate that rolling one die when you have advantage and disadvantage is yawn inducing, 'Yawn!'

They propose (while certainly worse for gameplay) two 'more mathematically interesting ways' to combine advantage and disadvantage.

### “advantage of disadvantage”
roll twice with disadvantage and then keep the higher result

### "disadvantage of advantage”
roll twice with advantage and then keep the lower result

## The Question they pose
Which situation produces the highest expected roll: advantage of disadvantage, disadvantage of advantage or rolling a single die?

## Answer
**Take disadvantage of advantage**

result from run 1: 10,000,000 rolls
> `regular expected roll                   10.499731925`

> `advantage of disadvantage expected roll 9.8337565`

> `disadvantage of advantage expected roll 11.1661691`

result from a run2: 10,000,000 rolls

> `regular expected roll                   10.500074675`

> `advantage of disadvantage expected roll 9.8345212`

> `disadvantage of advantage expected roll 11.1660673`

### Moral of the story
Adding this to your game causes more computation and arguing. If that is your thing, great! However I wouldn't reccomend this to your game. Instead I would get some old Dnd v 3.5 books from the discount bin and play that instead. Way way way more computation and arguing than you could ever hope for in 5e.

#### Also for extended thoughts on this topic ...
We have a podcast called Min Max Fun where we talk about making your games fun.
* Please check out our podcast episode on the topic: [#8 3.5 versus 5th edition](https://minmaxfun.buzzsprout.com/349301/1403029-8-3-5-versus-5th-edition)
* You can browse the full catalog here: [minmaxfun.com](https://minmaxfun.buzzsprout.com/)

##### Please please please please PR me if you see an improvement!
* I left a couple notes in the code where I would love a PR.


## Extra Credit!
> Instead of maximizing your expected roll, suppose you need to roll N or better with your 20-sided die. For each value of N, is it better to use advantage of disadvantage, disadvantage of advantage or rolling a single die?

### The attack plan
What we want to really know is the cumulative probability distribution function (CDF) for each of these options. That will tell us what probability of the rolls are above a certain value. For example if we take the roll of 11 and consult the CDF whichever function is the lowest has 'used up the least amount of gas', in other words has the most probability of giving a result above that number. We will actually present the reverse CDF because then we are looking for the distribution with the highest value (something humans prefer).

### The plots
![](https://github.com/alonzi/advantage-of-disadvantage/blob/master/extraCredit.png)

### The solution
For every value of N just look it up on the histogram. For example for N=1 it doesn't matter, they will all do it. For N=20 just roll that single d20. For everything in the middle you have to look to see which curve is higher.
