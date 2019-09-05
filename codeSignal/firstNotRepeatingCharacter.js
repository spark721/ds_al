
// CodeSignal > Interview Practice > Arrays
// Easy

/*
Asked by Amazon

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

    For s = "abacabad", the output should be
    firstNotRepeatingCharacter(s) = 'c'.

    There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

    For s = "abacabaabacaba", the output should be
    firstNotRepeatingCharacter(s) = '_'.

    There are no characters in this string that do not repeat.

*/

function rep(s) {
    for (let i = 0; i < s.length; i += 1) {

        if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
            return s[i];
        }
    }
    return '_';
}

console.log(rep('abacabaabacaba'));