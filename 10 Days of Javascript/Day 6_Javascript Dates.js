// ==============================
//         Information
// ==============================

// Title: Day 6: Javascript Dates
// Link: https://www.hackerrank.com/challenges/js10-date/problem
// Difficulty: Easy
// Max Score: 15
// Language: Javascript

// ==============================
//         Solution
// ==============================

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName;
    // Write your code here
    const newDate = new Date(dateString);
    const options = { weekday: 'long'};
    dayName = new Intl.DateTimeFormat('en-US', options).format(newDate)
    // dayName = newDate.getUTCDay();   // this returns 0-6 as number of day so above is necessary
    return dayName;
}


function main() {
    const d = +(readLine());
    
    for (let i = 0; i < d; i++) {
        const date = readLine();
        
        console.log(getDayName(date));
    }
}