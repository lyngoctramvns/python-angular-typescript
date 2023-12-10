## TypeScript vs Javascript

* Typescript is, in some sense, a superset of Javascript
* Typescript is essentially a *static checking* method for JS. It analyze the code for potential errors.
* There are errors, for example "2 + '2'" which shouldn't be allowed and will cause error when going into NodeJS module, etc.
* Typescript will prevented it happening by checking the error in the IDE
> Typescript is a **DEVELOPMENT TOOL**. Your code will still runs on JS. It is **NOT** a new programming language

### Installation

* Installation globally: npm install -g typescript
* installation in webapps: npm install typescript --save-dev

More on: [TypeScript Documentation](https://www.typescriptlang.org/download)

* Check version: tsc -v

### Types
* Number
* String
* Boolean
* Null
* Undefined
* Void
* Object
* Array
* Tuples
* Union
* ...
Special types: Any, Never, Unknown

=> Typescript is going to check which type of data type is coming in to as inputs

=> A function is returning a string

=> JS doesn't have an integer runtime, so there are no int & float. It just defined as number

### Best Practice

* You don't have to always use colons and then type on every typescript variable.
* Don't overuse ANY type, as it was not type-checked. Should use noImplicitAny from Typescript configs to limit this bad habit.