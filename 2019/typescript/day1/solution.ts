import * as fs from 'fs';

const allLines: string[] = fs.readFileSync('input.txt', 'utf-8').split(/\r?\n/);

let total: number = 0
for (const line of allLines) {
  total += Math.floor(parseInt(line) / 3) - 2
}

console.log(total)

total = 0
for (const line of allLines) {
  let requiredFuel: number = Math.floor(parseInt(line) / 3) - 2
  total += requiredFuel
  while (requiredFuel > 0) {
    requiredFuel = Math.floor(requiredFuel / 3) - 2
    total += Math.max(requiredFuel, 0)
  }
}

console.log(total)