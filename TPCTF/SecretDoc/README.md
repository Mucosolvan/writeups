```you found this strange string on the floor """1rMrhv9mEAWBU99vE0QIIBN6qavpGvkczWDsiMtJRf3Y"""```
There was also a hint, that `Google has something to do with it`

I've spent way too much time figuring out the first part of this task. We're given a `strange string` in a Python comment, which is commonly used as a documentation string.
At first, I tried googling that string, to maybe find out if it's hidden somewhere on an abandoned Github page? Nope, not this way.
But after googling, I've found that this string may represent something called `ei value` in Google searches. I fixated for some time on that, because of the hint. But this wasn't the solution either.

So, what is the solution? It is a part of a Google docs [link](https://docs.google.com/document/d/1rMrhv9mEAWBU99vE0QIIBN6qavpGvkczWDsiMtJRf3Y/edit)!
We're greeted with white `lol no flag here` on black background. But after selecting all what is on the picture we see hidden, black text.

```
I tried to write some code but my keyboard is broken
//four ops
var add = function(a,b){return a+b;};
 ar sub = function(a,b){return a-b;};
var mul = function(a,b){return a*b;};
var div = function(a,b){return a/b;};
function str(a){return a toString();};
REGEXMATCH=(g,h)=> .test(h);
function mo (a,b){return a%b} / who needs semico ons
console.log(String.fromCharCode(+REGEXMAT H(/abc/,"qabcd")*79)) // THE QUICK BROWN FOX JU PS OVER THE LAZY DOGS
console.log(String.fromCharCode(+REGEXMATCH(/abc/,"abcd")*mul(6,8))) // the quick brown fox  umps over the lazy dogs
```

We see that some characters are missing, exactly `v` from `var`, `.` from `a.toString()`, `g` from `g.test(h)`, `d` from `mod`, `/` from a comment, `l` from semicolons, `C` from `REGEXMATCH`, 
`M` from a comment, and, last, but not least, `j` from `jumps`. After fixing the [code](./script.js) it outputs `O` and `0`. 

Let's merge all those characters together, to get `v.gd/lCOM0j`, which is a broken link, but it led to [here](https://hexed.it/#base64+lzjb:AIlQTkcNChoKAAAAAA1JSERSAAAABIAAAAKIhAgCABKHSRZaAAcAAXNSR0IArs4EHOkADQRnQU1BAAAAsY8L/GEFAQAQCXBIWXMAAAQOwwQEAcdvqGQAAAAKD0lEQVQAeF7t28F24jAADAVQZub/v5kAmsioqpNAUigAHeDehZFkx1kYvwMcAECIA97TnwCzqGM4mM/XTgA2udWKoW7qPADWUOswnfrUpwEAQM+rZpuNOWcACkQnvS/6xrQAFWtYrOuxeiAAzCe7DG8BAAAA+CF/++c2LaIA1JSSbRaD4/EAmGueiSK3cpgAa5hPmmxbEaIAbYb2Rw0vetgAewEAgKe2L4AAtbwUwWnNxigAUi+Juq5hcTIAtL2a3lvbuTsAZqS4Ki/MdpggLIpjTe8AWLbLACxxNVTUkxcOAMdu0/tJbaOuAGsa2qptpT46AOvTsz5dl2eiQBjaWqy5egCieABJ//rnbbYkigD7po52W14YdQAT7aK2G1+RXQA4lmcGwyPZRoBRd+eTRVcPACsAL2nfTxDXtNwAshhdqqsHdpkAv7FOWsKpYhgAhqc26hfdEJwEbnwBNngB9wlgAL+rRq8Qk9SnAJMIQlXfuGjxAJ5endXJdPGXALZXAADAG3viAAC2K9VkfIooAJViGKKdotOnANgaxHx4vBkmAPXx08vK7trNAQBtrDqltEnvS0C4qkWobdQAEHwAX+SrpvdnOZkCbwDg7+AV/gP2QH8afnAodAAP/AACYQwAAN6TbwLAACkeRAB7NF/+fwAXAA38A/xC/EL8QvxC//xC/EL8QvxC/EL8QvxC/EL//EL8QvxC/EL8QvxC/EL8Qv/8QvxC/EL8QvxC/EL8QvxCA/xC/EIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK/vcPgAOg4AjnxzEl0bAAAAAABJRU5ErkIAYII=).

In the link we find a Base64 encoded image: !(image)[image.png]. Let's look at it using [Stegsolve](https://github.com/eugenekolo/sec-tools/blob/master/stego/stegsolve/stegsolve/stegsolve.jar). After looking at the picture in blue plane we get !(image2)[solved.png].


So, the flag is `tpctf{fl4g5_r_4_n00bs}`.
