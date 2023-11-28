def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    DAYS_OF_THE_WEEK = {   # Put this outside the function if SCREAMING_SNAKE
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    if (day_of_week in range(1,8)):    # Could use .get(), return none if not.
        return DAYS_OF_THE_WEEK[day_of_week]
    else:
        return None


# Uses a list instead of a dict in the solution.
