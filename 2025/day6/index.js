import fs from "fs"

const ops = {"+": [(a,b) => a+b, 0], "*": [(a,b) => a*b, 1]}


function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n").reverse().map(l => l.match(/\S+/g))
    let res = lines[0].reduce((t,_,i) => t+lines.reduce(([o,s],v) => !o?ops[v[i]]:[o, o(s,+v[i])], [])[1], 0)
    console.log(res)
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").split("\n")
    let op = [...(lines.pop()+" ").matchAll(/\S\s+/g)].map((m) => [m[0], m.index])
    let nums = lines[0].split("").map((c, i) => +lines.map(l => l[i]).join(""))
    let res = op.reduce((t,[m,i]) => t+nums.slice(i, i+m.length-1).reduce(...ops[m[0]]), 0)
    console.log(res)
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")