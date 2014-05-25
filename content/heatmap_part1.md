Title: Heatmap of UFO sightings (1/3): Introduction
Date: 2014-05-17 12:00
Category: 
Tags: 
Slug: ufo-heatmap-part1
Author: Sean Harnett
Summary: A heatmap of UFO sightings in the USA, normalized by population. Introduction.

## Adjusting heatmaps for population: addressing XKCD 1138

In *Machine Learning for Hackers* by Drew Conway and John Myles White, they introduce a data set of UFO sightings as an example. Googling around for other work on this data set produces some heatmaps of the sightings, here is one from [flowingdata.com](http://flowingdata.com/2011/07/07/where-the-aliens-are-flying-their-ufos/):

{% img {filename}/images/ufo_map_annotated1.png 600 %}

I was immediately reminded of the [XKCD comic](http://xkcd.com/1138/):

![xkcd heatmap]({filename}/images/heatmap_xkcd.png)

I decided to try adjusting the UFO sightings data for population, something I've never done before. Are UFO sightings distributed according to population? Or do some areas get more than their fair share of sightings?

##TL;DR

![my ufo heatmap]({filename}/images/ufo_sightings_normalized_smooth.png)

The western US gets a lot more sightings than the population would suggest, especially near Area 51. Read on to follow my data adventure.

##A little bit more

 I used Python to wrangle the data and ggplot2 from R to make the plots. The actual raw data looks like this:

![my raw heatmap]({filename}/images/ufo_sightings_normalized_raw.png)

I explored a couple different ways to smooth that out and arrive at the final image, which all gave pretty much the same result. Specifically, I looked at: 

* a beta-binomial maximum likelihood approach
* the R library lme4 for linear mixed-effects models
* the probabilistic programming language Stan

##Up Next

[Obtaining and cleaning the data](|filename|heatmap_part2.md)

This details the tedious process I went through to arrive at the 'raw' map above.

[Refining the results](|filename|heatmap_part3.md)

Here I show how I came up with the smoother map.