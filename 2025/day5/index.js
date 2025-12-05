import fs from "fs"

function partOne(file) {
    const [l1, l2] = fs.readFileSync(file, "utf8").trim().split("\n\n").map(l => l.split("\n"))
    let rng = l1.map(l => l.split("-").map(Number))
    let num = l2.map(Number).reduce((t,n) => t+rng.some(([r1,r2]) => n>=r1 && n<=r2), 0)
    console.log(num)
}


function partTwo(file) {
    const [l1] = fs.readFileSync(file, "utf8").trim().split("\n\n").map(l => l.split("\n"))
    let rng = l1.map(l => l.split("-").map(Number)).sort((a,b) => a[0]-b[0])
    let [num] = rng.reduce(([t,r],[a,b]) => b>r ? [t+(b-Math.max(a,r+1)+1), Math.max(r,b)] : [t,r], [0,0])
    console.log(num)
}


partOne("./example.txt")
partOne("./input.txt")
partTwo("./example.txt")
partTwo("./input.txt")