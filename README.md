# Sports_Highlight_Generator

## Inspiration
Publishing highlights after a sports game is a mandatory practice followed in the broadcast industry. A highlights video provides a quick snapshot of the event highlighting the interesting events in the game and thus providing the viewers an opportunity to get a quick summary of the game.
In a manual process, a video editor has to run through the entire game, identify candidate areas for the highlights and compile all the clips into a single compilation video. This can be a cumbersome process and time-consuming. 

## What it does
A Deep Learning Model to generate automatically generate highlights from a sports video Highlight-Detection-in-Sports-Videos-using-Audience-Reaction Highlights in a sports video are the key exciting moments in the match which attract the attention of the spectators in the match.

Original Video Link: https://www.youtube.com/watch?v=CGFgHjeEkbY
Highlight generated video: https://youtu.be/HagUinMhpbg

## How we built it
Using numpy and moviepy in Python

## Challenges we ran into
The algorithm can be confused by broadcasters who make lots of replays or lower the sound of the crowd after goals, and it may miscut some goals on penalties because the crowd starts whistling long before the shoot. So large-scale applications would require a less naive model.

## What we learned
How we can use machine learning (numpy and moviepy) to generate highlights of sports video.

## What's next for Sports Highlight Generator
The next step is to take each peak and convert it to a GIF for social sharing and automatically share:)
