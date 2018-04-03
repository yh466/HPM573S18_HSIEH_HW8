import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_gameset, coin_type):
    """ prints the outcomes of a simulated multi-gameset under transient state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and projection interval text of game reward
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_gameset.get_overall_mean_reward(),
        interval=multi_gameset.get_PI_mean_reward(alpha=P.ALPHA),
        deci=1)

    # print game reward statistics
    print(coin_type)
    print("  Estimate of mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)


def draw_histograms(multi_cohort_fair_coin, multi_cohort_unfair_coin):
    """ draws the histograms of average survival time
    :param multi_cohort_fair_coin: multiple gamesets simulated when the coin is fair
    :param multi_cohort_unfair_coin: multiple gamesets simulated when the coin is unfair
    """

    # histograms of game rewards
    set_of_game_rewards = [
        multi_cohort_fair_coin.get_all_mean_reward(),
        multi_cohort_unfair_coin.get_all_mean_reward()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of average game reward',
        x_label='Game reward',
        y_label='Counts',
        bin_width=50,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.5,
    #    x_range=[-50, 0]
    )


def print_comparative_outcomes(multi_cohort_fair_coin, multi_cohort_unfair_coin):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_fair_coin: multiple gamesets simulated when the coin is fair
    :param multi_cohort_unfair_coin: multiple gamesets simulated when the coin is unfair
    """

    # increase in survival time
    difference = Stat.DifferenceStatIndp(
        name='Change in expected reward',
        x=multi_cohort_unfair_coin.get_all_mean_reward(),
        y_ref=multi_cohort_fair_coin.get_all_mean_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=difference.get_mean(),
        interval=difference.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected change in mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    ### Commenting out the below section because some denominator turned out to be zero.
    ## % increase in mean survival time
    # relativeDiff = Stat.RelativeDifferenceIndp(
    #    name='% change in expected reward',
    #    x=multi_cohort_unfair_coin.get_all_total_rewards(),
    #    y_ref=multi_cohort_fair_coin.get_all_total_rewards()
    #)


    ## estimate and CI
    #estimate_CI = Format.format_estimate_interval(
    #    estimate=relativeDiff.get_mean(),
    #    interval=relativeDiff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
    #    deci=1,
    #    form=Format.FormatNumber.PERCENTAGE
    #)
    #print("Expected percentage change in mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
    #      estimate_CI)
