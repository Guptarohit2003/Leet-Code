import collections


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        n = len(deck)
        queue = collections.deque(range(n))
        result = [0] * n

        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())

        return result
