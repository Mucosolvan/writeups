After connecting we're welcomed by this:
```

                    +++     3DSCTF - MAZEREAPER     +++

 [+] After being captured by the Grim Reaper, you were taken to a secret reaping
     room for the secret games of death.

                                      ...
                                    ;::::;
                                  ;::::; :;
                                ;:::::'   :;
                               ;:::::;     ;.
                              ,:::::'       ;           OOO
                              ::::::;       ;          OOOOO
                              ;:::::;       ;         OOOOOOOO
                             ,;::::::;     ;'         / OOOOOOO
                           ;:::::::::`. ,,,;.        /  / DOOOOOO
                         .';:::::::::::::::::;,     /  /     DOOOO
                        ,::::::;::::::;;;;::::;,   /  /        DOOO
                       ;`::::::`'::::::;;;::::: ,#/  /          DOOO
                       :`:::::::`;::::::;;::: ;::#  /            DOOO
                       ::`:::::::`;:::::::: ;::::# /              DOO
                       `:`:::::::`;:::::: ;::::::#/               DOO
                        :::`:::::::`;; ;:::::::::##                DO
                        ::::`:::::::`;::::::::;:::#                DO
                        `:::::`::::::::::::;'`:;::#                D
                         `:::::`::::::::;' /  / `:#
                          ::::::`:::::;'  /  /   `#

 [+] As The Death loves to play with its victims, it loosed you at the
     beginning of a maze with a map and said: "There are keys and doors
     scattered around the labyrinth.The distance between each connected room is
     unitary. number of hits possible, I will not take your soul and I will set
     you free. "

 [+] Since she released you, you have highlighted the following
     information on the map:
     - A line with four values: number of rooms (nr), number of corridors
       between rooms (NC), number of keys (NK), number of doors (ND).
     - A line with the position that The Death left you (SP) and the place of
       the exit (EP).
     - A list of NC corridors between two rooms.
     - A list of NK with key locations (lower case).
     - And a list ND with the doors (capital letters) that need keys.

 [+] Example:
                                          +-+
                                          | |
                          +---------------+-+
+-+--------+           +--+
| |        |           |SP|        +----------------+--+
+-+        |           +--+        |                |EP|
           +-+---------+  +------+-+                +--+
           |a|                   |A|                |
           +-+                   +-+                |
                                   |                |
                                   +------+-+-------+
                                          | |
                                          +-+

 [+] For the example the answer is 4.

 [+] Sometimes The Reaper plays with no escape mazes. If this occurs,
     answer with -1.

 [+] Type 'start' for try to runaway:
```

To simplify the challenge, we're given a graph with `nr` vertices and `nc` edges. Furthermore, in some vertices we can find keys (represented by lowercase letters), and some vertices are blocked by doors (represented by capital letters). We can only open a door (visit vertex) after we collect all keys needed (`a` key opens `A` doors, `b` key - `B` doors and so on).

This is a simple graph problem, we can solve it using modified BFS. In our state, instead of just information if the vertex was visited, we need to remember which keys we currently have. Maximum number of states we have is given by `NR * 2^NK`. In the problem maximal number of rooms was something close to 150-200, and number of keys to 20.

Here is a [script](./script.py) that solves this task, it could be made faster but it worked, so... :D 

Flag is `3DS{br4vElY_Fac3_th3_$oUL_r3Ap3R}`.
