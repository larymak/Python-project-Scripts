#! /usr/bin/env python3
# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     game.py
   Author :       chenhao
   time：          2021/11/4 20:22
   Description :
-------------------------------------------------
"""
import collections
import logging
import abc
import math
import random
import time
import fire
from itertools import permutations
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s][%(filename)s:%(lineno)d]:%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

NUMBER_COUNT = 4
ALL_NUMBER = list(range(10))


class IPlayer:
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def guess(self) -> List[int]:
        pass

    def refresh(self):
        pass

    def notify(self, guess: List[int], judge_rs: dict):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class RandomPlayer(IPlayer):

    def guess(self) -> List[int]:
        return random.sample(ALL_NUMBER, NUMBER_COUNT)


class Human(IPlayer):
    def guess(self) -> List[int]:
        while True:
            try:
                logger.info("input your guess")
                guess = input()
                guess = [int(e) for e in guess]
                if len(guess) != NUMBER_COUNT:
                    raise Exception()
                return guess
            except Exception as e:
                logger.error(f"invalid input:{guess}, please input again!")
        return guess


class Node:
    def __init__(self, d):
        self.n = 0
        self.v = 0
        self.d = d
        if d < NUMBER_COUNT:
            self.children: List[Node] = [Node(d + 1) for _ in range(10)]
        else:
            self.children = None

    def get_val(self, p, c=1.0):
        v = self.n / p
        d = math.log(1 / (self.v + 1))
        return v + c * d

    def get_next(self, his):
        cands = [(idx, e, e.get_val(self.n)) for idx, e in enumerate(self.children) if e.n and idx not in his]
        # logger.info(cands)
        item = max(cands, key=lambda x: x[2])
        return item

    def clear(self):
        self.n = 0
        if self.children:
            for c in self.children:
                c.clear()

    def __repr__(self):
        return f"Node(n={self.n},v={self.v},d={self.d})"

    def __str__(self):
        return self.__repr__()


def update_tree(root, cand: List[int]):
    n = root
    for idx in cand:
        n.n += 1
        n = n.children[idx]
    n.n += 1


class TreePlayer(IPlayer):

    def __init__(self, name, wait=0):
        super().__init__(name=name)
        self.root = Node(d=0)
        self.cands = list(permutations(ALL_NUMBER, NUMBER_COUNT))
        self.wait = wait
        for cand in self.cands:
            update_tree(self.root, cand)

    def refresh(self):
        self.root = Node(d=0)
        self.cands = list(permutations(ALL_NUMBER, NUMBER_COUNT))
        for cand in self.cands:
            update_tree(self.root, cand)

    def guess(self) -> List[int]:
        n = self.root
        rs = []
        for _ in range(NUMBER_COUNT):
            idx, n, v = n.get_next(his=rs)
            n.v += 1
            rs.append(idx)
        time.sleep(self.wait)
        return rs

    def notify(self, guess: List[int], judge_rs: dict):
        tmp = len(self.cands)
        self.cands = [e for e in self.cands if judge_rs2str(judge_rs) == judge_rs2str(judge(e, guess))]
        logger.info(f"cut cands from {tmp} to {len(self.cands)} after cuts")
        self.root.clear()
        for cand in self.cands:
            update_tree(self.root, cand)


def judge(ans: List[int], gs: List[int]) -> dict:
    assert len(ans) == len(gs) == NUMBER_COUNT
    a_list = [e for e in zip(ans, gs) if e[0] == e[1]]
    a = len(a_list)
    b = len(set(ans) & set(gs))
    b -= a
    return dict(a=a, b=b)


def judge_rs2str(j_rs):
    a = j_rs["a"]
    b = j_rs["b"]
    return f"{a}A{b}B"


def run_game(player, rnd=10, answer=None):
    if not answer:
        answer = random.sample(ALL_NUMBER, NUMBER_COUNT)
    player.refresh()
    for idx in range(rnd):
        logger.info(f"round:{idx + 1}")
        guess = player.guess()
        judge_rs = judge(answer, guess)
        logger.info(f"{player} guess:{guess}, judge result:{judge_rs2str(judge_rs)}")
        if guess == answer:
            break
        player.notify(guess, judge_rs)
    logger.info(f"answer is :{answer}")
    if guess == answer:
        logger.info(f"{player} win in {idx + 1} rounds!")
        return idx
    else:
        logger.info(f"{player} failed!")
        return None


def compete(players, game_num, rnd=10, base_score=10):
    answers = [random.sample(ALL_NUMBER, NUMBER_COUNT) for _ in range(game_num)]
    score_board = collections.defaultdict(int)
    for g in range(game_num):
        logger.info(f"game:{g + 1}")
        for p in players:
            logger.info(f"player {p} try")
            s = run_game(player=p, rnd=rnd, answer=answers[g])
            s = base_score - s if s is not None else 0
            score_board[p] += s
            logger.info("press any key to select next player")
            _ = input()
        logger.info(f"current score board:{dict(score_board)}")
        logger.info("press any key to next game")
        _ = input()

    return score_board


def compete_with_ai(game_num=3):
    human = Human("Human")
    ai = TreePlayer("AI", wait=2)
    players = [human, ai]
    logger.info(f"Human Vs AI with {game_num} games")
    score_board = compete(players=players, game_num=game_num)
    logger.info("final score board:{}")
    logger.info(score_board)


def test_avg_step(test_num=100):
    ai = TreePlayer("AI", wait=0)
    steps = []
    for _ in range(test_num):
        steps.append(run_game(ai, rnd=10))
    avg = sum(steps) / len(steps)
    logger.info(f"{ai} avg cost{avg:.3f} steps with {test_num} tests")


if __name__ == '__main__':
    fire.Fire(compete_with_ai)
