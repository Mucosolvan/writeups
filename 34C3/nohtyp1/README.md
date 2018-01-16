In this easy RE challenge we're given a Python script: [snakes](./original.py) and a hint

```
$ cat flag | md5sum

5a76c600c2ca0f179b643a4fcd4bc7ac
```

The first thing to do is of course, deobfuscate the script to make it [human-readable](./script.py). 
We need to add newlines, change variables from series of `_` to normal names, change hex values to decimal ones, and reverse list given in script to simplify the program.

And voila: 
```
inp = input()
add = lambda y, z: y + (z ^ 21);
results = {
	False:lambda:print('Almost!!'),
	True:lambda:print('Correct!')
}

revList = [160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162][::-1]

results[
 [add(*element)
  for element in zip(list(map(ord,inp)), list(map(ord,inp))[::-1])] == revList
  and 'mo4r' in inp and '34C3_' in inp and inp.split('_')[3] == 'tzzzz']()
```

So, what does our script do? First it reads input, then we have a helper function, a dictonary that probably will tell us if we're correct or not, and a reverse list containing.. Containing what exactly? Let's see the most interesting part of a script:

```
results[
 [add(*element) for element in zip(list(map(ord,inp)), list(map(ord,inp))[::-1])] == revList
  and 'mo4r' in inp and '34C3_' in inp and inp.split('_')[3] == 'tzzzz']()
```

Let's boil it down:
`results[expr]()` - we're calling a lambda function from our dictionary, so if `expr == True` we get `Correct!`, which is exactly what we want.

`and 'mo4r' in inp and '34C3_' in inp and inp.split('_')[3] == 'tzzzz'` - if our input contains `mo4r`, `34C3`, we have at least 3 underscores in our string, and part between third `_` and fourth `_` or end of the word is equal to `tzzzz`, this expression holds true.

`add(*element) for element in zip(list(map(ord,inp)), list(map(ord,inp))[::-1])` - `list(map(ord, inp))` maps input characters into their ASCII values and makes a list of those, `zip()` zips a list of those ASCII values with the same list, but reversed, and then we call `add`. So essentially, we pair first character with the last one, second with the penultimate, and so on, call `add`, and compare results with `revList`.

So, we just need to prepare a string that satisfies all those criteria. To do that, the ability to reverse `add` is pretty useful.

```
def reverse(value, char):
	value -= ord(char)
	value ^= 21
	return chr(value)
```
Firstly, we know that our flag will begin with `34C3_`. Using `reverse` we can deduce last 5 characters of the flag, which are `tzzzz`.
That means we know one more character - before `tzzzz` we need an underscore, so using that we can get next character from the beginning, which is `m`. That leads us to a guess, since we need to fit `mo4r` into our string, let's do it right now, and add `_` after. Once again, decoding characters from the end gives us this part of flag: `34C3_mo4r_****4kes_tzzzz`. 

Right now we can either bruteforce last 4 characters and check the md5sum, or bruteforce and see if it makes sense in leet speak :D I've done the latter, and our flag is `34C3_mo4r_schn4kes_tzzzz`.


