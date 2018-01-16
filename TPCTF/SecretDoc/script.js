//four ops
var add = function(a,b){return a+b;};
var sub = function(a,b){return a-b;};
var mul = function(a,b){return a*b;};
var div = function(a,b){return a/b;};
function str(a){return a.toString();};
REGEXMATCH=(g,h)=>g.test(h);
function mod (a,b){return a%b} // who needs semicolons
console.log(String.fromCharCode(+REGEXMATCH(/abc/,"qabcd")*79)) // THE QUICK BROWN FOX JUMPS OVER THE LAZY DOGS
console.log(String.fromCharCode(+REGEXMATCH(/abc/,"abcd")*mul(6,8))) // the quick brown fox jumps over the lazy dogs

