class DrawdawnException(Exception):
    """Custom Exception for the drawdown function."""
    pass


def task_1(coin_prices_no: int, coin_prices: str) -> int:
    """Returns the largest drawdown in coin prices in a given period."""
    MAX_COIN_NO = 10**5
    MAX_COIN_VALUE = 10**9
    if coin_prices_no < 1 or coin_prices_no > MAX_COIN_NO:
        raise DrawdawnException(
            f"Coin prices number is not within allowed range [1, {MAX_COIN_NO}]"
        )

    def _is_high(last_val: int, curr_val: int, is_start=False) -> bool:
        """Checks if the price change is a high or down."""
        if is_start or curr_val >= last_val:
            return True
        return False

    max_local_high = 0
    min_local_down = MAX_COIN_VALUE
    max_local_drawdown = 0
    last_value = None
    for index, value_str in enumerate(coin_prices.split(" ")):
        try:
            value = int(value_str)
        except ValueError as err:
            raise DrawdawnException(str(err))
        if value < 0 or value > MAX_COIN_VALUE:
            raise DrawdawnException(
                f"Coin prices are not within allowed range [1, {MAX_COIN_VALUE}]"
            )

        # Skip check on the last value as it's not a drawdwon
        if index == coin_prices_no - 1:
            break
        if _is_high(last_value, value, index == 0) and value > max_local_high:
            max_local_drawdown = (
                value - min_local_down
                if value - min_local_down > max_local_drawdown
                else max_local_drawdown
            )
            max_local_high = value
        if not _is_high(last_value, value, index == 0) and value < max_local_high:
            max_local_drawdown = (
                max_local_high - value
                if max_local_high - value > max_local_drawdown
                else max_local_drawdown
            )
            min_local_down = value
        last_value = value

    return max_local_drawdown


if __name__ == "__main__":
    print(task_1(7, "10000 6000 8000 6000 12000 7000 15000"))
