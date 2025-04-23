type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let acc: number = init;
    for(const num of nums) {
        acc = fn(acc, num);
    }
    return acc;
};