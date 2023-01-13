
// https://leetcode.com/problems/two-sum/submissions/876820443/
const twoSum = function(nums, target) {
    for(let i=0; i<nums.length; i++) {
        for(let j=i+1; j<=nums.length; j++) {
           if(nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }
};

// // https://leetcode.com/problems/sqrtx/submissions/877180892/
const mySqrt = function(x) {
    return Math.floor(Math.pow(x, 0.5))
};
// https://leetcode.com/problems/pascals-triangle/submissions/877199803/
var generate = function(numRows) {
    let listMain = []
    for( let i=0; i<numRows; i++) {
        listMain.push([1])
        if(i >= 1) {
            listMain[i].push(1)
        }
    }
    listMain.forEach((value, indice) => {
        if(value.length >= 2) {
            for(let i=1; i<listMain[indice-1].length; i++){
                value.splice(i, 0, listMain[indice-1][i] + listMain[indice-1][i - 1])
            }
        }
    })
    return listMain

};

// https://leetcode.com/problems/divide-two-integers/submissions/877458815/
var divide = function(dividend, divisor) {
    let result = dividend / divisor
    if(dividend < divisor && dividend > 0 || divisor === 0) {
        return 0
    }

    if(contrains(dividend) && contrains(divisor)) {
        if( result > 10 || result < -10 ){
            if(result >= 2**31) {
                return result - 1
            }
            if(result <= -(2**31)) {
                return -(2**31)
            }
            return  result < 0 ? Math.ceil(result) : Math.floor(result)
        }
        if (result < 0) {
            result = String(result)
            return Number(`${result[0]}${result[1]}`)
        }

    }
    return Number(String(result)[0])

};

const contrains = function (number) {
    return -(2**31) <= number <= 2**31 - 1
}

console.log(twoSum([2,7,11,15], 9))
console.log(mySqrt(8))
console.log(generate(5))
console.log(divide(10, 3))

