# CardMaster
Helper program for the Card Master class from the [Steampunk Compendium](https://homebrewery.naturalcrit.com/share/r1mnLrkNrZ). 

## Packages Used
* Numpy
* Pandas
* OpenPyXL

## Goal
The Card Master class can easily become tedious and overwhelming when not playing with a physical deck of cards (like when playing online). This program seeks to automate the process in a flexible manner using Python and Excel. 

## Main Features
* Spreadsheet management of spell card collection, spell deck, hand, and discard pile.\
* Add spell card to collection (functional)
    * Checks: in spell list, duplicates, max spell level
* Deck building (in progress, can be done manually with Excel)
* Draw Hand (functional)
    * Draws 5 random cards from deck using PCG-64 psuedo-rng
* Draw Card (functional)
    * To Do: add check for hand size
* Discard Card (functional)

