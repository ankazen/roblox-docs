# Lua Style Guide 
Time:<em></em>

These rules are recommended, but do not need to be followed, are not arbitrary and **should in no way be considered as a reference**. These rules are only presentational, and so do not have to be followed for code to work, but they _might_ make code easier to read, write, and debug.

## Whitespace Rules

### Indentation

Each level of block should be indented by a single tab.
    
    
    local var = 10
    if var > 0 do
    	-- new block
    	for i = 1, var do
    		-- new block
    		print(i)
    		-- end block
    	end
    	-- end block
    end
    

### Expressions

Spaces are optional around `*` and `^/`. If there is one after, always put one before, and vice versa. Always include spaces before and after `=`, and all the other binary operators. Unary operators, such as `-a` and `!#a` should not have a space between the operator and the operand.  
Right:
    
    
    local a = (b + #t)*c
    local b = -a + 3*(c - a) / 2
    print(b == a)
    

Wrong:
    
    
    local a =(b+c)* d
    local b= -a+3*(c-a)/2
    print(b==a)
    

### Table Commas

Never put a space before a comma, but multiple spaces may come after. Make sure spacing is consistent. If the table is put on a single line, the comma after the last entry can usually be omitted.

Good:
    
    
    local data = {1,2,3}
    local data = {1, 2, 3}
    local data = { 1, 2, 3 }
    local data = {
    	1,
    	2,
    	3,
    }
    

Not good:
    
    
    local data = {1 ,2 ,3}
    local data = {	1  , 2,   3,} -- oh god what are you doing
    

Since tables accept either commas or semi-colons as separators, use semi-colons at the end of a line instead of commas.
    
    
    local data = {
    	1, 2, 3;
    	4, 5, 6;
    	7, 8, 9;
    }
    

## Line wrapping

### Function Calls

Say you have this function call, and you want to line-wrap it at the 1.
    
    
    local var = foo(aPart, anotherPart, 1, 5, 8, a, b, c, d)
    

The first option is to bring all the arguments to the next line, indent them one level (with a tab), and then wrap them. The close parenthesis should go on the following line:
    
    
    local var = foo(
    	aPart, anotherPart, 1,
    	5, 8, a, b, c, d
    )
    

The second option is to align the arguments by column. Note that this option, however, will be misinterpreted by many programming editors. This should be done with spaces, not tabs:
    
    
    local var = foo(aPart, anotherPart, 1,
                        5, 8, a, b, c, d)
    

### Nested function calls

The following function call
    
    
    local var = foo(bar(a, b, c, d, e, f), baz(z, y, x, w, v))
    

Could be line wrapped to one of
    
    
    local var = foo(
    	bar(
    		a, b, c,
    		d, e, f
    	),
    	baz(
    		z, y, x,
    		w, v
    	)
    )
    

or
    
    
    local var = foo(bar(a, b, c,
                            d, e, f),
                        baz(z, y, x,
                            w, v))
    

#### Table literals

Treat these in the same way as function calls.
    
    
    local my_table = {
    	a = "potato";
    	b = "Taco!";
    	c = 3.1416;
    	new = {
    		reaction = "yay!";
    	};
    }
    

## Semicolons

Besides seperating values in a table, semicolons (`;`) are used to denote the end of a statement. They are not required, but can solve some [Whitespace Ambiguities](Whitespace#Ambiguities).

Places to use semicolons:
    
    
    local assignment = "value";	-- after assignments
    print("here");	-- after function calls
    return;	-- at the end of **break** or **return**
    

Places to NOT use semicolons:
    
    
    for i = 1; 10 do end -- in loops
    do; end	-- after "do", this includes loops
    if (not true) then; end	-- after "then"
    print("first"; "second");	-- in function calls
    

## Scope

Variables and functions defined without the `local` keyword are global by default. Local variables are stored in the Lua registers, and are limited in scope to the block wherein they are declared. Local variables should almost always be preferred to global variables, as noted in [section 4.2 of **Programming in Lua**](http://www.lua.org/pil/4.2.html):

It is good programming style to use local variables whenever possible. Local variables help you avoid cluttering the global environment with unnecessary names. Moreover, the access to local variables is faster than to global ones.

Variables should usually be declared as late as possible. If a block itself contains many blocks (say, if a conditional statement contains many for loops), variables should be declared before the first block that uses them. If a bug in the code later is found related to this variable, it will be possible to know immediately that the variable is not used before the place where it is declared. Shortening the scope of the variable (it can only be used after it is declared) greatly increases readability.

A useful trick is to use the `do` statement to create a new block with no other purpose than creating a new scope. If a variable is only useful for a function, `bar` in the example below, the variable and function can be defined in a block created by a `do` statement so that the variable only exists in that function’s environment. This too increases readability, since people reading the code will know for sure the variable is not used anywhere outside of the function. Here’s an example:
    
    
    local bar
    do
    	local foo = {5, 4, 3}
    	function bar(quux)
    		foo[#foo + 1] = quux
    		return foo
    	end
    end
    
    bar(2)
    

In the example above, the variable `foo` can only be accessed from the function `bar` since the scope of `foo` ends once the block introduced by the `do` statement is over. Even though `foo` is out of scope after this block, `bar` retains access to `foo` as an upvalue and can used `foo` normally.

## See also

  * [Lua Style Guide](http://lua-users.org/wiki/LuaStyleGuide)



***__Roblox官方链接__:[Lua Style Guide](https://developer.roblox.com/zh-cn/articles/Lua-Style-Guide)