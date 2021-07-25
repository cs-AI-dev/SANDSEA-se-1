# Error Explanations
This file will explain how to interpret error codes that come up, found between the brackets in error codes. For example, `ERROR [ 1 ] "k" is not a valid command type`,
when cross-referenced with this file, is known to be a syntax error on the user's part.  

### [ 1 ] - Invalid Command Type
If input a command and receive error code 1, you entered a command type that wasn't registered with your version of SANDSEA. For example, `$` is for modifying your simulation, and
`?` is for queries. The command type is the first character of every command, and if you put in an unregistered one, you will get error code 1.
