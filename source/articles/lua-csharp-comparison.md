# Lua / C# Comparison 
Time:<em></em>

This article is a general overview of the Lua programming language and how its syntax compares to C#.

## General Differences

### Comments

#### Lua
    
    
    -- Single line comment
    
    --[[
    	Block comment
    --]]
    

#### C#
    
    
    // Single line comment
    
    /*
    	Block comment
    */
    

### Strings

#### Lua
    
    
    -- Multi-line string
    [[This is a string that,
    when printed, will appear
    on multiple lines]]
    
    
    
    -- Concatenation
    s1 = "This is a string "
    s2 = "made with two parts."
    endString = s1 .. s2
    

#### C#
    
    
    // Multi-line string
    "This is a string that,\nwhen printed, will appear\n on multiple lines."
    
    
    
    // Concatenation
    string s1 = "This is a string ";
    string s2 = "made with two parts.";
    string endString = s1 + s2;
    

### Conditional Operators

Lua C#

**Equal To**
`==`
`==`

**Greater Than**
`>`
`>`

**Less Than**
`<`
`<`

**Greater Than or Equal To**
`>=`
`>=`

**Less Than or Equal To**
`<=`
`<=`

**Not Equal To**
`~=`
`!=`

**And**
`and`
`&&`

**Or**
`or`
`&vert;&vert;`

### Arithmetic Operators

Lua C#

**Addition**
`+`
`+`

**Subtraction**
`-`
`-`

**Multiplication**
`*`
`*`

**Division**
`/`
`/`

**Modulus**
`%`
`%`

**Exponentiation**
`^`
`**`

### Reserved Keywords

Below are Lua’s reserved keywords mapped to their C# equivalent. Not all C# keywords are shown.

Lua C#

`and`

`break`
`break`

`do`
`do`

`if`
`if`

`else`
`else`

`elseif`
`else if`

`then`

`end`

`true`
`true`

`false`
`false`

`for`
`for` / `foreach`

`function`

`in`
`in`

`local`

`nil`
`null`

`not`

`or`

`repeat`

`return`
`return`

`until`

`while`
`while`

### Line Endings

Semicolons are **not** required in Lua, but they will work if used in your code.

### Scoping

In Lua, variables and logic can be written in a tighter scope than their function or class by nesting the logic within `do` and `end` keywords, similar to nesting it within curly brackets `{}` in C#. For more details on scope in Lua, please see the `/articles/Scope|Scope` article.

#### Lua
    
    
    local example = "Example text"
    
    do
    	example = example .. " changed!"
    	print(example)  -- Outputs 'Example text changed!'
    end
    
    print(example)  -- Outputs 'Example text'
    

#### C#
    
    
    string example = "Example text";
    
    {
    	example += " changed!";
    	Console.WriteLine(example);  // Outputs 'Example text changed!'
    }
    
    Console.WriteLine(example);  // Outputs 'Example text'
    

### Variables

In Lua, variables do **not** specify their type when being declared/defined. Also, Lua variables do not have access modifiers, although you may prefix “private” variables with an underscore for readability.

#### Lua
    
    
    local variableName = "value"
    
    
    
    -- "Public" declaration
    local variableName
    
    -- "Private" declaration
    local _variableName
    

#### C#
    
    
    string variableName = "value";
    
    
    
    // Public declaration
    public string variableName
    
    // Private declaration
    string variableName;
    

* * *

## Loops

### For Loops

#### Lua
    
    
    -- Forward loop
    for i = 1, 10 do
    	doSomething()
    end
    
    
    
    -- Reverse loop
    for i = 10, 1, -1 do
    	doSomething()
    end
    

#### C#
    
    
    // Forward loop
    for (int i = 1; i <= 10; i++) {
    	doSomething();
    }
    
    
    
    // Reverse loop
    for (int i = 10; i >= 1; i--) {
    	doSomething();
    }
    

### While Loops

#### Lua
    
    
    while boolExpression do
    	doSomething()
    end
    
    
    
    repeat
    	doSomething()
    until not boolExpression
    

#### C#
    
    
    while (boolExpression) {
    	doSomething();
    }
    
    
    
    do {
    	doSomething();
    } while (boolExpression)
    

### For Each Loops

#### Lua
    
    
    local abcList = {"a", "b", "c"}
    
    for i, v in ipairs(abcList) do
    	print(v)
    end
    
    
    
    local abcDictionary = { a=1, b=2, c=3 }
    
    for k, v in pairs(abcDictionary) do
    	print(k, v)
    end
    

#### C#
    
    
    List abcList = new List{"a", "b", "c"};
    
    foreach (string v in abcList) {
    	Console.WriteLine(v);
    }
    
    
    
    Dictionary abcDictionary = new Dictionary
    { {"a", 1}, {"b", 2}, {"c", 3} };
    
    foreach (KeyValuePair entry in abcDictionary) {
    	Console.WriteLine(entry.Key + " " + entry.Value);
    }
    

* * *

## Conditional Statements

#### Lua
    
    
    -- One condition
    if boolExpression then
    	doSomething()
    end
    
    -- Multiple conditions
    if not boolExpression then
    	doSomething()
    elseif otherBoolExpression then
    	doSomething()
    else
    	doSomething()
    end
    

#### C#
    
    
    // One condition
    if (boolExpression) {
    	doSomething();
    }
    
    // Multiple conditions
    if (!boolExpression) {
    	doSomething();
    }
    else if (otherBoolExpression) {
    	doSomething();
    }
    else {
    	doSomething();
    }
    

### Ternary Operations

Lua does not offer a direct equivalent to the C ternary operator `a?b:c`. However, the Lua idiom `(a and b) or c` offers a close approximation, provided `b` is not false.

#### Lua
    
    
    local max = (x>y and x) or y
    

#### C#
    
    
    int max = (x>y) ? x: y;
    

* * *

## Functions

Be sure to read our article on `articles/Understanding Functions in Roblox|Functions` to get a deeper understanding of Lua functions.

### Generic Functions

#### Lua
    
    
    -- Generic function
    local function increment(number)
    	return number + 1
    end
    

#### C#
    
    
    // Generic function
    int increment(int number) {
    	return number + 1;
    }
    

### Variable Argument Number

#### Lua
    
    
    -- Variable argument number
    local function variableArguments(...)
    	print(...)
    end
    

#### C#
    
    
    // Variable argument number
    void variableArguments(params string[] inventoryItems) {
    	for (item in inventoryItems) {
    		Console.WriteLine(item);
    	}
    }
    

### Named Arguments

#### Lua
    
    
    -- Named arguments
    local function namedArguments(args)
    	return args.name .. "'s birthday: " .. args.dob
    end
    
    namedArguments{name="Bob", dob="4/1/2000"}
    

#### C#
    
    
    // Named arguments
    string namedArguments(string name, string dob) {
    	return name + "'s birthday: " + dob;
    }
    
    namedArguments(name: "Bob", dob: "4/1/2000");
    

* * *

## Try/Catch Structures

#### Lua
    
    
    local function fireWeapon()
    	if not weaponEquipped then
    		error("No weapon equipped!")
    	end
    	-- Proceed...
    end
    
    local success, errorMessage = pcall(fireWeapon)
    if not success then
    	print(errorMessage)
    end
    

#### C#
    
    
    void fireWeapon() {
    	if (!weaponEquipped) {
    		// Use a user-defined exception
    		throw new InvalidWeaponException("No weapon equipped!");
    	}
    	// Proceed...
    }
    
    try {
    	fireWeapon();
    } catch (InvalidWeaponException ex) {
    	// An error was raised
    }
    

* * *

## Tables

Be sure to read the `articles/Table|Tables` article to get a deeper understanding on how you can use tables in Lua.

### Dictionary Tables

Tables in Lua can be used just like Dictionaries in C#.

#### Lua
    
    
    local dictionary = {
    	val1 = "this",
    	val2 = "is"
    }
    
    print(dictionary.val1)  -- Outputs 'this'
    print(dictionary[val1])  -- Outputs 'this'
    
    dictionary.val1 = nil  -- Removes 'val1' from table
    table.remove(dictionary, 1)  -- Also removes 'val1' from table
    
    dictionary["val3"] = "a dictionary"  -- Overwrites 'val3' or sets new key-value pair
    

#### C#
    
    
    Dictionary dictionary = new Dictionary()
    {
    	{ "val1", "this" },
    	{ "val2", "is" }
    };
    
    Console.WriteLine(dictionary["val1"]);  // Outputs 'this'
    
    dictionary.Remove("val1");  // Removes 'val1' from dictionary
    
    dictionary["val3"] = "a dictionary";  // Overwrites 'val3' or sets new key-value pair
    dictionary.Add("val3", "a dictionary");  // Creates a new key-value pair
    

### Numerically-Indexed Tables

Tables in Lua can also be used like a List in C#. The key difference is that indices start at **1** with Lua and **0** with C#.

#### Lua
    
    
    local NPCAttributes = {"strong", "intelligent"}
    
    print(NPCAttributes[1])  -- Outputs 'strong'
    
    print(#NPCAttributes)  -- Outputs the size of the list
    
    -- Append to the list
    table.insert(NPCAttributes, "humble")
    -- Another way...
    NPCAttributes[#NPCAttributes+1] = "humble"
    
    -- Insert at the beginning of the list
    table.insert(NPCAttributes, 1, "brave")
    
    -- Remove item at a given index
    table.remove(NPCAttributes, 3)
    

#### C#
    
    
    List NPCAttributes = new List{"strong", "intelligent"};
    
    Console.WriteLine(NPCAttributes[0]);  // Outputs 'strong'
    
    Console.WriteLine(NPCAttributes.Count);  // Outputs the size of the list
    
    // Append to the list
    NPCAttributes.Add("humble");
    // Another way...
    NPCAttributes.Insert(NPCAttributes.Count, "humble");
    
    // Insert at the beginning of the list
    NPCAttributes.Insert(0, "brave");
    
    // Remove item at a given index
    NPCAttributes.Remove(2);
    



***__Roblox官方链接__:[Lua / C# Comparison](https://developer.roblox.com/zh-cn/articles/lua-csharp-comparison)