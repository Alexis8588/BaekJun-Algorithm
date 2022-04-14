let inputA = readLine()
let inputB = readLine()

var x: Int = inputA[0]
var y: Int = inputB[0]

var asnwer: Int = 0

if (x != 0 && y != 0 && -1000 < x && x < 1000 & -1000 < y && y < 1000) {
    if (x < 0 && y < 0) {
        answer = 1
    } else if (x < 0 && y > 0) {
        answer = 4
    } else if (0 < x && y < 0) {
        answer = 3
    } else {
        answer = 2
    }
}
print(answer)