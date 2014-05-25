Title: Heatmap of UFO sightings (2/3): Obtaining and cleaning the data
Date: 2014-05-17 11:00
Category: 
Tags: 
Slug: ufo-heatmap-part2
Author: Sean Harnett
Summary: A heatmap of UFO sightings in the USA, normalized by population. Obtaining and cleaning the data.

This is the unpleasant part of data science that makes up around 80% of the work. I recommend skipping to [part 3](|filename|heatmap_part3.md) if you don't have much patience. I'll be using Python and the pandas data analysis library.

The original data can be downloaded from 
[Infochimps](http://www.infochimps.com/datasets/60000-documented-ufo-sightings-with-text-descriptions-and-metada).

###Cleaning steps

After a lengthy process, I arrive at a dataframe that looks like this:

<table>
  <thead>
    <tr style="text-align: right;">
      <th>state_county</th>
      <th>population</th>
      <th>num_sightings</th>
      <th>raw_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> alabama autauga</td>
      <td>  55246</td>
      <td>  2</td>
      <td> 0.000036</td>
    </tr>
    <tr>
      <td> alabama baldwin</td>
      <td> 195540</td>
      <td> 32</td>
      <td> 0.000164</td>
    </tr>
    <tr>
      <td> alabama barbour</td>
      <td>  27076</td>
      <td>  0</td>
      <td> 0.000000</td>
    </tr>
    <tr>
      <td>    alabama bibb</td>
      <td>  22512</td>
      <td>  1</td>
      <td> 0.000044</td>
    </tr>
    <tr>
      <td>  alabama blount</td>
      <td>  57872</td>
      <td>  0</td>
      <td> 0.000000</td>
    </tr>
  </tbody>
</table>

Plotting those raw rates on a map looks like this:

![my raw heatmap]({filename}/images/ufo_sightings_normalized_raw.png)

Below are the steps I took:

step | action | rows remaining
- | - | -
1 | convert avro format to pandas DataFrame | 61067
2 | remove rows with ill-formed dates | 60802
3 | remove rows before 1990-08-30 | 54444
4 | remove rows with location outside the contiguous 48 states plus DC | 45983
5 | make location all uppercase and remove parenthetical comments | 45983
6 | get county, latitude, longitude from mapquest API | 42998
7 | convert counties to those used in ggplot2 | 42624
8 | get county populations from US census data | 42624
9 | convert the census counties to what's used in ggplot2 | 42624

Continue reading if you're interested in the nitty-gritty.

###Getting it into a pandas dataframe

The data comes in a few formats, none of which I could get pandas to read correctly. I resorted to using the avro format using a separate library (which required Python 2.x):

{% include_code convert_data.py lang:python :hidefilename: convert avro to dataframe %}

{% notebook ufo_part2.ipynb %}