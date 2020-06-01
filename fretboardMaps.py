#!/usr/bin/env python3
"""
    fretboardMaps.py maps fretboard for 1 thru 6 string instruments.
    v0.01 Copyright (C) 2020 David Murray

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import pandas as pd
from tkinter import *

# globals
scale = ['0', '1', '2', '3', '4', '5', '6']
one_string = ['', '', '', '', '', '', '', '', '', '', '', '']
capo = 0
write2csv = False

fretNum = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11]
string1 = ['', '', '', '', '', '', '', '', '', '', '', '']
string2 = ['', '', '', '', '', '', '', '', '', '', '', '']
string3 = ['', '', '', '', '', '', '', '', '', '', '', '']
string4 = ['', '', '', '', '', '', '', '', '', '', '', '']
string5 = ['', '', '', '', '', '', '', '', '', '', '', '']
string6 = ['', '', '', '', '', '', '', '', '', '', '', '']

tcapo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
tvarS0 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS1 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS2 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS3 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS4 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS5 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']
tvarS6 = ['', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G']

tvar1 = ['notes', 'disp.Roman', 'disp.Numeric', 'disp.SOLFA_up',
         'disp.SOLFA_dn']

tvar2 = ['keys.C', 'keys.Db', 'keys.D', 'keys.Eb',
         'keys.E', 'keys.F', 'keys.F#', 'keys.G',
         'keys.Ab', 'keys.A', 'keys.Bb', 'keys.B']

tvar3 = ['scales.Major', 'scales.Ionian', 'scales.Mixolydian',
         'scales.Dorian', 'scales.natural_minor', 'scales.Aeolian',
         'scales.Phrygian', 'scales.Locrian', 'scales.Lydian',
         'scales.Pent_mode_1', 'scales.Pent_mode_2', 'scales.Pent_mode_3',
         'scales.Pent_mode_4',  'scales.Pent_mode_5', 'scales.Mtn_minor',
         'scales.Harmonic_maj', 'scales.Harmonic_min', 'scales.Chromatic']

tvar4 = ['chords.Maj', 'chords.7', 'chords.M7', 'chords.m',
         'chords.m7', 'chords.mM7', 'chords.aug', 'chords.aug7',
         'chords.sus2', 'chords.sus4', 'chords.dim', 'chords.dim7']

tvar5 = ['scale', 'chord']


"""
disp: alternate display representations
"""
disp = pd.DataFrame(
    {
        # Alternate display representations
        'Roman':      ['I',  'ii',  'II', 'iii', 'III', 'IV',
                       'v',  'V',   'vi', 'VI',  'vii', 'VII'],
        'Numeric':    ['1',  '2b',  '2',  '3b',  '3',   '4',
                       '5b', '5',   '6b', '6',   '7b',  '7'],
        'SOLFA_up':   ['Do', 'Di',  'Re', 'Ri',  'Mi',  'Fa',
                       'Fi', 'Sol', 'Si', 'La',  'Li',  'Ti'],
        'SOLFA_dn':   ['Do', 'Ra',  'Re', 'Me',  'Mi',  'Fa',
                       'Se', 'Sol', 'le', 'La',  'te',  'Ti'],
        }
    )


"""
keys: keys; cirle of 5ths representation (no enharmonics)
      Exception is Gb for F# because # is illegal variable
      name in python.
"""
keys = pd.DataFrame(
    {
        'C':  ['C',  'Db',  'D',  'Eb',  'E',   'F',
               'F#', 'G',   'Ab', 'A',   'Bb',  'B'],
        'G':  ['G',  'Ab',  'A',  'Bb',  'B',   'C',
               'Db', 'D',   'Eb', 'E',   'F',   'F#'],
        'D':  ['D',  'Eb',  'E',  'F',   'F#',  'G',
               'Ab', 'A',   'Bb', 'B',   'C',   'C#'],
        'A':  ['A',  'Bb',  'B',  'C',   'C#',  'D',
               'Eb', 'E',   'F',  'F#',  'G',   'G#'],
        'E':  ['E',  'F',   'F#', 'G',   'G#',  'A',
               'Bb', 'B',   'C',  'C#',  'D',   'D#'],
        'B':  ['B',  'C',   'C#', 'D',   'D#',  'E',
               'F',  'F#',  'G',  'G#',  'A',   'A#'],
        #  because F# is illegal name in python
        'Gb': ['F#', 'G',   'G#', 'A',   'A#',  'B',
               'C',  'C#',  'D',  'D#',  'E',   'F'],
        'Db': ['Db', 'D',   'Eb', 'E',   'F',   'Gb',
               'G',  'Ab',  'A',  'Bb',  'B',   'C'],
        'Ab': ['Ab', 'A',   'Bb', 'B',   'C',   'Db',
               'D',  'Eb',  'E',  'F',   'Gb',  'G'],
        'Eb': ['Eb', 'E',   'F',  'F#',  'G',   'Ab',
               'A',  'Bb',  'B',  'C',   'C#',  'D'],
        'Bb': ['Bb', 'B',   'C',  'Db',  'D',   'Eb',
               'E',  'F',   'Gb', 'G',   'Ab',  'A'],
        'F':  ['F',  'Gb',  'G',  'Ab',  'A',   'Bb',
               'B',  'C',   'Db', 'D',   'Eb',  'E'],
        }
    )

"""
scales: modal scales. You can add more in this format
"""
scales = pd.DataFrame(
    {
        'Lydian':        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        'Major':         [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        'Ionian':        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        'Mixolydian':    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        'Pent_mode_2':   [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        'Dorian':        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        'Mtn_minor':     [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        'Pent_mode_5':   [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        'natural_minor': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        'Aeolian':       [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        'Pent_mode_3':   [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        'Phrygian':      [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        'Pent_mode_1':   [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        'Locrian':       [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        'Pent_mode_4':   [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        'Harmonic_maj':  [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        'Harmonic_min':  [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        'Chromatic':     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        }
    )


"""
chords: basic chords defined
"""
chords = pd.DataFrame(
    {
        'Maj':     [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        'Maj7':    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        'MajM7':   [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        'm':       [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        'm7':      [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        'mM7':     [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        'aug':     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        'aug7':    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        'sus2':    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        'sus4':    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        'dim':     [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        'dim7':    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        }
    )


def helpFBM():
    """
    Basic help information
    """
    print('------------------------- help -----------------------------')
    print('[display] notes, Roman, numeric, SOLFA_up, SOLFA_dn')
    print('    default = notes')
    print()
    print('[key] C, Db, D, etc. for key of scale or root of chord')
    print('    default = C')
    print()
    print('[scale] Major, Mixolydian, natural minor, chromatic, et')
    print('    default = chromatic')
    print()
    print('[chord] Maj, 7, min, dim, etc. for chords')
    print('    default = Maj')
    print()
    print('[Scale or Chord] select scale or chord calculated output')
    print('    default = scale')
    print()
    print('[calculate] perform calculations and produce fretboard map')
    print()
    print('[quit] exits the script')
    print()
    print('( ) Write csv (*) No write csv selection')
    print('    default = No write')
    print()
    print('[capo] select capo fret number')
    print('    default = 0')
    print()
    print('[s1] - [s6] set note for string')
    print('------------------------------------------------------------')


def makeScale(key, scaleName):
    """
    makeScaleMake(key, scaleName) to crate a scale or chord
    >>> makeScale(keys.A, scales.Chromatic)
    ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb']
    >>> makeScale(keys.F, scales.Lydian)
    ['F', 'G', 'A', 'B', 'C', 'D', 'E']
    >>> makeScale(keys.C, scales.Major)
    ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    >>> makeScale(keys.C, scales.Ionian)
    ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    >>> makeScale(keys.G, scales.Mixolydian)
    ['G', 'A', 'B', 'C', 'D', 'E', 'F']
    >>> makeScale(keys.G, scales.Pent_mode_2)
    ['G', 'A', 'B', 'D', 'E', '', '']
    >>> makeScale(keys.D, scales.Dorian)
    ['D', 'E', 'F', 'G', 'A', 'B', 'C']
    >>> makeScale(keys.D, scales.Mtn_minor)
    ['D', 'E', 'F', 'G', 'A', 'C', '']
    >>> makeScale(keys.D, scales.Pent_mode_5)
    ['D', 'E', 'G', 'A', 'B', '', '']
    >>> makeScale(keys.A, scales.natural_minor)
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    >>> makeScale(keys.A, scales.Aeolian)
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    >>> makeScale(keys.A, scales.Pent_mode_3)
    ['A', 'B', 'D', 'E', 'G', '', '']
    >>> makeScale(keys.E, scales.Phrygian)
    ['E', 'F', 'G', 'A', 'B', 'C', 'D']
    >>> makeScale(keys.G, scales.Pent_mode_1)
    ['G', 'Bb', 'C', 'D', 'F', '', '']
    >>> makeScale(keys.B, scales.Locrian)
    ['B', 'C', 'D', 'E', 'F', 'G', 'A']
    >>> makeScale(keys.B, scales.Pent_mode_4)
    ['B', 'D', 'E', 'G', 'A', '', '']
    >>> makeScale(keys.C, scales.Harmonic_maj)
    ['C', 'D', 'E', 'F', 'G', 'Ab', 'B']
    >>> makeScale(keys.A, scales.Harmonic_min)
    ['A', 'B', 'C', 'D', 'E', 'F', 'G#']
    >>> makeScale(keys.C, chords.Maj)
    ['C', 'E', 'G', '', '', '', '']
    >>> makeScale(keys.C, chords.Maj7)
    ['C', 'E', 'G', 'Bb', '', '', '']
    >>> makeScale(keys.C, chords.MajM7)
    ['C', 'E', 'G', 'B', '', '', '']
    >>> makeScale(keys.C, chords.m)
    ['C', 'Eb', 'G', '', '', '', '']
    >>> makeScale(keys.C, chords.m7)
    ['C', 'Eb', 'G', 'Bb', '', '', '']
    >>> makeScale(keys.C, chords.mM7)
    ['C', 'Eb', 'G', 'B', '', '', '']
    >>> makeScale(keys.C, chords.aug)
    ['C', 'E', 'Ab', '', '', '', '']
    >>> makeScale(keys.C, chords.aug7)
    ['C', 'E', 'Ab', 'Bb', '', '', '']
    >>> makeScale(keys.C, chords.sus2)
    ['C', 'D', 'G', '', '', '', '']
    >>> makeScale(keys.C, chords.sus4)
    ['C', 'F', 'G', '', '', '', '']
    >>> makeScale(keys.C, chords.dim)
    ['C', 'Eb', 'F#', '', '', '', '']
    >>> makeScale(keys.C, chords.dim7)
    ['C', 'Eb', 'F#', 'A', '', '', '']
    """
    global scales
    global scale
    scale_l = ['', '', '', '', '', '', '']
    i = 0
    j = 0
    while i < 7 and j < 12:
        #  print(key, i, j, scale_l, scaleName)
        if scaleName[j] == 1:
            scale_l[i] = key[j]
            i = i + 1
            j = j + 1
        else:
            j = j + 1
    return scale_l


def makeString(stringNote0, key, mode, retVal, capo):
    """
    makeString(stringNote0, key, mode, retVal, capo)
    Populate a string (12 frets) with scale or cord information
    Note the test makeString('F#', keys.Gb, scales.Major, 1, 0)
    where the F# is data and keys.Gb is a variable name. Python
    varianles cannot contain #.
    >>> scale = makeScale(keys.C, scales.Ionian)
    >>> makeString('C', keys.C, scales.Major, 1, 0)
    ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B']
    >>> makeString('C', keys.C, scales.Major, 2, 0)
    ['I', '', 'II', '', 'III', 'IV', '', 'V', '', 'VI', '', 'VII']
    >>> makeString('C', keys.C, scales.Major, 3, 0)
    ['1', '', '2', '', '3', '4', '', '5', '', '6', '', '7']
    >>> makeString('C', keys.C, scales.Major, 4, 0)
    ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'Sol', '', 'La', '', 'Ti']
    >>> makeString('Db', keys.Db, scales.Major, 1, 0)
    ['Db', '', 'Eb', '', 'F', 'Gb', '', 'Ab', '', 'Bb', '', 'C']
    >>> makeString('D', keys.D, scales.Major, 1, 0)
    ['D', '', 'E', '', 'F#', 'G', '', 'A', '', 'B', '', 'C#']
    >>> makeString('Eb', keys.Eb, scales.Major, 1, 0)
    ['Eb', '', 'F', '', 'G', 'Ab', '', 'Bb', '', 'C', '', 'D']
    >>> makeString('E', keys.E, scales.Major, 1, 0)
    ['E', '', 'F#', '', 'G#', 'A', '', 'B', '', 'C#', '', 'D#']
    >>> makeString('F', keys.F, scales.Major, 1, 0)
    ['F', '', 'G', '', 'A', 'Bb', '', 'C', '', 'D', '', 'E']
    >>> makeString('F#', keys.Gb, scales.Major, 1, 0)
    ['F#', '', 'G#', '', 'A#', 'B', '', 'C#', '', 'D#', '', 'F']
    >>> makeString('G', keys.G, scales.Major, 1, 0)
    ['G', '', 'A', '', 'B', 'C', '', 'D', '', 'E', '', 'F#']
    >>> makeString('Ab', keys.Ab, scales.Major, 1, 0)
    ['Ab', '', 'Bb', '', 'C', 'Db', '', 'Eb', '', 'F', '', 'G']
    >>> makeString('A', keys.A, scales.Major, 1, 0)
    ['A', '', 'B', '', 'C#', 'D', '', 'E', '', 'F#', '', 'G#']
    >>> makeString('Bb', keys.Bb, scales.Major, 1, 0)
    ['Bb', '', 'C', '', 'D', 'Eb', '', 'F', '', 'G', '', 'A']
    >>> makeString('B', keys.B, scales.Major, 1, 0)
    ['B', '', 'C#', '', 'D#', 'E', '', 'F#', '', 'G#', '', 'A#']
    >>> makeString('C', keys.C, chords.Maj7, 1, 0)
    ['C', '', '', '', 'E', '', '', 'G', '', '', 'Bb', '']
    """
    global disp
    global scales
    global keys
    global chords
    global scale
    jj = 0
    str_tmp1 = ['', '', '', '', '', '', '', '', '', '', '', '']
    str_tmp2 = ['', '', '', '', '', '', '', '', '', '', '', '']
    str_tmp3 = ['', '', '', '', '', '', '', '', '', '', '', '']
    str_tmp4 = ['', '', '', '', '', '', '', '', '', '', '', '']
    str_tmp5 = ['', '', '', '', '', '', '', '', '', '', '', '']
    string_l = ['', '', '', '', '', '', '', '', '', '', '', '']
    str_tmp1[0] = stringNote0
    # find location
    i = 0
    j = 0
    while j < 12:
        # print(j, string_l[0], key[j])
        if str_tmp1[0] == key[j]:
            jj = j
        j = j + 1
    j = (jj + capo) % 12
    while i < 12:
        str_tmp1[i] = key[j]
        str_tmp2[i] = disp.Roman[j]
        str_tmp3[i] = disp.Numeric[j]
        str_tmp4[i] = disp.SOLFA_up[j]
        str_tmp5[i] = disp.SOLFA_dn[j]
        if mode[j] == 0:
            str_tmp1[i] = ''
            str_tmp2[i] = ''
            str_tmp3[i] = ''
            str_tmp4[i] = ''
            str_tmp5[i] = ''
        i = i + 1
        j = j + 1
        if j >= 12:
            j = 0
    # print('retVal =', retVal)
    if retVal == 0:
        x = 0
#        string_l = str_tmp1
    if retVal == 1:
        string_l = str_tmp1
    elif retVal == 2:
        string_l = str_tmp2
    elif retVal == 3:
        string_l = str_tmp3
    elif retVal == 4:
        string_l = str_tmp4
    elif retVal == 5:
        string_l = str_tmp5
    else:
        x = 0
    return string_l


def makeFretBoard(r, k, m, c=0, s1='', s2='', s3='', s4='', s5='', s6=''):
    """
    makeFretBoard() populates all strings for an instrument
    r = retval, k = key, m = mode, c = capo, s# = string
    >>> makeFretBoard(2, keys.C, scales.Ionian, 0, 'D', 'C', 'G', 'D')
    4
    >>> makeFretBoard(1, keys.A, scales.Ionian, 2, 'D', 'C', 'G', 'D')
    4
    """
    global keys
    global scales
    global scale
    global one_string
    global capo
    global strings
    global fretNum
    global string1
    global string2
    global string3
    global string4
    global string5
    global string6
    global write2csv

    stringCount = 0
    scale = makeScale(k, m)
    fretNum = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11]
    for i in range(len(fretNum)):
        fretNum[i] = fretNum[i] + c
    if s1 != '':
        string1 = makeString(s1, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string1 = ['', '', '', '', '', '', '', '', '', '', '', '']
    if s2 != '':
        string2 = makeString(s2, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string2 = ['', '', '', '', '', '', '', '', '', '', '', '']
    if s3 != '':
        string3 = makeString(s3, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string3 = ['', '', '', '', '', '', '', '', '', '', '', '']
    if s4 != '':
        string4 = makeString(s4, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string4 = ['', '', '', '', '', '', '', '', '', '', '', '']
    if s5 != '':
        string5 = makeString(s5, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string5 = ['', '', '', '', '', '', '', '', '', '', '', '']
    if s6 != '':
        string6 = makeString(s6, k, m, r, c)
        stringCount = stringCount + 1
    else:
        string6 = ['', '', '', '', '', '', '', '', '', '', '', '']
    return stringCount


def processGui(xc0, xs1, xs2, xs3, xs4, xs5, xs6, xar1, xar2,
               xar3, xar4, xar5):
    """
    processGui: decode GUI output, set defaults and use
    double checks on keys, scales and chords to flag possible
    errors if user adds something to one field and not the other
    """
    showVars = False  # debug
    global write2csv
    global tvar2
    global tvar3
    global tvar4

    # capo
    zc0 = xc0.get()
    if zc0 == 'capo':
        zc0 = 0  # default to 0
    zc0 = int(zc0)

    # strings
    zs1 = xs1.get()
    if zs1 == 's1':
        zs1 = ''
    zs2 = xs2.get()
    if zs2 == 's2':
        zs2 = ''
    zs3 = xs3.get()
    if zs3 == 's3':
        zs3 = ''
    zs4 = xs4.get()
    if zs4 == 's4':
        zs4 = ''
    zs5 = xs5.get()
    if zs5 == 's5':
        zs5 = ''
    zs6 = xs6.get()
    if zs6 == 's6':
        zs6 = ''

    # display
    zar1 = xar1.get()
    zari = 0
    if zar1 == 'display':
        zari = 1  # default notes
    elif zar1 == "notes":
        zari = 1
    elif zar1 == "disp.Roman":
        zari = 2
    elif zar1 == "disp.Numeric":
        zari = 3
    elif zar1 == "disp.SOLFA_up":
        zari = 4
    elif zar1 == "disp.SOLFA_dn":
        zari = 5

    # keys
    zar2 = xar2.get()
    if zar2 == 'key':
        zar2 = 'keys.C'  # default C
    z2save = zar2
    if zar2 == tvar2[0] and 'keys.C' == tvar2[0]:
        zar2 = keys.C
    elif zar2 == tvar2[1] and 'keys.Db' == tvar2[1]:
        zar2 = keys.Db
    elif zar2 == tvar2[2] and 'keys.D' == tvar2[2]:
        zar2 = keys.D
    elif zar2 == tvar2[3] and 'keys.Eb' == tvar2[3]:
        zar2 = keys.Eb
    elif zar2 == tvar2[4] and 'keys.E' == tvar2[4]:
        zar2 = keys.E
    elif zar2 == tvar2[5] and 'keys.F' == tvar2[5]:
        zar2 = keys.F
    elif zar2 == tvar2[6] and 'keys.F#' == tvar2[6]:
        zar2 = keys.Gb
    elif zar2 == tvar2[7] and 'keys.G' == tvar2[7]:
        zar2 = keys.G
    elif zar2 == tvar2[8] and 'keys.Ab' == tvar2[8]:
        zar2 = keys.Ab
    elif zar2 == tvar2[9] and 'keys.A' == tvar2[9]:
        zar2 = keys.A
    elif zar2 == tvar2[10] and 'keys.Bb' == tvar2[10]:
        zar2 = keys.Bb
    elif zar2 == tvar2[11] and 'keys.B' == tvar2[11]:
        zar2 = keys.B

    # scales
    zar3 = xar3.get()
    if zar3 == 'scale':
        zar3 = 'scales.Chromatic'  # default
    z3save = zar3
    if zar3 == tvar3[0] and 'scales.Major' == tvar3[0]:
        zar3 = scales.Major
    elif zar3 == tvar3[1] and 'scales.Ionian' == tvar3[1]:
        zar3 = scales.Ionian
    elif zar3 == tvar3[2] and 'scales.Mixolydian' == tvar3[2]:
        zar3 = scales.Mixolydian
    elif zar3 == tvar3[3] and 'scales.Dorian' == tvar3[3]:
        zar3 = scales.Dorian
    elif zar3 == tvar3[4] and 'scales.natural_minor' == tvar3[4]:
        zar3 = scales.natural_minor
    elif zar3 == tvar3[5] and 'scales.Aeolian' == tvar3[5]:
        zar3 = scales.Aeolian
    elif zar3 == tvar3[6] and 'scales.Phrygian' == tvar3[6]:
        zar3 = scales.Phrygian
    elif zar3 == tvar3[7] and 'scales.Locrian' == tvar3[7]:
        zar3 = scales.Locrian
    elif zar3 == tvar3[8] and 'scales.Lydian' == tvar3[8]:
        zar3 = scales.Lydian
    elif zar3 == tvar3[9] and 'scales.Pent_mode_1' == tvar3[9]:
        zar3 = scales.Pent_mode_1
    elif zar3 == tvar3[10] and 'scales.Pent_mode_2' == tvar3[10]:
        zar3 = scales.Pent_mode_2
    elif zar3 == tvar3[11] and 'scales.Pent_mode_3' == tvar3[11]:
        zar3 = scales.Pent_mode_3
    elif zar3 == tvar3[12] and 'scales.Pent_mode_4' == tvar3[12]:
        zar3 = scales.Pent_mode_4
    elif zar3 == tvar3[13] and 'scales.Pent_mode_5' == tvar3[13]:
        zar3 = scales.Pent_mode_5
    elif zar3 == tvar3[14] and 'scales.Mtn_minor' == tvar3[14]:
        zar3 = scales.Mtn_minor
    elif zar3 == tvar3[15] and 'scales.Harmonic_maj' == tvar3[15]:
        zar3 = scales.Harmonic_maj
    elif zar3 == tvar3[16] and 'scales.Harmonic_min' == tvar3[16]:
        zar3 = scales.Harmonic_min
    elif zar3 == tvar3[17] and 'scales.Chromatic' == tvar3[16]:
        zar3 = scales.Chromatic

    # chords
    zar4 = xar4.get()
    if zar4 == 'chord':
        zar4 = 'chords.Maj'
    z4save = zar4
    if zar4 == tvar4[0] and 'chords.Maj' == tvar4[0]:
        zar4 = chords.Maj
    elif zar4 == tvar4[1] and 'chords.7' == tvar4[1]:
        zar4 = chords.Maj7
    elif zar4 == tvar4[2] and 'chords.M7' == tvar4[2]:
        zar4 = chords.MajM7
    elif zar4 == tvar4[3] and 'chords.m' == tvar4[3]:
        zar4 = chords.m
    elif zar4 == tvar4[4] and 'chords.m7' == tvar4[4]:
        zar4 = chords.m7
    elif zar4 == tvar4[5] and 'chords.mM7' == tvar4[5]:
        zar4 = chords.mM7
    elif zar4 == tvar4[6] and 'chords.aug' == tvar4[6]:
        zar4 = chords.aug
    elif zar4 == tvar4[7] and 'chords.aug7' == tvar4[7]:
        zar4 = chords.aug7
    elif zar4 == tvar4[8] and 'chords.sus2' == tvar4[8]:
        zar4 = chords.sus2
    elif zar4 == tvar4[9] and 'chords.sus4' == tvar4[9]:
        zar4 = chords.sus4
    elif zar4 == tvar4[10] and 'chords.dim' == tvar4[10]:
        zar4 = chords.dim
    elif zar4 == tvar4[11] and 'chords.dim7' == tvar4[11]:
        zar4 = chords.dim7

    zar5 = xar5.get()
    if zar5 == 'Scale or Chord':
        zar5 = 'scale'

    if showVars is True:
        print()
        print(xc0, ' vc0 ', type(zc0), zc0)
        print(xs1, ' vs1 ', type(zs1), zs1)
        print(xs2, ' vs2 ', type(zs2), zs2)
        print(xs3, ' vs3 ', type(zs3), zs3)
        print(xs4, ' vs4 ', type(zs4), zs4)
        print(xs5, ' vs5 ', type(zs5), zs5)
        print(xs6, ' vs6 ', type(zs6), zs6)
        print(xar1, ' var1', type(zar1), zar1)
        print(xar1, ' vari', type(zari), zari)
        if isinstance(zar2, str):
            print(xar2, ' var2', type(zar2), zar2)
        else:
            print(xar2, ' var2', type(zar2), z2save)
        if isinstance(zar3, str):
            print(xar3, ' var3', type(zar3), zar3)
        else:
            print(xar3, ' var3', type(zar3), z3save)
        if isinstance(zar4, str):
            print(xar4, 'var4', type(zar4), zar4)
        else:
            print(xar4, 'var4', type(zar4), z4save)
        print(xar5, 'var5', type(zar5), zar5)
        print()

    #   makeFretBoard(0, keys.C, scales.Ionian, 0, 'D', 'C', 'G', 'D')
    if zar5 == 'scale':
        makeFretBoard(zari, zar2, zar3, zc0, zs1, zs2, zs3, zs4, zs5, zs6)
    else:  # 'chord'
        makeFretBoard(zari, zar2, zar4, zc0, zs1, zs2, zs3, zs4, zs5, zs6)
    print()
    print(fretNum)
    print(string1)
    print(string2)
    print(string3)
    print(string4)
    print(string5)
    print(string6)
    if write2csv is True:
        if zs1 != '':
            fn = open('outfile.csv', 'a')
            fn.write(z2save)
            i = 0
            # fret numbers
            fn.write(',')
            fn.write('T')
            while i < 12:
                fn.write(',')
                fn.write(str(fretNum[i]))
                i = i + 1
            fn.write('\n')
            if zar5 == 'scale':
                fn.write(z3save)
            else:
                fn.write(z4save)
            i = 0
            # string 1
            fn.write(',')
            fn.write(zs1)
            while i < 12:
                fn.write(',')
                fn.write(string1[i])
                i = i + 1
            fn.write('\n')

        if zs2 != '':
            i = 0
            # string 2
            fn.write(',')
            fn.write(zs2)
            while i < 12:
                fn.write(',')
                fn.write(string2[i])
                i = i + 1
            fn.write('\n')

        if zs3 != '':
            i = 0
            # string 3
            fn.write(',')
            fn.write(zs3)
            while i < 12:
                fn.write(',')
                fn.write(string3[i])
                i = i + 1
            fn.write('\n')

        if zs4 != '':
            i = 0
            # string 4
            fn.write(',')
            fn.write(zs4)
            while i < 12:
                fn.write(',')
                fn.write(string4[i])
                i = i + 1
            fn.write('\n')

        if zs5 != '':
            i = 0
            # string 5
            fn.write(',')
            fn.write(zs5)
            while i < 12:
                fn.write(',')
                fn.write(string5[i])
                i = i + 1
            fn.write('\n')

        if zs6 != '':
            i = 0
            # string 6
            fn.write(',')
            fn.write(zs6)
            while i < 12:
                fn.write(',')
                fn.write(string6[i])
                i = i + 1
            fn.write('\n')

        fn.write('\n')
        fn.close()
        print('Wrote results to outfile.csv')
    else:
        print('For formatted fretboad enable .csv save')


"""
    main starts here with GUI processing which uses the functions above
    to do the actual calculations. Future update might put the output in
    the GUI box but that is not a primary objective.
"""
root = Tk()
root.title('fretboardMaps.py v0.01')
root.geometry("300x300")

vc0 = StringVar(root)
vc0.set('capo')
vci = 0

vs1 = StringVar(root)
vs1.set('s1')

vs2 = StringVar(root)
vs2.set('s2')

vs3 = StringVar(root)
vs3.set('s3')

vs4 = StringVar(root)
vs4.set('s4')

vs5 = StringVar(root)
vs5.set('s5')

vs6 = StringVar(root)
vs6.set('s6')

var1 = StringVar(root)
var1.set('display')
var1i = 0

var2 = StringVar(root)
var2.set('key')

var3 = StringVar(root)
var3.set('scale')

var4 = StringVar(root)
var4.set('chord')

var5 = StringVar(root)
var5.set('Scale or Chord')

var6 = StringVar(root)
var6.set('action')

r2f = False


def g_get_capo(event):
    """
    g_get_capo fetches the capo number entry from the GUI
    """
    global xc0
    chosen_option = vc0.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("capo", chosen_option)


def g_get_s1(event):
    """
    g_get_s1 fetches the string # 1 number entry from the GUI
    """
    chosen_option = vs1.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string1", chosen_option)


def g_get_s2(event):
    """
    g_get_s2 fetches the string # 2 number entry from the GUI
    """
    chosen_option = vs2.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string2", chosen_option)


def g_get_s3(event):
    """
    g_get_s3 fetches the string # 3 number entry from the GUI
    """
    chosen_option = vs3.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string3", chosen_option)


def g_get_s4(event):
    """
    g_get_s4 fetches the string # 4 number entry from the GUI
    """
    chosen_option = vs4.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string4", chosen_option)


def g_get_s5(event):
    """
    g_get_s5 fetches the string # 5 number entry from the GUI
    """
    chosen_option = vs5.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string5", chosen_option)


def g_get_s6(event):
    """
    g_get_s6 fetches the string # 6 number entry from the GUI
    """
    chosen_option = vs6.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("string6", chosen_option)


def g_get_disp(event):
    """
    g_get_disp fetches the display mode entry from the GUI
    """
    chosen_option = var1.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("disp", chosen_option)


def g_get_key(event):
    """
    g_get_key fetches the key entry from the GUI
    """
    chosen_option = var2.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("key", chosen_option)


def g_get_scale(event):
    """
    g_get_scale fetches the scale type entry from the GUI
    """
    chosen_option = var3.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("scale", chosen_option)


def g_get_chord(event):
    """
    g_get_chord fetches the chord type entry from the GUI
    """
    chosen_option = var4.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("chord", chosen_option)


def g_get_outType(event):
    """
    g_get_outType fetches choice of scale or chord the GUI
    """
    chosen_option = var5.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=20, column=1)
    #  print("outType", chosen_option)


def calcCallBack():
    processGui(vc0, vs1, vs2, vs3, vs4, vs5, vs6, var1, var2, var3, var4, var5)


def helpCallBack():
    helpFBM()


def selwf():
    global write2csv
    selection = str(var.get())
    label.config(text=selection)
    if int(selection) == 1:
        write2csv = True
    else:
        write2csv = False
    #  print(selection, write2csv)


drop_menuC0 = OptionMenu(root, vc0, tcapo[0], tcapo[1], tcapo[2],
                         tcapo[3], tcapo[4], tcapo[5], tcapo[6],
                         tcapo[7], tcapo[8], tcapo[9], tcapo[10],
                         tcapo[11], command=g_get_capo)
drop_menuC0.grid(row=3, column=2)

drop_menus6 = OptionMenu(root, vs6, tvarS6[0], tvarS6[1], tvarS6[2],
                         tvarS6[3], tvarS6[4], tvarS6[5], tvarS6[6],
                         tvarS6[7], tvarS6[8], tvarS6[9], tvarS6[10],
                         tvarS6[11], tvarS6[12], command=g_get_s6)
drop_menus6.grid(row=15, column=2)

drop_menus5 = OptionMenu(root, vs5, tvarS5[0], tvarS5[1], tvarS5[2],
                         tvarS5[3], tvarS5[4], tvarS5[5], tvarS5[6],
                         tvarS5[7], tvarS5[8], tvarS5[9], tvarS5[10],
                         tvarS5[11], tvarS5[12], command=g_get_s5)
drop_menus5.grid(row=13, column=2)

drop_menus4 = OptionMenu(root, vs4, tvarS4[0], tvarS4[1], tvarS4[2],
                         tvarS4[3], tvarS4[4], tvarS4[5], tvarS4[6],
                         tvarS4[7], tvarS4[8], tvarS4[9], tvarS4[10],
                         tvarS4[11], tvarS4[12], command=g_get_s4)
drop_menus4.grid(row=11, column=2)

drop_menus3 = OptionMenu(root, vs3, tvarS3[0], tvarS3[1], tvarS3[2],
                         tvarS3[3], tvarS3[4], tvarS3[5], tvarS3[6],
                         tvarS3[7], tvarS3[8], tvarS3[9], tvarS3[10],
                         tvarS3[11], tvarS3[12], command=g_get_s3)
drop_menus3.grid(row=9, column=2)

drop_menus2 = OptionMenu(root, vs2, tvarS2[0], tvarS2[1], tvarS2[2],
                         tvarS2[3], tvarS2[4], tvarS2[5], tvarS2[6],
                         tvarS2[7], tvarS2[8], tvarS2[9], tvarS2[10],
                         tvarS3[11], tvarS3[12], command=g_get_s2)
drop_menus2.grid(row=7, column=2)

drop_menus1 = OptionMenu(root, vs1, tvarS1[0], tvarS1[1], tvarS1[2],
                         tvarS1[3], tvarS1[4], tvarS1[5], tvarS1[6],
                         tvarS1[7], tvarS1[8], tvarS1[9], tvarS1[10],
                         tvarS1[11], tvarS1[12], command=g_get_s1)
drop_menus1.grid(row=5, column=2)

drop_menu1 = OptionMenu(root, var1, tvar1[0], tvar1[1], tvar1[2], tvar1[3],
                        tvar1[4],
                        command=g_get_disp)
drop_menu1.grid(row=3, column=1)

drop_menu2 = OptionMenu(root, var2, tvar2[0], tvar2[1], tvar2[2], tvar2[3],
                        tvar2[4], tvar2[5], tvar2[6], tvar2[7],
                        tvar2[8], tvar2[9], tvar2[10], tvar2[11],
                        command=g_get_key)
drop_menu2.grid(row=5, column=1)

drop_menu3 = OptionMenu(root, var3, tvar3[0], tvar3[1], tvar3[2], tvar3[3],
                        tvar3[4], tvar3[5], tvar3[6], tvar3[7],
                        tvar3[8], tvar3[9], tvar3[10], tvar3[11],
                        tvar3[12], tvar3[13], tvar3[14], tvar3[15],
                        tvar3[16], tvar3[17], command=g_get_scale)
drop_menu3.grid(row=7, column=1)


drop_menu4 = OptionMenu(root, var4, tvar4[0], tvar4[1], tvar4[2], tvar4[3],
                        tvar4[4], tvar4[5], tvar4[6], tvar4[7], tvar4[8],
                        tvar4[9], tvar4[10], tvar4[11],
                        command=g_get_chord)
drop_menu4.grid(row=9, column=1)

drop_menu5 = OptionMenu(root, var5, tvar5[0], tvar5[1],
                        command=g_get_outType)
drop_menu5.grid(row=11, column=1)

B1 = Button(root, text="calculate", command=calcCallBack)
B1.grid(row=13, column=1)

B2 = Button(root, text="quit", command=root.destroy)
B2.grid(row=15, column=1)

B3 = Button(root, text="Help", command=helpCallBack)
B3.grid(row=3, column=3)

var = IntVar()
R1 = Radiobutton(root, text="Write csv", variable=var, value=1,
                 command=selwf)
R1.grid(row=16, column=1)

R2 = Radiobutton(root, text="No write csv", variable=var, value=0,
                 command=selwf)
R2.grid(row=16, column=2)
label = Label(root)
label.pack

print('')
print('fretboardMaps.py maps fretboard for 1 thru 6 string instruments.')
print('v0.01 Copyright (C) 2020 David Murray')
print()
print('This program is free software: you can redistribute it and/or modify')
print('it under the terms of the GNU General Public License as published by')
print('the Free Software Foundation, either version 3 of the License, or')
print('(at your option) any later version.')
print()
print('This program is distributed in the hope that it will be useful,')
print('but WITHOUT ANY WARRANTY; without even the implied warranty of')
print('MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the')
print('GNU General Public License for more details.')
print()
print('You should have received a copy of the GNU General Public License')
print('along with this program.  If not, see <https://www.gnu.org/licenses/>.')
print()

root.mainloop()


#  python -m doctest -v fretboardMaps.py
#  or
#  python -m doctest fretboardMaps.py
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#  python -m pydoc fretboardMaps
if __name__ == "__main__":
    import pydoc

#  pycodestyle fretboardMaps.py
#  to check for pep8 + compliance after updates
