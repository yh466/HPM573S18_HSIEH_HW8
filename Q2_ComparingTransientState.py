import Parameters as P
import CasinoModelClasses as Cls
import SupportTransientState as Support

# create multiple game sets for when the coin is fair
multiGameSetFairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_SETS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head=[P.HEAD_PROB_FAIR]*P.NUM_SIM_SETS,  # [p, p, ...]
    n_games_in_a_set=[P.REAL_SET_SIZE]*P.NUM_SIM_SETS  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)
# simulate all game sets
multiGameSetFairCoin.simulation()

# create multiple game sets for when the coin is unfair
multiGameSetUnfairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_SETS, 2*P.NUM_SIM_SETS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    prob_head=[P.HEAD_PROB_UNFAIR]*P.NUM_SIM_SETS,
    n_games_in_a_set=[P.REAL_SET_SIZE]*P.NUM_SIM_SETS  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)
# simulate all game sets
multiGameSetUnfairCoin.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiGameSetFairCoin, 'When the probability of flipping a head is 50%:')
Support.print_outcomes(multiGameSetUnfairCoin, 'When the probability of flipping a head is 45%:')

# draw histograms of average survival time
Support.draw_histograms(multiGameSetFairCoin, multiGameSetUnfairCoin)

# print comparative outcomes
Support.print_comparative_outcomes(multiGameSetFairCoin, multiGameSetUnfairCoin)
