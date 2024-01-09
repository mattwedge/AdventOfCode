// 45:41

import * as fs from 'fs'

const allLines: string[] = fs.readFileSync('input.txt', 'utf-8').split(/\r?\n/);
const vals: number[] = []
const numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
const numberStrings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for (const line of allLines) {
  let firstDigit = ""
  for (let i = 0; i < line.length; i++) {
    if (numbers.includes(line[i])) {
      firstDigit = line[i]
      break
    }
    for (const numberString of numberStrings) {
      if (line.slice(i, i + numberString.length) === numberString) {
        firstDigit = `${numberStrings.indexOf(numberString)}`
        break
      }
    }
    if (firstDigit) {
      break
    }
  }

  let lastDigit = ""
  for (let i = line.length - 1; i >= 0; i--) {
    if (numbers.includes(line[i])) {
      lastDigit = line[i]
      break
    }
    for (const numberString of numberStrings) {
      if (line.slice(i, i + numberString.length) === numberString) {
        lastDigit = `${numberStrings.indexOf(numberString)}`
        break
      }
    }

    if (lastDigit) {
      break
    }
  }

  const val = parseInt(`${firstDigit}${lastDigit}`)
  vals.push(val)
}

console.log(vals.reduce((a, b) => a + b))