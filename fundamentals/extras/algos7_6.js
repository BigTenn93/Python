/*
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// const str3 = "hello";
// const expected3 = "olleh";

// const str4 = "";
// const expected4 = "";

// /**
//  * Reverses the given str.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str String to be reversed.
//  * @returns {string} The given str reversed.
//  */

var str1 = "creature";
var str2 = "dog";
var str3 = "hello";
var strs = str1 + str2 + str3;

console.log(strs);


// function reverseString(str) {
//     var newString = "";
//     for (var i = str.length - 1; i >= 0; i--) {
//         newString += str[i];
//     }
//     return newString;
// }
// reverseString('creature');

// const str = 'guitar';
// console.log(str);
// let reversedStr = '';

// for (let i = str.length - 1; i >= 0; i--) {
//     reversedStr += str[i];
// }

// console.log(reversedStr);


// //TEST CODE FOR REVERSE
// console.log(reverseString(str1)) // Expected: erutaerc
// console.log(reverseString(str2)) // Expected: god
// console.log(reverseString(str3)) // Expected: olleh
// console.log(reverseString(str2)) // Expected: ""

// /*
//   Acronyms
//   Create a function that, given a string, returns the string’s acronym
//   (first letter of each word capitalized).
//   Do it with .split first if you need to, then try to do it without
// */

// const str5 = "object oriented programming";
// const expected5 = "OOP";

// // The 4 pillars of OOP
// const str6 = "abstraction polymorphism inheritance encapsulation";
// const expected6 = "APIE";

// const str7 = "software development life cycle";
// const expected7 = "SDLC";

// // Bonus: ignore extra spaces
// const str8= "  global       information tracker    ";
// const expected8 = "GIT";

// /**
//  * Turns the given str into an acronym.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str A string to be turned into an acronym.
//  * @returns {string} The acronym.
//  */
// function acronymize(str) {
//     //Your code here
// }
// // //TEST CODE FOR ACRONYMIZE
// console.log(acronymize(str5)) // Expected: OOP
// console.log(acronymize(str6)) // Expected: APIE
// console.log(acronymize(str7)) // Expected: SDLC
// //BONUS TEST CASE
// console.log(acronymize(str8)) // Expected: GIT
