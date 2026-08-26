// assert_demo.swift
// Glenn G. Chappell
// 2026-08-25
// Demo of assert in Swift


// max
// Return maximum value in given nonempty array of Int
func max(_ vals: [Int]) -> Int {
    assert(vals.count > 0)
    // TRY: add a second argument to the above assert call: a string

    var result: Int = vals[0]
    for val in vals {
        if val > result {
            result = val
        }
    }
    return result
}


// Sum a nonempty array; should work
print()
print("Press ENTER to find max value in array1 (nonempty) ",
      terminator: "")
_ = readLine()
let array1: [Int] = [1, 2, 3, 4]  // Nonempty array
print("Result: ", max(array1))

// Sum an empty array; should crash due to failed assertion
print()
print("Press ENTER to find max value in array2 (empty) ",
      terminator: "")
_ = readLine()
let array2: [Int] = []  // Empty array
print("Result: ", max(array2))

