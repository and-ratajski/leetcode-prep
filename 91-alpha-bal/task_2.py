from enum import Enum
from collections import namedtuple


class ItemEnum(Enum):
    QUANTITY = "QUANTITY"
    PRIORITY = "PRIORITY"


class CommandEnum(Enum):
    ORDER = "ORDER"
    CHECK = "CHECK"
    FILL = "FILL"


def task_2(command_no: int, *args):
    """
    Queue with trading requests.

    Todo:
        Implement queue as a hashmap
    """
    queue = []
    Order = namedtuple("Order", "timestamp order_id valid_until prio quantity")

    def _validate_command(command: list):
        """In this place various commands should be validated."""
        pass

    for arg in args:
        destr_arg = str(arg).split(" ")
        _validate_command(destr_arg)

        # ORDER
        if destr_arg[0] == CommandEnum.ORDER.value:
            order = Order._make(destr_arg[1:])
            queue.append(order)
        # CHECK
        elif destr_arg[0] == CommandEnum.CHECK.value:
            check_timestamp = destr_arg[1]
            check_item = destr_arg[2]

            if check_item == ItemEnum.QUANTITY.value:
                acc = 0
                for index, order in enumerate(queue):
                    if order.timestamp <= check_timestamp:
                        acc += int(order.quantity)
                    else:
                        del queue[index]
                print(acc)
            elif check_item == ItemEnum.PRIORITY.value:
                highest_prio = -1
                matching_id = "NONE"
                for index, order in enumerate(queue):
                    if order.timestamp <= check_timestamp:
                        _order_prio = int(order.prio)
                        highest_prio = _order_prio if _order_prio > highest_prio else highest_prio
                        matching_id = order.order_id
                    else:
                        del queue[index]
                print(matching_id)
            else:
                raise Exception("Invalid CHECK item type")
        # FILL
        elif destr_arg[0] == CommandEnum.FILL.value:
            fill_timestamp = destr_arg[1]
            fill_order_id = destr_arg[2]
            for index, order in enumerate(queue):
                if order.timestamp <= fill_timestamp:
                    if order.order_id == fill_order_id:
                        print(order.order_id)
                        del queue[index]
                else:
                    del queue[index]


if __name__ == "__main__":
    task_2(
        11,
        "ORDER 1 aaaaaa 12 10 8",
        "ORDER 2 bbbbbb 15 5 12",
        "ORDER 3 cccccc 8 7 25",
        "CHECK 4 QUANTITY",
        "CHECK 5 PRIORITY",
        "FILL 7 aaaaaa",
        "CHECK 8 QUANTITY",
        "CHECK 9 PRIORITY",
        "FILL 14 bbbbbb",
        "CHECK 16 QUANTITY",
        "CHECK 200 PRIORITY"
    )

    # command_no = input()
    # commands = []
    # for n in range(int(command_no)):
    #     cmd = input()
    #     commands.append(str(cmd))
    # # print()
    # task_2(int(command_no), *commands)
