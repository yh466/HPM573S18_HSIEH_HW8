import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, coin_type):
    """ prints the outcomes of a simulated game-set under steady state
    :param sim_output: output of a simulated cohort
    :param coin_type: fair or unfair coin
    """

    # mean and confidence interval text of expected game reward
    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    # print game reward statistics
    print(coin_type)
    print("Estimate of game reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_CI_text)


def draw_reward_histograms(sim_output_fair_coin, sim_output_unfair_coin):
    """ draws the histograms of game rewards
    :param sim_output_fair_coin: output of a cohort simulated game-set with a fair coin
    :param sim_output_unfair_coin: output of a cohort simulated game-set with an unfair coin
    """

    # histograms of game rewards
    set_of_game_rewards = [
        sim_output_fair_coin.get_rewards(),
        sim_output_unfair_coin.get_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of game reward',
        x_label='Game rewards',
        y_label='Counts',
        bin_width=50,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.6
    )


def print_comparative_outcomes(sim_output_fair_coin, sim_output_unfair_coin):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_fair_coin: output of a cohort simulated game-set with a fair coin
    :param sim_output_unfair_coin: output of a cohort simulated game-set with an unfair coin
    """

    # increase in survival time
    difference = Stat.DifferenceStatIndp(
        name='Change in game rewards',
        x=sim_output_unfair_coin.get_rewards(),
        y_ref=sim_output_fair_coin.get_rewards()  # the base case, the status quo
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=difference.get_mean(),                   # the mean difference in game rewards
        interval=difference.get_t_CI(alpha=P.ALPHA),      # the CI associated with the mean difference
        deci=1
    )
    print("Average change in game rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)


    ### I didn't get any reward = 0 and was able to get an estimate of % change
    ### but will still comment out the section below to be consistent with transient state estimation.
    ##  % increase in survival time
    #relativeDiff = Stat.RelativeDifferenceIndp(
    #    name='Average % change in game reward',
    #    x=sim_output_unfair_coin.get_rewards(),
    #    y_ref=sim_output_fair_coin.get_rewards()
    #)

    ## estimate and CI
    #estimate_CI = Format.format_estimate_interval(
    #    estimate=relativeDiff.get_mean(),
    #    interval=relativeDiff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
    #    deci=1,
    #    form=Format.FormatNumber.PERCENTAGE
    #)
    #print("Average percentage change in game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
    #      estimate_CI)
