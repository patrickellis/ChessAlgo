Chess Algo [![GitHub version](https://badge.fury.io/gh/patrickellis%2Fchessalgo.svg)](https://badge.fury.io/gh/patrickellis%2Fchessalgo)
======
<a href="https://www.patrickellis.dev/all/projects/chessalgo" target="_blank"> View the project page on my site </a>
## Description
ChessAlgo is a computer-vision driven Chess AI that processes visual data to parse a chess position on the screen, detect moves played in sequence by an opponent, and calculate the optimal response in an adjustable time period up to and including instantaneous play. It is capable of fully autonomous operation and uses a mouse handler API to respond to events independently of a human user. 

## Puzzle Solving
I wanted a practical use for the program other than playing versus AI programs and other players, so I adapted the use case to be able to begin playing from any position - assuming it is our turn to play. 
This means that the bot can solve puzzles dynamically on almost any website.

<p align="center">
  <img src = "https://github.com/patrickellis/Portfolio/blob/master/images/docs/ant-gif.gif" style="padding-top:100px; width:350px;height:350px;" width="650" />
</p>

## Artifical Intelligence
ChessAlgo involves a sequential pre-processing pipeline. The first step involves locating the board on the screen, done through (relatively) straightforward gradient analysis. 

<p align="center">
  <img src = "https://github.com/patrickellis/Portfolio/blob/master/images/docs/anti-gif-2.gif" style="padding-top:100px; width:350px;height:350px;" width="650" />
</p>
