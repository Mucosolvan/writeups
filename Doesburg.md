After downloading a file from the link we see a pretty picture: ![](original_piet.png?raw=true)

Trying typical stegano methods (LSB, pallettes, watching hex) we get no new information.
Let's use the task name then! After googling Doesburg we are greeted with a wikipedia page of a Dutch painter, who created something called `De Stijl`.
Since we are looking for his friends, let's try looking for painters from this group. The first one mentioned is `Piet Mondriaan`.
Lo and behold, there is ano esoteric language named after our painter, called simply `Piet`.

[Piet interpreter](https://www.bertnase.de/npiet)

Some needed things about how Piet works:
1. Colors are not important, transitions between them are.
2. White color is just a noop.
3. Black color restricts the flow of a program (nothing can get through)
4. Interpreting starts from top-left corner and goes right.

After interpreting the original image with `npiet original_piet.png` we are prompted for input and then program seems to loop indefinitely.
Luckily, our interpret has some neat options like `-t`, which shows stack values and operations in order, or `-e n` which stops the program after n steps.

Using that we can see that, indeed, our program loops forever, our input is popped from stack immediately after we enter it, and stack values are `87 82 79 78 71`.
`87 82 79 78 71` = WRONG in ASCII, so we are suggested that, it is not the correct execution.

But there is so much more code in this picture we don't even reach! Let's change this picture, shall we?

As I said before, interpreting starts from top-left codel(pixel) and goes to the right. Next block is black, which redirects our control flow downwards. After that we insert things on the stack, get our input, disregard it and loop indefinitely in white area in the middle. But behind this top-left black codel there is a huge part along the borders. We can change black codel to a white one (noop) to get to this part: ![](piet.png?raw=true)
