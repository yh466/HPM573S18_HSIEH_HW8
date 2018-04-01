# HW 8 Problem 1

import Parameters as P
import CasinoModelClasses as Cls
import SupportSteadyState as Support

print('Problem 1')

# create a set of games for when the coin is fair
setOfGamesFairCoin = Cls.SetOfGames(id=1, prob_head=P.HEAD_PROB_FAIR, n_games=P.SIM_SET_SIZE)
# simulate the set of games
fairCoinOutcome = setOfGamesFairCoin.simulation()


# create a set of games for when the coin is unfair
setOfGamesUnfairCoin = Cls.SetOfGames(id=2, prob_head=P.HEAD_PROB_UNFAIR, n_games=P.SIM_SET_SIZE)
# simulate the set of games
unfairCoinOutcome = setOfGamesUnfairCoin.simulation()

# print outcomes of each cohort
Support.print_outcomes(fairCoinOutcome, 'When the probability of flipping a head is 50%:')
Support.print_outcomes(unfairCoinOutcome, 'When the probability of flipping a head is 45%:')

# draw survival curves and histograms
Support.draw_reward_histograms(fairCoinOutcome, unfairCoinOutcome)

# print comparative outcomes
Support.print_comparative_outcomes(fairCoinOutcome, unfairCoinOutcome)
