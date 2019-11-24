# Fantasy Sports Calculator Main Project
# _Author_ Donovan Smith

print('Hello welcome to your fantasy sports calculator!')
circle = int(1)
while circle == 1:
    sport = str(input("Would you like to calculate football, basketball, "
                      "or baseball? "))


    def football():
        """

        """
        global points_on_fgs, points_given, yards_given, total_points, x, receps
        name = input('What is the name of the player?')
        num = int(input('How many weeks would you like to calculate?'))
        pos1 = True
        while pos1 == True:
            pos = str(input('Enter the abbreviation of the position of the player '
                            'you would like to calculate: '))
            for x in range(num):
                if pos == 'WR':
                    week_rush_tds = float(input('How many touchdowns did your player '
                                                'rush or catch this week?'))
                    week_receiving_yds = float(input('How many yards did your player '
                                                     'have receiving or rushing this '
                                                     'week?'))
                    receps = float(input('How many receptions did your player '
                                             'have '
                                             'this week?'))
                    total_points = float(((week_rush_tds * 6) + (week_receiving_yds
                                                                 * .1) + receps))
                    pos1 = False
                elif pos.capitalize() == 'RB':
                    week_rush_tds = float(input('How many touchdowns did'
                                                'your player rush or catch this week?'))
                    week_receiving_yds = float(input('How many yards did your player '
                                                     'have receiving or rushing this '
                                                     'week?'))
                    receps = float(input('How many receptions did your player '
                                         'have '
                                         'this week?'))
                    total_points = float(((week_rush_tds * 6) + (week_receiving_yds
                                                                 * .1) + receps))
                    pos1 = False
                elif pos.capitalize() == 'TE':
                    week_rush_tds = float(input('How many touchdowns did your player '
                                                'rush or catch this week?'))
                    week_receiving_yds = float(input('How many yards did your player '
                                                     'have receiving or rushing this '
                                                     'week?'))
                    receps = float(input('How many receptions did your player '
                                         'have '
                                         'this week?'))
                    total_points = float(((week_rush_tds * 6) + (week_receiving_yds
                                                                 * .1) + receps))
                    pos1 = False
                elif pos.capitalize() == 'QB':
                    week_pass_tds = float(input('How many touchdowns did your player '
                                                'throw for?'))
                    week_pass_yds = float(input('How many yards did your player '
                                                'throw for?'))
                    week_int = float(input('How many interceptions did your player '
                                           'throw?'))
                    total_points = float(((week_pass_tds * 4) + (
                            week_pass_yds * .05) + (week_int * -2)))
                    pos1 = False
                elif pos.capitalize() == 'DT/S':
                    kick_punt_ret = int(input("How many kickoffs or punt returns did "
                                              "your special team return?"))
                    def_touchdown = int(input("How many touchdowns did your defense "
                                              "score?"))
                    sack = int(input("How many sacks did your defense have?"))
                    blocks = int(input("How many field goal or extra points did your "
                                       "defense block?"))
                    fumb_int_safety = int(input("How many total fumble recoveries, "
                                                "interceptions(Not for a Touchdown) "
                                                ", and safeties"
                                                "did your defense get?"))
                    points_allow = int(
                        input("How many points did your defense allow?"))
                    yards_allow = int(input("How many total yards did your defense "
                                            "allow?"))
                    if points_allow == 0:
                        (points_given) = 5
                    elif 1 <= points_allow <= 6:
                        (points_given) = 4
                    elif 7 <= points_allow <= 13:
                        (points_given) = 3
                    elif 14 <= points_allow <= 17:
                        (points_given) = 1
                    elif 18 <= points_allow <= 27:
                        (points_given) = 0
                    elif 28 <= points_allow <= 34:
                        (points_given) = -1
                    elif 35 <= points_allow <= 45:
                        (points_given) = -3
                    elif points_allow >= 46:
                        (points_given) = -5
                    if yards_allow < 100:
                        (yards_given) = 5
                    elif 100 <= yards_allow <= 199:
                        (yards_given) = 3
                    elif 200 <= yards_allow <= 299:
                        (yards_given) = 2
                    elif 300 <= yards_allow <= 349:
                        (yards_given) = 0
                    elif 350 <= yards_allow <= 399:
                        (yards_given) = -1
                    elif 400 <= yards_allow <= 449:
                        (yards_given) = -3
                    elif 450 <= yards_allow <= 499:
                        (yards_given) = -5
                    elif 500 <= yards_allow <= 549:
                        (yards_given) = -6
                    elif yards_allow >= 550:
                        (yards_given) = -7
                    total_points = int(
                        (kick_punt_ret * 6) + (def_touchdown * 6) + sack + (blocks
                                                                            * 2) + (
                                fumb_int_safety * 2) + points_given + (
                            yards_given))
                    pos1 = False
                elif pos.capitalize() == 'K':
                    pat = int(input("How many extra points did you kicker make?"))
                    missed_fg = int(input("How many total fields goals and extra "
                                          "points did your kicker miss?"))
                    made_fg = int(
                        input("How many field goals did your kicker make"))
                    if made_fg > 0:
                        for y in range(made_fg):
                            distance = int(input("How far was the field goal?"))
                            if 0 <= distance <= 39:
                                (points_on_fgs) = 3
                            elif 40 <= distance <= 49:
                                (points_on_fgs) = 4
                            elif distance >= 50:
                                (points_on_fgs) = 5
                    if made_fg == 0:
                        points_on_fgs = int(0)
                    total_points = int(pat + (missed_fg * -1) + points_on_fgs)
                    pos1 = False

        print(name, "week", (x + 1), "totals were", format(total_points, '.2f'))


    def basketball():
        """

        """
        global total_points1
        name = input('What is your players name?')
        week1 = True
        while week1 == True:
            week = int(input('How many games would you like to calculate?'))
            if week > 0:
                for x in range(week):
                    fgm = int(input('How many field goals did you player make?'))
                    fga = int(input('How many field goals did you player attempt?'))
                    ftm = int(input('How mnay free throws did your player make?'))
                    fta = int(input('how many free throws did your player attempt?'))
                    rebounds = int(input('How many rebounds did your player have?'))
                    assists = int(input('How many assists did your player have?'))
                    steals = int(input('How many steals did your player have?'))
                    blocks = int(input('How many blocks did your player have?'))
                    turnovers = int(input('How many turnovers did your player have?'))
                    points = int(input('How many points did your player have?'))
                    total_points1 = (fgm + (fga * -1) + ftm + (fta * -1) + (
                        rebounds) + assists + steals + blocks + (
                                                turnovers * -1) + points)
                    week1 = False
            elif week < 0:
                print('Input not understood. Enter a positive whole number.')
                week1 = True
        print('Total points were:', total_points1)


    def baseball():
        """

        """
        global win1, loss1, save1, quality1, single, double, triple, home_runs, caught_stolen, stolen
        pos = str(input('What position is your player? '))
        if pos.capitalize() == 'Pitcher':
            win_loss = str(input('Did you pitcher get a win or a loss? '))
            if win_loss.capitalize() == 'Win':
                win1 = int(7)
                loss1 = int(0)
            elif win_loss.capitalize() == 'Loss':
                loss1 = int(-5)
                win1 = int(0)
            save = str(input('Did your pitcher earn a save? '))
            if save.capitalize() == 'Yes':
                save1 = int(7)
            elif save.capitalize() == 'No':
                save1 = int(0)
            quality = str(input('Did your pitcher earn a quality start? '))
            if quality.capitalize() == 'Yes':
                quality1 = int(3)
            elif quality.capitalize() == 'no':
                quality1 = int(0)
            strike_outs = int(input('How many strikeouts did your pitcher have? '))
            walks = int(input('How many batters did your people walk? '))
            innings = int(input('How many innings did your pitcher pitch? '))
            hits_allow = int(input('How many hits did your pitcher allow? '))
            earned_runs = int(
                input('How many earned runs did your pitcher have? '))
            hit_batters = int(input('How many batters did your pitcher hit?'))
            total_points3 = (win1 + loss1 + save1 + quality1 + (
                    strike_outs * .5) + (walks * -1) + (innings * 3) + (
                                     hits_allow * -1) + (earned_runs * -1) + (
                                     hit_batters * -1))
            print('Your players total points were:', total_points3)

        elif pos != 'pitcher':
            hits = str(input('Did your player get a hit?'))
            if hits.capitalize() == 'Yes':
                single = int(input('How many singles  did your player have?'))
                double = int(input('How many doubles did your player have?'))
                triple = int(input('How many triples did your player have?'))
                home_runs = int(input('How many homeruns did your player hit?'))
            elif hits.capitalize() == 'No':
                single = int(0)
                double = int(0)
                triple = int(0)
                home_runs = int(0)
            rbi = int(input('How many RBIs did your player have?'))
            run = int(input('How many times did your player score?'))
            walk = int(input('How many times was your player walked?'))
            steal = input('Did your player attempt to steal?')
            did_steal = True
            while did_steal == True:
                if steal.capitalize() == 'yes':
                    stolen = int(input('How many bases did your player steal?'))
                    caught_stolen = int(input('How many times did your player '
                                              'get caught stealing?'))
                    did_steal = False
                if steal.capitalize() == 'No':
                    stolen = int(0)
                    caught_stolen = int(0)
                    did_steal = False
                if steal.capitalize() != 'Yes' or 'No':
                    print('Your input for ')
                    did_steal = True
            strike = int(input('How many times did your player strikeout?'))
            hbp = int(input('How many times did your player get hit by a pitch'))
            total_points2 = (single + (double * 2) + (triple * 3) + (home_runs *
                                                                     4) +
                             rbi + walk + (stolen * 2) + (
                                     caught_stolen * -1) + (strike * -.5) + hbp)
            print('Your players total points were:', total_points2)


    if sport.capitalize() == 'Football':
        football()
        circle = int(0)
    elif sport.capitalize() == 'Basketball':
        basketball()
        circle = int(0)
    elif sport.capitalize() == 'Baseball':
        baseball()
        circle = (0)
    else:
        print('Input was not understood, please enter another sport.')
        circle = int(1)
