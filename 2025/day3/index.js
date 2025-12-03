import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    console.log(lines.reduce((t,l,v)=>+((v=""+Math.max(...l.slice(0,-1)))+Math.max(...l.slice(l.indexOf(v)+1)))+t,0))
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let f=(l,c=12,v)=>c?(v=Math.max(...l.slice(0,l.length-c+1)))+f(l.slice(l.indexOf(v)+1),c-1):""
    console.log(lines.reduce((t,l)=>+f(l)+t,0))
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")