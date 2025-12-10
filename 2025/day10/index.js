import { init } from 'z3-solver';
const { Context } = await init();
import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n").map(l => l.split(" "))

    let total = 0
    lines.forEach((line) => {
        console.log(line)
        let statestr = line[0].substring(1, line[0].length-1)
        let state = 0
        statestr.split("").forEach((v, i) => {
            if (v=="#") state += 2**i
        })
        let numbuttons = line.slice(1,line.length-1).map(b => b.match(/\d+/g).map(Number))
        let buttons = numbuttons.map(b => b.reduce((t, v) => t+2**v, 0))

        console.log({state, numbuttons, buttons})

        let bestPresses = null
        let minPresses = Infinity
        for (let bm = 0; bm < 2**buttons.length; bm++) {
            let sol = 0
            let presses = buttons.filter((b, i) => (bm >> i) & 1)
            presses.forEach(b => sol ^= b)
            if (sol === state && presses.length <= minPresses) {
                minPresses = presses.length
                bestPresses = presses
            }
        }
        console.log({minPresses, bestPresses})
        total += minPresses
    })
    console.log(total)
    
}

async function partTwo(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n").map(l => l.split(" "))

    async function solveLine(line) {
        let buttons = line.slice(1,line.length-1).map(b => b.match(/\d+/g).map(Number))
        let goalState = line[line.length-1].match(/\d+/g).map(Number)

        const {Int, Solver, Optimize} = new Context('main');
        let vars = buttons.map((b, i) => Int.const(`b${i}`))

        // let s = new Solver()
        let o = new Optimize()
        vars.forEach(v => o.add(v.ge(Int.val(0))))

        for (let i = 0; i < goalState.length; i++) {
            let g = goalState[i]
            let sum = vars.reduce((t, v, j) => {
                if (buttons[j].includes(i)) {
                    return t.add(v)
                } else {
                    return t
                }
            }, Int.val(0))
            o.add(sum.eq(Int.val(g)))
        }

        let total = vars.reduce((t, v) => t.add(v), Int.val(0))
        o.minimize(total)

        let cr = await o.check()

        let model = o.model()
        let res = model.toString()
        // console.log({res})
        
        let buttonPresses = vars.map(v => {
            let val = model.get(v)
            return Number(val)
        })
        // console.log({buttonPresses})

        return buttonPresses.reduce((t, v) => t + v, 0)
    }

    let total = 0
    for (let line of lines) {
        let presses = await solveLine(line)
        total += presses
        console.log({presses, total})
    }
    
    console.log(total)
}

// partOne("./example.txt")
// partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")