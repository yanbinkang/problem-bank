def check_cycle(first_node):
    slow_runner = first_node
    fast_runner = first_node

    while fast_runner != None and fast_runner.get_next() != None:
        slow_runner = slow_runner.get_next()
        fast_runner = fast_runner.get_next().get_next()

        if fast_runner == slow_runner:
            return True

    return False
