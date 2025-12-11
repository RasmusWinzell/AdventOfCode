import { init } from 'z3-solver';
const { Context } = await init();
import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n").map(l => l.split(" "))

    let total = 0
    lines.forEach((line) => {
        let [stateStr, ...btns] = line.slice(0,line.length-1)
        let state = stateStr.split("").reduce((s, v, i) => v=="#" ? s + 2**(i-1) : s, 0)
        let buttons = btns.map(b => b.match(/\d+/g).reduce((t, v) => t+2**v, 0))

        let minPresses = Infinity
        for (let bm = 0; bm < 2**buttons.length; bm++) {
            let presses = buttons.filter((b, i) => (bm >> i) & 1)
            let sol = presses.reduce((s, v) => s ^ v, 0)
            if (sol === state && presses.length <= minPresses) minPresses = presses.length
        }
        total += minPresses
    })
    console.log(total)
}

async function partTwo(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n").map(l => l.split(" "))

    async function solveLine(line) {
        let goalState = line[line.length-1].match(/\d+/g).map(Number)
        let buttons = line.slice(1,line.length-1).map(b => b.match(/\d+/g).map(Number))

        const {Int, Optimize} = new Context(line);
        let o = new Optimize()
        let vars = buttons.map((b, i) => Int.const(`b${i}`))
        vars.forEach(v => o.add(v.ge(Int.val(0))))

        goalState.forEach((g, i) => {
            o.add(vars.reduce((t, v, j) => buttons[j].includes(i) ? t.add(v) : t, Int.val(0)).eq(Int.val(g)))
        })

        let total = vars.reduce((t, v) => t.add(v), Int.val(0))
        o.minimize(total)

        await o.check()
        let model = o.model()
        
        return vars.reduce((t, v) => t + Number(model.get(v)), 0)
    }

    let total = (await Promise.all(lines.map(solveLine))).reduce((a, b) => a + b, 0)
    
    console.log(total)
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")