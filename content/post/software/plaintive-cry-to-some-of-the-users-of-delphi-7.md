---
date: "2009-04-21"
tags: ["delphi", "rants"]
title: "Next in the series of plaintive Delphi cries, one to (some of) the users of Delphi"
---

To many of the Delphi developers I have encountered:

Please memorise the following: **Format**

Compare:

<code>
Message := 'There are ' + IntToStr(numBunnies) + ' bunnies in the forest.' + #13 + 'That comes to ' + FloatToStrF(bunnyDensity, ffFixed, 4, 2) + 'bunnies per acre.';
</code>

vs

<code>
Message := Format('There are %d bunnies in the forest.%cThat comes to %2.2f bunnies per acre.',[numBunnies, #13, bunnyDensity]);
</code>

See how much prettier that is? Please start using it. I beg of you.

Also, consider:

<code>
function FunctionNamedFoo: Boolean;
</code>

a function which returns a value. You can either place the return value of the function into the keyword variable *Result* or into the locally-scoped variable *FunctionNamedFoo*. As you write more and more functions, please decide on the style you prefer and stick to it. Please.

I personally prefer the FunctionNamedFoo approach, since it makes searching the source code much easier. My despair on this issue is however so great that I no longer care which you choose, as long as you choose but **one**.

**Delphi developers I have encountered**: Thank you for listening.

**Everyone else**: My apologies. I do feel better now though.
